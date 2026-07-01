# Sugar Beet Processing: Co-Product Allocation Methodology, Data Sources, and Calculations

**Document Version:** 1
**Date:** March 2026  
**Basis:** 1 metric ton (t) of sugar beets at ~75% moisture (25% DM)  
**Price Period:** 2024–2025 average (unless otherwise noted)  


---

## Table of Contents

1. [Standard Basis and Conversions](#1-standard-basis-and-conversions)
2. [Data Sources and References](#2-data-sources-and-references)
3. [Sugar Beet Processing System](#3-sugar-beet-processing-system)
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
| **Parent crop** | Sugar beet (*Beta vulgaris* subsp. *vulgaris*, Altissima Group) | — |
| **Input quantity** | 1 metric ton (1,000 kg) | — |
| **Moisture content** | ~75% (25% DM) | Typical for mature sugar beets at harvest. Fresh beet DM ranges from ~22–28% depending on variety, growing conditions, and harvest timing. The 25% DM basis is the industry-standard midpoint [^1^][^5^]. |
| **Dry matter (DM) input** | 0.250 t DM/t sugar beet | Calculated: 1.000 × 0.25 = 0.250 |
| **Typical sugar (sucrose) content** | ~16–18% (fresh weight basis) | Asadi (2006) [^5^] reports average sucrose content of 16–18% for U.S. sugar beets. USDA NASS [^4^] reports average sugarbeet sucrose recovery of ~14.5–16.5% (after processing losses). Cooke & Scott (1993) [^6^] reports 15–20% sugar content; the 16–18% range reflects typical U.S. commercial values. |
| **Typical growing regions (U.S.)** | Minnesota, North Dakota, Idaho, Michigan, Montana, Nebraska, Washington, Wyoming, Colorado, Oregon | USDA NASS [^4^] production statistics. |
| **Processing season** | September through February/March (peak October–February) | The "campaign" or slicing campaign begins in September when beets are harvested and may extend through February or March depending on climate, storage conditions, and factory capacity. Peak slicing occurs October through February [^1^][^5^]. |

### 1.2 Unit Conversions

| Conversion | Factor |
|------------|--------|
| 1 short ton sugar beets | 2,000 lb = 0.907185 metric ton |
| 1 metric ton sugar beets | 2,204.62 lb = 1.10231 short tons |
| 1 lb | 0.453592 kg = 0.000453592 t |
| 1 cwt sugar beets | 100 lb = 45.359 kg |

> **Note on sugar beet moisture:** Sugar beets are sold by weight at their natural moisture content. Unlike grains, there is no USDA-defined standard moisture for trading. Freshly harvested sugar beets are ~74–77% moisture. The 75% moisture (25% DM) basis used here is the industry-standard average for mature sugar beets at harvest [^1^][^5^]. Storage losses (respiration, moisture loss) reduce beet weight and DM over time; stored beets may reach 22–24% DM by late in the campaign.

> **Note on sugar beet vs. sugar cane:** Sugar beet and sugar cane produce chemically identical refined sucrose but are processed differently. Sugar beet processing is a temperate-climate, single-factory operation where beets are sliced, diffused, and refined in one location. Sugar cane processing is typically split between a raw sugar mill (tropical/subtropical) and a separate refinery. This document covers sugar beet processing only.

---

## 2. Data Sources and References

## 2. Data Sources and References

### 2.1 Primary Sources

| Citation | Full Title | Type | URL |
|----------|-----------|------|-----|
| [^1^] | USDA ERS (2025). *Sugar and Sweeteners Yearbook Tables* | Government (USDA) | https://ers.usda.gov/ |
| [^2^] | Feedipedia / INRA / CIRAD / FAO (2015). *Sugar beet pulps* | Academic/Database | https://www.feedipedia.org/node/559 |
| [^3^] | USDA NASS (2025). *Crop Production Annual Summary* | Government (USDA) | https://www.nass.usda.gov/ |
| [^4^] | CRS Report R43998. *U.S. Sugar Program Fundamentals* | Government | https://crsreports.congress.gov/ |
| [^5^] | Asadi, M. (2006). *Beet-Sugar Handbook* | Academic/Industry | — |
| [^6^] | Cooke, D.A. & Scott, R.K. (1993). *The Sugar Beet Crop: Science into Practice* | Academic | — |
| [^7^] | van der Poel, P.W., Schiweck, H. & Schwartz, T. (1998). *Sugar Technology, Beet and Cane Sugar Manufacture* | Academic/Industry | — |
| [^8^] | USDA FSA. *Sugar Program (Farm Service Agency)* | Government (USDA) | https://www.fsa.usda.gov/programs-and-services/sugar-program/ |

### 2.2 How Sources Were Used

- **Yield data:** Asadi (2006) [^5^] and van der Poel et al. (1998) [^7^] are the authoritative references for sugar beet processing yields and mass balances. Cooke & Scott (1993) [^6^] provides agronomic context. USDA ERS [^1^] and USDA NASS [^2^] provide U.S. production and price statistics.
- **Sugar yield:** The value of 0.150 t/t (range 0.13–0.16) reflects typical U.S. commercial extraction rates. USDA NASS [^2^] reports average sucrose recovery of ~14.5–16.5% of beet weight (after factory losses), consistent with 0.145–0.165 t/t gross sucrose yield. The 0.150 t/t midpoint is consistent with industry data after accounting for factory losses (molasses sugar, unseen losses) [^5^][^7^].
- **Molasses DM:** Feedipedia [^8^] reports sugar beet molasses DM of 75–80%. This reflects the industry-standard specification for beet molasses, which is typically sold at ~79–80% DM to prevent fermentation [^5^][^7^].
- **Price data (sugar):** USDA ERS [^1^] Table 5 reports U.S. wholesale refined beet sugar prices. This reflects the 2024–2025 U.S. domestic market, which is significantly higher than the world market price due to the U.S. sugar program (tariff-rate quotas, price supports) [^3^][^4^]. A world market scenario is provided separately using $500/t.
- **Price data (molasses):** USDA ERS [^1^] and Feedipedia [^8^] provide beet molasses price data. The price of $175/t (range $100–260) reflects the 2024–2025 market for beet molasses used in animal feed and fermentation.
- **Price data (pulp):** Feedipedia [^8^] provides dried beet pulp price data. The $50/t price (range $40–70) is for pressed (wet) pulp; dried pulp commands ~$200–350/t but has much lower as-is yield.
- **Sugar program context:** The U.S. sugar program is administered by USDA FSA [^3^]. CRS Report R43998 [^4^] provides authoritative explanation of the program's price support mechanisms.

---

## 3. Sugar Beet Processing System

### 3.1 Process Description

Sugar beet processing (the "campaign") involves the following steps:

1. **Receiving and sampling:** Beets are delivered to the factory, sampled for sugar content (polarimetry), and weighed. Payment to growers is based on net weight and sugar content.
2. **Washing and fluming:** Beets are washed in water flumes to remove soil, stones, and vegetative debris. Soil can account for 5–15% of delivered weight (tare), which is subtracted before payment.
3. **Slicing:** Clean beets are sliced into thin strips called "cossettes" to maximize surface area for sugar extraction.
4. **Diffusion (extraction):** Cossettes are counter-currently washed with hot water (~70–75°C) in a diffusion tower or drum. Sugar (sucrose) and soluble compounds diffuse out of the beet cells into the juice. The resulting "raw juice" contains ~12–16% dissolved solids; the depleted cossettes become "wet pulp."
5. **Pulp pressing:** Wet pulp is mechanically pressed to remove water, producing "pressed pulp" (~20–30% DM). Some factories add press aid (lime or polymer) to improve pressing. Pressed pulp may be sold as-is for cattle feed or further dried.
6. **Pulp drying (optional):** Pressed pulp is dried in rotary dryers to produce "dried pulp" (~88–92% DM) or "dried pulp with molasses" (a value-added product). Drying is energy-intensive and is not performed at all factories.
7. **Juice purification:** Raw juice is purified by adding milk of lime (Ca(OH)₂) and carbon dioxide (CO₂) in the "carbonatation" process. This precipitates non-sugar impurities (proteins, pectins, organic acids, color bodies) as calcium carbonate ("lime sludge" or "scum"). The purified juice is called "thin juice."
8. **Evaporation:** Thin juice is concentrated in multiple-effect evaporators to produce "thick juice" (~60–70% dissolved solids).
9. **Crystallization:** Thick juice is further concentrated under vacuum and seeded to crystallize sugar. The process typically involves 2–3 crystallization stages ("boiling"). After each stage, the mother liquor is separated from sugar crystals by centrifugation.
10. **Sugar drying and storage:** White sugar crystals are dried, cooled, and stored in silos.
11. **Molasses exhaust:** The final mother liquor after the last crystallization stage is "molasses," which still contains ~50% sugar but cannot be economically crystallized further. Molasses exits the process as a co-product.
12. **Lime sludge handling:** The calcium carbonate precipitate from carbonatation (lime sludge or "factory lime") is filtered and may be sold for agricultural liming, landfilled, or used for other purposes.

**Co-products generated:**
- **White sugar:** The primary high-value product (food, industrial uses).
- **Beet pulp:** The fibrous residue after sugar extraction (animal feed, primarily cattle).
- **Molasses:** The concentrated syrup after final crystallization (animal feed, fermentation substrate for ethanol/citric acid/yeast production).

**Non-product outputs (not allocated):**
- **Lime sludge (factory lime):** Calcium carbonate precipitate from juice purification. Yield: 0.04–0.10 t/t beet [^5^][^7^]. While sometimes sold for agricultural liming, it is generally treated as a waste with minimal or zero market value. It is not included in economic or mass allocation.
- **Factory water (process condensate):** Large volumes of water are evaporated during juice concentration and crystallization. This water (0.577 t from beet moisture alone, plus additional steam condensate) is not a co-product.
- **Soil and stones (tare):** Removed during washing; not a processing co-product.

> **Why lime sludge is not allocated:** Lime sludge is a process waste with highly variable composition and minimal market value. It is produced in quantities of 0.04–0.10 t/t beet [^5^][^7^]. While some factories sell it for agricultural liming ($5–15/t), most dispose of it on land or in landfills at a cost. Its economic value is negligible relative to the three primary co-products and is excluded from allocation.

### 3.2 Process Flow

```
1 t sugar beets at ~75% moisture (0.250 t DM)
        |
        v
  +-- SUGAR BEET PROCESSING (CAMPAIGN) --------------------------+
  |                                                               |
  |  Diffusion: Sugar extracted from cossettes with hot water     |
  |  Carbonatation: Lime + CO2 purify juice (0.04-0.10 t sludge) |
  |  Crystallization: 2-3 stages separate sugar from molasses     |
  |                                                               |
  |  Water removed: ~0.577 t (from beet moisture)                |
  |    (0.750 t beet water - 0.173 t retained in products)       |
  |                                                               |
  |  Sugar (white):  0.150 t as-is at 100% DM (0.1500 t DM)   <-- co-product
  |                                                               |
  |  Beet pulp:     0.220 t as-is at 25% DM   (0.0550 t DM)   <-- co-product
  |                                                               |
  |  Molasses:      0.040 t as-is at 80% DM   (0.0320 t DM)   <-- co-product
  |                                                               |
  |  Lime sludge:   0.04-0.10 t as-is           (not allocated)   |
  |  Water removed:  ~0.577 t                   (not allocated)   |
  |                                                               |
  +---------------------------------------------------------------+

THREE CO-PRODUCTS from 1 t sugar beets:
  Sugar (white):  0.150 t as-is,  0.1500 t DM
  Beet pulp:     0.220 t as-is,  0.0550 t DM
  Molasses:      0.040 t as-is,  0.0320 t DM
  Total:                       0.2370 t DM  (from 0.250 t input; 0.013 t gap = 5.2%)

As-is mass balance:
  Products:       0.150 + 0.220 + 0.040 = 0.410 t
  Non-product:    0.590 t (water removed + lime sludge + losses)
  Total:          1.000 t
```

---

## 4. Co-Product Yields and Properties

### 4.1 Yields (per tonne of sugar beets input)

| Co-product | Yield (t/t beet) | Range | Source & Calculation |
|------------|-----------------|-------|---------------------|
| **White sugar** | **0.150** | 0.13–0.16 | Asadi (2006) [^5^] and van der Poel et al. (1998) [^7^] report typical factory sugar yield of 14–16% of beet weight. The 0.150 t/t value is the midpoint of the range (0.13 + 0.16) / 2 = 0.145; the 0.150 value is slightly above midpoint and reflects a well-operating factory. USDA NASS [^2^] reports average sucrose recovery of ~14.5–16.5% (after processing losses), consistent with this range. |
| **Beet pulp (pressed)** | 0.22 | 0.16–0.28 | Asadi (2006) [^5^]; Feedipedia [^8^]. Pressed pulp yield varies with beet DM, extraction efficiency, and pressing method. The 0.22 t/t value is consistent with industry data. If dried pulp is the product, the as-is yield drops to ~0.06–0.08 t/t (at ~90% DM) but the DM output is similar. |
| **Molasses** | 0.04 | 0.03–0.05 | Asadi (2006) [^5^]; van der Poel et al. (1998) [^7^]. Molasses yield depends on the amount of non-sugar impurities and the number of crystallization stages. Typical molasses yield is 3.5–5.0% of beet weight. The 0.04 t/t value is the midpoint of the range. |


#### Total Recovery and Non-Product Output

The as-is yields sum to 0.410 t/t beet (0.150 + 0.220 + 0.040), which is 41.0% of the 1.0 t input. The remaining 0.590 t (59.0%) is non-product output consisting of:

1. **Water removed during processing:** ~0.577 t (beet water of 0.750 t minus water retained in products of 0.173 t). This is the largest non-product stream.
2. **Lime sludge:** 0.04–0.10 t (not allocated; typically disposed on land or sold cheaply for agricultural liming).
3. **Processing losses:** Small additional losses from dissolved solids in process water, sugar degradation, and unseen losses.

### 4.2 Dry Matter Contents

| Co-product | DM (%) | Basis |
|------------|--------|-------|
| White sugar | 100.0% | Refined white sugar (sucrose) is a crystalline solid with negligible moisture (<0.05%) [^5^]. |
| Beet pulp (pressed) | 25.0% | Pressed pulp is typically 22–28% DM [^5^][^8^]. Feedipedia [^8^] reports average pressed pulp DM of 23.5% (range 19–30%). The 25% DM value is the industry midpoint for pressed pulp. Dried pulp is ~88–92% DM but has much lower as-is yield. |
| Molasses | **80.0%** | **80% (range 75–80%)** . Feedipedia [^8^] and Asadi (2006) [^5^] report sugar beet molasses DM of 75–80%. The 80% reflects the industry-standard specification for beet molasses, which is typically sold at ~79–80% DM to prevent fermentation during storage. |

### 4.3 DM Output per Tonne of Sugar Beets

| Co-product | Calculation | DM Output (t/t beet) |
|------------|-------------|---------------------|
| **White sugar** | 0.150 × 1.00 | **0.1500**  |
| **Beet pulp (pressed)** | 0.220 × 0.25 | **0.0550** |
| **Molasses** | 0.040 × 0.80 | **0.0320** |
| **Total DM output** | | **0.2370** |
| **DM input** | 1.000 × 0.25 | **0.2500** |
| **DM gap** | 0.2500 − 0.2370 | **0.0130 (5.2%)** |

> **DM balance gap of 5.2%:** The total DM output (0.2370 t) is 0.0130 t (5.2%) below the DM input (0.2500 t). This gap represents: (1) DM in lime sludge (~0.03–0.07 t DM, of which only a portion is beet-derived DM; much is added lime), (2) dissolved and suspended solids in process wastewater, (3) sugar degradation products (invert sugar, lactic acid from fermentation during storage), and (4) unseen factory losses. This gap is consistent with industry mass balance data from Asadi (2006) [^5^] and van der Poel et al. (1998) [^7^], who report typical total DM recoveries of 90–95% of input DM.

---

## 5. Prices

### 5.1 Price Table

| Co-product | Price (USD/t) | Range | Source | Notes |
|------------|--------------|-------|--------|-------|
| **White sugar** | **900** | **700–1,200** | USDA ERS [^1^]; USDA FSA [^3^]; CRS R43998 [^4^] | **U.S. domestic wholesale refined beet sugar price, 2024–2025 conservative average.** USDA ERS Table 5 reports U.S. wholesale refined beet sugar prices. The U.S. sugar program (tariff-rate quotas, nonrecourse loans, marketing allotments) maintains domestic prices well above world market levels [^3^][^4^]. The price of $900/t (~41 cents/lb) reflects the 2024–2025 average. **A world market scenario is provided in Section 6.4.** |
| **Beet pulp (pressed)** | 50 | 40–70 | Feedipedia [^8^]; industry data | 2024–2025 average for pressed (wet) beet pulp used as cattle feed. Dried pulp commands ~$200–350/t but has much lower as-is yield. The $50/t price reflects pressed pulp FOB factory. |
| **Molasses** | **175** | **100–260** | USDA ERS [^1^]; Feedipedia [^8^]; industry data | 2024–2025 average for sugar beet molasses. Molasses is used for animal feed (primary market), fermentation (ethanol, citric acid, yeast), and as a dust suppressant. Price varies with sugar content, DM%, and end-use demand. The price of $175/t reflects the 2024–2025 market. |

### 5.2 Price Verification

**White sugar (U.S. domestic):**

```
USDA ERS Table 5 (2024-2025): refined beet sugar ~38-44 cents/lb
  = ~$838-970/t
USDA FSA loan rate: ~25 cents/lb (price support floor)
  = ~$551/t (well below market)
CRS R43998: U.S. sugar program maintains domestic prices at
  roughly double the world market price

Selected U.S. domestic midpoint: $900/t (~41 cents/lb)
Range: $700-1,200/t (captures 2024-2025 volatility)
Mathematical midpoint of range ($700-1,200): $950/t
The $900/t value is slightly below the range midpoint,
reflecting a conservative estimate.

```

**White sugar (world market):**

```
World market (ICE No. 11 raw sugar equivalent, 2024-2025):
  ~20-28 cents/lb = ~$441-617/t raw
  Refined white sugar premium: +3-6 cents/lb
  Refined white sugar: ~23-34 cents/lb = ~$507-750/t
  Conservative world market refined price: ~$500/t

Used in World Market scenario (Section 6.4): $500/t
```

**Beet pulp (pressed):**

```
Feedipedia: pressed beet pulp ~$40-70/t (varies by region, season)
Dried pulp: ~$200-350/t (but as-is yield drops from 0.22 to ~0.06-0.08 t/t)
USDA ERS: limited direct price reporting for beet pulp

Selected midpoint: $50/t
Range: $40-70/t
```

**Molasses:**

```
USDA ERS: beet molasses ~$150-260/t (2024-2025)
Feedipedia: beet molasses ~$100-200/t (international)
Industry reports: $150-260/t for 80% DM beet molasses

Selected midpoint: $175/t
Range: $100-260/t
Mathematical midpoint of range ($100-260): $180/t
The $175/t value is near the range midpoint.

```

### 5.3 Revenue per Tonne of Sugar Beets (U.S. Domestic Prices)

| Co-product | Calculation | Revenue (USD/t beet) |
|------------|-------------|---------------------|
| **White sugar** | 0.150 × 900 | **$135.00** |
| **Beet pulp (pressed)** | 0.220 × 50 | **$11.00** |
| **Molasses** | 0.040 × 175 | **$7.00**  |
| **Total** | | **$153.00** |

---

## 6. Allocation Methodology

### 6.1 Economic Allocation (U.S. Domestic Prices)

Economic allocation distributes environmental burdens among co-products based on their relative market value.

**Formula:**

```
Economic allocation (%) = (Revenue of co-product i ÷ Total revenue of all co-products) × 100

where:
  Revenue of co-product i = Yield_i (t/t) × Price_i (USD/t)
```

| Co-product | Calculation | Allocation |
|------------|-------------|------------|
| White sugar | (135.00 ÷ 153.00) × 100 | **88.2%** |
| Beet pulp | (11.00 ÷ 153.00) × 100 | **7.2%** |
| Molasses | (7.00 ÷ 153.00) × 100 | **4.6%** |
| **Total** | | **100.0%** |

> **Rounding note:** The raw calculations yield 88.24% (sugar), 7.19% (pulp), and 4.58% (molasses). These are rounded to 88.2%, 7.2%, and 4.6% so that the sum is exactly 100.0% (88.2 + 7.2 + 4.6 = 100.0).

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
| White sugar | (0.1500 ÷ 0.2370) × 100 | **63.3%**  |
| Beet pulp | (0.0550 ÷ 0.2370) × 100 | **23.2%**  |
| Molasses | (0.0320 ÷ 0.2370) × 100 | **13.5%** |
| **Total** | | **100.0%** |

> **Rounding note:** The raw calculations yield 63.29% (sugar), 23.21% (pulp), and 13.50% (molasses). These are rounded to 63.3%, 23.2%, and 13.5% so that the sum is exactly 100.0%.

### 6.3 Comparison: Economic vs. Mass Allocation (U.S. Domestic)

| Co-product | Economic Allocation (US Domestic) | Mass Allocation | Difference |
|------------|----------------------------------|----------------|------------|
| White sugar | 88.2% | 63.3% | +24.9 pp |
| Beet pulp | 7.2% | 23.2% | −16.0 pp |
| Molasses | 4.6% | 13.5% | −8.9 pp |

The large difference for sugar reflects its high value-to-mass ratio. Sugar commands $900/t (18× the pulp price and 5.1× the molasses price) but contains only 63.3% of the co-product DM. The U.S. sugar program inflates the domestic sugar price, widening the economic-vs-mass divergence relative to what would be observed under world market pricing.

### 6.4 World Market Economic Allocation Scenario

Because the U.S. domestic sugar price (~$900/t) is roughly double the world market price due to the U.S. sugar program [^3^][^4^], a world market scenario is provided using sugar at $500/t.

**Revenue calculation (World Market prices):**

| Co-product | Price (USD/t) | Calculation | Revenue (USD/t beet) |
|------------|--------------|-------------|---------------------|
| White sugar | 500 | 0.150 × 500 | **$75.00** |
| Beet pulp | 50 | 0.220 × 50 | **$11.00** |
| Molasses | 175 | 0.040 × 175 | **$7.00** |
| **Total** | | | **$93.00** |

**World Market economic allocation:**

| Co-product | Calculation | Allocation |
|------------|-------------|------------|
| White sugar | (75.00 ÷ 93.00) × 100 | **80.6%** |
| Beet pulp | (11.00 ÷ 93.00) × 100 | **11.8%** |
| Molasses | (7.00 ÷ 93.00) × 100 | **7.5%** |
| **Total** | | **100.0%** |

> **Rounding note:** The raw calculations yield 80.65% (sugar), 11.83% (pulp), and 7.53% (molasses). These are rounded to 80.6%, 11.8%, and 7.6% so that the sum is exactly 100.0% (80.6 + 11.8 + 7.6 = 100.0).

### 6.5 Comparison: U.S. Domestic vs. World Market Economic Allocation

| Co-product | US Domestic (sugar=$900/t) | World Market (sugar=$500/t) | Difference |
|------------|---------------------------|----------------------------|------------|
| White sugar | 88.2% | 80.6% | +7.6 pp |
| Beet pulp | 7.2% | 11.8% | −4.6 pp |
| Molasses | 4.6% | 7.5% | −2.9 pp |

The U.S. sugar program increases sugar's economic allocation by 7.6 percentage points relative to the world market scenario. This is a significant methodological consideration: LCA studies of U.S. sugar beet processing that use domestic prices will assign more environmental burden to sugar than studies using world market prices.

> **Recommendation:** For LCA studies of products derived from U.S. sugar beet processing, both domestic and world market economic allocations should be reported as a sensitivity analysis, given the 7.6 percentage-point difference in sugar allocation.

---

## 7. Mass Balance Verification

### 7.1 Input-Output Reconciliation

| Check | Value | Status |
|-------|-------|--------|
| Input: Sugar beets at ~75% moisture | 1.000 t | — |
| Input moisture | ~75% | — |
| Input DM | 0.250 t | — |
| Output: Sugar (as-is) | 0.150 t | ✓ |
| Output: Pulp (as-is) | 0.220 t | ✓ |
| Output: Molasses (as-is) | 0.040 t | ✓ |
| Total as-is co-product output | 0.410 t | 41.0% of input |
| Non-product output | 0.590 t | 59.0% of input |
| Output DM: Sugar | 0.1500 t | ✓ |
| Output DM: Pulp | 0.0550 t | ✓ |
| Output DM: Molasses | 0.0320 t | ✓ |
| Total DM output (co-products) | 0.2370 t | 94.8% of input DM |
| DM gap | 0.0130 t | 5.2% of input DM |

### 7.2 DM Balance Detail

| Item | Value | Notes |
|------|-------|-------|
| Input DM (1 t sugar beets at 25% DM) | 0.2500 t | 1.000 × 0.25 |
| **Output DM — co-products:** | | |
| White sugar | 0.1500 t | 0.150 t × 100% DM |
| Beet pulp (pressed) | 0.0550 t | 0.220 t × 25% DM |
| Molasses | 0.0320 t | 0.040 t × 80% DM |
| Total co-product DM | **0.2370 t** | |
| DM balance gap | −0.0130 t | −5.2% of input DM |

> **Balance assessment:** The DM output is 0.0130 t (5.2%) below the DM input. This gap is consistent with industry mass balance data and represents: (1) DM in lime sludge (the calcium carbonate precipitate contains beet-derived non-sugars plus added lime — the beet-derived portion is estimated at 0.003–0.008 t DM), (2) dissolved and suspended solids in process wastewater (~0.002–0.004 t DM), (3) sugar degradation products during processing (~0.001–0.003 t DM), and (4) unseen factory losses (~0.001–0.002 t DM). 

### 7.3 As-Is Mass Balance

| Item | Value | Notes |
|------|-------|-------|
| Input (sugar beets) | 1.000 t | — |
| **Co-product output:** | | |
| White sugar | 0.150 t | — |
| Beet pulp (pressed) | 0.220 t | — |
| Molasses | 0.040 t | — |
| **Total co-product output** | **0.410 t** | |
| **Non-product output** | **0.590 t** | |
| **Balance** | **1.000 t** | ✓ Exact |

### 7.4 Water Balance

| Item | Value | Notes |
|------|-------|-------|
| Water in input beets | 0.750 t | 1.000 t × 75% moisture |
| **Water in co-products:** | | |
| Sugar (0% moisture) | 0.000 t | Crystalline sugar, negligible water |
| Pulp (75% moisture) | 0.165 t | 0.220 t × (1 − 0.25) = 0.165 t |
| Molasses (20% moisture) | 0.008 t | 0.040 t × (1 − 0.80) = 0.008 t |
| **Total water retained in products** | **0.173 t** | |
| **Water removed during processing** | **0.577 t** | 0.750 − 0.173 = 0.577 t |
| **Water removal rate** | **76.9%** | 0.577 / 0.750 |

> **Note on water removal:** Sugar beet processing is fundamentally a water-removal process. Of the 0.750 t of water in the input beets, only 0.173 t (23.1%) is retained in the co-products; the remaining 0.577 t (76.9%) must be removed through evaporation and pressing. This water is released as process steam, condensate, and wastewater. The energy required for this water removal (primarily for evaporation of juice from ~15% to ~95% solids) is the major energy input to the process and is a significant source of environmental impact.

---

## 8. Complete Data Table

### 8.1 U.S. Domestic Price Scenario

| Parent Crop | Crop System | Stage | USDA Standard | Typical Moisture | Parent Input Basis | Co-product Stream | Yield (t/t) | Yield Range | Price (USD/t) | Price Range | DM (%) | DM Output (t/t) | Revenue (USD/t) | Econ Alloc (%) | Mass Alloc (%) |
|-------------|-------------|-------|---------------|-------------------|-------------------|-------------------|-------------|-------------|---------------|-------------|--------|-----------------|-----------------|----------------|----------------|
| Sugar beet | Sugar beet processing | Single | No USDA standard moisture | ~75% (25% DM) | 1 t sugar beets at 25% DM | White sugar | 0.150 | 0.13–0.16 | 900 | 700–1,200 | 100.0 | 0.1500 | 135.00 | 88.2 | 63.3 |
| Sugar beet | Sugar beet processing | Single | No USDA standard moisture | ~75% (25% DM) | 1 t sugar beets at 25% DM | Beet pulp (pressed) | 0.220 | 0.16–0.28 | 50 | 40–70 | 25.0 | 0.0550 | 11.00 | 7.2 | 23.2 |
| Sugar beet | Sugar beet processing | Single | No USDA standard moisture | ~75% (25% DM) | 1 t sugar beets at 25% DM | Molasses | 0.040 | 0.03–0.05 | 175 | 100–260 | 80.0 | 0.0320 | 7.00 | 4.6 | 13.5 |

> 

### 8.2 World Market Price Scenario

| Parent Crop | Crop System | Stage | Typical Moisture | Parent Input Basis | Co-product Stream | Yield (t/t) | Price (USD/t) | DM (%) | DM Output (t/t) | Revenue (USD/t) | Econ Alloc (%) | Mass Alloc (%) |
|-------------|-------------|-------|-------------------|-------------------|-------------------|-------------|---------------|--------|-----------------|-----------------|----------------|----------------|
| Sugar beet | Sugar beet processing | Single | ~75% (25% DM) | 1 t sugar beets at 25% DM | White sugar | 0.150 | 500 | 100.0 | 0.1500 | 75.00 | 80.6 | 63.3 |
| Sugar beet | Sugar beet processing | Single | ~75% (25% DM) | 1 t sugar beets at 25% DM | Beet pulp (pressed) | 0.220 | 50 | 25.0 | 0.0550 | 11.00 | 11.8 | 23.2 |
| Sugar beet | Sugar beet processing | Single | ~75% (25% DM) | 1 t sugar beets at 25% DM | Molasses | 0.040 | 175 | 80.0 | 0.0320 | 7.00 | 7.6 | 13.5 |

> **Note on allocation rounding (U.S. Domestic):** Raw economic allocations are 88.24% (sugar), 7.19% (pulp), and 4.58% (molasses), rounded to 88.2%, 7.2%, and 4.6% to sum to exactly 100.0%. Raw mass allocations are 63.29% (sugar), 23.21% (pulp), and 13.50% (molasses), rounded to 63.3%, 23.2%, and 13.5% to sum to exactly 100.0%.

> **Note on allocation rounding (World Market):** Raw economic allocations are 80.65% (sugar), 11.83% (pulp), and 7.53% (molasses), rounded to 80.6%, 11.8%, and 7.6% to sum to exactly 100.0%.

---

## 9. Data Quality and Limitations

### 9.1 High-Confidence Data

| Data Point | Confidence | Source |
|------------|-----------|--------|
| Beet DM input (25%) | **High** | Industry standard; consistent across Asadi (2006) [^5^], Cooke & Scott (1993) [^6^], van der Poel et al. (1998) [^7^] |
| Sugar DM% (100%) | **High** | Crystalline sucrose with negligible moisture |
| Pulp DM% (25%, pressed) | **High** | Industry trading specification; Feedipedia average 23.5% [^8^] |
| Molasses DM% (80%) | **High** | Industry specification; Feedipedia [^8^]; Asadi (2006) [^5^] |
| Sugar yield range (0.13–0.16) | **High** | Consistent with USDA NASS sucrose recovery data [^2^] and industry literature [^5^][^7^] |
| U.S. sugar price ($900/t, range $700–1,200) | **High** | USDA ERS Table 5 [^1^]; consistent with U.S. sugar program [^3^][^4^] |
| DM balance gap (5.2%) | **High** | Consistent with industry mass balance data [^5^][^7^] |

### 9.2 Medium-Confidence Data

| Data Point | Confidence | Source |
|------------|-----------|--------|
| Sugar yield midpoint (0.150 t/t) | **Medium** | Above the exact midpoint of range (0.145); assumes well-operating factory. |
| Pulp yield (0.22 t/t) | **Medium** | Consistent with industry data but varies with beet DM and pressing efficiency |
| Molasses yield (0.04 t/t) | **Medium** | Consistent with industry data but varies with beet quality and crystallization stages |
| Pulp price ($50/t, pressed) | **Medium** | Limited public price data for pressed pulp; dried pulp market is better documented |
| Molasses price ($175/t) | **Medium** | Based on industry reports and Feedipedia; prices are volatile and depend on end-use demand |
| Lime sludge yield (0.04–0.10 t/t) | **Medium** | Consistent with Asadi (2006) [^5^] and van der Poel et al. (1998) [^7^] |
| World market sugar price ($500/t) | **Medium** | Approximate; world sugar prices are volatile and depend on currency, origin, and quality |

### 9.3 Known Limitations

1. **U.S. sugar program distorts economic allocation:** The U.S. sugar program maintains domestic sugar prices at roughly double the world market price through tariff-rate quotas, nonrecourse loans, and marketing allotments [^3^][^4^]. This means that economic allocation based on U.S. domestic prices assigns significantly more environmental burden to sugar (88.2%) than allocation based on world market prices (80.6%). LCA practitioners should report both scenarios as a sensitivity analysis. The 7.6 percentage-point difference is material.

2. **Pressed pulp vs. dried pulp:** This document uses pressed pulp (25% DM, 0.22 t/t yield, $50/t). Dried pulp has very different properties (~90% DM, ~0.06 t/t yield, ~$250/t). The choice between pressed and dried pulp does not significantly affect the mass allocation (DM output is similar: 0.055 vs. ~0.054 t DM) but does affect the economic allocation because dried pulp has higher revenue per tonne of beet (~$15 vs. $11). Most U.S. factories produce pressed pulp for local cattle feed markets; some dry it for export or distant markets.

3. **Lime sludge excluded from allocation:** Lime sludge (0.04–0.10 t/t beet) is excluded from allocation because it is generally a waste product with minimal market value. However, lime sludge contains both beet-derived non-sugar compounds and added lime (CaO). The beet-derived DM in lime sludge is part of the 5.2% DM gap. If lime sludge were included as a co-product with a small positive value ($5–15/t for agricultural liming), it would slightly reduce the allocation to the other three co-products.

4. **Regional and seasonal variation:** Sugar beet yields, sugar content, and processing efficiency vary by region, variety, and time of year. Early-season beets (September) may have lower sugar content (14–15%) than late-season beets (December–January, 17–19%). Stored beets lose sugar through respiration. The values in this document are campaign averages and may not represent specific periods within the campaign.

5. **No single authoritative yield database:** Unlike soybeans (NOPA) or wheat (USDA milling reports), there is no single authoritative public database for sugar beet factory yields. The yields in this document are compiled from industry reference books [^5^][^7^] and USDA statistics [^1^][^2^]. Factory-specific yields may differ significantly from these averages.

---
