#!/usr/bin/env python3
"""
Monte Carlo Uncertainty Propagation for LCA Co-Product Allocation Factors — V1
================================================================================
"""
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# ── Font setup ─────────────────────────────────────────────────────────────────
if os.name == 'nt':
    _fps = ['C:\\Windows\\Fonts\\msyh.ttc', 'C:\\Windows\\Fonts\\arial.ttf']
else:
    _fps = ['/usr/share/fonts/truetype/chinese/SarasaMonoSC-Regular.ttf',
            '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf']
for fp in _fps:
    if os.path.exists(fp):
        try: fm.fontManager.addfont(fp)
        except Exception: pass
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'Sarasa Mono SC', 'DejaVu Sans', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

# ══════════════════════════════════════════════════════════════════════════════
# CO-PRODUCT FIGURE — mappings + plot function
# ══════════════════════════════════════════════════════════════════════════════
CROP_ORDER_FIG = [
    "Soybean (Crushing)", "Canola (Crushing)", "Flaxseed (Crushing)",
    "Sunflower (Crushing)", "Safflower (Crushing)",
    "Peanut (Shelling → Crushing)", "Almond (Hulling)",
    "Corn (Wet Milling)", "Corn (Dry Milling)", "Wheat (Flour Milling)",
    "Oat (Milling)", "Rice (Hulling → Milling)",
    "Corn (Dry-Grind Ethanol)", "Wheat (Dry-Grind Ethanol)",
    "Barley (Malting → Brewing)",
    "Sugar Beet (Processing)", "Sugarcane (Milling)",
    "Sweet Corn (Canning)", "Potato (Processing)", "Citrus (Processing)",
    "Cotton (Ginning → Crushing)", "Cotton (Ginning — seed sold)",
]
SYSTEM_GROUP_FIG = {
    "Soybean (Crushing)":           "Oilseeds",
    "Canola (Crushing)":            "Oilseeds",
    "Flaxseed (Crushing)":          "Oilseeds",
    "Sunflower (Crushing)":         "Oilseeds",
    "Safflower (Crushing)":         "Oilseeds",
    "Peanut (Shelling → Crushing)": "Nuts & Specialty",
    "Almond (Hulling)":             "Nuts & Specialty",
    "Corn (Wet Milling)":           "Grains & Milling",
    "Corn (Dry Milling)":           "Grains & Milling",
    "Wheat (Flour Milling)":        "Grains & Milling",
    "Oat (Milling)":                "Grains & Milling",
    "Rice (Hulling → Milling)":     "Grains & Milling",
    "Corn (Dry-Grind Ethanol)":     "Bioenergy",
    "Wheat (Dry-Grind Ethanol)":    "Bioenergy",
    "Barley (Malting → Brewing)":   "Bioenergy",
    "Sugar Beet (Processing)":      "Sugar Crops",
    "Sugarcane (Milling)":          "Sugar Crops",
    "Sweet Corn (Canning)":         "Fruits, Veg & Specialty",
    "Potato (Processing)":          "Fruits, Veg & Specialty",
    "Citrus (Processing)":          "Fruits, Veg & Specialty",
    "Cotton (Ginning → Crushing)":  "Fiber Crops",
    "Cotton (Ginning — seed sold)": "Fiber Crops",
}
CROP_SHORT_FIG = {
    "Soybean (Crushing)":           "Soybean",
    "Canola (Crushing)":            "Canola",
    "Flaxseed (Crushing)":          "Flaxseed",
    "Sunflower (Crushing)":         "Sunflower",
    "Safflower (Crushing)":         "Safflower",
    "Peanut (Shelling → Crushing)": "Peanut",
    "Almond (Hulling)":             "Almond",
    "Corn (Wet Milling)":           "Corn Wet Mill",
    "Corn (Dry Milling)":           "Corn Dry Mill",
    "Wheat (Flour Milling)":        "Wheat Flour",
    "Oat (Milling)":                "Oat",
    "Rice (Hulling → Milling)":     "Rice",
    "Corn (Dry-Grind Ethanol)":     "Corn Ethanol",
    "Wheat (Dry-Grind Ethanol)":    "Wheat Ethanol",
    "Barley (Malting → Brewing)":   "Barley/Brew",
    "Sugar Beet (Processing)":      "Sugar Beet",
    "Sugarcane (Milling)":          "Sugarcane",
    "Sweet Corn (Canning)":         "Sweet Corn",
    "Potato (Processing)":          "Potato",
    "Citrus (Processing)":          "Citrus",
    "Cotton (Ginning → Crushing)":  "Cotton (seed crushed)",
    "Cotton (Ginning — seed sold)": "Cotton (seed sold)",
}
COPRODUCT_SHORT_FIG = {
    "Malt (intermediate)":           "Malt (int.)",
    "Brown rice (intermediate)":     "Brown rice (int.)",
    "Shelled kernels (intermediate)": "Shelled kernels (int.)",
    "Brewers spent grain (dried)":   "Brewers grain",
    "Processed potato products":     "Potato products",
    "Potato processing waste":       "Potato waste",
    "Cannery waste silage":          "Cannery waste",
    "Cottonseed linters":            "CS linters",
    "Cottonseed hulls":              "CS hulls",
    "Cottonseed meal":               "CS meal",
    "Cottonseed oil":                "CS oil",
    "Corn meal & grits":             "Corn meal/grits",
    "Soybean meal (48% protein)":     "Soybean meal (48%)",
    "Sunflower meal (dehulled)":     "Sunflower meal",
    "Safflower meal (non-dehulled)": "Safflower meal",
    "Wheat flour (all-purpose)":     "Wheat flour",
    "White rice (head rice)":        "White rice",
    "Distillers grains (total)":     "Distillers grains",
    "Corn gluten feed (dry)":        "Corn gluten feed",
    "Soybean hulls (whole)":         "Soybean hulls",
    "Canola oil (crude)":            "Canola oil",
}
GROUP_ORDER_FIG = [
    "Oilseeds", "Nuts & Specialty", "Grains & Milling",
    "Bioenergy", "Sugar Crops", "Fruits, Veg & Specialty", "Fiber Crops",
]
GROUP_BG_FIG = {
    "Oilseeds":                (1.00, 0.96, 0.78, 0.55),
    "Nuts & Specialty":        (1.00, 0.85, 0.68, 0.55),
    "Grains & Milling":        (0.75, 0.93, 0.75, 0.55),
    "Bioenergy":               (0.68, 0.85, 0.90, 0.55),
    "Sugar Crops":             (0.88, 0.70, 0.88, 0.45),
    "Fruits, Veg & Specialty": (1.00, 0.74, 0.74, 0.45),
    "Fiber Crops":             (0.82, 0.82, 0.82, 0.50),
}
TIER_COLOR_FIG = {"High": "#C0392B", "Moderate": "#E59B27", "Low": "#27AE60"}


