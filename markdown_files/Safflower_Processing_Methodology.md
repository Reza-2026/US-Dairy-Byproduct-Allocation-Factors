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
| **Moisture content** | 9.0% | Safflower is **not** a grain for which official U.S. standards exist (7 CFR 810.101 lists barley, canola, corn, flaxseed, mixed grain, oats, rye, sorghum, soybeans, sunflower seed, triticale and wheat) [^1^], so there is no USDA standard moisture. Extension guidance across the U.S. growing area gives ≤8% for safe long-term storage [^10^][^11^][^12^]; harvest and delivery moisture typically runs 8–10%. The 9.0% basis used here is a representative trading moisture within that band. |
| **Dry matter (DM) input** | 0.910 t DM/t safflower seed | Calculated: 1.000 × (1 − 0.09) = 0.910 |
| **Bushel equivalent** | 58.0 bushels/t | 1,000 kg ÷ 17.237 kg/bu (38 lb/bu) |
| **Bushel weight** | 38 lb (17.237 kg) | Conventional bushel weight for safflower [^12^] ("weighs about 38 lb/bushel"); Oregon State [^11^] treats 38 lb/bu or higher as premium quality. Measured test weights range roughly 36–42 lb/bu by variety and hull content [^10^]. There is no USDA grain standard for safflower [^1^]. |
| **Typical oil content** | ~40% (as-is basis at 9% moisture), equivalent to ~44% (dry matter basis) | **U.S. commercial safflower.** Montana dryland trials report 37–42% seed oil content as a three-year average [^9^]; Montana State cultivar × water trials span 36.3–44.8% [^13^]. Oregon State [^11^] reports 32–52% across commercial varieties with the seed market demanding above 34%; NDSU [^10^] gives 30–50%. The ~40% as-is midpoint is used here. See the note below on why world-average figures are lower. |

### 1.2 Convention for Adopted Values

Every yield, price, and DM% in this document is reported as an adopted point value together with the range it was drawn from. **Unless a row states otherwise, the adopted value is the midpoint of its stated range**, and the range is the parameter that carries the evidence. Point values are given to the precision the underlying sources support and are not intended to imply plant-level accuracy. Derived quantities (DM outputs, revenues, allocation percentages) are carried at four decimals internally and reported to one decimal place.

### 1.3 Unit Conversions

| Conversion | Factor |
|------------|--------|
| 1 bushel safflower | 38 lb = 17.237 kg (conventional bushel weight) |
| 1 lb | 0.453592 kg = 0.000453592 t |
| 1 t safflower seed | ~58.0 bushels (at 38 lb/bu) |
| 1 short ton | 2,000 lb = 0.907185 metric ton |
| 1 metric ton | 2,204.62 lb = 1.10231 short tons |

> **Note on safflower varieties:** Two main types of safflower are grown commercially: **high-linoleic** (traditional, ~70–80% linoleic acid, used for edible oil and paint) and **high-oleic** (developed for stability, ~75–80% oleic acid, used for food and frying). Both types have similar oil content and yield similar amounts of oil and meal. The high-oleic variety typically commands a price premium. This table covers both types, with the price range capturing the difference.

> **Note on scope — U.S. safflower, not world-average safflower:** This document models **U.S. commercial safflower**, which is grown predominantly in Montana, together with North Dakota, California and neighbouring states. That matters for the seed parameters, because U.S. commercial germplasm is materially higher in oil and lower in hull than the world safflower population. Feedipedia's feed tables, compiled from worldwide seed accessions, give 28.3 ± 4.5% oil on a dry matter basis and a hull fraction of about 45% (range 33–60%) [^14^]; those figures are dominated by traditional thick-hulled types grown in India and elsewhere and are **not** representative of what U.S. crushers receive. Montana trials report 37–42% seed oil [^9^], and the U.S. seed market pays a premium for oil content above 34% [^11^]. Where this document quotes seed composition, it uses the U.S. figures; Feedipedia is used for meal and hull composition, where the two agree more closely.

> **Note on safflower vs. sunflower:** Although both are oilseeds in the Asteraceae family, safflower and sunflower differ in several respects. Safflower has **thicker hulls** (~25–35% of seed weight for U.S. commercial varieties, against ~20–30% for oil-type sunflower) and **lower meal protein** (~22–25% for non-dehulled safflower meal against ~28–32% for non-dehulled sunflower meal), and it is a far smaller crop with much less price transparency. Seed oil content is closer than the hull difference suggests: U.S. safflower at ~44% DM against oil-type sunflower at ~46% DM. The decisive processing difference is that sunflower is routinely dehulled before extraction and safflower usually is not, which is why sunflower carries a separate hulls co-product in this work and safflower does not.

