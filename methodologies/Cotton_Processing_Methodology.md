# Cotton Processing: Co-Product Allocation Methodology, Data Sources, and Calculations

**Document Version:** 1.0  
**Date:** May 2026  
**Basis:** 1 metric ton (t) of seed cotton at ~10% moisture (90% DM)  
**Price Period:** 2024–2025 average (unless otherwise noted)

---

## Table of Contents

1. [Standard Basis and Conversions](#1-standard-basis-and-conversions)
2. [Data Sources and References](#2-data-sources-and-references)
3. [Cotton Processing System](#3-cotton-processing-system)
4. [Co-Product Yields and Properties](#4-co-product-yields-and-properties)
5. [Prices](#5-prices)
6. [Allocation Methodology](#6-allocation-methodology)
7. [Mass Balance Verification](#7-mass-balance-verification)
8. [Complete Data Table](#8-complete-data-table)
9. [Data Quality and Limitations](#9-data-quality-and-limitations)


---

## 1. Standard Basis and Conversions

### 1.1 Parent Input Definition

| Parameter | Value | Source |
|-----------|-------|--------|
| **Parent crop** | Seed cotton (unginned cotton, lint + seed) | — |
| **Input quantity** | 1 metric ton (1,000 kg) | — |
| **Moisture content** | ~10% (90% DM) | Industry average for seed cotton at the gin [^1^]; moisture varies 8–12% depending on harvest conditions and storage |
| **Dry matter (DM) input** | 0.900 t DM/t seed cotton | Calculated: 1.000 × 0.90 = 0.900 |
| **Bale equivalent** | ~1.75 bales/t (480-lb gross weight bale) | 1 t seed cotton produces 0.38 t lint; at 480 lb (217.72 kg) per bale, bales per tonne of lint = 1,000 ÷ 217.72 ≈ 4.59. Note: 4.59 is the number of bales per tonne of lint; from 1 t seed cotton producing 0.38 t lint, the result is 0.38 × 4.59 = 1.75 bales. |
| **Typical lint turnout** | ~36–40% of seed cotton weight | Industry average for US upland cotton [^1^] |

### 1.2 Unit Conversions

| Conversion | Factor |
|------------|--------|
| 1 bale of cotton (US) | 480 lb gross weight ≈ 217.72 kg (net ~215 kg lint) |
| 1 lb | 0.453592 kg = 0.000453592 t |
| 1 t seed cotton | ~1.75 bales of lint (at 0.38 t lint/t seed cotton and 480 lb/bale) |
| 1 short ton | 2,000 lb = 0.907185 metric ton |
| 1 metric ton | 2,204.62 lb = 1.10231 short tons |

> **Note on seed cotton definition:** "Seed cotton" refers to the harvested, unginned product consisting of cotton lint (fiber) still attached to the cottonseed. It is the input to the ginning process (Stage 1). The term is distinct from "cotton lint" (the ginned fiber) and "whole cottonseed" (the seed after ginning), which are the co-products of Stage 1.

> **Note on cotton types:** This document models **upland cotton** (*Gossypium hirsutum*), which represents ~95% of US cotton production. Pima/ELS cotton (*Gossypium barbadense*) has different lint characteristics (longer staple, higher price) and is not covered here.

---

## 2. Data Sources and References

### 2.1 Primary Sources

| Citation | Full Title | Type | URL |
|----------|-----------|------|-----|
| [^1^] | USDA AMS — Cotton Varieties Planted and Ginning Reports | Government (USDA) | https://www.ams.usda.gov/ |
| [^2^] | ICAC (2024). *Cotton: Review of the World Situation* | Intergovernmental Organization | https://www.icac.org/ |
| [^3^] | USDA ERS (2025). *Cotton and Wool Outlook* | Government (USDA) | https://ers.usda.gov/ |
| [^4^] | USDA NASS (2025). *Cotton Ginning Annual Summary* | Government (USDA) | https://www.nass.usda.gov/ |
| [^5^] | ICE Futures U.S. — Cotton No. 2 Futures | Exchange/Market | https://www.theice.com/products/254/Cotton-No-2-Futures |
| [^6^] | Anthony, W.S. and Mayfield, W.D. (Eds.) (1994). *Handbook for Cotton Ginners*. USDA Agricultural Handbook 503 | Academic/Government | — |
| [^7^] | O'Brien, R.D., Jones, L.A., King, C.C., Wakelyn, P.J., and Wan, P.J. (2005). "Cottonseed Oil." Chapter 3 in *Bailey's Industrial Oil and Fat Products*, 6th ed., Vol. 2. Wiley-Interscience. DOI: 10.1002/0471678493.bio026 | Academic | — |
| [^8^] | Feedipedia — Cottonseed meal and hulls (INRAE/CIRAD/AFZ/FAO) | Research Consortium/Database | https://www.feedipedia.org/ |
| [^9^] | OECD-FAO (2025). *Agricultural Outlook: Cotton Chapter* | International Organization | https://www.oecd.org/ |
| [^10^] | National Cottonseed Products Association (2025). *Cottonseed Trading Rules, Bylaws & Charter* | Industry Association | https://www.cottonseed.com/ |

### 2.2 How Sources Were Used

- **Yield data (Stage 1):** USDA NASS [^4^], Anthony and Mayfield [^6^], and ICAC [^2^] provided cotton ginning yield data. Lint turnout and seed yield ranges reflect variation across cotton varieties, growing conditions, and ginning technology.
- **Yield data (Stage 2):** O'Brien et al. [^7^], NCPA [^10^], and ICAC [^2^] provided cottonseed crushing yield data. Ranges reflect variation across extraction methods (expeller vs. solvent) and seed dehulling configurations.
- **Price data (lint):** USDA ERS [^3^] and ICE Futures U.S. [^5^] provided cotton lint price data from futures and spot markets.
- **Price data (seed products):** USDA ERS [^3^], Feedipedia [^8^], and NCPA [^10^] provided cottonseed oil, meal, hulls, and linters price data.
- **DM contents:** USDA AMS [^1^] provided cotton moisture standards. NCPA [^10^] and O'Brien et al. [^7^] provided cottonseed product specifications.
- **Market outlook context:** OECD-FAO [^9^] provides cotton market outlook projections and long-term price trends that inform the selection of price ranges.

> **Note on URL specificity:** References [^1^] (USDA AMS), [^3^] (USDA ERS), and [^4^] (USDA NASS) currently link to organizational homepages rather than specific report pages. This is because specific annual reports and extension PDFs rotate URLs with each publication cycle. Specific annual NASS Cotton Ginning Annual Summary reports, ERS Cotton and Wool Outlook reports, and AMS cotton ginning reports were consulted; homepage URLs are provided for general navigation as specific report URLs are not persistent.

---

## 3. Cotton Processing System

### 3.1 Process Description

Cotton processing consists of two distinct stages: ginning (Stage 1) and cottonseed crushing (Stage 2).

**Stage 1: Cotton Ginning**

1. **Receiving and drying:** Seed cotton is received at the gin and dried to the optimal moisture level (~6–8%) for efficient ginning.
2. **Cleaning:** Foreign matter (burrs, sticks, leaves, sand, dust) is removed through a series of cylinders and screens.
3. **Ginning:** Seed cotton passes through gin stands where rotating saws pull the lint fibers away from the seed. The lint is separated from the seed.
4. **Lint cleaning:** Ginned lint passes through lint cleaners to remove remaining trash and short fibers (motes).
5. **Baling:** Cleaned lint is compressed into 480-lb bales for market.

**Stage 1 co-products:**
- **Cotton lint:** The primary high-value product — textile fiber.
- **Whole cottonseed:** The seed with short fibers (linters) still attached. This is a **dual-pathway product**: it can be (a) used directly as cattle feed (high-energy, high-protein supplement for dairy rations) without further processing, OR (b) sent to Stage 2 (cottonseed crushing) to produce oil, meal, hulls, and linters. The allocation depends on which pathway is used (see Section 6).

**Stage 2: Cottonseed Crushing**

1. **Delinting:** Short fibers (linters) remaining on the seed after ginning are removed in one or two cuts using delinting saws.
2. **Dehulling:** Seed hulls are partially removed using bar knives or impact dehullers. In typical commercial practice, partial dehulling removes ~70–80% of hulls; the remainder stays with the kernel and ends up in the meal.
3. **Flaking and conditioning:** Dehulled kernels (meats) are flaked and heated to improve oil extractability.
4. **Pressing:** Mechanical screw presses (expellers) remove ~50–60% of the oil, producing a pressed cake.
5. **Solvent extraction:** Hexane extracts the remaining oil from the pressed cake.
6. **Desolventizing and toasting:** Meal is heated to remove residual hexane and toast the protein (reducing gossypol toxicity).
7. **Hull blending:** Some hulls may be added back to the meal to achieve the target protein specification (41% protein meal requires ~10–15% hull addition).

**Stage 2 co-products:**
- **Cottonseed oil:** The primary high-value product — cooking oil, shortening, soap, biodiesel.
- **Cottonseed meal:** Protein-rich animal feed (41–44% protein, solvent-extracted).
- **Cottonseed hulls:** Low-value roughage for cattle feed, mulch.
- **Cottonseed linters:** Cellulose fiber for chemical cellulose, medical pads, paper, batting.

> **Note on dual pathway for whole cottonseed:** Whole cottonseed is unique among intermediate products in this review because it has a significant market as a standalone final product (cattle feed). In practice, a portion of the cottonseed produced at the gin is sold directly to dairy operations, and the remainder is crushed. This creates two distinct allocation scenarios that must be clearly separated:
> - **Pathway A (cottonseed used directly):** Stage 1 only. Two final products: lint and whole cottonseed. The allocation is simply the Stage 1 result.
> - **Pathway B (cottonseed crushed):** Stage 1 + Stage 2. The seed's burden from Stage 1 is cascaded through Stage 2 into 4 final products (oil, meal, hulls, linters). The Stage 2 allocations are expressed as sub-shares of the cottonseed's share, so their sum never exceeds the cottonseed's Stage 1 allocation.
>
> **Critical distinction between pathways for economic allocation:** In Pathway A, cottonseed is valued at its market price as whole cottonseed ($290/t). In Pathway B, cottonseed is valued at its **derived value** — the sum of its downstream co-product revenues ($373.63/t cottonseed = $224.18/t seed cotton). Because the derived value exceeds the market price (the processing adds value), cottonseed carries a larger share of the total economic burden in Pathway B (26.9%) than in Pathway A (22.3%), and lint's share correspondingly decreases from 77.7% to 73.1%. For mass allocation, DM is conserved, so lint's mass allocation is essentially the same in both pathways (38.5%).
>
> The complete data table (Section 8) and cascade allocation (Section 6) present Pathway B results, with the Stage 2 products' allocations always summing to the whole cottonseed's share (26.9% economic, 61.5% mass).

### 3.2 Process Flow

```
STAGE 1: COTTON GINNING

1 t seed cotton at 90% DM (0.900 t DM)
        │
        ▼
  ┌─ COTTON GINNING ──────────────────────────────┐
  │                                                 │
  │  Gin trash / losses: ~0.02 t as-is (~2%)       │
  │  (burrs, sticks, motes, fine debris)            │
  │  DM losses: ~0.012 t DM (1.3%)                 │
  │                                                 │
  │  Cotton lint: 0.38 t at 90% DM              ◄── co-product (final)
  │    (0.342 t DM)                                │
  │                                                 │
  │  Whole cottonseed: 0.60 t at 91% DM         ◄── DUAL PATHWAY:
  │    (0.546 t DM)                                   Pathway A: final product (cattle feed)
  │                                                    Pathway B: intermediate → Stage 2
  └─────────────────────────────────────────────────┘

PATHWAY A: COTTONSEED USED DIRECTLY (as cattle feed)
  → Two final products: lint + whole cottonseed
  → Allocation: Lint 77.7%, Seed 22.3% (economic)
              Lint 38.5%, Seed 61.5% (mass)

PATHWAY B: COTTONSEED CRUSHED (Stage 2)

0.60 t whole cottonseed (= 1 t cottonseed at 91% DM = 0.910 t DM)
        │
        ▼
  ┌─ COTTONSEED CRUSHING ─────────────────────────┐
  │                                                 │
  │  Processing losses: ~0.01 t as-is (~1%)        │
  │  (handling, residual solvent, moisture)         │
  │  DM losses: ~0.009 t DM (0.96%)                │
  │                                                 │
  │  Cottonseed oil: 0.17 t at 100% DM          ◄── co-product (final)
  │    (0.170 t DM)                                │
  │                                                 │
  │  Cottonseed meal: 0.475 t at 88% DM         ◄── co-product (final)
  │    (0.418 t DM)                                │
  │                                                 │
  │  Cottonseed hulls: 0.275 t at 90% DM       ◄── co-product (final)
  │    (0.2475 t DM)                               │
  │                                                 │
  │  Cottonseed linters: 0.07 t at 94% DM      ◄── co-product (final)
  │    (0.0658 t DM)                               │
  │                                                 │
  └─────────────────────────────────────────────────┘

PATHWAY B — CASCADE ALLOCATION (per 1 t seed cotton):
  All values on seed cotton basis. The 4 Stage 2 products are sub-shares
  of the cottonseed's Stage 1 allocation. Their allocations always sum to
  the cottonseed's share.

  ECONOMIC ALLOCATION:              MASS ALLOCATION:
  (cottonseed valued at derived     (DM conserved → same as
   value = $224.18/t seed cotton)    direct allocation)

  Lint:     73.1% (cascade S1)      Lint:     38.5% (same as direct)
  Oil:      12.2% (26.9%×45.5%)     Oil:      11.6% (61.5%×18.9%)
  Meal:     11.1% (26.9%×41.3%)     Meal:     28.5% (61.5%×46.4%)
  Hulls:     1.8% (26.9%×6.6%)      Hulls:    16.9% (61.5%×27.5%)
  Linters:   1.8% (26.9%×6.6%)      Linters:   4.5% (61.5%×7.3%)
  ─────────────────                  ─────────────────
  Total:   100.0%                    Total:   100.0%
  (Seed-derived: 26.9%)              (Seed-derived: 61.5%)

  KEY: Lint econ 73.1% ≠ 77.7% (direct) because cottonseed's
  derived value ($224.18) > market price ($174.00), increasing
  cottonseed's share of the economic pie.
  Lint mass 38.5% ≈ 38.5% (direct) because DM is conserved.
```

---

## 4. Co-Product Yields and Properties

### 4.1 Stage 1: Cotton Ginning Yields

| Co-product | Yield (t/t seed cotton) | Range | Source & Calculation |
|------------|------------------------|-------|---------------------|
| **Cotton lint** | 0.38 | 0.36–0.40 | Midpoint of range. Industry average for US upland cotton ginning [^1^][^6^]. The 0.38 value is the mathematical midpoint of the stated range. Lint turnout varies with variety, growing conditions, and gin efficiency. Higher micronaire cotton tends to have higher lint turnout. |
| **Whole cottonseed** | 0.60 | 0.58–0.62 | Midpoint of range. Complement to lint yield [^1^][^6^]. The 0.60 value is the mathematical midpoint. Seed yield is inversely related to lint turnout. |

> **Note on yield relationship:** Lint and seed yields are inversely related. The values (0.38 lint, 0.60 seed) sum to 0.98 t/t, leaving 2% for gin trash (burrs, sticks, motes, and fine debris).

### 4.2 Stage 2: Cottonseed Crushing Yields

| Co-product | Yield (t/t whole cottonseed) | Range | Source & Calculation |
|------------|------------------------------|-------|---------------------|
| **Cottonseed oil** | 0.17 | 0.16–0.18 | Midpoint of range. Industry average for solvent extraction [^7^][^10^]. The 0.17 value is the mathematical midpoint. Expeller-only yields are ~0.13–0.16 t/t; solvent extraction achieves ~0.16–0.18 t/t. |
| **Cottonseed meal** | 0.475 | 0.45–0.50 | Midpoint of range. Represents 41% protein, solvent-extracted meal with some residual hulls [^7^][^10^]. The 0.475 value is the mathematical midpoint. Meal yield varies with protein specification (41% protein = higher yield with more hulls; 44% protein = lower yield with fewer hulls) and oil extraction efficiency. |
| **Cottonseed hulls** | 0.275 | 0.25–0.30 | Midpoint of range. Represents separated hulls after partial dehulling [^7^]. The 0.275 value is the mathematical midpoint. Hull yield depends on the degree of dehulling: more complete dehulling produces more separated hulls but reduces meal yield and meal protein content. |
| **Cottonseed linters** | 0.07 | 0.05–0.09 | Midpoint of range. Represents combined first-cut and second-cut linters [^7^][^10^]. The 0.07 value is the mathematical midpoint. Linters yield varies with delinting method (saw-type vs. abrasive), number of cuts, and seed variety. |

> **Note on yield relationships:** Oil and meal yields are inversely related (more oil extraction means less meal). Hull yield depends on the degree of dehulling. Linters are removed before dehulling and oil extraction. The four co-products sum to 0.99 t/t (0.17 + 0.475 + 0.275 + 0.07), with ~1% processing losses.

> **Note on basis for Pathway B:** Section 4.2 shows Stage 2 yields per tonne of whole cottonseed (the natural processing basis). For Pathway B calculations (Sections 6.3 and 8), these yields are converted to a seed cotton basis by multiplying by the cottonseed yield (0.60 t seed/t seed cotton): Oil 0.102, Meal 0.285, Hulls 0.165, Linters 0.042 t/t seed cotton. All Pathway B results are presented on this consistent seed cotton basis.

### 4.3 Dry Matter Contents

**Stage 1:**

| Co-product | DM (%) | Basis |
|------------|--------|-------|
| Cotton lint | 90.0% | Cotton lint at the gin typically has 8–12% moisture. The USDA marketing standard is 8.5% moisture (91.5% DM), but actual moisture varies significantly with harvesting conditions and gin drying. The 90% DM value is a reasonable industry average for lint at the gin [^1^]. |
| Whole cottonseed | 91.0% | Whole cottonseed (with linters attached) typically has 8–10% moisture. The 91% DM value is consistent with industry data for cottonseed entering the oil mill [^7^]. |

**Stage 2:**

| Co-product | DM (%) | Basis |
|------------|--------|-------|
| Cottonseed oil | 100.0% | Crude and refined cottonseed oil are essentially pure lipid with negligible moisture (<0.1%). |
| Cottonseed meal | 88.0% | Standard trading specification: maximum 12% moisture = minimum 88% DM [^10^]. Solvent-extracted, 41% protein meal is typically delivered at 10–12% moisture. Consistent with the 88% DM used for all other oilseed meals in this review (soybean, canola, sunflower, safflower, flaxseed). |
| Cottonseed hulls | 90.0% | Cottonseed hulls are typically 89–91% DM (9–11% moisture). The 90% DM value represents the industry average [^10^]. |
| Cottonseed linters | 94.0% | Cotton linters are cellulose fibers with low moisture content (5–7% moisture, 93–95% DM). The 94% DM value represents the industry average for mechanically delinted linters [^7^]. |



### 4.4 DM Output per Tonne

**Stage 1 (per tonne of seed cotton):**

| Co-product | Calculation | DM Output (t/t seed cotton) |
|------------|-------------|----------------------------|
| **Cotton lint** | 0.38 × 0.90 | **0.3420** |
| **Whole cottonseed** | 0.60 × 0.91 | **0.5460** |
| **Total** | | **0.8880** |

**Stage 2 (per tonne of whole cottonseed):**

| Co-product | Calculation | DM Output (t/t cottonseed) |
|------------|-------------|---------------------------|
| **Cottonseed oil** | 0.17 × 1.00 | **0.1700** |
| **Cottonseed meal** | 0.475 × 0.88 | **0.4180** |
| **Cottonseed hulls** | 0.275 × 0.90 | **0.2475** |
| **Cottonseed linters** | 0.07 × 0.94 | **0.0658** |
| **Total** | | **0.9013** |

**Pathway B: Cascade DM Output (per tonne of seed cotton):**

All 5 final products on a common seed cotton basis. Stage 2 DM outputs are converted by multiplying by the cottonseed yield (0.60 t seed/t seed cotton).

| Co-product | Calculation | DM Output (t/t seed cotton) |
|------------|-------------|----------------------------|
| **Cotton lint** | 0.38 × 0.90 | **0.3420** |
| **Cottonseed oil** | 0.60 × 0.17 × 1.00 | **0.1020** |
| **Cottonseed meal** | 0.60 × 0.475 × 0.88 | **0.2508** |
| **Cottonseed hulls** | 0.60 × 0.275 × 0.90 | **0.1485** |
| **Cottonseed linters** | 0.60 × 0.07 × 0.94 | **0.0395** |
| **Total** | | **0.8828** |
| *DM input (1 t seed cotton at 90% DM)* | | *0.9000* |
| *DM balance gap (combined losses)* | | *−0.0172 (1.91%)* |

> **Note on DM balance:** The total DM output of 0.8828 t is 1.91% below the 0.9000 t DM input. This combines Stage 1 losses (gin trash, 1.33% of seed cotton DM) and Stage 2 losses (processing, 0.96% of cottonseed DM × 0.60 = 0.58% of seed cotton DM). The total 1.91% gap is well within acceptable limits. Critically, this total is less than 1.0, confirming that DM is properly conserved.
---

## 5. Prices

### 5.1 Stage 1 Prices

| Co-product | Price (USD/t) | Range | Source | Notes |
|------------|--------------|-------|--------|-------|
| **Cotton lint** | 1,600 | 1,200–2,000 | USDA ERS [^3^]; ICE Futures U.S. [^5^] | 2024–2025 average for US upland cotton (strict low middling 1-1/16" staple). Equivalent to ~$0.73/lb. Prices vary with quality (staple length, micronaire, strength, color grade) and market conditions. Midpoint of range: ($1,200 + $2,000) / 2 = $1,600. |
| **Whole cottonseed** | 290 | 200–380 | USDA ERS [^3^]; NCPA [^10^]; industry estimates | 2024–2025 average for whole cottonseed at the oil mill or feed lot. Used as cattle feed or sold for crushing. Price depends on proximity to oil mills, dairy demand, and seasonal supply. Midpoint of range: ($200 + $380) / 2 = $290. |

### 5.2 Stage 2 Prices

| Co-product | Price (USD/t) | Range | Source | Notes |
|------------|--------------|-------|--------|-------|
| **Cottonseed oil** | 1,000 | 800–1,200 | USDA ERS [^3^] | 2024–2025 average for crude cottonseed oil (FOB). Prices track other vegetable oils but at a discount to soybean oil. Used for cooking oil, shortening, soap, and biodiesel. Midpoint of range: ($800 + $1,200) / 2 = $1,000. |
| **Cottonseed meal** | 325 | 250–400 | USDA ERS [^3^]; Feedipedia [^8^]; NCPA [^10^] | 2024–2025 average for solvent-extracted, 41% protein meal. Prices vary with protein content and regional demand. 44% protein meal commands ~$30–50/t premium. Midpoint of range: ($250 + $400) / 2 = $325. |
| **Cottonseed hulls** | 90 | 60–120 | Feedipedia [^8^]; NCPA [^10^]; university extension feed reports | 2024–2025 average for cottonseed hulls used as cattle feed roughage. Low-value product; price varies with proximity to dairy operations. Some markets price hulls at $0 (given away) when transportation costs exceed value. Midpoint of range: ($60 + $120) / 2 = $90. |
| **Cottonseed linters** | 350 | 200–500 | NCPA [^10^]; O'Brien et al. [^7^]; industry estimates | 2024–2025 average across linter grades and end uses. First-cut linters (longer fibers, chemical cellulose): ~$300–600/t. Second-cut linters (shorter fibers, batting/paper): ~$150–350/t. Blended average: ~$350/t. Midpoint of range: ($200 + $500) / 2 = $350. |

### 5.3 Price Verification

**Cotton lint:**

```
ICE Futures U.S. Cotton No. 2 (2025): ~$0.65-0.85/lb = $1,430-1,875/t
USDA ERS (2025): average spot price ~$0.70-0.80/lb = $1,540-1,765/t
Historical range (2020-2025): $0.50-1.50/lb = $1,100-3,300/t

Selected midpoint: $1,600/t
Mathematical midpoint of range ($1,200-2,000): $1,600/t ✓
The price midpoint IS the true mathematical midpoint of the stated range.
```

**Whole cottonseed:**

```
USDA ERS (2025): ~$220-320/t (at the oil mill)
NCPA (2025): ~$200-350/t
Feed value premium during drought: up to $380/t

Selected midpoint: $290/t
Mathematical midpoint of range ($200-380): $290/t ✓
The price midpoint IS the true mathematical midpoint of the stated range.
```

**Cottonseed oil:**

```
USDA ERS (2025): crude cottonseed oil ~$850-1,050/t
Feedipedia indicative values: ~$800-1,100/t
Discount to soybean oil: typically $50-150/t

Selected midpoint: $1,000/t
Mathematical midpoint of range ($800-1,200): $1,000/t ✓
The price midpoint IS the true mathematical midpoint of the stated range.
```

**Cottonseed meal:**

```
USDA ERS (2025): 41% protein meal ~$280-380/t
NCPA (2025): ~$250-400/t
Feedipedia indicative values: comparable to canola meal (~$250-350/t)

Selected midpoint: $325/t
Mathematical midpoint of range ($250-400): $325/t ✓
The price midpoint IS the true mathematical midpoint of the stated range.
```

### 5.4 Revenue per Tonne

**Stage 1 (per tonne of seed cotton) — Pathway A:**

| Co-product | Calculation | Revenue (USD/t seed cotton) |
|------------|-------------|----------------------------|
| **Cotton lint** | 0.38 × 1,600 | **$608.00** |
| **Whole cottonseed** | 0.60 × 290 | **$174.00** |
| **Total** | | **$782.00** |

**Stage 2 (per tonne of whole cottonseed):**

| Co-product | Calculation | Revenue (USD/t cottonseed) |
|------------|-------------|---------------------------|
| **Cottonseed oil** | 0.17 × 1,000 | **$170.00** |
| **Cottonseed meal** | 0.475 × 325 | **$154.38** |
| **Cottonseed hulls** | 0.275 × 90 | **$24.75** |
| **Cottonseed linters** | 0.07 × 350 | **$24.50** |
| **Total** | | **$373.63** |

**Pathway B: Cascade Revenue (per tonne of seed cotton):**

All 5 final products on a common seed cotton basis. Stage 2 revenues are converted by multiplying by the cottonseed yield (0.60 t seed/t seed cotton).

| Co-product | Calculation | Revenue (USD/t seed cotton) |
|------------|-------------|----------------------------|
| **Cotton lint** | 0.38 × 1,600 | **$608.00** |
| **Cottonseed oil** | 0.102 × 1,000 | **$102.00** |
| **Cottonseed meal** | 0.285 × 325 | **$92.63** |
| **Cottonseed hulls** | 0.165 × 90 | **$14.85** |
| **Cottonseed linters** | 0.042 × 350 | **$14.70** |
| **Total** | | **$832.18** |

> **Note on intermediate product valuation:** The whole cottonseed market price revenue is $174.00/t seed cotton (0.60 × $290), while the derived value (sum of co-product revenues) is $224.18/t seed cotton (0.60 × $373.63). The derived value exceeds the market price by $50.18/t seed cotton ($83.63/t cottonseed), representing the gross processing margin before deducting crushing costs. In Pathway A, cottonseed is valued at its market price, giving total revenue of $782.00/t seed cotton. In Pathway B, cottonseed is valued at its derived value (the revenue its co-products generate), giving total revenue of $832.18/t seed cotton. This distinction is critical for cascade economic allocation: the larger economic pie in Pathway B reduces lint's economic share from 77.7% to 73.1%, while cottonseed-derived products carry 26.9% (vs. 22.3% in Pathway A).

---

## 6. Allocation Methodology

### 6.1 Dual Pathway Overview

Whole cottonseed has a **dual pathway**: it can be used directly as cattle feed (Pathway A) or crushed into 4 products (Pathway B). The allocation depends on which pathway is used.

**Pathway A — Cottonseed used directly (Stage 1 only):**

Two final products: cotton lint and whole cottonseed. The allocation is simply the Stage 1 result (Section 6.2). Cottonseed is valued at its market price ($290/t).

**Pathway B — Cottonseed crushed (Stage 1 + Stage 2 cascade):**

The seed's share of Stage 1 burden is cascaded through Stage 2 and distributed among 4 final products (oil, meal, hulls, linters). The Stage 2 products' allocations are **sub-shares of the cottonseed's share** — they always sum to the cottonseed's Stage 1 allocation and never exceed it.

**Critical difference for economic allocation:** In Pathway B, cottonseed is valued at its **derived value** (the sum of its 4 co-product revenues: $224.18/t seed cotton) rather than its market price ($174.00/t seed cotton). Because the derived value is higher, cottonseed carries a larger share of the total economic burden (26.9% vs. 22.3%), and lint's share correspondingly decreases (73.1% vs. 77.7%). This reflects the economic reality that processing cottonseed creates additional value — the co-products are collectively worth more than the raw seed.

**For mass allocation,** DM is conserved regardless of processing pathway, so lint's mass allocation is essentially the same in both pathways (38.5%). The small Stage 2 DM losses (0.96%) do not meaningfully change lint's proportional share.

```
Pathway A (seed at market price):   Pathway B (seed at derived value):
  Lint:       77.7% (econ)           Lint:       73.1% (econ, cascade S1)
  Seed:       22.3% (econ)           Oil:        12.2% = 26.9% × 45.5%
                                     Meal:       11.1% = 26.9% × 41.3%
                                     Hulls:       1.8% = 26.9% × 6.6%
                                     Linters:     1.8% = 26.9% × 6.6%
                                     ─────────────────────────────────
                                     Seed-derived: 26.9% (= cottonseed's share)
                                     Total:      100.0%

  Lint:       38.5% (mass)           Lint:       38.5% (mass, same as direct)
  Seed:       61.5% (mass)           Oil:        11.6% = 61.5% × 18.9%
                                     Meal:       28.5% = 61.5% × 46.4%
                                     Hulls:      16.9% = 61.5% × 27.5%
                                     Linters:     4.5% = 61.5% × 7.3%
                                     ─────────────────────────────────
                                     Seed-derived: 61.5% (= cottonseed's share)
                                     Total:      100.0%
```

> **Critical point:** Under Pathway B, the 4 Stage 2 economic allocations (12.2% + 11.1% + 1.8% + 1.8% = 26.9%) always sum exactly to the whole cottonseed's Stage 1 share. The same principle applies to mass allocation: the 4 Stage 2 mass allocations (11.6% + 28.5% + 16.9% + 4.5% = 61.5%) sum to the cottonseed's Stage 1 mass share. This ensures that the crushing products never claim more burden than the cottonseed itself carries.

### 6.2 Pathway A: Cotton Ginning Only (seed used directly)

**Economic allocation:**

| Co-product | Calculation | Allocation |
|------------|-------------|------------|
| Cotton lint | (608.00 ÷ 782.00) × 100 | **77.7%** |
| Whole cottonseed | (174.00 ÷ 782.00) × 100 | **22.3%** |
| **Total** | | **100.0%** |

**Mass allocation:**

| Co-product | Calculation | Allocation |
|------------|-------------|------------|
| Cotton lint | (0.3420 ÷ 0.8880) × 100 | **38.5%** |
| Whole cottonseed | (0.5460 ÷ 0.8880) × 100 | **61.5%** |
| **Total** | | **100.0%** |

**Comparison:**

| Co-product | Economic | Mass | Difference |
|------------|----------|------|------------|
| Cotton lint | 77.7% | 38.5% | +39.2 pp |
| Whole cottonseed | 22.3% | 61.5% | −39.2 pp |

The 39.2 pp difference reflects lint's high value-to-mass ratio. Lint commands $1,600/t (5.5× the seed price) but carries only 38.5% of the DM.

### 6.3 Pathway B: Cascade Allocation (seed crushed)

The cascade first assigns burdens in Stage 1 (to lint and seed), then distributes the seed's burden in Stage 2 among 4 final products. All calculations are on a **per-tonne-of-seed-cotton basis**.

**Stage 1 of the cascade (economic):**

In Pathway B, cottonseed is valued at its **derived value** — the total revenue its downstream co-products generate — rather than its market price as whole cottonseed. This is because when cottonseed is crushed, its economic worth to the system is determined by the value of the products it becomes, not by the price at which it could have been sold as a raw material. The derived value ($224.18/t seed cotton = 0.60 × $373.63/t cottonseed) exceeds the market price ($174.00/t seed cotton = 0.60 × $290/t), reflecting the value added by processing.

| Co-product | Revenue (USD/t seed cotton) | Allocation |
|------------|----------------------------|------------|
| Cotton lint | $608.00 | (608.00 ÷ 832.18) × 100 = **73.1%** |
| Cottonseed (at derived value) | $224.18 | (224.18 ÷ 832.18) × 100 = **26.9%** |
| **Total** | **$832.18** | **100.0%** |

> **Why lint's economic share changes:** In Pathway A, the total economic pie is $782.00 (lint $608 + seed at market price $174), and lint gets 77.7%. In Pathway B, the total economic pie is $832.18 (lint $608 + seed at derived value $224.18), and lint gets 73.1%. The pie is larger because cottonseed's derived value ($224.18) exceeds its market price ($174.00) by $50.18 — the gross processing margin. Since lint's revenue is unchanged but the total pie is bigger, lint's share shrinks. This is the correct economic treatment: when cottonseed is further processed, the additional value created by processing increases cottonseed's claim on the total environmental burden.

**Stage 1 of the cascade (mass):**

Mass allocation is based on DM outputs on a seed cotton basis. Since DM is conserved regardless of downstream processing, the Stage 1 mass split is the same as Pathway A.

| Co-product | DM Output (t/t seed cotton) | Allocation |
|------------|----------------------------|------------|
| Cotton lint | 0.3420 | (0.3420 ÷ 0.8880) × 100 = **38.5%** |
| Cottonseed | 0.5460 | (0.5460 ÷ 0.8880) × 100 = **61.5%** |
| **Total** | **0.8880** | **100.0%** |

**Stage 2 internal allocation (reference for cascade sub-shares):**

These internal allocations show how cottonseed's burden is divided among its 4 products within Stage 2. They are **sub-shares of cottonseed's share**, not shares of the total seed cotton burden. They are calculated per tonne of cottonseed and then applied as proportional subdivisions.

*Economic (internal, per tonne of cottonseed):*

| Co-product | Calculation | Internal Allocation |
|------------|-------------|-------------------|
| Cottonseed oil | (170.00 ÷ 373.63) × 100 | **45.5%** |
| Cottonseed meal | (154.38 ÷ 373.63) × 100 | **41.3%** |
| Cottonseed hulls | (24.75 ÷ 373.63) × 100 | **6.6%** |
| Cottonseed linters | (24.50 ÷ 373.63) × 100 | **6.6%** |
| **Total** | | **100.0%** |

*Mass (internal, per tonne of cottonseed):*

| Co-product | Calculation | Internal Allocation |
|------------|-------------|-------------------|
| Cottonseed oil | (0.1700 ÷ 0.9013) × 100 | **18.9%** |
| Cottonseed meal | (0.4180 ÷ 0.9013) × 100 | **46.4%** |
| Cottonseed hulls | (0.2475 ÷ 0.9013) × 100 | **27.5%** |
| Cottonseed linters | (0.0658 ÷ 0.9013) × 100 | **7.3%** |
| **Total** | | **100.0%** |

**Economic cascade (primary result):**

| Final co-product | Calculation | Allocation | Sub-share of seed's 26.9% |
|-----------------|-------------|------------|--------------------------|
| Cotton lint | Direct from Stage 1 | **73.1%** | — |
| Cottonseed oil | 26.9% × 45.5% | **12.2%** | 45.5% of seed's share |
| Cottonseed meal | 26.9% × 41.3% | **11.1%** | 41.3% of seed's share |
| Cottonseed hulls | 26.9% × 6.6% | **1.8%** | 6.6% of seed's share |
| Cottonseed linters | 26.9% × 6.6% | **1.8%** | 6.6% of seed's share |
| **Total** | | **100.0%** | |
| *Seed-derived subtotal* | *12.2 + 11.1 + 1.8 + 1.8* | *26.9%* | *= cottonseed's Stage 1 share* |

**Mass cascade (primary result):**

| Final co-product | Calculation | Allocation | Sub-share of seed's 61.5% |
|-----------------|-------------|------------|--------------------------|
| Cotton lint | Direct from Stage 1 | **38.5%** | — |
| Cottonseed oil | 61.5% × 18.9% | **11.6%** | 18.9% of seed's share |
| Cottonseed meal | 61.5% × 46.4% | **28.5%** | 46.4% of seed's share |
| Cottonseed hulls | 61.5% × 27.5% | **16.9%** | 27.5% of seed's share |
| Cottonseed linters | 61.5% × 7.3% | **4.5%** | 7.3% of seed's share |
| **Total** | | **100.0%** | |
| *Seed-derived subtotal* | *11.6 + 28.5 + 16.9 + 4.5* | *61.5%* | *= cottonseed's Stage 1 share* |

**Cascade comparison:**

| Final co-product | Economic (cascade) | Mass (cascade) | Difference |
|-----------------|-------------------|----------------|------------|
| Cotton lint | 73.1% | 38.5% | +34.6 pp |
| Cottonseed oil | 12.2% | 11.6% | +0.6 pp |
| Cottonseed meal | 11.1% | 28.5% | −17.4 pp |
| Cottonseed hulls | 1.8% | 16.9% | −15.1 pp |
| Cottonseed linters | 1.8% | 4.5% | −2.7 pp |

**Pathway comparison (direct vs. cascade):**

| Co-product | Econ — Direct (A) | Econ — Cascade (B) | Difference | Mass — Direct (A) | Mass — Cascade (B) | Difference |
|------------|-------------------|-------------------|------------|-------------------|-------------------|------------|
| Cotton lint | 77.7% | 73.1% | −4.6 pp | 38.5% | 38.5% | 0.0 pp |
| Cottonseed / seed-derived | 22.3% | 26.9% | +4.6 pp | 61.5% | 61.5% | 0.0 pp |

> **Key insight:** The economic allocation of lint differs between pathways (77.7% direct vs. 73.1% cascade) because cottonseed's derived value ($224.18) exceeds its market price ($174.00), increasing cottonseed's share of the larger economic pie. The mass allocation of lint is the same in both pathways (38.5%) because DM is conserved — the mass of cottonseed derivatives equals the mass of cottonseed, so the proportional split is unchanged. This asymmetry between economic and mass allocation in the cascade is the correct and expected result.

### 6.4 Stage 2 Internal Allocation (reference for cascade calculations)

The Stage 2 internal allocations show how the cottonseed's burden is divided among its 4 products. These are **sub-shares of the cottonseed's share**, not shares of the total seed cotton burden. They are provided here for transparency and to document the cascade calculation inputs.

**Stage 2 economic allocation (internal, per tonne of cottonseed):**

| Co-product | Calculation | Internal Allocation |
|------------|-------------|-------------------|
| Cottonseed oil | (170.00 ÷ 373.63) × 100 | **45.5%** |
| Cottonseed meal | (154.38 ÷ 373.63) × 100 | **41.3%** |
| Cottonseed hulls | (24.75 ÷ 373.63) × 100 | **6.6%** |
| Cottonseed linters | (24.50 ÷ 373.63) × 100 | **6.6%** |
| **Total** | | **100.0%** |

**Stage 2 mass allocation (internal, per tonne of cottonseed):**

| Co-product | Calculation | Internal Allocation |
|------------|-------------|-------------------|
| Cottonseed oil | (0.1700 ÷ 0.9013) × 100 | **18.9%** |
| Cottonseed meal | (0.4180 ÷ 0.9013) × 100 | **46.4%** |
| Cottonseed hulls | (0.2475 ÷ 0.9013) × 100 | **27.5%** |
| Cottonseed linters | (0.0658 ÷ 0.9013) × 100 | **7.3%** |
| **Total** | | **100.0%** |

> **Note:** These internal allocations sum to 100% of the cottonseed's burden, not 100% of the seed cotton burden. To convert to seed cotton basis, multiply by the cottonseed's Stage 1 share: economic × 26.9%, mass × 61.5%. See Section 6.3 for the cascade results.

---

## 7. Mass Balance Verification

### 7.1 Stage 1: Cotton Ginning

| Check | Value | Status |
|-------|-------|--------|
| Input: Seed cotton at 90% DM | 1.000 t | — |
| Input DM | 0.900 t | — |
| Output: Cotton lint (as-is) | 0.380 t | ✓ |
| Output: Whole cottonseed (as-is) | 0.600 t | ✓ |
| Total as-is output | 0.980 t | 98.0% of input |
| Gin trash / losses (as-is) | 0.020 t | 2.0% of input ✓ |
| Output DM: Lint | 0.342 t | ✓ |
| Output DM: Seed | 0.546 t | ✓ |
| Total DM output | 0.888 t | 98.7% of input DM ✓ |

**Stage 1 DM Balance Detail:**

| Item | Value | Notes |
|------|-------|-------|
| Input DM (1 t seed cotton at 90% DM) | 0.9000 t | 1.000 × 0.90 |
| **Output DM — co-products:** | | |
| Cotton lint | 0.3420 t | 0.38 t × 90% DM |
| Whole cottonseed | 0.5460 t | 0.60 t × 91% DM |
| Total co-product DM | **0.8880 t** | |
| DM balance gap | −0.0120 t | −1.33% of input DM |

> **Balance assessment:** The DM output is 0.012 t (1.33%) below the DM input. This deficit represents gin trash (burrs, sticks, motes, and fine debris) that is removed during cleaning and ginning but not captured as a co-product. The 1.33% DM gap is well within the acceptable range and consistent with industry data showing 2–5% gin trash by weight (at ~60–70% DM).

### 7.2 Stage 2: Cottonseed Crushing

| Check | Value | Status |
|-------|-------|--------|
| Input: Whole cottonseed at 91% DM | 1.000 t | — |
| Input DM | 0.910 t | — |
| Output: Cottonseed oil (as-is) | 0.170 t | ✓ |
| Output: Cottonseed meal (as-is) | 0.475 t | ✓ |
| Output: Cottonseed hulls (as-is) | 0.275 t | ✓ |
| Output: Cottonseed linters (as-is) | 0.070 t | ✓ |
| Total as-is output | 0.990 t | 99.0% of input |
| Processing losses (as-is) | 0.010 t | 1.0% of input ✓ |
| Output DM: Oil | 0.1700 t | ✓ |
| Output DM: Meal | 0.4180 t | ✓ |
| Output DM: Hulls | 0.2475 t | ✓ |
| Output DM: Linters | 0.0658 t | ✓ |
| Total DM output | 0.9013 t | 99.0% of input DM ✓ |

**Stage 2 DM Balance Detail:**

| Item | Value | Notes |
|------|-------|-------|
| Input DM (1 t cottonseed at 91% DM) | 0.9100 t | 1.000 × 0.91 |
| **Output DM — co-products:** | | |
| Cottonseed oil | 0.1700 t | 0.17 t × 100% DM |
| Cottonseed meal | 0.4180 t | 0.475 t × 88% DM |
| Cottonseed hulls | 0.2475 t | 0.275 t × 90% DM |
| Cottonseed linters | 0.0658 t | 0.07 t × 94% DM |
| Total co-product DM | **0.9013 t** | |
| DM balance gap | −0.0087 t | −0.96% of input DM |

> **Balance assessment:** The DM output is 0.0087 t (0.96%) below the DM input. This small deficit represents processing losses (handling, residual solvent, moisture adjustment, fines) and is well within the acceptable range. 

### 7.3 As-Is Mass Balance

**Stage 1:**

| Item | Value | Notes |
|------|-------|-------|
| Input (seed cotton) | 1.000 t | — |
| **Output:** | | |
| Cotton lint | 0.380 t | — |
| Whole cottonseed | 0.600 t | — |
| **Total output** | **0.980 t** | |
| **Gin trash / losses** | **0.020 t** | 2.0%: burrs, sticks, motes, fine debris |
| **Balance** | **1.000 t** | ✓ Exact |

**Stage 2:**

| Item | Value | Notes |
|------|-------|-------|
| Input (whole cottonseed) | 1.000 t | — |
| **Output:** | | |
| Cottonseed oil | 0.170 t | — |
| Cottonseed meal | 0.475 t | — |
| Cottonseed hulls | 0.275 t | — |
| Cottonseed linters | 0.070 t | — |
| **Total output** | **0.990 t** | |
| **Processing losses** | **0.010 t** | 1.0%: handling, moisture loss, fines |
| **Balance** | **1.000 t** | ✓ Exact |

### 7.4 Cascade DM Balance (Pathway B, per tonne of seed cotton)

All 5 final products on a common seed cotton basis, confirming that total DM does not exceed 1.0.

| Item | Value | Notes |
|------|-------|-------|
| Input DM (1 t seed cotton at 90% DM) | 0.9000 t | |
| **Output DM — final co-products:** | | |
| Cotton lint | 0.3420 t | 0.38 × 0.90 |
| Cottonseed oil | 0.1020 t | 0.60 × 0.17 × 1.00 |
| Cottonseed meal | 0.2508 t | 0.60 × 0.475 × 0.88 |
| Cottonseed hulls | 0.1485 t | 0.60 × 0.275 × 0.90 |
| Cottonseed linters | 0.0395 t | 0.60 × 0.07 × 0.94 |
| **Total co-product DM** | **0.8828 t** | |
| DM balance gap | −0.0172 t | −1.91% of input DM |

> **Balance assessment:** The total cascade DM output is 0.8828 t, which is 1.91% below the 0.9000 t DM input. This gap combines Stage 1 losses (gin trash, 0.0120 t = 1.33% of input DM) and Stage 2 losses (processing, 0.0052 t = 0.58% of input DM). The total is well within acceptable limits.

---

## 8. Complete Data Table

**Pathway A: Cottonseed used directly (Stage 1 only)**

| Parent Crop | Crop System | Stage | USDA Standard | Standard Moisture | Parent Input Basis | Co-product Stream | Yield (t/t seed cotton) | Yield Range | Price (USD/t) | Price Range | DM (%) | DM Output (t/t seed cotton) | Revenue (USD/t seed cotton) | Econ Alloc (%) | Mass Alloc (%) |
|-------------|-------------|-------|---------------|-------------------|-------------------|-------------------|-------------|-------------|---------------|-------------|--------|-----------------|-----------------|----------------|----------------|
| Cotton | Cotton ginning | Stage 1 | USDA AMS HVI classing | ~10% (seed cotton) | 1 t seed cotton at 90% DM | Cotton lint | 0.38 | 0.36–0.40 | 1,600 | 1,200–2,000 | 90.0 | 0.3420 | 608.00 | 77.7 | 38.5 |
| Cotton | Cotton ginning | Stage 1 | USDA AMS HVI classing | ~10% (seed cotton) | 1 t seed cotton at 90% DM | Whole cottonseed | 0.60 | 0.58–0.62 | 290 | 200–380 | 91.0 | 0.5460 | 174.00 | 22.3 | 61.5 |

**Pathway B: Cottonseed crushed (Stage 1 + Stage 2 cascade)**

All values below are on a **per-tonne-of-seed-cotton basis** for consistency. Stage 2 yields, DM outputs, and revenues are converted from the per-cottonseed basis (Section 4.2) by multiplying by the cottonseed yield (0.60 t seed/t seed cotton). The Stage 2 products' allocations are sub-shares of the cottonseed's 26.9% (economic) or 61.5% (mass), and their sum never exceeds the cottonseed's share.

| Parent Crop | Crop System | Stage | USDA Standard | Standard Moisture | Parent Input Basis | Co-product Stream | Yield (t/t seed cotton) | Yield Range | Price (USD/t) | Price Range | DM (%) | DM Output (t/t seed cotton) | Revenue (USD/t seed cotton) | Econ Alloc — cascade (%) | Mass Alloc — cascade (%) |
|-------------|-------------|-------|---------------|-------------------|-------------------|-------------------|-------------|-------------|---------------|-------------|--------|-----------------|-----------------|----------------|----------------|
| Cotton | Cotton ginning | Stage 1 | USDA AMS HVI classing | ~10% (seed cotton) | 1 t seed cotton | Cotton lint | 0.380 | 0.36–0.40 | 1,600 | 1,200–2,000 | 90.0 | 0.3420 | 608.00 | 73.1 | 38.5 |
| Cotton | Cottonseed crushing | Stage 2 | NCPA specifications | ~9% (whole cottonseed) | 1 t seed cotton | Cottonseed oil | 0.102 | 0.096–0.108 | 1,000 | 800–1,200 | 100.0 | 0.1020 | 102.00 | 12.2 (= 26.9% × 45.5%) | 11.6 (= 61.5% × 18.9%) |
| Cotton | Cottonseed crushing | Stage 2 | NCPA specifications | ~9% (whole cottonseed) | 1 t seed cotton | Cottonseed meal | 0.285 | 0.270–0.300 | 325 | 250–400 | 88.0 | 0.2508 | 92.63 | 11.1 (= 26.9% × 41.3%) | 28.5 (= 61.5% × 46.4%) |
| Cotton | Cottonseed crushing | Stage 2 | NCPA specifications | ~9% (whole cottonseed) | 1 t seed cotton | Cottonseed hulls | 0.165 | 0.150–0.180 | 90 | 60–120 | 90.0 | 0.1485 | 14.85 | 1.8 (= 26.9% × 6.6%) | 16.9 (= 61.5% × 27.5%) |
| Cotton | Cottonseed crushing | Stage 2 | NCPA specifications | ~9% (whole cottonseed) | 1 t seed cotton | Cottonseed linters | 0.042 | 0.030–0.054 | 350 | 200–500 | 94.0 | 0.0395 | 14.70 | 1.8 (= 26.9% × 6.6%) | 4.5 (= 61.5% × 7.3%) |
| | | | | | | **Seed-derived subtotal** | | | | | | | | **26.9** (= cottonseed's Stage 1 share) | **61.5** (= cottonseed's Stage 1 share) |
| | | | | | | **Total** | | | | | | **0.8828** | **832.18** | **100.0** | **100.0** |

> **Key principle:** The 4 Stage 2 cascade allocations always sum to the cottonseed's Stage 1 share. For economic allocation: 12.2 + 11.1 + 1.8 + 1.8 = 26.9%. For mass allocation: 11.6 + 28.5 + 16.9 + 4.5 = 61.5%. This ensures that the crushing products never claim more burden than the cottonseed itself carries.

> **Basis conversion note:** Stage 2 yields above are on a seed cotton basis (e.g., Oil 0.102 = 0.60 × 0.17). The per-cottonseed basis yields are: Oil 0.17, Meal 0.475, Hulls 0.275, Linters 0.07 t/t cottonseed (see Section 4.2). Yield ranges above are also on seed cotton basis (e.g., Oil 0.096–0.108 = 0.60 × 0.16–0.18). All DM outputs and revenues are on seed cotton basis, so they can be summed across all rows without basis inconsistency.

> **Stage 2 internal allocations (for reference):** Within Stage 2, the cottonseed's burden is divided as: Oil 45.5%/18.9%, Meal 41.3%/46.4%, Hulls 6.6%/27.5%, Linters 6.6%/7.3% (economic/mass). These internal percentages are the basis for the cascade calculation but are NOT the final allocations — they must be multiplied by the cottonseed's Stage 1 share (26.9% economic, 61.5% mass) to convert to seed cotton basis.

---

## 9. Data Quality and Limitations

### 9.1 High-Confidence Data

| Data Point | Confidence | Source |
|------------|-----------|--------|
| Lint yield (0.38 t/t) | **High** | Well-documented; midpoint of narrow range [^1^][^6^] |
| Seed yield (0.60 t/t) | **High** | Well-documented; midpoint of narrow range [^1^][^6^] |
| Oil yield (0.17 t/t) | **High** | Well-documented for solvent extraction [^7^][^10^] |
| Oil DM% (100%) | **High** | Pure lipid with negligible moisture |
| Meal DM% (88%) | **High** | Industry trading specification (max 12% moisture) [^10^] |
| Lint price ($1,600/t) | **High** | Well-documented commodity with transparent pricing [^3^] |
| DM balances (1.3% and 0.96%) | **High** | Well within acceptable range |

### 9.2 Medium-Confidence Data

| Data Point | Confidence | Source |
|------------|-----------|--------|
| Linters yield (0.07 t/t) | **Medium** | Varies with delinting method and number of cuts; range is 0.05–0.09 |
| Linters price ($350/t) | **Medium** | Wide range ($200–500) reflecting different linter grades and end uses |
| Seed price ($290/t) | **Medium** | Varies with region, season, and dairy demand |
| Hulls yield (0.275 t/t) | **Medium** | Depends on degree of dehulling (partial vs. complete) |
| Hulls price ($90/t) | **Medium** | Low-value product with limited price transparency |
| Meal yield (0.475 t/t) | **Medium** | Depends on protein specification and hull blend |

### 9.3 Known Limitations

1. **Cottonseed linters recovery varies:** Not all cottonseed crushing facilities recover linters as a separate co-product. Some facilities leave linters on the seed (or partially on the hulls), in which case: (a) linters mass is captured in the meal/hulls, (b) there is no separate linters co-product, and (c) meal yield is higher (~0.53–0.55 t/t) and meal protein is lower (~36–38%). This table models the standard commercial practice of linters removal. Studies using data from facilities that do not remove linters should adjust the allocation model accordingly.

2. **Partial dehulling configuration:** This table represents partial dehulling, where ~70–80% of hulls are separated and the remainder stays with the meal. This produces 41% protein meal (the most common grade). Alternative configurations include:
   - **No dehulling:** Meal yield ~0.55–0.60 t/t, ~30–36% protein, lower price; hulls yield ~0.25 t/t
   - **Complete dehulling:** Meal yield ~0.40–0.43 t/t, ~48–50% protein, higher price; hulls yield ~0.35–0.40 t/t
   
   The degree of dehulling significantly affects meal and hulls yields, meal protein content, and prices. Studies should match the dehulling configuration to their specific processing facility.

3. **Gossypol toxicity limits feed use:** Cottonseed products contain gossypol, a naturally occurring polyphenolic compound that is toxic to monogastric animals (poultry, swine) at high concentrations. This limits the use of cottonseed meal primarily to ruminant feed (cattle, sheep). Gossypol also limits the use of whole cottonseed as feed. The gossypol content affects market prices and demand patterns, particularly for meal. Solvent extraction and meal toasting reduce free gossypol levels, but the residual levels still restrict end markets.

4. **Lint quality affects price:** Cotton lint prices vary dramatically with quality (staple length, micronaire, strength, color grade, leaf grade). The $1,600/t midpoint reflects average-quality upland cotton. Premium cotton (long staple, high micronaire, clean) can exceed $2,000/t, while discounted cotton (short staple, low micronaire, high trash) can fall below $1,200/t. The economic allocation is sensitive to lint price: under Pathway A, if lint price drops to $1,200/t, lint's economic allocation drops from 77.7% to ~72%; under Pathway B (cascade), the same price drop reduces lint's allocation from 73.1% to ~67%.

5. **Cottonseed as cattle feed (dual pathway):** Whole cottonseed is a significant cattle feed product, especially for dairy rations (high energy from oil, high protein, effective fiber). In practice, a substantial fraction of cottonseed is fed directly rather than crushed — the split varies by region (more crushing near oil mills, more direct feeding near dairy operations) and season. This document presents both pathways explicitly (see Sections 6.1–6.3 and 8): Pathway A (seed used directly) and Pathway B (seed crushed). LCA practitioners must select the pathway that matches their specific system boundary. If a study covers a mixed system where some seed is fed and some is crushed, a weighted average of the two pathway allocations may be appropriate.

6. **Regional variation:** Cotton ginning and crushing are concentrated in the US South and West (Texas, Georgia, Arkansas, Mississippi, California). Prices, yields, and gin trash composition vary by region due to variety differences, growing conditions, and proximity to end markets. Texas cotton typically has lower lint turnout (~36–38%) than Mississippi Delta cotton (~38–42%).

7. **Organic and non-GMO cotton:** Organic and non-GMO cotton lint commands a significant premium (~$300–800/t above conventional), and organic cottonseed products may also have higher prices. This table uses conventional cotton prices. Studies focused on organic cotton should use organic-specific pricing.

8. **Cottonseed oil as a byproduct vs. co-product:** In some economic frameworks, cottonseed oil is treated as a byproduct (with meal as the primary product) because the crushing decision is driven by meal demand rather than oil demand. This distinction affects the interpretation of economic allocation but does not change the calculation method. Under the co-product framework used in this review, all products with market value are treated equally.

---