def plot_coproduct_divergence(div_df, block_df, output_dir=None):
    import matplotlib.patches as mpatches
    if output_dir is None:
        output_dir = OUTPUT_DIR

    df = div_df.copy()
    df["SystemGroup"] = df["Crop"].map(SYSTEM_GROUP_FIG)
    crop_rank = {c: i for i, c in enumerate(CROP_ORDER_FIG)}
    df["CropOrder"] = df["Crop"].map(crop_rank)
    df = df.sort_values(["CropOrder", "Spread_pp"], ascending=[True, False]).reset_index(drop=True)
    df["CropShort"]      = df["Crop"].map(lambda x: CROP_SHORT_FIG.get(x, x))
    df["CoproductShort"] = df["Co-product"].map(lambda x: COPRODUCT_SHORT_FIG.get(x, x))
    df["YLabel"]         = df["CropShort"] + "  ·  " + df["CoproductShort"]
    n = len(df)

    # ── Figure sizing: wider for readable labels ──────────────────────────
    row_h = 0.38                              # inches per co-product row
    fig_h = max(16, n * row_h + 2.0)         # auto-scale height
    fig_w = 16                                # was 11" — too narrow for labels
    fig, ax = plt.subplots(figsize=(fig_w, fig_h))
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    group_extents = {}
    for g in GROUP_ORDER_FIG:
        idxs = df.index[df["SystemGroup"] == g].tolist()
        if idxs:
            group_extents[g] = (min(idxs), max(idxs))

    for g, (y0, y1) in group_extents.items():
        ax.axhspan(y0 - 0.5, y1 + 0.5, color=GROUP_BG_FIG[g], zorder=0)
        # Separator line between groups
        if y1 < n - 1:
            ax.axhline(y1 + 0.5, color="white", lw=1.5, zorder=1)

    is_int = df.get("Product_type", pd.Series(["Final"] * n)).eq("Intermediate")
    for i, row in df.iterrows():
        if is_int.iloc[i]:
            ax.barh(i, row["Spread_pp"], color=TIER_COLOR_FIG[row["Tier"]],
                    edgecolor="white", linewidth=0.8, hatch="///", alpha=0.55,
                    height=0.72, zorder=2)
        else:
            ax.barh(i, row["Spread_pp"], color=TIER_COLOR_FIG[row["Tier"]],
                    edgecolor="none", height=0.72, zorder=2)

    for x_thresh, label in [(5, "5 pp"), (20, "20 pp")]:
        ax.axvline(x_thresh, color="gray", lw=1.0, ls="--", zorder=3, alpha=0.7)
        ax.text(x_thresh + 0.3, -0.9, label, fontsize=8, color="gray", va="top", ha="left")

    ax.set_yticks(range(n))
    label_fs = min(9.5, 720 / n)          # auto-scale font for tall figures
    ax.set_yticklabels(df["YLabel"], fontsize=label_fs)
    ax.set_ylim(-0.8, n - 0.2)
    ax.invert_yaxis()
    # ── X-axis: auto-range with 12% headroom instead of fixed 82 ─────────
    max_spread = df["Spread_pp"].max()
    x_max = min(85, max(max_spread * 1.12, 25))
    ax.set_xlim(0, x_max)
    ax.set_xlabel("Spread (pp) = max − min across Economic, Mass & Energy allocation", fontsize=10)
    ax.tick_params(axis="x", labelsize=9)
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="x", lw=0.4, alpha=0.4, zorder=1)

    legend_handles = [
        mpatches.Patch(color=TIER_COLOR_FIG["High"],     label="High  (Spread > 20 pp)"),
        mpatches.Patch(color=TIER_COLOR_FIG["Moderate"], label="Moderate  (5–20 pp)"),
        mpatches.Patch(color=TIER_COLOR_FIG["Low"],      label="Low  (< 5 pp)"),
        mpatches.Patch(facecolor="#999999", hatch="///", alpha=0.55, edgecolor="white",
                       label="Cascade intermediate (not a final co-product)"),
    ]
    ax.legend(handles=legend_handles, loc="lower right", fontsize=9,
              frameon=True, framealpha=0.9, edgecolor="#cccccc")

    fig.suptitle("Figure 2. Co-product Divergence Index\n"
                 "Spread across Economic, Mass & Energy Allocation Methods",
                 x=0.45, fontsize=13, fontweight="bold", ha="center")

    fig.text(0.02, 0.005,
             "Hatched bars are cascade intermediates (malt, brown rice, shelled peanut kernels). They are shown as a diagnostic of "
             "stage-1 method sensitivity and are excluded from the summary statistics: they are not final co-products, and their spread "
             "is already carried into their stage-2 products.\n"
             "Cotton is modelled as two distinct processing blocks — seed sold (Pathway A) and seed crushed (Pathway B). The two are "
             "alternative fates of the same gin output, so cotton lint appears under both.",
             fontsize=7.5, color="#444444", ha="left", va="bottom", wrap=True)

    # ── Layout: generous left margin for labels ───────────────────────────
    plt.tight_layout(rect=[0.22, 0.045, 0.98, 0.96])
    out_path = os.path.join(output_dir, "divergence_index_figure_v10.png")
    plt.savefig(out_path, dpi=400, bbox_inches="tight", facecolor="white")
    plt.close()
    print(f"  Co-product figure saved: {out_path}")
    return out_path

# ── Reproducibility ────────────────────────────────────────────────────────────
np.random.seed(42)
N_ITER = 10_000
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ══════════════════════════════════════════════════════════════════════════════
# PERT Distribution Sampler
# ══════════════════════════════════════════════════════════════════════════════
def sample_pert(min_val, mode_val, max_val, size=N_ITER, lambd=4.0):
    """Sample from PERT (modified beta) distribution."""
    if min_val == mode_val == max_val:
        return np.full(size, min_val)
    mean = (min_val + lambd * mode_val + max_val) / (lambd + 2)
    if abs(mode_val - mean) < 1e-10:
        alpha = 1.0 + lambd / 2.0
        beta_param = alpha
    else:
        alpha = (mean - min_val) * (2 * mode_val - min_val - max_val) / (
            (mode_val - mean) * (max_val - min_val))
        beta_param = alpha * (max_val - mean) / (mean - min_val)
    alpha = max(alpha, 0.1)
    beta_param = max(beta_param, 0.1)
    samples = np.random.beta(alpha, beta_param, size=size)
    return min_val + samples * (max_val - min_val)