---

## 2. Data Sources and References

### 2.1 Primary Sources

| Citation | Full Title | Type | URL |
|----------|-----------|------|-----|
| [^1^] | USDA AMS. *Official United States Standards for Grain*, 7 CFR 810.101 — grains for which standards are established (safflower is not among them) | Government (USDA) | https://www.ecfr.gov/current/title-7/subtitle-B/chapter-VIII/subchapter-A/part-810 |
| [^2^] | FAO. *Crop Information: Safflower* (water relations and agronomy); plus Eckey, E.W. (1992). *Minor Oil Crops* (FAO technical bulletin, includes safflower processing section) | International Organization | https://www.fao.org/land-water/databases-and-software/crop-information/safflower/en |
| [^3^] | USDA ERS (August 2025). *Oil Crops Outlook* | Government (USDA) | https://ers.usda.gov/ |
| [^4^] | USDA WASDE (February 2026). *World Agricultural Supply and Demand Estimates* | Government (USDA) | https://www.usda.gov/ |
| [^5^] | Tridge. *Safflower Oil Price Data* | Industry/Market | https://dir.tridge.com/prices/safflower-oil |
| [^6^] | IndexBox. *World: Safflower Seed — Market Report. Analysis and Forecast to 2025* | Industry/Market | https://www.indexbox.io/ |
| [^7^] | Bergman, J.W. and Flynn, C.R. (2001). "High oleic safflower as a diesel fuel extender: A potential new market for Montana safflower." *5th International Safflower Conference Proceedings* | Academic (Conference) | — |
| [^8^] | Tridge. *Safflower Meal Price (Global)* | Industry/Market | https://dir.tridge.com/prices/safflower-meal |
| [^9^] | eXtension Farm Energy. *Safflower (Carthamus tinctorius L.) for Biofuel Production* — Montana dryland trial seed oil content and meal protein | University Extension | https://farm-energy.extension.org/safflower-carthamus-tinctorius-l-for-biofuel-production/ |
| [^10^] | NDSU Extension. *Safflower Production* (A-870) | University Extension | https://www.ndsu.edu/agriculture/sites/default/files/2021-05/a870.pdf |
| [^11^] | Oregon State University Extension. *Safflower* (EM 8792) | University Extension | https://extension.oregonstate.edu/sites/extd8/files/documents/em8792.pdf |
| [^12^] | University of Wisconsin, Corn Agronomy. *Alternative Field Crops: Safflower* | University Extension | https://corn.agronomy.wisc.edu/Crops/Safflower.aspx |
| [^13^] | Montana State University. *Fertilizer Facts FF14 — Safflower Seed Yield and Oil Content as Affected by Water and Nitrogen* | University Research | https://landresources.montana.edu/fertilizerfacts/documents/FF14SafflowerYieldNWater.pdf |
| [^14^] | Feedipedia. *Safflower (Carthamus tinctorius) seeds and oil meal* (INRAE/CIRAD/AFZ/FAO) | Scientific Database | https://www.feedipedia.org/node/49 |
| [^15^] | Saskatchewan Agriculture / Agriculture and Agri-Food Canada. *Safflower Production on the Canadian Prairies: revisited in 2004* | Government (Canada) | https://s3.wp.wsu.edu/uploads/sites/2171/2017/08/SafflowerProduction_Canada.pdf |

### 2.2 How Sources Were Used

- **Yield data:** USDA ERS [^3^], FAO [^2^], and Bergman & Flynn [^7^] provided safflower crush yield data. The ranges reflect variation across extraction methods (expeller vs. solvent) and seed varieties.
- **Price data (oil):** USDA ERS [^3^], WASDE [^4^], and Tridge [^5^] provided safflower oil price data. Safflower oil is a specialty oil with less price transparency than major vegetable oils.
- **Price data (meal):** USDA ERS [^3^], Tridge [^8^], and IndexBox [^6^] provided safflower meal price data. Safflower meal is a niche product with limited markets.
- **Seed composition (oil content, hull fraction):** U.S. extension and research sources were used in preference to world-average feed tables, because U.S. commercial safflower is higher in oil and lower in hull than the global seed population. Montana dryland trials [^9^] and Montana State cultivar trials [^13^] provided seed oil content; NDSU [^10^], Oregon State [^11^] and Wisconsin [^12^] provided corroborating ranges, test weight and storage moisture. Dehulled-kernel oil content, used to derive the hull fraction, comes from the Canadian Prairies review [^15^].
- **Meal composition:** Meal protein for non-dehulled and dehulled safflower meal is consistent across [^9^][^10^][^11^][^12^][^15^] and Feedipedia [^14^].
- **DM contents:** Industry trading specifications for safflower meal (max 12% moisture = min 88% DM) and oil (negligible moisture = ~100% DM).

