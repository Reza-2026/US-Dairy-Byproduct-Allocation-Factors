# Safflower Crushing: Co-Product Allocation Methodology, Data Sources, and Calculations

**Document Version:** 1.0
**Date:** June 2026  
**Basis:** 1 metric ton (t) of safflower seed at 9% moisture  
**Price Period:** 2024–2025 average (unless otherwise noted)  

---

## Table of Contents

1. [Standard Basis and Conversions](#1-standard-basis-and-conversions)
2. [Data Sources and References](#2-data-sources-and-references)
3. [Safflower Crushing System](#3-safflower-crushing-system)
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
| **Parent crop** | Safflower (*Carthamus tinctorius*) | — |
| **Input quantity** | 1 metric ton (1,000 kg) | — |
| **Moisture content** | 9.0% | As stated in original table. The USDA standard moisture for safflower is 8% [^1^]; the 9% basis is within the typical harvest moisture range (8–10%) and is retained for continuity with prior versions. |
| **Dry matter (DM) input** | 0.910 t DM/t safflower seed | Calculated: 1.000 × (1 − 0.09) = 0.910 |
| **Bushel equivalent** | 55.1 bushels/t | 1,000 kg ÷ 18.144 kg/bu (40 lb at typical test weight) |
| **Bushel weight** | 40 lb (18.144 kg) | Typical test weight for commercial safflower. USDA FSA standard weight is 36 lb/bu; typical test weights range from 38–42 lb/bu depending on variety and hull content. [^1^] |
| **Typical oil content** | ~36% (dry matter basis) | Industry average for commercial safflower varieties. Range is approximately 25–45% DM depending on variety and environment. [^2^] |

### 1.2 Unit Conversions

| Conversion | Factor |
|------------|--------|
| 1 bushel safflower | ~40 lb ≈ 18.14 kg (at typical test weight) |
| 1 lb | 0.453592 kg = 0.000453592 t |
| 1 t safflower seed | ~55.1 bushels (at 40 lb/bu) |
| 1 short ton | 2,000 lb = 0.907185 metric ton |
| 1 metric ton | 2,204.62 lb = 1.10231 short tons |

> **Note on safflower varieties:** Two main types of safflower are grown commercially: **high-linoleic** (traditional, ~70–80% linoleic acid, used for edible oil and paint) and **high-oleic** (developed for stability, ~75–80% oleic acid, used for food and frying). Both types have similar oil content (~25–45% on a DM basis, with ~36% as a typical midpoint for commercial varieties) and yield similar amounts of oil and meal. The high-oleic variety typically commands a price premium. This table covers both types, with the price range capturing the difference.

> **Note on safflower vs. sunflower:** Although they are both oilseeds in the Asteraceae family, safflower and sunflower differ in several key respects. Safflower has **thicker hulls** (30–50% of seed weight vs. 20–30% for oil-type sunflower), lower oil content (~36% DM vs. ~42% DM for oil-type sunflower), and lower meal protein (~20–24% for non-dehulled vs. ~25–28% for non-dehulled sunflower meal). Safflower is also a much smaller crop globally, with less price transparency and market data. The thicker hull content of safflower is the primary reason non-dehulled safflower meal has lower protein than non-dehulled sunflower meal.

---

## 2. Data Sources and References

### 2.1 Primary Sources

| Citation | Full Title | Type | URL |
|----------|-----------|------|-----|
| [^1^] | USDA AMS (formerly GIPSA) — Grain Inspection Standards for Safflower (FGIS-9180.53) | Government (USDA) | https://www.ams.usda.gov/ |
| [^2^] | FAO. *Crop Information: Safflower* (water relations and agronomy); plus Eckey, E.W. (1992). *Minor Oil Crops* (FAO technical bulletin, includes safflower processing section) | International Organization | https://www.fao.org/land-water/databases-and-software/crop-information/safflower/en |
| [^3^] | USDA ERS (August 2025). *Oil Crops Outlook* | Government (USDA) | https://ers.usda.gov/ |
| [^4^] | USDA WASDE (February 2026). *World Agricultural Supply and Demand Estimates* | Government (USDA) | https://www.usda.gov/ |
| [^5^] | Tridge. *Safflower Oil Price Data* | Industry/Market | https://dir.tridge.com/prices/safflower-oil |
| [^6^] | IndexBox. *World: Safflower Seed — Market Report. Analysis and Forecast to 2025* | Industry/Market | https://www.indexbox.io/ |
| [^7^] | Bergman, J.W. and Flynn, C.R. (2001). "High oleic safflower as a diesel fuel extender: A potential new market for Montana safflower." *5th International Safflower Conference Proceedings* | Academic (Conference) | — |
| [^8^] | Tridge. *Safflower Meal Price (Global)* | Industry/Market | https://dir.tridge.com/prices/safflower-meal |
| [^9^] | OECD-FAO (2025). *Agricultural Outlook 2025–2034: Oilseeds and Oilseed Products* (Chapter 3) | International Organization | https://www.oecd.org/ |

### 2.2 How Sources Were Used

- **Yield data:** USDA ERS [^3^], FAO [^2^], and Bergman & Flynn [^7^] provided safflower crush yield data. The ranges reflect variation across extraction methods (expeller vs. solvent) and seed varieties.
- **Price data (oil):** USDA ERS [^3^], WASDE [^4^], and Tridge [^5^] provided safflower oil price data. Safflower oil is a specialty oil with less price transparency than major vegetable oils.
- **Price data (meal):** USDA ERS [^3^], Tridge [^8^], and IndexBox [^6^] provided safflower meal price data. Safflower meal is a niche product with limited markets.
- **DM contents:** Industry trading specifications for safflower meal (max 12% moisture = min 88% DM) and oil (negligible moisture = ~100% DM).

---

## 3. Safflower Crushing System

### 3.1 Process Description

Safflower crushing involves the following steps:

1. **Cleaning:** Foreign material (dirt, weed seeds, chaff) is removed.
2. **Conditioning (optional dehulling):** Safflower seeds have **thick fibrous hulls representing 30–50% of seed weight** for traditional varieties (reduced-hull varieties exist at 15–25%). Unlike sunflower, most commercial safflower crushing does NOT dehull the seed before extraction. The hulls remain with the meal, producing non-dehulled meal with ~20–24% protein. Some specialty operations do dehull for higher-protein meal (~35–42% protein), but this is less common.
3. **Conditioning:** Seeds are heated to improve oil extractability.
4. **Flaking:** Seeds are rolled into thin flakes to rupture cell walls and increase surface area.
5. **Pressing (optional):** Some facilities use a mechanical screw press (expeller) to remove ~50–70% of the oil before solvent extraction.
6. **Solvent extraction:** Hexane is used to extract the remaining oil from the pressed cake or flakes.
7. **Desolventizing:** Hexane is removed from the oil and meal.
8. **Oil refining:** Crude oil is degummed, neutralized, bleached, and deodorized.
9. **Meal processing:** Meal is dried, cooled, and ground to specification.

**Co-products generated (non-dehulled configuration):**
- **Safflower oil:** The primary high-value product (food, industrial, nutraceutical).
- **Safflower meal (non-dehulled):** The primary high-volume co-product (ruminant animal feed, low-protein roughage).

> **Why no separate hulls line:** Unlike sunflower (where dehulling is standard and produces a distinct hulls co-product), safflower is typically crushed WITHOUT dehulling. The thick hulls (30–50% of seed weight) remain with the meal, and the meal yield of 0.605 t/t reflects this non-dehulled configuration. If a specific crushing facility does dehull safflower, a hulls line would need to be added, meal yield would drop to ~0.40–0.45 t/t, meal protein would rise to ~35–42%, and meal price would increase accordingly. See Section 9.3.1 for the dehulled configuration comparison.

### 3.2 Process Flow

```
1 t safflower seed at 9% moisture (0.910 t DM)
        │
        ▼
  ┌─ SAFFLOWER CRUSHING (non-dehulled) ───────────┐
  │                                                 │
  │  Processing losses: ~0.02 t as-is (~2%)        │
  │  (handling, residual solvent, moisture loss)    │
  │                                                 │
  │  Safflower oil: 0.375 t as-is (0.3750 t DM) ◄── co-product
  │                                                 │
  │  Safflower meal: 0.605 t as-is (0.5324 t DM)◄── co-product
  │  (includes hulls; non-dehulled)                 │
  │                                                 │
  └─────────────────────────────────────────────────┘

TWO CO-PRODUCTS from 1 t safflower seed:
  Safflower oil:  0.375 t as-is,  0.3750 t DM
  Safflower meal: 0.605 t as-is,  0.5324 t DM
  Total:                        0.9074 t DM  (from 0.910 t input; ~0.0026 t losses)
```

---

## 4. Co-Product Yields and Properties

### 4.1 Yields (per tonne of safflower seed input)

| Co-product | Yield (t/t safflower) | Range | Source & Calculation |
|------------|----------------------|-------|---------------------|
| **Safflower oil** | 0.375 | 0.35–0.40 | Industry standard for solvent extraction [^2^][^3^][^7^]. The 0.375 value is the exact mathematical midpoint of the range: (0.35 + 0.40) / 2 = 0.375. Yields vary with oil content (25–45% DM basis), extraction efficiency, and variety (high-linoleic vs. high-oleic). Expeller-only yields are ~0.28–0.33 t/t; solvent extraction achieves ~0.35–0.40 t/t. |
| **Safflower meal (non-dehulled)** | 0.605 | 0.58–0.63 | Industry standard for non-dehulled, solvent-extracted meal [^2^][^7^]. The 0.605 value is the exact mathematical midpoint of the range: (0.58 + 0.63) / 2 = 0.605. This is also consistent with mass balance: 1.00 − 0.375 (oil) − 0.020 (losses) = 0.605. Meal yield is inversely related to oil yield: higher oil extraction means less meal. Non-dehulled meal includes hulls (30–50% of seed weight) and has ~20–24% protein. |

> **Note on yield relationship:** Oil and meal yields are inversely related, as with all oilseeds. When more oil is extracted, less meal is produced. The values in this table (0.375 oil, 0.605 meal) sum to 0.98 t/t, consistent with ~2% processing losses. Both yield values are exact midpoints of their respective ranges, satisfying the midpoint rule.

### 4.2 Dry Matter Contents

| Co-product | DM (%) | Basis |
|------------|--------|-------|
| Safflower oil | 100.0% | Crude and refined safflower oil are essentially pure lipid (triglycerides) with negligible moisture (<0.1%). |
| Safflower meal (non-dehulled) | 88.0% | Standard trading specification: maximum 12% moisture = minimum 88% DM. Non-dehulled, solvent-extracted meal is typically delivered at 10–12% moisture. The 88% DM value represents the standard trading basis. |


### 4.3 DM Output per Tonne of Safflower Seed

| Co-product | Calculation | DM Output (t/t safflower) |
|------------|-------------|--------------------------|
| **Safflower oil** | 0.375 × 1.00 | **0.3750** |
| **Safflower meal** | 0.605 × 0.88 | **0.5324** |
| **Total** | | **0.9074** |

---

## 5. Prices

### 5.1 Price Table

| Co-product | Price (USD/t) | Range | Source | Notes |
|------------|--------------|-------|--------|-------|
| **Safflower oil** | 1,300 | 1,000–1,600 | USDA ERS [^3^]; WASDE [^4^]; Tridge [^5^] | 2024–2025 average. Safflower oil is a specialty oil commanding a premium over commodity vegetable oils. High-oleic varieties fetch higher prices ($1,400–1,800/t) than high-linoleic ($900–1,300/t). The midpoint of $1,300/t reflects a weighted average. Midpoint of range: ($1,000 + $1,600) / 2 = $1,300. |
| **Safflower meal (non-dehulled)** | 150 | 100–200 | USDA ERS [^3^]; Tridge [^8^]; IndexBox [^6^] | 2024–2025 average. Safflower meal is a low-protein (~20–24%) feed ingredient, less valuable than sunflower or soybean meal. Used primarily in ruminant rations as a protein and fiber source. Limited price transparency due to small market. Midpoint of range: ($100 + $200) / 2 = $150. |

### 5.2 Price Verification

**Safflower oil:**

```
USDA ERS (2025): limited direct reporting; estimated ~$1,200-1,400/t
Tridge (2024-2025): safflower oil import/export prices ~$1,000-1,600/t
  depending on grade and origin
IMARC Group (2025): USA safflower oil prices ~$1,399/t (Dec 2025 Q4)
High-oleic premium: +$200-400/t above high-linoleic

Selected midpoint: $1,300/t
Mathematical midpoint of range ($1,000-1,600): $1,300/t ✓
The price midpoint IS the true mathematical midpoint of the stated range.
```

**Safflower meal (non-dehulled):**

```
USDA ERS (2025): ~$120-180/t (non-dehulled, ~22% protein)
Tridge (2024): global safflower meal ~$200/t range
Comparable feed ingredient prices: cottonseed meal ~$200-260/t;
  canola meal ~$180-240/t (both higher protein)

Selected midpoint: $150/t
Mathematical midpoint of range ($100-200): $150/t ✓
The price midpoint IS the true mathematical midpoint of the stated range.
```

### 5.3 Revenue per Tonne of Safflower Seed

| Co-product | Calculation | Revenue (USD/t safflower) |
|------------|-------------|--------------------------|
| **Safflower oil** | 0.375 × 1,300 | **$487.50** |
| **Safflower meal** | 0.605 × 150 | **$90.75** |
| **Total** | | **$578.25** |

---

## 6. Allocation Methodology

### 6.1 Economic Allocation

Economic allocation distributes environmental burdens among co-products based on their relative market value.

**Formula:**

```
Economic allocation (%) = (Revenue of co-product i ÷ Total revenue of all co-products) × 100

where:
  Revenue of co-product i = Yield_i (t/t) × Price_i (USD/t)
```

| Co-product | Calculation | Allocation |
|------------|-------------|------------|
| Safflower oil | (487.50 ÷ 578.25) × 100 | **84.3%** |
| Safflower meal | (90.75 ÷ 578.25) × 100 | **15.7%** |
| **Total** | | **100.0%** |

> **Rounding note:** The raw calculations yield 84.31% (oil) and 15.69% (meal). These are rounded to 84.3% and 15.7% so that the sum is exactly 100.0%.

### 6.2 Mass Allocation

Mass allocation distributes burdens based on the dry matter content of each co-product.

**Formula:**

```
Mass allocation (%) = (DM output of co-product i ÷ Total DM output of all co-products) × 100

where:
  DM output of co-product i = Yield_i (t/t) × DM_i (%)
```

| Co-product | Calculation | Allocation |
|------------|-------------|------------|
| Safflower oil | (0.3750 ÷ 0.9074) × 100 | **41.3%** |
| Safflower meal | (0.5324 ÷ 0.9074) × 100 | **58.7%** |
| **Total** | | **100.0%** |

> **Rounding note:** The raw calculations yield 41.33% (oil) and 58.67% (meal). These are rounded to 41.3% and 58.7% so that the sum is exactly 100.0%.

### 6.3 Comparison: Economic vs. Mass Allocation

| Co-product | Economic Allocation | Mass Allocation | Difference |
|------------|-------------------|----------------|------------|
| Safflower oil | 84.3% | 41.3% | +43.0 pp |
| Safflower meal | 15.7% | 58.7% | −43.0 pp |

The extreme difference reflects safflower oil's exceptionally high value-to-mass ratio. Oil commands $1,300/t (8.7× the meal price) but contains only 41.3% of the DM. This is one of the largest economic-vs-mass divergences among all the oilseeds reviewed, driven by safflower oil's specialty premium and safflower meal's low protein content (and correspondingly low price).

---

## 7. Mass Balance Verification

### 7.1 Input-Output Reconciliation

| Check | Value | Status |
|-------|-------|--------|
| Input: Safflower seed at 9% moisture | 1.000 t | — |
| Input moisture | 9.0% | — |
| Input DM | 0.910 t | — |
| Output: Safflower oil (as-is) | 0.375 t | ✓ |
| Output: Safflower meal (as-is) | 0.605 t | ✓ |
| Total as-is output | 0.980 t | 98.0% of input |
| Processing losses (as-is) | 0.020 t | 2.0% of input ✓ |
| Output DM: Oil | 0.375 t | ✓ |
| Output DM: Meal | 0.532 t | ✓ |
| Total DM output | 0.907 t | 99.7% of input DM ✓ |

### 7.2 DM Balance Detail

| Item | Value | Notes |
|------|-------|-------|
| Input DM (1 t safflower seed at 9% moisture) | 0.9100 t | 1.000 × (1 − 0.09) |
| **Output DM — co-products:** | | |
| Safflower oil | 0.3750 t | 0.375 t × 100% DM |
| Safflower meal | 0.5324 t | 0.605 t × 88% DM |
| Total co-product DM | **0.9074 t** | |
| DM balance gap | −0.0026 t | −0.29% of input DM |

> **Balance assessment:** The DM output is 0.0026 t (0.29%) below the DM input. This small deficit represents processing losses (handling, residual solvent, moisture adjustment) and is well within the acceptable range.

### 7.3 As-Is Mass Balance

| Item | Value | Notes |
|------|-------|-------|
| Input (safflower seed) | 1.000 t | — |
| **Output:** | | |
| Safflower oil | 0.375 t | — |
| Safflower meal | 0.605 t | — |
| **Total output** | **0.980 t** | |
| **Processing losses** | **0.020 t** | 2.0%: handling, moisture loss, fines |
| **Balance** | **1.000 t** | ✓ Exact |

---

## 8. Complete Data Table

| Parent Crop | Crop System | Stage | USDA Standard | Standard Moisture | Parent Input Basis | Co-product Stream | Yield (t/t) | Yield Range | Price (USD/t) | Price Range | DM (%) | DM Output (t/t) | Revenue (USD/t) | Econ Alloc (%) | Mass Alloc (%) |
|-------------|-------------|-------|---------------|-------------------|-------------------|-------------------|-------------|-------------|---------------|-------------|--------|-----------------|-----------------|----------------|----------------|
| Safflower | Safflower crushing | Single | 36 lb/bu standard weight (USDA FSA) | 9% | 1 t safflower seed at 9% moisture | Safflower oil | 0.375 | 0.35–0.40 | 1,300 | 1,000–1,600 | 100.0 | 0.375 | 487.50 | 84.3 | 41.3 |
| Safflower | Safflower crushing | Single | 36 lb/bu standard weight (USDA FSA) | 9% | 1 t safflower seed at 9% moisture | Safflower meal (non-dehulled) | 0.605 | 0.58–0.63 | 150 | 100–200 | 88.0 | 0.532 | 90.75 | 15.7 | 58.7 |

> **Note on allocation rounding:** Raw economic allocations are 84.31% (oil) and 15.69% (meal), rounded to 84.3% and 15.7% to sum to exactly 100.0%. Raw mass allocations are 41.33% (oil) and 58.67% (meal), rounded to 41.3% and 58.7% to sum to exactly 100.0%.

---
## 9. Data Quality and Limitations

### 9.1 High-Confidence Data

| Data Point | Confidence | Source |
|------------|-----------|--------|
| Oil yield (0.375 t/t) | **High** | Industry standard for solvent extraction; exact midpoint of verified range [^2^][^3^] |
| Meal yield (0.605 t/t, non-dehulled) | **High** | Consistent with non-dehulled meal production; exact midpoint of range; mass-balance consistent [^7^] |
| Oil DM% (100%) | **High** | Pure lipid with negligible moisture |
| Meal DM% (88%) | **High** | Industry trading specification (max 12% moisture) |
| Oil price ($1,300/t) | **Medium-High** | Consistent with 2024-2025 data from Tridge, IMARC Group, and USDA ERS |
| Meal price ($150/t) | **Medium** | Small market with limited price transparency |
| DM balance (0.29% gap) | **High** | Well within acceptable range |

### 9.2 Medium-Confidence Data

| Data Point | Confidence | Source |
|------------|-----------|--------|
| Oil yield range (0.35–0.40) | **Medium** | Reflects high-oil varieties and solvent extraction; typical safflower may yield 0.32–0.35 t/t |
| Meal yield range (0.58–0.63) | **Medium** | Inverse relationship with oil yield; actual values depend on extraction efficiency |
| Price ranges | **Medium** | Safflower has less market data than major oilseeds; ranges are estimated from limited sources |
| Processing losses (2%) | **Medium** | Estimated from yield balance; not directly measured |

### 9.3 Known Limitations

1. **Non-dehulled configuration only:** This table represents non-dehulled safflower crushing (hulls mixed into meal). A dehulled configuration would produce:
   - Oil: ~0.37–0.40 t/t (slightly higher oil yield due to better extraction from dehulled kernels)
   - Meal (dehulled): ~0.40–0.45 t/t at ~35–42% protein, priced ~$250–350/t
   - Hulls: ~0.18–0.22 t/t at ~88–90% DM, priced ~$60–100/t
   - The dehulled configuration changes allocations significantly, especially mass allocation (hulls would carry ~18–20% of DM).

2. **Limited market data:** Safflower is a minor oilseed globally (~0.6 Mt/year production vs. ~60 Mt for sunflower). Price transparency is limited, and prices can be volatile due to thin markets. The price ranges are wider (relative to midpoint) than for major oilseeds to reflect this uncertainty.

3. **Economic allocation is very sensitive to oil price:** Safflower oil's high price ($1,300/t) and meal's low price ($150/t) mean the economic allocation is dominated by oil (84.3%). If oil drops to $1,000/t, oil's economic allocation drops to 80.9%. If meal price doubles to $300/t, oil's economic allocation drops to 72.3%. This sensitivity should be considered in LCA studies.

4. **Oil variety premium:** High-oleic safflower oil commands a significant premium over high-linoleic oil ($1,400–1,800/t vs. $900–1,300/t). The $1,300/t midpoint is a weighted average. Studies focused on a specific variety should use variety-specific pricing.

5. **Meal protein content limitation:** Non-dehulled safflower meal at ~20–24% protein is less valuable than most other oilseed meals (sunflower ~25–28%, canola ~35–38%, soybean ~44–48%). This limits its use primarily to ruminant feed. If safflower meal is used for poultry or swine, it must be supplemented with higher-protein ingredients, which affects its effective value.

6. **Regional variation:** Safflower is grown in semi-arid regions (US Northern Plains, India, Mexico, Argentina, Australia). Prices and yields vary by region due to variety differences, processing infrastructure, and local demand.

7. **Hull content variation:** Traditional safflower varieties have hull content of 30–50% of seed weight. Specialized reduced-hull (partial hull) varieties have been developed with hull content of 15–25%. The 30–50% range used in this document applies to traditional varieties, which dominate commercial production. Reduced-hull varieties would have different meal yields and protein content.

---