# ══════════════════════════════════════════════════════════════════════════════
# CROP DATA (UPDATED TO MATCH SPREADSHEET EXACTLY)
# ══════════════════════════════════════════════════════════════════════════════
CROPS = {
    "soybean": {
        "name": "Soybean (Crushing)", "type": "single",
        "products": [
            {"name": "Soybean oil",            "yield": 0.195, "yield_range": (0.19, 0.20), "price": 1050, "price_range": (900, 1200), "dm": 1.00, "ge": 39.3, "ge_range": (38.5, 40.0)},
            {"name": "Soybean meal (48% protein)",     "yield": 0.750, "yield_range": (0.74, 0.76), "price":  370, "price_range": (340,  400), "dm": 0.89, "ge": 19.7, "ge_range": (16.3, 20.2)},
            {"name": "Soybean hulls (whole)",          "yield": 0.055, "yield_range": (0.05, 0.06), "price":  140, "price_range": (110,  170), "dm": 0.89, "ge": 18.1, "ge_range": (15.4, 19.9)},
        ],
    },
    "canola": {
        "name": "Canola (Crushing)", "type": "single",
        "products": [
            {"name": "Canola oil (crude)",  "yield": 0.420, "yield_range": (0.40, 0.44), "price":  950, "price_range": (800, 1100), "dm": 1.00, "ge": 39.3, "ge_range": (38.5, 40.0)},
            {"name": "Canola meal", "yield": 0.560, "yield_range": (0.54, 0.58), "price":  310, "price_range": (250,  370), "dm": 0.88, "ge": 19.7, "ge_range": (16.1, 21.2)},
        ],
    },
    "flaxseed": {
        "name": "Flaxseed (Crushing)", "type": "single",
        "products": [
            {"name": "Linseed oil",  "yield": 0.400, "yield_range": (0.36, 0.44), "price": 1300, "price_range": (1000, 1600), "dm": 1.00, "ge": 39.3, "ge_range": (38.5, 40.0)},
            {"name": "Linseed meal", "yield": 0.585, "yield_range": (0.55, 0.62), "price":  400, "price_range": (300,  500), "dm": 0.88, "ge": 19.5, "ge_range": (15.9, 22.8)},
        ],
    },
    "sunflower": {
        "name": "Sunflower (Crushing)", "type": "single",
        "products": [
            {"name": "Sunflower oil",   "yield": 0.400, "yield_range": (0.35, 0.45), "price": 1000, "price_range": (750, 1250), "dm": 1.00, "ge": 39.3, "ge_range": (38.5, 40.0)},
            {"name": "Sunflower meal (dehulled)",  "yield": 0.380, "yield_range": (0.34, 0.42), "price":  260, "price_range": (200,  320), "dm": 0.90, "ge": 19.4, "ge_range": (14.3, 21.8)},
            {"name": "Sunflower hulls", "yield": 0.200, "yield_range": (0.15, 0.25), "price":   80, "price_range": ( 50,  110), "dm": 0.90, "ge": 20.1, "ge_range": (14.5, 22.9)},
        ],
    },
    "safflower": {
        "name": "Safflower (Crushing)", "type": "single",
        "products": [
            {"name": "Safflower oil",  "yield": 0.375, "yield_range": (0.35, 0.40), "price": 1300, "price_range": (1000, 1600), "dm": 1.00, "ge": 39.3, "ge_range": (38.5, 40.0)},
            {"name": "Safflower meal (non-dehulled)", "yield": 0.605, "yield_range": (0.58, 0.63), "price":  150, "price_range": (100,  200), "dm": 0.88, "ge": 19.0, "ge_range": (14.7, 20.9)},
        ],
    },
    "corn_wet": {
        "name": "Corn (Wet Milling)", "type": "single",
        "products": [
            {"name": "Corn starch",       "yield": 0.560, "yield_range": (0.54, 0.58), "price":  400, "price_range": (350,  450), "dm": 0.995, "ge": 17.5, "ge_range": (17.3, 17.7)},
            {"name": "Corn gluten meal",  "yield": 0.045, "yield_range": (0.04, 0.05), "price":  550, "price_range": (500,  600), "dm": 0.905, "ge": 23.9, "ge_range": (22.4, 25.1)},
            {"name": "Corn gluten feed (dry)",  "yield": 0.220, "yield_range": (0.20, 0.24), "price":  160, "price_range": (140,  180), "dm": 0.88,  "ge": 18.8, "ge_range": (14.8, 19.1)},
            {"name": "Corn germ",         "yield": 0.075, "yield_range": (0.07, 0.08), "price":  250, "price_range": (200,  300), "dm": 0.85,  "ge": 28.9, "ge_range": (22.9, 29.5)},
            {"name": "Corn steep liquor", "yield": 0.260, "yield_range": (0.22, 0.30), "price":  150, "price_range": (100,  200), "dm": 0.25,  "ge": 17.5, "ge_range": (17.1, 19.0)},
        ],
    },
    "corn_dry": {
        "name": "Corn (Dry Milling)", "type": "single",
        "products": [
            {"name": "Corn meal & grits", "yield": 0.560, "yield_range": (0.54, 0.58), "price": 230, "price_range": (200, 260), "dm": 0.89, "ge": 18.6, "ge_range": (16.9, 18.7)},
            {"name": "Hominy feed",        "yield": 0.350, "yield_range": (0.32, 0.38), "price": 165, "price_range": (160, 170), "dm": 0.87, "ge": 18.7, "ge_range": (14.1, 19.0)},
            {"name": "Corn germ",          "yield": 0.075, "yield_range": (0.07, 0.08), "price": 250, "price_range": (200, 300), "dm": 0.85, "ge": 28.9, "ge_range": (22.9, 29.5)},
        ],
    },
    "wheat_flour": {
        "name": "Wheat (Flour Milling)", "type": "single",
        "products": [
            {"name": "Wheat flour (all-purpose)",       "yield": 0.730, "yield_range": (0.71, 0.75), "price": 420,   "price_range": (380, 460), "dm": 0.86, "ge": 18.3, "ge_range": (17.0, 18.7)},
            {"name": "Wheat bran",        "yield": 0.160, "yield_range": (0.14, 0.18), "price": 170,   "price_range": (150, 190), "dm": 0.86, "ge": 18.9, "ge_range": (15.9, 20.1)},
            {"name": "Wheat middlings",   "yield": 0.110, "yield_range": (0.09, 0.13), "price": 145,   "price_range": (130, 160), "dm": 0.86, "ge": 19.2, "ge_range": (15.8, 19.6)},
        ],
    },
    "oat": {
        "name": "Oat (Milling)", "type": "single",
        "products": [
            {"name": "Food oats",     "yield": 0.600, "yield_range": (0.58, 0.62), "price": 375, "price_range": (300, 450), "dm": 0.90, "ge": 19.5, "ge_range": (16.6, 20.6)},
            {"name": "Oat hulls",     "yield": 0.250, "yield_range": (0.22, 0.28), "price":  80, "price_range": (50,  110), "dm": 0.90, "ge": 18.4, "ge_range": (14.5, 19.2)},
            {"name": "Oat mill feed", "yield": 0.100, "yield_range": (0.08, 0.12), "price": 180, "price_range": (140, 220), "dm": 0.90, "ge": 17.5, "ge_range": (14.4, 18.9)},
        ],
    },
    "corn_ethanol": {
        "name": "Corn (Dry-Grind Ethanol)", "type": "single",
        "products": [
            {"name": "Fuel ethanol", "yield": 0.310, "yield_range": (0.30, 0.32), "price": 535, "price_range": (500, 570), "dm": 1.00, "ge": 29.7, "ge_range": (29.7, 29.7)},
            {"name": "Distillers grains (total)",         "yield": 0.270, "yield_range": (0.24, 0.30), "price": 160, "price_range": (140, 180), "dm": 0.88, "ge": 21.4, "ge_range": (17.2, 22.3)},
            {"name": "Corn oil",     "yield": 0.013, "yield_range": (0.008, 0.018), "price": 830, "price_range": (660, 1000), "dm": 1.00, "ge": 39.3, "ge_range": (38.5, 40.0)},
        ],
    },
    "wheat_ethanol": {
        "name": "Wheat (Dry-Grind Ethanol)", "type": "single",
        "products": [
            {"name": "Fuel ethanol", "yield": 0.300, "yield_range": (0.28, 0.32), "price": 550, "price_range": (520, 580), "dm": 1.00, "ge": 29.7, "ge_range": (29.7, 29.7)},
            {"name": "Wheat DGS",   "yield": 0.325, "yield_range": (0.30, 0.35), "price": 145, "price_range": (120, 170), "dm": 0.88, "ge": 20.3, "ge_range": (16.1, 21.2)},
        ],
    },
    "sugar_beet": {
        "name": "Sugar Beet (Processing)", "type": "single",
        "products": [
            {"name": "Refined sugar",   "yield": 0.145, "yield_range": (0.13, 0.16), "price": 950, "price_range": (700, 1200), "dm": 1.00, "ge": 16.5, "ge_range": (16.4, 16.6)},
            {"name": "Beet pulp (wet)", "yield": 0.220, "yield_range": (0.16, 0.28), "price":  55, "price_range": (40,   70), "dm": 0.25, "ge": 17.1, "ge_range": (14.9, 18.6)},
            {"name": "Beet molasses",   "yield": 0.040, "yield_range": (0.03, 0.05), "price": 180, "price_range": (100,  260), "dm": 0.80, "ge": 14.5, "ge_range": (13.9, 15.5)},
        ],
    },
    "sugarcane": {
        "name": "Sugarcane (Milling)", "type": "single",
        "products": [
            {"name": "Raw sugar",      "yield": 0.110, "yield_range": (0.10, 0.12),  "price": 600, "price_range": (450, 750), "dm": 1.00, "ge": 16.0, "ge_range": (15.5, 17.1)},
            {"name": "Cane molasses",  "yield": 0.0425, "yield_range": (0.035, 0.050), "price": 180, "price_range": (130, 230), "dm": 0.75, "ge": 14.7, "ge_range": (13.7, 15.5)},
        ],
    },
    "sweet_corn": {
        "name": "Sweet Corn (Canning)", "type": "single",
        "products": [
            {"name": "Edible kernels",       "yield": 0.350, "yield_range": (0.30, 0.40), "price": 575,  "price_range": (450, 700), "dm": 0.25,  "ge": 18.3, "ge_range": (16.9, 18.6)},
            {"name": "Cannery waste silage", "yield": 0.580, "yield_range": (0.54, 0.62), "price":  22.5, "price_range": (15,   30), "dm": 0.225, "ge": 17.5, "ge_range": (13.5, 18.1)},
        ],
    },
    "potato": {
        "name": "Potato (Processing)", "type": "single",
        "products": [
            {"name": "Processed potato products", "yield": 0.840, "yield_range": (0.80, 0.88), "price": 1000, "price_range": (700, 1300), "dm": 0.21, "ge": 17.5, "ge_range": (16.0, 18.5)},
            {"name": "Potato processing waste",   "yield": 0.160, "yield_range": (0.12, 0.20), "price":   35, "price_range": (20,   50), "dm": 0.20, "ge": 16.5, "ge_range": (14.9, 18.5)},
        ],
    },
    "almond": {
        "name": "Almond (Hulling)", "type": "single",
        "products": [
            {"name": "Almond kernels", "yield": 0.310, "yield_range": (0.27, 0.35), "price": 4800, "price_range": (4300, 5300), "dm": 0.95, "ge": 30.7, "ge_range": (26.8, 32.6)},
            {"name": "Almond hulls",   "yield": 0.490, "yield_range": (0.45, 0.53), "price":   90, "price_range": (60,  120),  "dm": 0.90, "ge": 17.0, "ge_range": (14.5, 18.8)},
            {"name": "Almond shells",  "yield": 0.200, "yield_range": (0.16, 0.24), "price":   40, "price_range": (20,   60),  "dm": 0.90, "ge": 19.5, "ge_range": (13.8, 22.4)},
        ],
    },
    "citrus": {
        "name": "Citrus (Processing)", "type": "single",
        "products": [
            {"name": "Citrus juice",      "yield": 0.535, "yield_range": (0.45, 0.62), "price": 500, "price_range": (350, 650), "dm": 0.12, "ge": 16.5, "ge_range": (15.9, 17.9)},
            {"name": "Citrus pulp (wet)", "yield": 0.300, "yield_range": (0.25, 0.35), "price":  10, "price_range": (5,   15),  "dm": 0.20, "ge": 17.6, "ge_range": (13.6, 18.0)},
        ],
    },
    "cotton_a": {
        "name": "Cotton (Ginning — seed sold)", "type": "single",
        "products": [
            {"name": "Cotton lint",      "yield": 0.380, "yield_range": (0.36, 0.40), "price": 1600, "price_range": (1200, 2000), "dm": 0.90, "ge": 17.5, "ge_range": (14.9, 18.6)},
            {"name": "Whole cottonseed", "yield": 0.480, "yield_range": (0.45, 0.51), "price":  290, "price_range": (200,  380), "dm": 0.91, "ge": 23.8, "ge_range": (19.8, 25.2)},
        ],
    },
    "cotton_b": {
        "name": "Cotton (Ginning → Crushing)", "type": "single",
        "products": [
            {"name": "Cotton lint",        "yield": 0.380, "yield_range": (0.36,  0.40),  "price": 1600, "price_range": (1200, 2000), "dm": 0.90, "ge": 17.5, "ge_range": (14.9, 18.6)},
            {"name": "Cottonseed oil",     "yield": 0.0816, "yield_range": (0.0768, 0.0864), "price": 1000, "price_range": (800, 1200),  "dm": 1.00, "ge": 39.3, "ge_range": (38.5, 40.0)},
            {"name": "Cottonseed meal",    "yield": 0.2280, "yield_range": (0.2160, 0.2400), "price":  325, "price_range": (250,  400),  "dm": 0.88, "ge": 20.0, "ge_range": (15.8, 20.2)},
            {"name": "Cottonseed hulls",   "yield": 0.1320, "yield_range": (0.1200, 0.1440), "price":   90, "price_range": (60,   120),  "dm": 0.90, "ge": 19.8, "ge_range": (14.5, 22.5)},
            {"name": "Cottonseed linters", "yield": 0.0336, "yield_range": (0.0240, 0.0432), "price":  350, "price_range": (200,  500),  "dm": 0.94, "ge": 17.5, "ge_range": (15.9, 18.2)},
        ],
    },
    # ── Cascade crops ──────────────────────────────────────────────────────────
    "barley": {
        "name": "Barley (Malting → Brewing)", "type": "cascade",
        "stage1": {
            "name": "Malting", "intermediate_idx": 0,
            "products": [
                {"name": "Malt (intermediate)", "yield": 0.840, "yield_range": (0.78, 0.90), "price": 375, "price_range": (250, 500), "dm": 0.95, "ge": 19.5, "ge_range": (17.6, 20.4)},
                {"name": "Malt sprouts",         "yield": 0.040, "yield_range": (0.03, 0.05), "price": 200, "price_range": (150, 250), "dm": 0.93, "ge": 18.4, "ge_range": (16.1, 20.0)},
            ],
        },
        "stage2": {
            "name": "Brewing", "basis": "per_t_malt",
            "products": [
                {"name": "Beer",                        "yield": 4.600, "yield_range": (4.0, 5.2),   "price": 400, "price_range": (300, 500), "dm": 0.085, "ge": 22.7, "ge_range": (22.0, 23.9)},
                {"name": "Brewers spent grain (dried)", "yield": 0.160, "yield_range": (0.14, 0.18), "price": 185, "price_range": (150, 220), "dm": 0.91,  "ge": 20.0, "ge_range": (16.2, 21.6)},
            ],
        },
    },
    "rice": {
        "name": "Rice (Hulling → Milling)", "type": "cascade",
        "stage1": {
            "name": "Hulling", "intermediate_idx": 0,
            "products": [
                {"name": "Brown rice (intermediate)", "yield": 0.800, "yield_range": (0.78, 0.82), "price": 480, "price_range": (380, 580), "dm": 0.86, "ge": 18.1, "ge_range": (17.0, 18.8)},
                {"name": "Rice hulls",                "yield": 0.200, "yield_range": (0.18, 0.22), "price":  40, "price_range": (20,   60), "dm": 0.90, "ge": 16.3, "ge_range": (13.8, 18.2)},
            ],
        },
        "stage2": {
            "name": "Milling", "basis": "per_t_brown_rice",
            "products": [
                {"name": "White rice (head rice)",    "yield": 0.650, "yield_range": (0.58, 0.72), "price": 550, "price_range": (400, 700), "dm": 0.88, "ge": 18.0, "ge_range": (17.0, 18.4)},
                {"name": "Rice bran",     "yield": 0.080, "yield_range": (0.06, 0.10), "price": 220, "price_range": (140, 300), "dm": 0.89, "ge": 20.5, "ge_range": (17.3, 23.4)},
                {"name": "Rice mill feed", "yield": 0.050, "yield_range": (0.03, 0.07), "price": 160, "price_range": (100, 220), "dm": 0.89, "ge": 16.5, "ge_range": (14.4, 19.8)},
            ],
        },
    },
    "peanut": {
        "name": "Peanut (Shelling → Crushing)", "type": "cascade",
        "stage1": {
            "name": "Shelling", "intermediate_idx": 0,
            "products": [
                {"name": "Shelled kernels (intermediate)", "yield": 0.700, "yield_range": (0.68, 0.72), "price": 800, "price_range": (600, 1000), "dm": 0.92, "ge": 29.3, "ge_range": (25.9, 31.0)},
                {"name": "Peanut hulls",                  "yield": 0.230, "yield_range": (0.20, 0.26), "price":  40, "price_range": (30,   50),  "dm": 0.91, "ge": 19.8, "ge_range": (13.6, 21.5)},
            ],
        },
        "stage2": {
            "name": "Crushing", "basis": "per_t_kernels",
            "products": [
                {"name": "Peanut oil",  "yield": 0.420, "yield_range": (0.39, 0.45), "price": 1600, "price_range": (1400, 1800), "dm": 1.00, "ge": 39.3, "ge_range": (38.5, 40.0)},
                {"name": "Peanut meal", "yield": 0.540, "yield_range": (0.50, 0.58), "price":  250, "price_range": (200,  300),  "dm": 0.88, "ge": 20.0, "ge_range": (17.2, 21.4)},
            ],
        },
    },
}
# ══════════════════════════════════════════════════════════════════════════════
# ALLOCATION COMPUTATION FUNCTIONS
# ══════════════════════════════════════════════════════════════════════════════
def compute_single_stage_allocation(products_samples):
    """Compute economic, mass, and energy allocation for a single-stage crop."""
    revenues       = np.array([p['yield_s'] * p['price_s'] for p in products_samples])
    total_revenue  = revenues.sum(axis=0)
    dm_outputs     = np.array([p['yield_s'] * p['dm_s']    for p in products_samples])
    total_dm       = dm_outputs.sum(axis=0)
    energy_outputs = np.array([p['yield_s'] * p['dm_s'] * p['ge_s'] * 1000 for p in products_samples])
    total_energy   = energy_outputs.sum(axis=0)
    econ_alloc   = np.where(total_revenue > 0, revenues       / total_revenue * 100, 0)
    mass_alloc   = np.where(total_dm     > 0, dm_outputs      / total_dm      * 100, 0)
    energy_alloc = np.where(total_energy > 0, energy_outputs  / total_energy  * 100, 0)
    return {'econ': econ_alloc, 'mass': mass_alloc, 'energy': energy_alloc}