---

## 3. Safflower Crushing System

### 3.1 Process Description

Safflower crushing involves the following steps:

1. **Cleaning:** Foreign material (dirt, weed seeds, chaff) is removed.
2. **Conditioning (optional dehulling):** Safflower seeds have **thick fibrous hulls, about 25–35% of seed weight for U.S. commercial varieties** (see Section 4.1; traditional thick-hulled germplasm grown outside North America runs 40–50% [^14^]). Unlike sunflower, most commercial safflower crushing does NOT dehull the seed before extraction. The hulls remain with the meal, producing non-dehulled meal at ~22–25% protein [^9^][^11^][^12^][^15^]. Some specialty operations do dehull for higher-protein meal (~40% protein [^9^][^11^]), but this is less common.
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

> **Why no separate hulls line:** Unlike sunflower (where dehulling is standard and produces a distinct hulls co-product), safflower is typically crushed WITHOUT dehulling — the Canadian Prairies review notes that "most commercial safflower meal includes hulls" [^15^]. The hulls (~25–35% of seed weight) remain with the meal, and the meal yield of 0.605 t/t reflects this non-dehulled configuration. If a specific crushing facility does dehull safflower, a hulls line would need to be added, meal yield would drop to ~0.40–0.45 t/t, meal protein would rise to ~40% [^9^][^11^], and meal price would increase accordingly.

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
| **Safflower oil** | 0.375 | 0.35–0.40 | Solvent extraction of U.S. commercial safflower [^2^][^3^][^7^]; reproduced from seed composition in the note below. Yields vary with seed oil content (37–42% as-is for Montana seed [^9^]), extraction efficiency, and variety. Expeller-only yields are ~0.28–0.33 t/t because 6–10% residual oil is left in the cake; solvent extraction achieves ~0.35–0.40 t/t at ~1% residual oil. |
| **Safflower meal (non-dehulled)** | 0.605 | 0.58–0.63 | Derived as the residual of the as-is balance: 1.00 − 0.375 (oil) − 0.020 (losses) = 0.605, and consistent with reported yields for non-dehulled solvent-extracted meal [^2^][^7^]. Because the meal yield is the residual, the as-is balance in Section 7.3 closes by construction rather than by independent measurement; the dry-matter balance in Section 7.2 is the check that carries information. Meal yield is inversely related to oil yield: higher oil extraction means less meal. Non-dehulled meal includes the hulls (~25–35% of seed weight) and runs ~22–25% protein [^9^][^11^][^12^][^15^]. |

*Reconciling the oil yield with seed composition:* The oil yield can be derived from the seed itself, and doing so reproduces the adopted value. U.S. commercial safflower carries ~40% oil on an as-is basis at 9% moisture (Montana dryland trials: 37–42% [^9^]; Montana State cultivar trials: 36.3–44.8% [^13^]), so 1 t of seed contains about 0.40 t of oil. Commercial solvent extraction leaves roughly 1% residual oil in the meal, recovering ~93–96%.

| Seed oil content (as-is) | Extraction recovery | Oil yield (t/t seed) |
|---|---|---|
| 37% | 93% | 0.344 |
| **40%** | **94%** | **0.376** |
| 42% | 96% | 0.403 |

The adopted **0.375 t/t** and the stated range **0.35–0.40** both follow from this. Read in reverse, 0.375 t/t implies a seed oil content of 39.9% as-is (43.8% DM), which sits inside the Montana range.

*Deriving the hull fraction:* Dehulled safflower kernel is relatively constant in oil content at 59–64% on a dry basis [^15^], so the hull fraction follows from seed oil content: at ~44% oil on a DM basis, the kernel is roughly 69–75% of the seed and the hull 25–31%. Across the U.S. seed oil range this gives a hull fraction of about **25–35%**, which is the figure used throughout this document. Feedipedia's ~45% hull [^14^] reflects worldwide germplasm, not U.S. commercial seed.

