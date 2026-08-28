# Sweet Corn Canning: Co-Product Allocation Methodology, Data Sources, and Calculations

**Document Version:** 1.0   
**Date:** June 2026  
**Basis:** 1 metric ton (t) of fresh sweet corn ears at harvest (~75% moisture)  
**Price Period:** 2024–2025 average (unless otherwise noted)  
---

## Table of Contents

1. [Standard Basis and Conversions](#1-standard-basis-and-conversions)
2. [Data Sources and References](#2-data-sources-and-references)
3. [Sweet-Corn Canning System](#3-sweet-corn-canning-system)
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
| **Parent crop** | Sweet corn (*Zea mays* var. *saccharata*) | — |
| **Input quantity** | 1 metric ton (1,000 kg) of fresh ears in husks | — |
| **Moisture content at harvest** | ~75% (range 70–80%) | USDA NASS [^1^]; industry average for fresh sweet corn at harvest |
| **Dry matter (DM) input** | ~0.25 t DM/t fresh ears | Calculated: 1.000 × (1 − 0.75) = 0.25 |
| **Bushel equivalent** | ~63.0 bushels/t | 1,000 kg ÷ 15.876 kg/bu (35 lb in husks) [^2^] |
| **Bushel weight (in husks)** | 35.0 lb (15.876 kg) | Industry convention [^2^] |

> **Note on bushel weight:** Unlike field corn (which has a standardized USDA bushel weight of 56 lb), sweet corn has no universally standardized USDA bushel weight. The 35 lb/bu figure for sweet corn in husks is an industry convention used for reference purposes only. Sweet corn is commercially traded on a per-ton fresh weight basis, not by the bushel. The bushel equivalent is provided here for cross-commodity comparison only.

### 1.2 Convention for Adopted Values

Every yield, price, and DM% in this document is reported as an adopted point value together with the range it was drawn from. **Unless a row states otherwise, the adopted value is the midpoint of its stated range**, and the range is the parameter that carries the evidence. Two values in this document are not simple midpoints and say so where they appear: the cannery waste yield, which is computed as the residual of the as-is balance (Section 4.1), and the cannery waste price, which is a percentage of a benchmark silage price (Section 5.3). Point values are given to the precision the underlying sources support. This document is self-contained: all reconciliations are internal to sweet corn canning and no comparison is made to other crop processing systems.

### 1.3 Unit Conversions

| Conversion | Factor |
|------------|--------|
| 1 bushel sweet corn (in husks) | 35.0 lb = **15.876 kg** |
| 1 lb | 0.453592 kg = 0.000453592 t |
| 1 t fresh sweet corn ears | **~63.0 bushels** |

### 1.4 Why Sweet Corn Has No "Standard Moisture"

Unlike field corn, which is dried to 15.5% moisture for storage and trading, sweet corn:
- Is harvested at high moisture (70–80%) for immediate processing [^1^]
- Must be processed within hours of harvest to preserve sugar content [^3^]
- Is never stored or traded as a dry commodity
- Is contracted between growers and processors on a **per-ton fresh weight** basis [^3^]

---

## 2. Data Sources and References

### 2.1 Primary Sources

| Citation | Full Title | Type | URL |
|----------|-----------|------|-----|
| [^1^] | USDA NASS (2025). *Vegetables Annual Summary* | Government (USDA) | https://www.nass.usda.gov/ |
| [^2^] | USDA ERS (2025). *Vegetables and Pulses Yearbook Tables* | Government (USDA) | https://ers.usda.gov/ |
| [^3^] | USDA AMS (2025). *Fruit and Vegetable Market News* | Government (USDA) | https://www.ams.usda.gov/ |
| [^4^] | Feedipedia / INRAE / CIRAD / AFZ / FAO. *Corn silage and by-products* | Research Consortium/Database | https://www.feedipedia.org/ |
| [^5^] | Crowley, J.W. & Howard, W.T., rev. Shaver, R.D. (2003). *Sweet Corn (Cannery) By-Products*. University of Wisconsin-Madison, Department of Dairy Science | University/Extension | https://shaverlab.dysci.wisc.edu/wp-content/uploads/sites/204/2015/04/SweetCornReport.pdf |
| [^6^] | Rankin, M. (2015). *Pricing Corn Silage*. University of Wisconsin Extension | University/Extension | https://fyi.extension.wisc.edu/ |
| [^7^] | USDA AMS (2025). *Hay and Forage Market News* | Government (USDA) | https://www.ams.usda.gov/ |

### 2.2 How Sources Were Used

- **Yield data (kernel recovery):** Industry consensus and extension service reports indicate 30–40% kernel recovery from green (fresh) ear weight [^1^][^3^], well established across processing hybrids and cutting styles. The adopted value is the midpoint, 35%.
- **Yield data (waste):** Calculated as the remainder of fresh ear weight after kernel removal, adjusted for process losses. The waste yield range is systematically derived from the kernel yield range (see Section 4.1).
- **DM contents (kernels):** Sweet corn kernels at harvest typically contain 72–78% moisture, i.e. 22–28% DM [^1^][^2^]; the adopted 25% is the midpoint.
- **DM contents (waste):** Cannery waste silage typically contains 75–80% moisture, i.e. 20–25% DM [^4^][^5^]; the adopted 22.5% is the midpoint.
- **Price data (waste):** UW Extension recommends valuing cannery waste at 50–70% of corn silage value [^6^], benchmarked against USDA AMS corn silage prices [^7^]. Applying the midpoint of the guidance (60%) to the midpoint of the silage price range ($37.50/t) gives the adopted $22.50/t.
- **Price data (kernels):** No USDA price series exists for processor-gate sweet corn kernels. The price was estimated from processor economics and wholesale kernel markets (see Section 5.2 for full derivation).

---

## 3. Sweet-Corn Canning System

### 3.1 Process Description

Sweet corn canning involves the following steps:

1. **Receiving:** Fresh ears in husks are delivered to the cannery within hours of harvest.
2. **Husking:** Husks and silks are removed mechanically.
3. **Trimming:** Damaged or undersized ears are culled.
4. **Blanching:** Ears are briefly heated in water to set the milk and loosen the hull.
5. **Cutting:** Kernels are cut from the cob (whole-kernel or cream-style).
6. **Washing/Sorting:** Kernels are washed and inspected.
7. **Canning/Freezing:** Kernels are filled into cans or frozen.
8. **Waste collection:** Husks, cobs, culled ears, stalk fragments, and process water are collected as "cannery waste."

**Co-products generated:**
- **Edible kernels:** The primary product (whole-kernel or cream-style).
- **Cannery waste silage:** A mixture of husks, cobs, culled ears, stalk fragments, and some unrecovered kernels, typically ensiled and fed to livestock.

### 3.2 Process Flow

```
1 t fresh sweet corn ears at ~75% moisture (0.250 t DM)
        │
        ▼
  ┌─ SWEET CORN CANNING ────────────────────────────┐
  │                                                   │
  │  Process losses: ~0.07 t as-is (~7%)             │
  │  (husks/silks blown away, kernel fragments       │
  │   lost in wash water, water evaporation,          │
  │   trimming losses)                                │
  │  DM losses: ~0.032 t DM (12.8%)                  │
  │  (soluble sugars in blanch water, fine particles, │
  │   metabolic losses)                               │
  │                                                   │
  │  Edible kernels: 0.35 t at 25% DM            ◄── co-product
  │    (0.08750 t DM)                                 │
  │                                                   │
  │  Cannery waste silage: 0.58 t at 22.5% DM    ◄── co-product
  │    (0.13050 t DM)                                 │
  │                                                   │
  └───────────────────────────────────────────────────┘

ALLOCATION (single stage, US Domestic):
  Economic:   Kernels 93.9%, Waste 6.1%
  Mass:       Kernels 40.1%, Waste 59.9%
```

---

## 4. Co-Product Yields and Properties

### 4.1 Co-Product Yields

| Co-product | Yield (t/t fresh ears) | Range | Source & Calculation |
|------------|------------------------|-------|---------------------|
| **Edible kernels** | 0.35 | 0.30–0.40 | Industry consensus and extension reporting give 30–40% kernel recovery from green (fresh) ear weight [^1^][^3^]. The adopted 0.35 t/t is the midpoint of that range and represents an industry-average recovery across hybrid types and cutting styles. |
| **Cannery waste silage** | 0.58 | 0.54–0.62 | Derived as the residual of the as-is balance rather than measured directly: waste = 1.0 − kernel yield − process losses. At the adopted kernel yield of 0.35 t/t with ~7% process losses, waste = 1.0 − 0.35 − 0.07 = **0.58 t/t**. The stated band of 0.54–0.62 is a rounded envelope spanning the kernel yield range (0.30–0.40) at a 7–8% loss allowance; see the derivation note below. |

#### Yield Calculation Rationale

**Edible kernels:**

The range reported by industry data and extension sources is **30–40%** of fresh ear weight [^1^][^3^]; the adopted value is its midpoint, 35% (0.35 t/t). This represents an industry-average recovery across:
- Processing hybrids (typically 35–40% recovery)
- Standard cutting styles (whole-kernel and cream-style)
- Commercial cannery operations


**Cannery waste:**

The waste fraction is calculated systematically:
```
Waste yield = 1.0 - kernel yield - process losses

At the adopted kernel yield (0.35 t/t), 7% losses:
  Waste = 1.0 - 0.35 - 0.07 = 0.58 t/t   <- adopted

Bounds across the kernel yield range, at 7-8% losses:
  kernel 0.40, 7% loss -> 0.53 t/t      kernel 0.30, 7% loss -> 0.63 t/t
  kernel 0.40, 8% loss -> 0.52 t/t      kernel 0.30, 8% loss -> 0.62 t/t

Stated band: 0.54-0.62 t/t (rounded envelope inside the above)
```

> **Note on how the waste yield range is bounded:** Because the waste yield is a residual, its bounds depend on both the kernel yield range and the process loss allowance, and the two interact:
>
> | Loss allowance | At kernel yield 0.40 | At kernel yield 0.30 |
> |---|---|---|
> | 7% | 0.53 t/t | 0.63 t/t |
> | 8% | 0.52 t/t | 0.62 t/t |
>
> The band stated in this document, **0.54–0.62 t/t**, is a rounded envelope that lies inside both of those. The adopted value of 0.58 t/t is not taken from that band; it is the residual computed at the adopted kernel yield (0.35 t/t) with the 7% loss used throughout Section 7. It happens to coincide with the centre of the stated band. Users applying a different kernel yield should recompute the waste yield as the residual rather than interpolating within the band.

The process loss of ~7-8% represents:
- Husk and silk removal losses (not collected as waste)
- Kernel fragments lost during cutting and washing (down the drain)
- Water balance (some water added during blanching, some lost as steam)

### 4.2 Dry Matter Contents

| Co-product | DM (%) | Range | Basis |
|------------|--------|-------|-------|
| Edible kernels | **25.0%** | 22–28% | Sweet corn kernels at harvest typically contain 72–78% moisture, i.e. 22–28% DM [^1^][^2^]. The adopted 25.0% is the midpoint of that range. |
| Cannery waste silage | **22.5%** | 20–25% | Cannery waste silage typically contains 75–80% moisture, i.e. 20–25% DM [^4^][^5^]. Crowley & Howard [^5^] describe the material as "about 80 percent water" (~20% DM), the low end of the band; Feedipedia [^4^] spans the wider range. The adopted 22.5% is the midpoint. |


### 4.3 DM Output per Tonne

| Co-product | Calculation | DM Output (t/t fresh ears) |
|------------|-------------|---------------------------|
| **Edible kernels** | 0.35 × 0.25 | **0.08750** |
| **Cannery waste silage** | 0.58 × 0.225 | **0.13050** |
| **Total** | | **0.21800** |

---

## 5. Prices

### 5.1 Co-Product Prices

| Co-product | Price (USD/t) | Range | Source | Notes |
|------------|--------------|-------|--------|-------|
| **Edible kernels** | 575 | 450–700 | Estimated from processor economics | No USDA kernel price series exists. Sweet corn is contracted to growers at ~$100–150/t fresh ears [^3^]. At 35% kernel recovery, raw material cost alone is $286–429/t kernels. Add processing, canning, and margin → $450–700/t for wholesale canned/frozen kernels. The adopted **$575/t** is the midpoint of that derived range. |
| **Cannery waste silage** | **22.50** | 15–30 | UW Extension [^6^] | UW Extension recommends 50–70% of corn silage value. Corn silage (2024–25): ~$30–45/t wet basis [^7^]. The adopted **$22.50/t** is 60% (the midpoint of the 50–70% guidance) applied to $37.50/t (the midpoint of the silage price range); see Section 5.3. |

### 5.2 Price Derivation for Edible Kernels

```
Step 1: Grower contract price
  Sweet corn growers receive: $100–150/t fresh ears

Step 2: Kernel raw material cost
  At 35% recovery: $100/0.35 = $286/t kernels to $150/0.35 = $429/t kernels

Step 3: Processing costs (canning-specific)
  Husking & cutting:       ~$40–65/t kernels
  Blanching & washing:     ~$25–40/t kernels
  Canning & packaging:     ~$55–90/t kernels (cans, filling, retorting)
  Overhead & margin:       ~$40–70/t kernels
  Total processing:        $160–265/t kernels

Step 4: Total processor gate price
  Low:  $286 + $160 = $446/t → round to $450/t
  High: $429 + $265 = $694/t → round to $700/t
  Derived range: $450–700/t

Midpoint: ($450 + $700) / 2 = $575/t
```


### 5.3 Price Derivation for Cannery Waste

```
UW Extension recommendation [^6^]: 50–70% of corn silage value
Corn silage value [^7^]: $30–45/t wet basis

Adopted value (midpoints of both inputs):
  Percentage midpoint: (50% + 70%) / 2 = 60%
  Corn silage midpoint: ($30 + $45) / 2 = $37.50/t
  Adopted waste price:  60% x $37.50 = $22.50/t

Bounds (combining the extremes of both inputs):
  Low:  50% x $30 = $15.00/t
  High: 70% x $45 = $31.50/t
  Stated range: $15-30/t (rounded)

Note: the adopted $22.50/t is the product of the two midpoints, while the
midpoint of the bounds above is $23.25/t. The two differ because the waste
price is the product of two ranges, and the product of midpoints is not the
midpoint of the products. The adopted value follows the first route because
that is how the UW Extension guidance is applied in practice - a percentage
of a prevailing silage price - rather than by averaging extreme cases.
```

### 5.4 Revenue per Tonne

| Co-product | Calculation | Revenue (USD/t fresh ears) |
|------------|-------------|---------------------------|
| **Edible kernels** | 0.35 × 575 | **$201.25** |
| **Cannery waste silage** | 0.58 × 22.50 | **$13.05** |
| **Total** | | **$214.30** |

---

## 6. Allocation Methodology

### 6.1 Economic Allocation

```
Economic allocation (%) = (Revenue of co-product i ÷ Total revenue of all co-products) × 100

where:
  Revenue of co-product i = Yield_i (t/t) × Price_i (USD/t)
```

| Co-product | Calculation | Allocation |
|------------|-------------|------------|
| Edible kernels | (201.25 ÷ 214.30) × 100 | **93.9%** |
| Cannery waste silage | (13.05 ÷ 214.30) × 100 | **6.1%** |
| **Total** | | **100.0%** |

> **Rounding note:** The precise economic allocation percentages are Kernels 93.91% and Waste 6.09%. When rounded to one decimal place, the sum equals 100.0%.

### 6.2 Mass Allocation

```
Mass allocation (%) = (DM output of co-product i ÷ Total DM output of all co-products) × 100

where:
  DM output of co-product i = Yield_i (t/t) × DM_i (%)
```

| Co-product | Calculation | Allocation |
|------------|-------------|------------|
| Edible kernels | (0.08750 ÷ 0.21800) × 100 | **40.1%** |
| Cannery waste silage | (0.13050 ÷ 0.21800) × 100 | **59.9%** |
| **Total** | | **100.0%** |

> **Calculation note:** Mass allocation is computed from the precise DM output values (0.08750 and 0.13050 t) to avoid accumulation of rounding error. The precise values are 40.14% (kernels) and 59.86% (waste), rounded to one decimal place as 40.1% and 59.9%.

### 6.3 Comparison

| Co-product | Economic | Mass | Difference |
|------------|----------|------|------------|
| Edible kernels | 93.9% | 40.1% | +53.8 pp |
| Cannery waste silage | 6.1% | 59.9% | −53.8 pp |

The 53.8 pp difference reflects the value-to-mass ratio of sweet corn kernels: they command $575/t, 25.6× the waste price, but carry only 40.1% of the co-product dry matter. The waste stream's share of the burden differs roughly tenfold between the two methods, so the choice of method should be stated explicitly for this system.

### 6.4 Why Economic Allocation Is So Skewed

In sweet corn canning, economic allocation is heavily skewed toward edible kernels (**93.9%**) because:

1. **High value of food product:** Sweet corn kernels are a premium food ingredient with a wholesale value of $450–700/t.
2. **Low value of waste:** Cannery waste is a low-quality feedstuff with limited markets, valued at only $15–30/t.
3. **No intermediate or secondary products:** Sweet corn canning produces one high-value food product and one low-value feed stream, with no marketable intermediate between them, so there is nothing to moderate the split.

A skew of this size is characteristic of food processing systems in which the primary product captures nearly all of the economic value and the co-product is a low-value feed or disposal stream.

---

## 7. Mass Balance Verification

### 7.1 Input-Output Reconciliation

| Check | Value | Status |
|-------|-------|--------|
| Input: Fresh sweet corn ears | 1.000 t | — |
| Input moisture | ~75% | — |
| Input DM | 0.250 t | — |
| Output: Edible kernels (as-is) | 0.350 t | ✓ |
| Output: Cannery waste (as-is) | 0.580 t | ✓ |
| Total as-is output | 0.930 t | 93.0% of input |
| Output DM: Kernels | 0.08750 t | ✓ |
| Output DM: Waste | 0.13050 t | ✓ |
| Total DM output | 0.21800 t | 87.2% of input DM |

### 7.2 Explanation of Missing Mass

The as-is output sum (0.930 t) is 93% of the input mass (1.0 t). The missing 7% (~70 kg) represents:
- **Husks and silks** blown away during husking (not collected as waste)
- **Kernel fragments** lost during cutting and washing (down the drain)
- **Water loss** during blanching (evaporation)
- **Trimming losses** (tips and damaged ends removed before cutting)

The DM output sum (0.21800 t) is 87.2% of the input DM (0.250 t). The missing 12.8% (~32 kg DM) represents:
- **Soluble solids** lost in blanching and wash water — sweet corn has high sugar content at harvest, and a significant fraction dissolves in the blanching water during the brief heating step
- **Fine particles** not recovered from process water
- **Respiration and metabolic losses** during the brief period between harvest and processing
- **Organic material in husks and silks** that are blown away and not collected

Both balances are **physically reasonable** for a wet food processing operation. The 7% as-is process loss is consistent with industry expectations of 5–8% total loss. The 12.8% DM loss is higher than some dry processing systems but is expected for sweet corn canning due to the significant soluble sugar losses during blanching — a characteristic feature of sweet corn that distinguishes it from lower-sugar crops.

### 7.3 DM Balance Detail

| Item | Value | Notes |
|------|-------|-------|
| Input DM (1 t fresh ears at 75% moisture) | 0.2500 t | 1.000 × 0.25 |
| **Output DM — co-products:** | | |
| Edible kernels | 0.08750 t | 0.35 t × 25% DM |
| Cannery waste silage | 0.13050 t | 0.58 t × 22.5% DM |
| Total co-product DM | **0.21800 t** | |
| DM balance gap | −0.03200 t | −12.8% of input DM |

> **Balance assessment:** The DM output is 0.032 t (12.8%) below the DM input. The deficit is the residual of the balance, not a measured quantity. It is apportioned below across the pathways that plausibly carry it; the figures are estimates chosen to be consistent with the residual rather than independent measurements, and the first is the largest and least certain of them:
>
> 1. **Soluble sugar losses in blanching and wash water (~0.015 t DM, ~6.0%):** Sweet corn kernels carry 10–15% sugar (sucrose, glucose and fructose) on a fresh-weight basis. During blanching — brief immersion in hot water at ~85–95°C — part of that sugar leaches into the blanching water. Leaching of solubles during blanching is well documented; the quantity assigned here is an estimate, and it is the largest single term in the apportionment.
>
> 2. **Non-recovered organic matter in husks and silks (~0.010 t DM, ~4.0%):** Husks and silks are blown away during mechanical husking and not collected as cannery waste. While much of this material is low-DM (high moisture), the organic fraction contributes to the DM gap.
>
> 3. **Fine particle and drain losses (~0.004 t DM, ~1.6%):** Kernel fragments, tip kernels, and fine particulate matter lost during cutting and washing, not captured in either product stream.
>
> 4. **Metabolic and other losses (~0.003 t DM, ~1.2%):** Includes respiration losses between harvest and processing (sweet corn metabolizes sugars rapidly at ambient temperature), minor mechanical spillage, and foam losses.
>
> **Sum of the apportionment:** 0.015 + 0.010 + 0.004 + 0.003 = 0.032 t DM (12.8%), which equals the residual by construction.
>
> The sugar term should be read with care. At 10–15% sugar on a fresh-weight basis the kernels carry roughly 0.035–0.053 t of sugar, so a 0.015 t loss would represent about a third of it — high for a brief hot-water immersion. The true split between blanch-water sugar loss and uncollected husk and silk material is not resolved by the data available here, and a plant-specific balance would be needed to separate them.

### 7.4 Why Cannery Waste Is Less Than (1 − Kernel Yield)

- Kernel yield: 0.35 t/t
- Waste yield: 0.58 t/t
- Sum: 0.35 + 0.58 = 0.93 t/t

The waste yield (0.58 t/t) is **less than** the theoretical remainder (1 − 0.35 = 0.65 t/t) because:
1. **Process losses:** Husks, silks, and trimming debris are not collected as waste.
2. **Water balance:** Some water is added during blanching, but more is lost as steam and drainage.
3. **Kernel fragments:** Some kernels are lost during cutting and washing and do not enter either product stream.

---

## 8. Complete Data Table

| Parent Crop | Crop System | Stage | USDA Standard | Standard Moisture | Parent Input Basis | Co-product Stream | Yield (t/t) | Yield Range | Price (USD/t) | Price Range | DM (%) | DM Output (t/t) | Revenue (USD/t) | Econ Alloc (%) | Mass Alloc (%) |
|-------------|-------------|-------|---------------|-------------------|-------------------|-------------------|-------------|-------------|---------------|-------------|--------|-----------------|-----------------|----------------|----------------|
| Sweet corn | Sweet-corn canning | Single | 35 lb/bushel (industry convention, not USDA standard) | ~75% (harvest) | 1 t fresh ears | Edible kernels | 0.35 | 0.30–0.40 | 575 | 450–700 | 25.0 | 0.08750 | 201.25 | 93.9 | 40.1 |
| Sweet corn | Sweet-corn canning | Single | 35 lb/bushel (industry convention, not USDA standard) | ~75% (harvest) | 1 t fresh ears | Cannery waste silage | 0.58 | 0.54–0.62 | 22.50 | 15–30 | 22.5 | 0.13050 | 13.05 | 6.1 | 59.9 |

---

## 9. Data Quality and Limitations

### 9.1 High-Confidence Data (Government and Established Sources)

| Data Point | Confidence | Source |
|------------|-----------|--------|
| Kernel recovery range (30–40%) | **High** | Industry consensus; extension reports [^1^][^3^] |
| Sweet corn harvest moisture (70–80%) | **High** | USDA NASS [^1^]; well-established industry average |
| Cannery waste moisture (75–80%) | **High** | Feedipedia [^4^]; Crowley & Howard [^5^] |
| Cannery waste value (50–70% of corn silage) | **High** | UW Extension [^6^] |
| Corn silage prices ($30–45/t) | **High** | USDA AMS [^7^] |

### 9.2 Medium-Confidence Data (Estimated or Industry Sources)

| Data Point | Confidence | Source |
|------------|-----------|--------|
| Kernel yield (0.35 t/t) | **Medium** | Midpoint of the 30–40% range; actual recovery varies by hybrid and cutting style |
| Kernel DM% (25%) | **Medium** | Midpoint of the 22–28% range; kernel moisture varies with hybrid and harvest timing |
| Kernel price ($575/t) | **Medium** | No USDA price series; estimated from processor economics. This is the most uncertain parameter in the methodology. |
| Waste yield (0.58 t/t) | **Medium** | Residual of the as-is balance at the adopted kernel yield and 7% process losses; not directly measured |
| Waste price ($22.50/t) | **Medium** | Based on UW Extension [^6^] guidance relative to corn silage; highly variable by region |
| Waste yield range (0.54–0.62 t/t) | **Medium** | Rounded envelope of the residual across the kernel yield range at 7–8% process losses (Section 4.1) |

### 9.3 Known Limitations

1. **No standardized moisture basis:** Unlike field corn, sweet corn is not traded on a standardized moisture basis. All values are on a fresh-weight basis at harvest moisture.

2. **Hybrid variation:** Kernel recovery varies significantly by hybrid (30–50%) and cutting style (whole-kernel vs. cream-style). The 30–40% range represents the most common processing hybrids; specialty or supersweet hybrids may achieve higher recovery.

3. **Regional price variation:** Cannery waste value depends on local livestock feed markets and transportation costs. In regions with concentrated dairy operations (e.g., Wisconsin, Minnesota), waste may command higher prices.

4. **Seasonal variation:** Sweet corn is a seasonal crop (summer harvest in most regions), so prices and availability vary throughout the year.

5. **Missing co-products:** Some canneries separate cobs for specialized uses (e.g., biomass, crafts), but most combine all waste into a single "cannery waste" stream.

6. **Process water not allocated:** Water added during blanching and washing is not separately tracked or allocated in this analysis.

7. **Bushel equivalent uncertainty:** The 63.0 bushels/t figure is based on the 35 lb/bu industry convention, but this is not a standardized USDA bushel weight and actual bushel weights vary by hybrid and growing conditions. Sweet corn is commercially traded by the ton, not by the bushel.

8. **Kernel price estimation:** The $575/t kernel price is the most uncertain parameter in this methodology. No USDA price series exists for processor-gate sweet corn kernels, and the price is derived entirely from processor economics. Economic allocation is sensitive to this parameter: a 10% change in kernel price would shift economic allocation by approximately 0.5–0.6 pp. LCA practitioners should test sensitivity of allocation results to this parameter.

9. **DM balance gap:** The 12.8% DM gap is higher than typical for dry processing systems but is explained by the significant soluble sugar losses during blanching of sweet corn. This is a well-documented phenomenon in sweet corn processing. The gap could be reduced by tracking blanching water losses as a separate non-marketed output, but this is beyond the scope of this allocation methodology.

---