def compute_deterministic_allocation(products_data):
    """Compute deterministic allocation factors using midpoint values."""
    revenues       = np.array([p['yield'] * p['price']              for p in products_data])
    dm_outputs     = np.array([p['yield'] * p['dm']                 for p in products_data])
    energy_outputs = np.array([p['yield'] * p['dm'] * p['ge'] * 1000 for p in products_data])
    total_revenue  = revenues.sum()
    total_dm       = dm_outputs.sum()
    total_energy   = energy_outputs.sum()
    econ_alloc   = (revenues      / total_revenue * 100).tolist() if total_revenue > 0 else [0.0]*len(products_data)
    mass_alloc   = (dm_outputs    / total_dm      * 100).tolist() if total_dm      > 0 else [0.0]*len(products_data)
    energy_alloc = (energy_outputs/ total_energy  * 100).tolist() if total_energy  > 0 else [0.0]*len(products_data)
    return {'econ': econ_alloc, 'mass': mass_alloc, 'energy': energy_alloc}


def compute_cascade_allocation(stage1_products, stage2_products, intermediate_idx):
    """2-stage cascade allocation (Rice, Barley, Peanut)."""
    s1 = compute_single_stage_allocation(stage1_products)
    s2 = compute_single_stage_allocation(stage2_products)
    s1_ie = s1['econ'][intermediate_idx]
    s1_im = s1['mass'][intermediate_idx]
    s1_in = s1['energy'][intermediate_idx]
    results = {'econ': [], 'mass': [], 'energy': [], 'names': [], 'stages': []}
    for i, p in enumerate(stage1_products):
        if i != intermediate_idx:
            results['econ'].append(s1['econ'][i]); results['mass'].append(s1['mass'][i])
            results['energy'].append(s1['energy'][i]); results['names'].append(p['name'])
            results['stages'].append('Stage 1')
    results['econ'].append(s1_ie); results['mass'].append(s1_im); results['energy'].append(s1_in)
    results['names'].append(stage1_products[intermediate_idx]['name'])
    results['stages'].append('Stage 1 (intermediate)')
    for i, p in enumerate(stage2_products):
        results['econ'].append(s1_ie * s2['econ'][i] / 100)
        results['mass'].append(s1_im * s2['mass'][i] / 100)
        results['energy'].append(s1_in * s2['energy'][i] / 100)
        results['names'].append(p['name']); results['stages'].append('Stage 2 (cascade)')
    return results