> **Note on yield relationship:** Oil and meal yields are inversely related, as with all oilseeds. When more oil is extracted, less meal is produced. The values in this table (0.375 oil, 0.605 meal) sum to 0.98 t/t, consistent with ~2% processing losses.

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
| **Safflower oil** | 1,300 | 1,000–1,600 | USDA ERS [^3^]; WASDE [^4^]; Tridge [^5^] | 2024–2025 average. Safflower oil is a specialty oil commanding a premium over commodity vegetable oils. High-oleic varieties fetch higher prices ($1,400–1,800/t) than high-linoleic ($900–1,300/t). The midpoint of $1,300/t reflects a weighted average. |
| **Safflower meal (non-dehulled)** | 150 | 100–200 | USDA ERS [^3^]; Tridge [^8^]; IndexBox [^6^] | 2024–2025 average. Safflower meal is a low-protein (~22–25%) feed ingredient, less valuable than sunflower or soybean meal. Used primarily in ruminant rations as a protein and fiber source. Limited price transparency due to small market. |

### 5.2 Price Verification

**Safflower oil:**

```
USDA ERS (2025): limited direct reporting; estimated ~$1,200-1,400/t
Tridge (2024-2025): safflower oil import/export prices ~$1,000-1,600/t
  depending on grade and origin
IMARC Group (2025): USA safflower oil prices ~$1,399/t (Dec 2025 Q4)
High-oleic premium: +$200-400/t above high-linoleic

Adopted: $1,300/t, the midpoint of the $1,000–1,600 range
```

**Safflower meal (non-dehulled):**