def compute_cascade_derived_allocation(stage1_products, stage2_products, intermediate_idx):
    """Cascade allocation for Cotton Pathway B: cottonseed price derived endogenously."""
    derived_price = sum(p['yield_s'] * p['price_s'] for p in stage2_products)
    stage1_products[intermediate_idx]['price_s'] = derived_price
    s1 = compute_single_stage_allocation(stage1_products)
    s2 = compute_single_stage_allocation(stage2_products)
    s1_ie = s1['econ'][intermediate_idx]
    s1_im = s1['mass'][intermediate_idx]
    s1_in = s1['energy'][intermediate_idx]
    results = {'econ': [], 'mass': [], 'energy': [], 'names': [], 'stages': []}
    for i, p in enumerate(stage1_products):
        if i != intermediate_idx:
            results['econ'].append(s1['econ'][i]); results['mass'].append(s1['mass'][i])
            results['energy'].append(s1['energy'][i]); results['names'].append(p['name'])
            results['stages'].append('Stage 1')
    results['econ'].append(s1_ie); results['mass'].append(s1_im); results['energy'].append(s1_in)
    results['names'].append(stage1_products[intermediate_idx]['name'])
    results['stages'].append('Stage 1 (intermediate)')
    for i, p in enumerate(stage2_products):
        results['econ'].append(s1_ie * s2['econ'][i] / 100)
        results['mass'].append(s1_im * s2['mass'][i] / 100)
        results['energy'].append(s1_in * s2['energy'][i] / 100)
        results['names'].append(p['name']); results['stages'].append('Stage 2 (cascade)')
    return results


def compute_cascade_deterministic(stage1_data, stage2_data, intermediate_idx, derived_price=False):
    """Deterministic cascade allocation."""
    if derived_price:
        derived_val = sum(p['yield'] * p['price'] for p in stage2_data)
        original_price = stage1_data[intermediate_idx]['price']
        stage1_data[intermediate_idx]['price'] = derived_val
    s1_det = compute_deterministic_allocation(stage1_data)
    s2_det = compute_deterministic_allocation(stage2_data)
    if derived_price:
        stage1_data[intermediate_idx]['price'] = original_price
    s1_ie = s1_det['econ'][intermediate_idx]
    s1_im = s1_det['mass'][intermediate_idx]
    s1_in = s1_det['energy'][intermediate_idx]
    det = {'econ': [], 'mass': [], 'energy': [], 'names': [], 'stages': []}
    for i, p in enumerate(stage1_data):
        if i != intermediate_idx:
            det['econ'].append(s1_det['econ'][i]); det['mass'].append(s1_det['mass'][i])
            det['energy'].append(s1_det['energy'][i]); det['names'].append(p['name'])
            det['stages'].append('Stage 1')
    det['econ'].append(s1_ie); det['mass'].append(s1_im); det['energy'].append(s1_in)
    det['names'].append(stage1_data[intermediate_idx]['name'])
    det['stages'].append('Stage 1 (intermediate)')
    for i, p in enumerate(stage2_data):
        det['econ'].append(s1_ie * s2_det['econ'][i] / 100)
        det['mass'].append(s1_im * s2_det['mass'][i] / 100)
        det['energy'].append(s1_in * s2_det['energy'][i] / 100)
        det['names'].append(p['name']); det['stages'].append('Stage 2 (cascade)')
    return det


def sample_products(product_defs, skip_price_idx=None):
    """Sample PERT distributions for yield, price, GE."""
    samples = []
    for idx, p in enumerate(product_defs):
        ps = {
            'name':    p['name'],
            'yield_s': sample_pert(p['yield_range'][0], p['yield'],   p['yield_range'][1]),
            'price_s': (np.zeros(N_ITER) if (skip_price_idx is not None and idx == skip_price_idx)
                        else sample_pert(p['price_range'][0], p['price'], p['price_range'][1])),
            'dm_s':    np.full(N_ITER, p['dm']),
            'ge_s':    sample_pert(p['ge_range'][0],   p['ge'],      p['ge_range'][1]),
        }
        samples.append(ps)
    return samples

# ══════════════════════════════════════════════════════════════════════════════
# CO-PRODUCT DIVERGENCE  (V10: Spread = max - min, clean column names)
# ══════════════════════════════════════════════════════════════════════════════
def calculate_divergence(results_df):
    """
    Co-product level divergence index.

    Spread = max(Economic, Mass, Energy) - min(Economic, Mass, Energy)
    at midpoint allocation values.  Method-count-agnostic — works if a 4th
    method is ever added.

    Output columns: Crop, Co-product, Stage,
                    Economic, Mass, Energy,   <- midpoint alloc factors (pp)
                    Spread_pp, Tier, Product_type

    Product_type is 'Final' or 'Intermediate'.  Cascade intermediates (malt,
    brown rice, shelled peanut kernels) are retained as rows because their
    spread is a useful diagnostic of stage-1 method sensitivity, but they are
    EXCLUDED from the summary statistics: nobody needs an allocation factor for
    them, and their spread is not independent of their children's — each
    stage-2 factor is the intermediate's share x a sub-share, so counting both
    puts the same sensitivity into the mean twice.
    """
    print("\nCalculating co-product divergence...")
    pivot = results_df.pivot_table(
        index=['Crop', 'Co-product', 'Stage'],
        columns='Method',
        values='Midpoint'
    ).reset_index()
    pivot.columns.name = None

    records = []
    for _, row in pivot.iterrows():
        vals = {'Economic': row.get('Economic', np.nan),
                'Mass':     row.get('Mass',     np.nan),
                'Energy':   row.get('Energy',   np.nan)}
        valid = [v for v in vals.values() if not np.isnan(v)]
        spread = (max(valid) - min(valid)) if len(valid) >= 2 else np.nan
        tier = ('High' if spread > 20 else 'Moderate' if spread >= 5 else 'Low') if not np.isnan(spread) else 'Unknown'
        records.append({
            'Crop':       row['Crop'],
            'Co-product': row['Co-product'],
            'Stage':      row['Stage'],
            'Economic':   vals['Economic'],
            'Mass':       vals['Mass'],
            'Energy':     vals['Energy'],
            'Spread_pp':  round(spread, 2) if not np.isnan(spread) else np.nan,
            'Tier':       tier,
            'Product_type': ('Intermediate' if row['Stage'] == 'Stage 1 (intermediate)'
                             else 'Final'),
        })
    return pd.DataFrame(records)

# ══════════════════════════════════════════════════════════════════════════════
# BLOCK-LEVEL DIVERGENCE  (V10 NEW)
# ══════════════════════════════════════════════════════════════════════════════
def _block_spread_arrays_single(crop_data):
    """
    Return stacked (N_products × N_ITER) spread arrays for a single-stage crop.
    Internally resamples PERT — called once per crop in compute_block_divergence_mc.
    """
    ps = sample_products(crop_data['products'])
    alloc = compute_single_stage_allocation(ps)
    # shape: (3, N_products, N_ITER)
    stacked = np.stack([alloc['econ'], alloc['mass'], alloc['energy']], axis=0)
    # Spread per co-product per iteration: (N_products, N_ITER)
    spread = stacked.max(axis=0) - stacked.min(axis=0)
    return spread


def _block_spread_arrays_cascade(crop_data):
    """
    Return stacked spread arrays for cascade crops (Rice, Barley, Peanut).

    The intermediate product row is EXCLUDED.  D_block applies a factor of 1/2
    to correct for the zero-sum constraint, which holds only over a set of
    allocations summing to 100%.  Final products satisfy that; adding the
    intermediate does not (its burden is redistributed into the stage-2
    products, so the rows would sum to ~200%).  Including it would inflate
    D_block for cascade crops and make them incomparable with single-stage
    blocks such as cotton.
    """
    int_idx = crop_data['stage1']['intermediate_idx']
    s1 = sample_products(crop_data['stage1']['products'])
    s2 = sample_products(crop_data['stage2']['products'])
    res = compute_cascade_allocation(s1, s2, int_idx)
    keep = [i for i, st in enumerate(res['stages']) if st != 'Stage 1 (intermediate)']
    econ   = np.array([res['econ'][i]   for i in keep])   # (n_final, N_ITER)
    mass   = np.array([res['mass'][i]   for i in keep])
    energy = np.array([res['energy'][i] for i in keep])
    stacked = np.stack([econ, mass, energy], axis=0)  # (3, n_final, N_ITER)
    spread  = stacked.max(axis=0) - stacked.min(axis=0)
    return spread


def compute_block_divergence_mc(crops=CROPS):
    """
    Compute block-level divergence D_block = ½ × Σ_j Spread_j per MC iteration.

    Physical interpretation: the fraction of total block burden that could shift
    between co-products purely due to allocation method choice.  The ½ factor
    corrects for the zero-sum constraint (positive deviations = negative
    deviations within any block).

    The sum runs over FINAL products only.  For cascade crops the intermediate
    is excluded, because its burden is redistributed into the stage-2 products
    and counting both would break the zero-sum property the ½ factor relies on.
    N_coproducts below is therefore the number of final co-products.

    Also computes the deterministic D_block from midpoint allocation values
    and classifies blocks using the same thresholds applied to D_block_det
    (not Max Spread):
        Low:      D_block_det  < 5 pp
        Moderate: 5 ≤ D_block_det ≤ 10 pp
        High:     D_block_det  > 10 pp
    (Thresholds halved relative to co-product tiers because D_block is the
    mean-like aggregate, not the worst-case single co-product.)

    Returns
    -------
    pd.DataFrame with columns:
        Crop, N_coproducts,
        D_block_det,              <- deterministic midpoint value
        D_block_P5/P50/P95,       <- MC distribution percentiles
        D_block_CI_width,         <- P95 - P5
        Block_tier
    """
    print("\nComputing block-level divergence (MC)...")
    records = []

    for crop_key, crop_data in crops.items():
        ctype = crop_data['type']

        # --- MC spread arrays ---
        if ctype == 'single':
            spread = _block_spread_arrays_single(crop_data)   # (N_cp, N_ITER)
        elif ctype in ('cascade', 'cascade_derived'):
            spread = _block_spread_arrays_cascade(crop_data)  # (N_cp_total, N_ITER)
        else:
            continue

        n_cp = spread.shape[0]
        D_arr = 0.5 * spread.sum(axis=0)   # (N_ITER,) — D_block per iteration

        # --- Deterministic D_block from midpoint inputs ---
        if ctype == 'single':
            det = compute_deterministic_allocation(crop_data['products'])
            det_vals = np.array([det['econ'], det['mass'], det['energy']])  # (3, N_cp)
        else:
            int_idx = crop_data['stage1']['intermediate_idx']
            s1d = [dict(p) for p in crop_data['stage1']['products']]
            s2d = [dict(p) for p in crop_data['stage2']['products']]
            det = compute_cascade_deterministic(s1d, s2d, int_idx, derived_price=False)
            keep = [i for i, st in enumerate(det['stages']) if st != 'Stage 1 (intermediate)']
            det_vals = np.array([[det[m][i] for i in keep]
                                 for m in ('econ', 'mass', 'energy')])  # (3, N_final)

        det_spread = det_vals.max(axis=0) - det_vals.min(axis=0)  # (N_cp,)
        D_block_det = 0.5 * det_spread.sum()

        # Tier applied to D_block_det
        if D_block_det > 10:
            tier = 'High'
        elif D_block_det >= 5:
            tier = 'Moderate'
        else:
            tier = 'Low'

        records.append({
            'Crop':            crop_data['name'],
            'N_coproducts':    n_cp,
            'D_block_det':     round(float(D_block_det), 2),
            'D_block_P5':      round(float(np.percentile(D_arr,  5)), 2),
            'D_block_P50':     round(float(np.percentile(D_arr, 50)), 2),
            'D_block_P95':     round(float(np.percentile(D_arr, 95)), 2),
            'D_block_CI_width':round(float(np.percentile(D_arr, 95) - np.percentile(D_arr, 5)), 2),
            'Block_tier':      tier,
        })

    return pd.DataFrame(records).sort_values('D_block_det', ascending=False).reset_index(drop=True)