```
USDA ERS (2025): ~$120-180/t (non-dehulled, ~22% protein)
Tridge (2024): global safflower meal ~$200/t range
Comparable feed ingredient prices: cottonseed meal ~$200-260/t;
  canola meal ~$180-240/t (both higher protein)

Adopted: $150/t, the midpoint of the $100–200 range
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

> **Balance assessment:** The DM output is 0.0026 t (0.29%) below the DM input. Because the meal yield is derived as the as-is residual, the as-is balance closes automatically; this dry-matter check is the one that carries information, and it is satisfied independently — the meal DM implied by the residual yield (0.5324 t) is within 0.3% of the non-oil dry matter available in the seed (0.910 − 0.375 = 0.535 t). The small deficit is consistent with handling losses, residual solvent removal and moisture adjustment.

### 7.3 As-Is Mass Balance

| Item | Value | Notes |
|------|-------|-------|
| Input (safflower seed) | 1.000 t | — |
| **Output:** | | |
| Safflower oil | 0.375 t | — |
| Safflower meal | 0.605 t | — |
| **Total output** | **0.980 t** | |
| **Processing losses** | **0.020 t** | 2.0%: handling, moisture loss, fines |
| **Balance** | **1.000 t** | Closes by construction — the meal yield is set as 1.00 − oil − losses (Section 4.1) |

---

## 8. Complete Data Table

| Parent Crop | Crop System | Stage | USDA Standard | Standard Moisture | Parent Input Basis | Co-product Stream | Yield (t/t) | Yield Range | Price (USD/t) | Price Range | DM (%) | DM Output (t/t) | Revenue (USD/t) | Econ Alloc (%) | Mass Alloc (%) |
|-------------|-------------|-------|---------------|-------------------|-------------------|-------------------|-------------|-------------|---------------|-------------|--------|-----------------|-----------------|----------------|----------------|
| Safflower | Safflower crushing | Single | No USDA grain standard; 38 lb/bu conventional | 9% | 1 t safflower seed at 9% moisture | Safflower oil | 0.375 | 0.35–0.40 | 1,300 | 1,000–1,600 | 100.0 | 0.375 | 487.50 | 84.3 | 41.3 |
| Safflower | Safflower crushing | Single | No USDA grain standard; 38 lb/bu conventional | 9% | 1 t safflower seed at 9% moisture | Safflower meal (non-dehulled) | 0.605 | 0.58–0.63 | 150 | 100–200 | 88.0 | 0.532 | 90.75 | 15.7 | 58.7 |

> **Note on allocation rounding:** Raw economic allocations are 84.31% (oil) and 15.69% (meal), rounded to 84.3% and 15.7% to sum to exactly 100.0%. Raw mass allocations are 41.33% (oil) and 58.67% (meal), rounded to 41.3% and 58.7% to sum to exactly 100.0%.

---
## 9. Data Quality and Limitations

### 9.1 High-Confidence Data

| Data Point | Confidence | Source |
|------------|-----------|--------|
| Seed oil content (~40% as-is) | **High** | Montana dryland trials 37–42% [^9^]; MSU cultivar trials 36.3–44.8% [^13^]; corroborated by [^10^][^11^] |
| Oil yield (0.375 t/t) | **High** | Reproduced from seed oil content and extraction recovery (Section 4.1) [^2^][^3^][^9^] |
| Oil DM% (100%) | **High** | Pure lipid with negligible moisture |
| Meal DM% (88%) | **High** | Industry trading specification (max 12% moisture) |
| Meal protein (~22–25%, non-dehulled) | **High** | Consistent across [^9^][^10^][^11^][^12^][^15^] and Feedipedia [^14^] |
| Oil price ($1,300/t) | **Medium-High** | Consistent with 2024–2025 data from Tridge [^5^], IMARC Group, and USDA ERS [^3^] |
| Meal yield (0.605 t/t, non-dehulled) | **Medium-High** | Derived as the as-is residual rather than measured independently; consistent with reported non-dehulled meal yields [^7^] |
| Meal price ($150/t) | **Medium** | Small market with limited price transparency |

### 9.2 Medium-Confidence Data

| Data Point | Confidence | Source |
|------------|-----------|--------|
| Oil yield range (0.35–0.40) | **Medium-High** | Brackets the yields implied by the Montana seed oil range at 93–96% extraction recovery (0.344–0.403, Section 4.1). Seed from outside the U.S., which is lower in oil, would yield less |
| Meal yield range (0.58–0.63) | **Medium** | The inverse of the oil yield range; actual values depend on extraction efficiency and hull fraction |
| Price ranges | **Medium** | Safflower has less market data than major oilseeds; ranges are estimated from limited sources |
| Processing losses (2%) | **Medium** | Estimated from yield balance; not directly measured |

### 9.3 Known Limitations

1. **Non-dehulled configuration only:** This table represents non-dehulled safflower crushing (hulls mixed into meal). A dehulled configuration would produce:
   - Oil: ~0.37–0.40 t/t (slightly higher oil yield due to better extraction from dehulled kernels)
   - Meal (dehulled): ~0.40–0.45 t/t at ~40% protein [^9^][^11^], priced ~$250–350/t
   - Hulls: ~0.18–0.22 t/t at ~88–90% DM, priced ~$60–100/t
   - The dehulled configuration changes allocations significantly, especially mass allocation (hulls would carry ~18–20% of DM).

2. **Limited market data:** Safflower is a minor oilseed globally (~0.6 Mt/year production against ~60 Mt for sunflower), and the U.S. crop is smaller still. Price transparency is limited and prices can be volatile in thin markets. The price ranges are wider, relative to the adopted value, than for major oilseeds to reflect this. Prices are the least well-constrained parameters in this table — see limitation 3.

3. **Economic allocation is sensitive to the oil-to-meal price ratio:** Safflower oil's high price ($1,300/t) against meal's low price ($150/t) means the economic allocation is dominated by oil (84.3%). If oil falls to $1,000/t, oil's economic allocation falls to **80.5%** ($375.00 ÷ $465.75). If the meal price doubles to $300/t, oil's economic allocation falls to **72.9%** ($487.50 ÷ $669.00). Both are larger movements than any plausible change in the yields, so studies sensitive to this crop should test the price assumption rather than the yield assumption.

4. **Oil variety premium:** High-oleic safflower oil commands a significant premium over high-linoleic oil ($1,400–1,800/t vs. $900–1,300/t). The $1,300/t midpoint is a weighted average. Studies focused on a specific variety should use variety-specific pricing.

5. **Meal protein content limitation:** Non-dehulled safflower meal at ~22–25% protein is less valuable than most other oilseed meals (sunflower ~28–32%, canola ~35–38%, soybean ~44–48%). This limits its use primarily to ruminant feed. If safflower meal is used for poultry or swine, it must be supplemented with higher-protein ingredients, which affects its effective value.

6. **Regional variation:** Safflower is grown in semi-arid regions (US Northern Plains, India, Mexico, Argentina, Australia). Prices and yields vary by region due to variety differences, processing infrastructure, and local demand.

7. **Hull content and seed origin:** This document uses a hull fraction of ~25–35% of seed weight, derived in Section 4.1 from U.S. seed oil content and the 59–64% dehulled-kernel oil content reported for the Canadian Prairies [^15^]. Traditional thick-hulled germplasm grown outside North America carries substantially more hull — Feedipedia gives about 45%, range 33–60%, across worldwide accessions, with a corresponding seed oil content of 28.3 ± 4.5% DM [^14^]. Applying this table to non-U.S. safflower would therefore overstate the oil yield and understate the meal yield; the seed composition should be re-derived for that case.

---