# ══════════════════════════════════════════════════════════════════════════════
# MAIN SIMULATION
# ══════════════════════════════════════════════════════════════════════════════
def run_simulation():
    all_results = []
    for crop_key, crop_data in CROPS.items():
        print(f"  Processing: {crop_data['name']}...")
        if crop_data['type'] == 'single':
            ps    = sample_products(crop_data['products'])
            alloc = compute_single_stage_allocation(ps)
            det   = compute_deterministic_allocation(crop_data['products'])
            for i, p in enumerate(ps):
                for method, a_arr, d_arr in [
                    ('Economic', alloc['econ'], det['econ']),
                    ('Mass',     alloc['mass'], det['mass']),
                    ('Energy',   alloc['energy'], det['energy']),
                ]:
                    arr = a_arr[i]
                    all_results.append({
                        'Crop': crop_data['name'], 'Co-product': p['name'],
                        'Stage': 'Single', 'Method': method,
                        'Deterministic': d_arr[i],
                        'Midpoint': float(np.median(arr)),
                        'P5':  float(np.percentile(arr,  5)),
                        'P50': float(np.percentile(arr, 50)),
                        'P95': float(np.percentile(arr, 95)),
                        'Std': float(np.std(arr)),
                        'CV':  float(np.std(arr) / max(np.mean(arr), 0.001) * 100),
                        'CI_Width': float(np.percentile(arr, 95) - np.percentile(arr, 5)),
                    })

        elif crop_data['type'] == 'cascade':
            int_idx   = crop_data['stage1']['intermediate_idx']
            s1_samp   = sample_products(crop_data['stage1']['products'])
            s2_samp   = sample_products(crop_data['stage2']['products'])
            res       = compute_cascade_allocation(s1_samp, s2_samp, int_idx)
            s1d = [dict(p) for p in crop_data['stage1']['products']]
            s2d = [dict(p) for p in crop_data['stage2']['products']]
            det = compute_cascade_deterministic(s1d, s2d, int_idx, derived_price=False)
            for i, name in enumerate(res['names']):
                for method, a_arrs, d_arr in [
                    ('Economic', res['econ'],   det['econ']),
                    ('Mass',     res['mass'],   det['mass']),
                    ('Energy',   res['energy'], det['energy']),
                ]:
                    arr = a_arrs[i]
                    all_results.append({
                        'Crop': crop_data['name'], 'Co-product': name,
                        'Stage': res['stages'][i], 'Method': method,
                        'Deterministic': d_arr[i],
                        'Midpoint': float(np.median(arr)),
                        'P5':  float(np.percentile(arr,  5)),
                        'P50': float(np.percentile(arr, 50)),
                        'P95': float(np.percentile(arr, 95)),
                        'Std': float(np.std(arr)),
                        'CV':  float(np.std(arr) / max(np.mean(arr), 0.001) * 100),
                        'CI_Width': float(np.percentile(arr, 95) - np.percentile(arr, 5)),
                    })

        elif crop_data['type'] == 'cascade_derived':
            int_idx = crop_data['stage1']['intermediate_idx']
            s1_samp = sample_products(crop_data['stage1']['products'], skip_price_idx=int_idx)
            s2_samp = sample_products(crop_data['stage2']['products'])
            res     = compute_cascade_derived_allocation(s1_samp, s2_samp, int_idx)
            s1d = [dict(p) for p in crop_data['stage1']['products']]
            s2d = [dict(p) for p in crop_data['stage2']['products']]
            det = compute_cascade_deterministic(s1d, s2d, int_idx, derived_price=True)
            for i, name in enumerate(res['names']):
                for method, a_arrs, d_arr in [
                    ('Economic', res['econ'],   det['econ']),
                    ('Mass',     res['mass'],   det['mass']),
                    ('Energy',   res['energy'], det['energy']),
                ]:
                    arr = a_arrs[i]
                    all_results.append({
                        'Crop': crop_data['name'], 'Co-product': name,
                        'Stage': res['stages'][i], 'Method': method,
                        'Deterministic': d_arr[i],
                        'Midpoint': float(np.median(arr)),
                        'P5':  float(np.percentile(arr,  5)),
                        'P50': float(np.percentile(arr, 50)),
                        'P95': float(np.percentile(arr, 95)),
                        'Std': float(np.std(arr)),
                        'CV':  float(np.std(arr) / max(np.mean(arr), 0.001) * 100),
                        'CI_Width': float(np.percentile(arr, 95) - np.percentile(arr, 5)),
                    })

    return pd.DataFrame(all_results)

# ══════════════════════════════════════════════════════════════════════════════
# VISUALIZATIONS
# ══════════════════════════════════════════════════════════════════════════════
def create_visualizations(results_df, div_df, block_df):
    """Create all diagnostic figures."""
    print("\nGenerating visualizations...")
    plot_coproduct_divergence(div_df, block_df)
    TIER_COLOR = {'High': '#C0392B', 'Moderate': '#E59B27', 'Low': '#27AE60'}

    # 1. CI Width by method (top 20)
    fig, axes = plt.subplots(1, 3, figsize=(20, 8))
    for idx, method in enumerate(['Economic', 'Mass', 'Energy']):
        ax = axes[idx]
        mdf = results_df[results_df['Method'] == method].copy().sort_values('CI_Width').tail(20)
        colors = plt.cm.RdYlGn_r(np.linspace(0.2, 0.8, len(mdf)))
        ylabels = [f"{r['Crop']}\n{r['Co-product']}" for _, r in mdf.iterrows()]
        ax.barh(range(len(mdf)), mdf['CI_Width'].values, color=colors, edgecolor='gray', lw=0.5)
        ax.set_yticks(range(len(mdf))); ax.set_yticklabels(ylabels, fontsize=7)
        ax.set_xlabel('90% CI Width (pp)', fontsize=9)
        ax.set_title(f'{method}\nTop 20 Widest CI', fontsize=11, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'uncertainty_ci_width.png'), dpi=300, bbox_inches='tight')
    plt.close()

    # 2. Co-product divergence tier distribution + histogram (final co-products only)
    div_final = div_df[div_df['Product_type'] == 'Final'] if 'Product_type' in div_df else div_df
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    tier_order  = ['Low', 'Moderate', 'High']
    tier_colors = ['#27AE60', '#E59B27', '#C0392B']
    tier_counts = div_final['Tier'].value_counts().reindex(tier_order, fill_value=0)
    axes[0].bar(tier_counts.index, tier_counts.values, color=tier_colors, edgecolor='gray')
    axes[0].set_ylabel('Number of Co-products', fontsize=11)
    axes[0].set_title('Co-Product Divergence Tier Distribution\n(final co-products only)',
                      fontsize=12, fontweight='bold')
    for i, (tier, cnt) in enumerate(zip(tier_counts.index, tier_counts.values)):
        axes[0].text(i, cnt + 0.3, f'{cnt} ({cnt/len(div_final)*100:.0f}%)', ha='center', fontsize=10, fontweight='bold')
    axes[1].hist(div_final['Spread_pp'].dropna(), bins=30, color='#3498db', edgecolor='gray', alpha=0.7)
    for xv, lbl, col in [(5, '5 pp', '#E59B27'), (20, '20 pp', '#C0392B')]:
        axes[1].axvline(x=xv, color=col, ls='--', lw=2, label=lbl)
    axes[1].set_xlabel('Spread (pp)', fontsize=11); axes[1].set_ylabel('Frequency', fontsize=11)
    axes[1].set_title('Distribution of Co-Product Spread', fontsize=12, fontweight='bold')
    axes[1].legend(fontsize=10)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'divergence_coproduct.png'), dpi=300, bbox_inches='tight')
    plt.close()

    # 3. Top 10 co-products — pairwise divergences (final co-products only)
    top10 = div_final.nlargest(10, 'Spread_pp')
    fig, ax = plt.subplots(figsize=(12, 8))
    ylabels = [f"{r['Crop']}\n{r['Co-product']}" for _, r in top10.iterrows()]
    x = np.arange(len(top10)); w = 0.25
    ax.bar(x - w, (top10['Economic'] - top10['Mass']).abs(),   w, label='|Econ − Mass|',   color='#C0392B')
    ax.bar(x,     (top10['Economic'] - top10['Energy']).abs(), w, label='|Econ − Energy|', color='#3498db')
    ax.bar(x + w, (top10['Mass']     - top10['Energy']).abs(), w, label='|Mass − Energy|', color='#27AE60')
    ax.set_ylabel('Absolute Pairwise Difference (pp)', fontsize=11)
    ax.set_title('Top 10 Co-Products — Pairwise Method Divergences', fontsize=12, fontweight='bold')
    ax.set_xticks(x); ax.set_xticklabels(ylabels, fontsize=7, rotation=45, ha='right')
    ax.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'top10_coproduct_pairwise.png'), dpi=300, bbox_inches='tight')
    plt.close()

    # 4. Block-level D_block with MC uncertainty bands  (V10: replaces mean-of-max)
    bdf = block_df.sort_values('D_block_P50', ascending=True).reset_index(drop=True)
    fig, ax = plt.subplots(figsize=(12, 9))
    colors = [TIER_COLOR[t] for t in bdf['Block_tier']]
    ax.barh(range(len(bdf)), bdf['D_block_det'], color=colors, edgecolor='none', height=0.55, zorder=2, label='Deterministic D_block')
    # MC uncertainty: horizontal error bar from P5 to P95
    for i, row in bdf.iterrows():
        ax.plot([row['D_block_P5'], row['D_block_P95']], [i, i], color='#333333', lw=2.0, zorder=3)
        ax.plot(row['D_block_P50'], i, 'D', color='white', markersize=5, zorder=4, markeredgecolor='#333333', markeredgewidth=0.8)
    for xv, col, lbl in [(5, '#E59B27', '5 pp'), (10, '#C0392B', '10 pp')]:
        ax.axvline(xv, color=col, ls='--', lw=1.2, alpha=0.8, label=f'{lbl} threshold')
    ax.set_yticks(range(len(bdf))); ax.set_yticklabels(bdf['Crop'], fontsize=8.5)
    ax.set_xlabel('Block Divergence Index D_block (pp) = ½ × Σ Spread', fontsize=10)
    ax.set_title('Block-Level Divergence Index with MC Uncertainty (P5–P95)\n'
                 'Color = Block tier  |  Bar = Deterministic  |  ◆ = MC P50  |  Line = MC P5–P95',
                 fontsize=11, fontweight='bold')
    ax.spines[['top','right']].set_visible(False)
    ax.grid(axis='x', lw=0.4, alpha=0.4)
    # Tier legend
    import matplotlib.patches as mpatches
    handles = [mpatches.Patch(color=TIER_COLOR[t], label=f'{t} (D_block)') for t in ['High','Moderate','Low']]
    ax.legend(handles=handles, loc='lower right', fontsize=9)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'block_divergence_mc.png'), dpi=300, bbox_inches='tight')
    plt.close()

    print(f"  Figures saved to {OUTPUT_DIR}/")

# ══════════════════════════════════════════════════════════════════════════════
# EXECUTION
# ══════════════════════════════════════════════════════════════════════════════
if __name__ == '__main__':
    print("=" * 80)
    print("Monte Carlo Uncertainty Propagation — V10")
    print("=" * 80)

    # ── Step 1: run MC simulation ──────────────────────────────────────────────
    print("\n[1/4] Running MC simulation...")
    results_df = run_simulation()
    results_df.to_csv(os.path.join(OUTPUT_DIR, 'mc_allocation_uncertainty_v10.csv'), index=False)

    # ── Step 2: co-product divergence ──────────────────────────────────────────
    print("\n[2/4] Co-product divergence...")
    div_df = calculate_divergence(results_df)
    div_df.to_csv(os.path.join(OUTPUT_DIR, 'divergence_index_v10.csv'), index=False)

    # ── Step 3: block-level divergence (MC) ────────────────────────────────────
    print("\n[3/4] Block-level divergence (MC P5/P50/P95)...")
    block_df = compute_block_divergence_mc()
    block_df.to_csv(os.path.join(OUTPUT_DIR, 'block_divergence_v10.csv'), index=False)

    # ── Step 4: visualizations ─────────────────────────────────────────────────
    print("\n[4/4] Figures...")
    create_visualizations(results_df, div_df, block_df)

    # ── Jensen's inequality check ──────────────────────────────────────────────
    print("\n--- Jensen's Inequality Check (MC Median vs Deterministic) ---")
    for method in ['Economic', 'Mass', 'Energy']:
        mdf   = results_df[results_df['Method'] == method]
        diffs = mdf['Midpoint'] - mdf['Deterministic']
        print(f"  {method}: mean(MC_median − Det) = {diffs.mean():.3f} pp, "
              f"max |diff| = {diffs.abs().max():.3f} pp")

    # ── Co-product summary (final co-products only) ────────────────────────────
    div_final = div_df[div_df['Product_type'] == 'Final']
    n_int     = len(div_df) - len(div_final)
    print("\n--- Co-Product Divergence Summary (final co-products only) ---")
    print(f"  Final co-products: {len(div_final)}"
          f"   (excludes {n_int} cascade intermediates: malt, brown rice, peanut kernels)")
    for tier in ['Low', 'Moderate', 'High']:
        n   = (div_final['Tier'] == tier).sum()
        pct = n / len(div_final) * 100
        print(f"  {tier:10s}: {n:3d}  ({pct:.1f}%)")
    print(f"  Mean Spread : {div_final['Spread_pp'].mean():.2f} pp")
    print(f"  Max  Spread : {div_final['Spread_pp'].max():.2f} pp")
    print("  Note: cotton is modelled as two distinct processing blocks — seed sold")
    print("        (Pathway A) and seed crushed (Pathway B). They are alternative fates")
    print("        of the same gin output, so cotton lint is listed under both.")

    # ── Block-level summary ────────────────────────────────────────────────────
    print("\n--- Block-Level D_block Summary (½ × Σ Spread) ---")
    print(f"  {'Crop':<40} {'D_det':>6}  {'P5':>6}  {'P50':>6}  {'P95':>6}  {'CI':>6}  Tier")
    for _, row in block_df.iterrows():
        print(f"  {row['Crop']:<40} {row['D_block_det']:>6.1f}  "
              f"{row['D_block_P5']:>6.1f}  {row['D_block_P50']:>6.1f}  "
              f"{row['D_block_P95']:>6.1f}  {row['D_block_CI_width']:>6.1f}  {row['Block_tier']}")

    print("\nV1 COMPLETE.")
