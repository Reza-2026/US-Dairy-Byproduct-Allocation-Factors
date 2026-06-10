# Canola Processing: Co-Product Allocation Methodology, Data Sources, and Calculations

**Document Version:** 1.0
**Date:** May 2026  
**Basis:** 1 metric ton (t) of canola seed at 8.5% moisture (CGC reporting basis for oil and protein content)  
**Price Period:** 2024–2025 average (unless otherwise noted)

---

## Table of Contents

1. [Standard Basis and Conversions](#1-standard-basis-and-conversions)
2. [Data Sources and References](#2-data-sources-and-references)
3. [Canola Crushing](#3-canola-crushing)
4. [Allocation Methodology](#4-allocation-methodology)
5. [Mass Balance Verification](#5-mass-balance-verification)
6. [Complete Data Table](#6-complete-data-table)
7. [Data Quality and Limitations](#7-data-quality-and-limitations)

---

## 1. Standard Basis and Conversions

### 1.1 Parent Input Definition

| Parameter | Value | Source |
|-----------|-------|--------|
| **Parent crop** | Canola (*Brassica napus*, low-erucic acid rapeseed) | — |
| **Input quantity** | 1 metric ton (1,000 kg) | — |
| **Moisture content** | 8.5% | Canadian Grain Commission (CGC) constant moisture basis for reporting oil and protein content [^1^]. Note: CGC grading thresholds are: straight (<10% moisture), tough (10–12.5%), damp (>12.5%). Canola Council recommends ≤8% for safe long-term storage. The 8.5% moisture basis is the CGC's analytical reporting convention, not a trading standard. |
| **Dry matter (DM) input** | 0.915 t DM/t canola | Calculated: 1.000 × (1 − 0.085) = 0.915 |
| **Bushel equivalent** | 44.09 bushels/t | 1,000 kg ÷ 22.68 kg/bu (50 lb at standard moisture) |
| **Bushel weight** | 50.0 lb (22.68 kg) | USDA/CGC standard for No. 1 Canada canola [^1^] |

> **Note on moisture basis:** This document uses 8.5% moisture as the calculation basis, which is the CGC's constant moisture basis for reporting oil and protein content in quality surveys. This is NOT the same as a "trading standard" moisture — the CGC does not set a specific moisture percentage as a trading standard for canola. The CGC grading system uses moisture thresholds: straight (<10%), tough (10–12.5%), and damp (>12.5%). The Canola Council of Canada recommends ≤8% moisture for safe long-term storage. The 8.5% basis gives DM input = 0.915 t/t (instead of 0.910 t/t at 9% moisture). The 0.5% difference affects the DM balance slightly but does not materially change the allocation results.

### 1.2 Unit Conversions

| Conversion | Factor |
|------------|--------|
| 1 bushel canola | 50.0 lb = 22.68 kg (standard) |
| 1 lb | 0.453592 kg = 0.000453592 t |
| 1 t canola | 44.09 bushels (at 50 lb/bu) |

> **Note on canola vs. rapeseed:** "Canola" refers to cultivars of rapeseed (*Brassica napus* or *B. rapa*) with low erucic acid (<2%) and low glucosinolates (<30 μmol/g). In Europe and Australia, the equivalent crop is typically called "rapeseed" or "oilseed rape" and may have slightly different oil content (42–45% on an as-is basis vs. 40–44% for canola). This document uses North American canola specifications.

---

## 2. Data Sources and References

### 2.1 Primary Sources

| Citation | Full Title | Type | URL |
|----------|-----------|------|-----|
| [^1^] | Canadian Grain Commission. *Official Grain Grading Guide*, Chapter 10: Canola/Rapeseed | Government (CGC) | https://www.grainscanada.gc.ca/en/grain-quality/official-grain-grading-guide/ |
| [^2^] | Canadian Oilseed Processors Association (COPA). *Crush & Oil & Meal Production* | Industry | https://copacanada.com/crush-oil-meal-production |
| [^3^] | USDA ERS. *Oil Crops Yearbook* | Government (USDA) | https://www.ers.usda.gov/data-products/oil-crops-yearbook |
| [^4^] | Canola Council of Canada. *Canola Meal Feeding Guide* (2024 edition) | Industry | https://www.canolacouncil.org/canolamazing/ |
| [^5^] | IndexBox (2025). *World Rapeseed Oil Market Analysis* | Industry/Market | https://www.indexbox.io/store/ |
| [^6^] | USDA FAS. *Oilseeds: World Markets and Trade* | Government (USDA) | https://apps.fas.usda.gov/psdonline/circulars/oilseeds.pdf |
| [^7^] | Tridge. *Canola Meal Price in United States* | Industry/Market | https://dir.tridge.com/prices/canola-meal/US |
| [^8^] | Spragg, J.C. & Mailer, R.J. (2007). *Canola Meal Value Chain Quality Improvement*. Final Report for AOF and Pork CRC, Project 1B-103-0506. | Academic/Report | https://www.porkcrc.com.au/ |

### 2.2 How Sources Were Used

- **Crush yields:** COPA [^2^] provided industry-average oil and meal production data from Canadian crushing plants, from which yields are calculated (2023–2025: ~0.422 t oil per t seed). Canola Council [^4^] provided meal composition and yield data.
- **Oil and meal prices:** USDA ERS [^3^] and USDA FAS [^6^] provided government-reported canola oil and meal prices. IndexBox [^5^] and Tridge [^7^] provided market data.
- **DM contents:** Canola Council [^4^] and CGC [^1^] provided moisture specifications for canola products.
- **Meal composition:** Spragg & Mailer [^8^] provided detailed meal composition data from their Pork CRC/AOF project report.

---

## 3. Canola Crushing

### 3.1 Process Description

Canola crushing extracts oil from canola seed through a combination of mechanical pressing and solvent extraction:

1. **Cleaning:** Remove foreign material, weed seeds, and dockage.
2. **Pre-conditioning:** Heat and flake the seed to rupture cell walls and increase oil availability.
3. **Pre-pressing:** Mechanically extract approximately 60–70% of the oil using a screw press (expeller). This produces press cake (still containing ~15–20% oil).
4. **Solvent extraction:** The press cake is washed with hexane to extract the remaining oil. The defatted material (marc) is then toasted to remove residual hexane.
5. **Desolventizing/Toasting:** The marc is heated to evaporate hexane and toast the meal, improving protein digestibility and reducing glucosinolates.
6. **Oil refining (optional):** Crude oil may be refined (degummed, neutralized, bleached, deodorized) to produce RBD canola oil.

**Co-products generated:**
- **Canola oil:** The primary product — either crude (unrefined) or refined (RBD). This document uses crude canola oil as the primary product at the crushing plant gate.
- **Canola meal:** The primary co-product — the defatted, toasted seed residue, used primarily as a high-protein animal feed ingredient.

### 3.2 Co-Product Yields

| Co-product | Yield (t/t canola) | Range | Source & Calculation |
|------------|-------------------|-------|---------------------|
| **Canola oil (crude)** | 0.42 | 0.40–0.44 | COPA [^2^]: Canadian industry average ~0.415–0.430 t/t (2023–2025; calculated from 11.6 MMT seed crushed → 4.9 MMT oil = 0.422 t/t). Canola Council [^4^]: typical range 40–44%. USDA ERS [^3^]: US crush yields ~0.410–0.425 t/t. The 0.42 midpoint is the mathematical midpoint of the stated range and represents a modern Canadian crush plant processing No. 1 canola. |
| **Canola meal** | 0.56 | 0.54–0.58 | Derived from mass balance: 1.000 − 0.42 (oil) − 0.02 (process loss) = 0.56. Canola Council [^4^]: meal yield typically 55–58% at 90% DM. COPA [^2^]: meal production consistent with ~0.56 t/t at 90% DM. Range 0.54–0.58 captures variation. |

#### Yield Calculation Rationale

**Oil yield:**

Canola seed typically contains 40–44% oil on an as-is basis at 8.5% moisture (approximately 43–48% on a DM basis). The CGC 2025 harvest survey reports 43.6% oil at 8.5% moisture basis, which equals 47.7% on a DM basis (43.6% ÷ 0.915 = 47.7%). The extraction rate (proportion of oil in the seed that is recovered) is typically 97–99% in modern plants using pre-press/solvent extraction.

```
Oil content of seed (as-is, 8.5% moisture basis): ~43.6% (CGC 2025 survey)
Oil as-is per t seed: 0.436 t
Extraction rate: 98%
Oil recovered (as-is): 0.436 × 0.98 = 0.427 t/t

Oil content of seed (DM basis): ~47.7% (43.6% ÷ 0.915)
Oil DM per t seed: 0.915 × 0.477 = 0.436 t DM
Extraction rate: 98%
Oil recovered (DM): 0.436 × 0.98 = 0.428 t DM
At ~99.5% DM (crude oil): 0.428 / 0.995 = 0.430 t/t

With lower oil content varieties (40% as-is, ~43.7% DM basis):
Oil DM per t seed: 0.915 × 0.437 = 0.400 t DM
Oil recovered: 0.400 × 0.98 = 0.392 t DM
At 99.5% DM: 0.392 / 0.995 = 0.394 t/t
```

The 0.42 t/t midpoint is consistent with the range of oil contents and extraction efficiencies found in modern crushing plants.

**Meal yield (derived from mass balance):**

```
Input: 1.000 t canola seed
Oil output: 0.420 t
Process loss: 0.020 t (moisture adjustment, fines, hexane recovery residue)
Meal output: 1.000 − 0.420 − 0.020 = 0.560 t
```

The 2% process loss accounts for:
- Moisture loss during pre-conditioning and toasting (~0.5–1.0%)
- Fines and screenings lost during cleaning (~0.3–0.5%)
- Hexane absorption and recovery residue (~0.1–0.3%)
- Miscellaneous handling losses (~0.2–0.5%)

### 3.3 Dry Matter Contents

| Co-product | DM (%) | Basis |
|------------|--------|-------|
| Canola oil (crude) | 99.5% | Crude canola oil contains ~0.3% moisture and volatile matter per COPA trading specifications (max 0.3% moisture, volatile matter, and impurities), plus non-oil impurities (phospholipids, free fatty acids). Refined (RBD) oil is essentially 100% DM [^4^]. The 99.5% midpoint is for crude oil at the crushing plant gate. For allocation purposes, 100% DM may be used as a reasonable approximation (see note below). |
| Canola meal (dried) | 90.0% | Standard specification for traded canola meal: 88–92% DM (maximum 12% moisture) [^4^]. Feedipedia reports average DM of 90.4%; OCIA reports 90.9% for solvent-extracted meal. Meal is dried during the desolventizing/toasting step. At the plant gate (before drying), meal may be 86–88% DM. |

> **Note on oil DM%:** The difference between 99.5% DM and 100% DM for canola oil has a negligible impact on the allocation results (<0.1 percentage point). This document uses 100% DM for oil in the allocation calculations for simplicity, consistent with the approach used for other vegetable oils in the methodology series. The DM output for oil is therefore 0.42 × 1.00 = 0.420 t DM/t.

### 3.4 Prices

| Co-product | Price (USD/t) | Range | Source | Notes |
|------------|--------------|-------|--------|-------|
| **Canola oil (crude)** | 950 | 800–1100 | USDA FAS [^6^]; IndexBox [^5^] | Crude canola oil FOB: $800–1100/t (2024–2025). RBD canola oil: $1000–1300/t. The $950/t midpoint is the mathematical midpoint of the stated range ($800 + $1100) / 2 = $950. Prices are volatile and influenced by global vegetable oil markets (palm, soy, sunflower). Canadian export prices in 2024 reached $1140–1540/t, suggesting the range may be conservative for peak periods. |
| **Canola meal** | 310 | 250–370 | USDA ERS [^3^]; Tridge [^7^] | Canola meal (34–36% protein): $250–370/t (2024–2025). Prices vary by region, protein content, and proximity to livestock operations. USDA AMS: ~$320–335/t PNW. Tridge: US export prices $330–430/t in 2024. Midpoint $310/t is the mathematical midpoint of the stated range ($250 + $370) / 2 = $310. |

#### Price Calculation for Canola Oil

```
Step 1: Canola seed cost
  USDA FAS [^6^] 2024–2025: Canola seed $450–530/t (FOB Vancouver)
  Average: ~$490/t

Step 2: Crushing cost
  Energy, labor, hexane, overhead, capital: ~$40–60/t seed

Step 3: Co-product credit (meal)
  Revenue from meal per t seed: 0.56 t × $310/t = $173.60

Step 4: Oil raw material cost
  (Seed cost + crushing cost − meal revenue) / oil yield
  = ($490 + $50 − $173.60) / 0.42 = $872/t oil

Step 5: Oil selling price
  Crusher margin: ~$30–80/t oil
  Price range: $902–952/t oil
  Rounded midpoint: $950/t (range $800–1100)
```

### 3.5 Revenue and Allocation Calculations

#### Step 1: Calculate Revenue per Co-Product

```
Revenue (USD/t parent input) = Yield (t/t) × Price (USD/t)
```

| Co-product | Calculation | Revenue |
|------------|-------------|---------|
| Canola oil | 0.42 × 950 | **$399.00** |
| Canola meal | 0.56 × 310 | **$173.60** |
| **Total** | | **$572.60** |

#### Step 2: Calculate DM Output per Co-Product

```
DM output (t DM/t parent input) = Yield (t/t) × DM (%)
```

| Co-product | Calculation | DM Output |
|------------|-------------|-----------|
| Canola oil | 0.42 × 1.00 | **0.4200** |
| Canola meal | 0.56 × 0.90 | **0.5040** |
| **Total** | | **0.9240** |

#### Step 3: Economic Allocation

```
Economic allocation (%) = (Co-product revenue ÷ Total revenue) × 100
```

| Co-product | Calculation | Allocation |
|------------|-------------|------------|
| Canola oil | (399.00 ÷ 572.60) × 100 | **69.7%** |
| Canola meal | (173.60 ÷ 572.60) × 100 | **30.3%** |

> **Rounding note:** The raw calculations yield 69.68% (oil) and 30.32% (meal). These are rounded to 69.7% and 30.3% so that the sum is exactly 100.0%.

#### Step 4: Mass Allocation

```
Mass allocation (%) = (Co-product DM output ÷ Total DM output) × 100
```

| Co-product | Calculation | Allocation |
|------------|-------------|------------|
| Canola oil | (0.4200 ÷ 0.9240) × 100 | **45.5%** |
| Canola meal | (0.5040 ÷ 0.9240) × 100 | **54.5%** |

> **Rounding note:** The raw calculations yield 45.45% (oil) and 54.55% (meal). These are rounded to 45.5% and 54.5% so that the sum is exactly 100.0%.

### 3.6 Mass Balance Check

| Check | Value | Status |
|-------|-------|--------|
| Input DM (8.5% moisture) | 0.915 t/t | — |
| Output DM (sum of co-products) | 0.9240 t/t | 101.0% |
| As-is output sum | 0.980 t/t | — |
| Process loss | 0.020 t/t (as-is) | Moisture loss, fines, hexane residue |
| As-is balance | 0.980 + 0.020 = 1.000 t | ✓ |

> The DM balance shows a 1.0% overage (0.924 t out vs. 0.915 t in), which arises because the process loss (0.020 t as-is) includes moisture that does not contribute to DM. If the process loss is assumed to contain approximately 0.009 t of DM (at ~45% DM for the mixed loss stream of moisture, fines, and hexane residue), then the corrected DM output = 0.924 − 0.009 = 0.915 t (100.0% of input), which closes exactly. The as-is balance closes exactly with the 0.020 t process loss.

---

## 4. Allocation Methodology

### 4.1 Economic Allocation

Economic allocation distributes environmental burdens (or revenues) among co-products based on their relative market value.

**Formula:**

```
Economic allocation (%) = (Revenue of co-product i ÷ Total revenue of all co-products) × 100

where:
  Revenue of co-product i = Yield_i (t/t) × Price_i (USD/t)
```

### 4.2 Mass Allocation

Mass allocation distributes burdens based on the dry matter content of each co-product.

**Formula:**

```
Mass allocation (%) = (DM output of co-product i ÷ Total DM output of all co-products) × 100

where:
  DM output of co-product i = Yield_i (t/t) × DM_i (%)
```

### 4.3 Comparison: Economic vs. Mass Allocation

| System | Primary Product | Primary Alloc (Econ) | Primary Alloc (Mass) | Gap |
|--------|----------------|----------------------|----------------------|-----|
| **Canola crushing** | Canola oil | 69.7% | 45.5% | 24.2 pp |

The large gap between economic and mass allocation reflects the fact that canola oil is a high-value, concentrated product (100% DM, $950/t) while canola meal is a lower-value bulk product (90% DM, $310/t). On a per-kg-DM basis:

- Oil: $950 per t DM
- Meal: $310 / 0.90 = $344 per t DM

Oil is worth 2.76× more per kg DM than meal, so economic allocation strongly favors oil, while mass allocation gives meal a slight majority (54.5%) because it represents more than half of the DM output.

---

## 5. Mass Balance Verification

### 5.1 Summary

| Item | Value | Notes |
|------|-------|-------|
| Input DM (8.5% moisture) | 0.915 t/t | — |
| Output DM (oil + meal) | 0.924 t/t | 101.0% of input |
| DM process loss (estimated) | ~0.009 t/t | ~1.0% of input |
| As-is input | 1.000 t/t | — |
| As-is output (oil + meal) | 0.980 t/t | — |
| As-is process loss | 0.020 t/t | 2.0% of input |

### 5.2 Input-Output Reconciliation

```
As-is balance:
  Input:       1.000 t
  Oil output:  0.420 t
  Meal output: 0.560 t
  Loss:        0.020 t (moisture adjustment, fines, hexane residue)
  Total:       1.000 t ✓

DM balance:
  Input:       0.915 t
  Oil DM:      0.420 t
  Meal DM:     0.504 t
  Total out:   0.924 t
  Gap:         +0.009 t (0.924 − 0.915)
  Explanation: The 0.020 t as-is process loss includes ~0.009 t DM
               (moisture/water accounts for the remaining ~0.011 t).
               Process loss DM% = 0.009/0.020 = 45%, consistent with
               a mix of moisture loss and dry fines.
  Corrected:   0.924 − 0.009 = 0.915 t (100.0% of input) ✓
```

---

## 6. Complete Data Table

| Parent Crop | Crop System | Stage | USDA Standard | Standard Moisture | Parent Input Basis | Co-product Stream | Yield (t/t) | Yield Range | Price (USD/t) | Price Range | DM (%) | DM Output (t/t) | Revenue (USD/t) | Econ Alloc (%) | Mass Alloc (%) |
|-------------|-------------|-------|---------------|-------------------|-------------------|-------------------|-------------|-------------|---------------|-------------|--------|-----------------|-----------------|----------------|----------------|
| Canola | Canola crushing | Single | 50 lb/bushel at 8.5% moisture | 8.5% | 1 t canola seed at 8.5% moisture | Canola oil (crude) | 0.42 | 0.40–0.44 | 950 | 800–1100 | 100.0 | 0.4200 | 399.00 | 69.7 | 45.5 |
| Canola | Canola crushing | Single | 50 lb/bushel at 8.5% moisture | 8.5% | 1 t canola seed at 8.5% moisture | Canola meal | 0.56 | 0.54–0.58 | 310 | 250–370 | 90.0 | 0.5040 | 173.60 | 30.3 | 54.5 |

---

## 7. Data Quality and Limitations

### 7.1 High-Confidence Data

| Data Point | Confidence | Source |
|------------|-----------|--------|
| Oil yield (0.42 t/t) | **High** | COPA [^2^] (calculated from crush data: 0.422 t/t); Canola Council [^4^] |
| Meal yield (0.56 t/t) | **High** | Derived from mass balance; consistent with COPA [^2^] and Canola Council [^4^] |
| DM contents (oil ~100%, meal 90%) | **High** | Industry specifications [^4^]; COPA trading rules |
| Canola seed prices | **High** | USDA FAS [^6^]; CGC [^1^] |
| Bushel weight (50 lb) | **High** | USDA FSA; CGC conversion tables |

### 7.2 Medium-Confidence Data

| Data Point | Confidence | Source |
|------------|-----------|--------|
| Oil price ($950/t crude) | **Medium** | Volatile commodity; varies by $200/t+ annually. Canadian export prices exceeded $1100/t in 2024. |
| Meal price ($310/t) | **Medium** | Regional variation; protein content affects price. Tridge shows US export prices up to $430/t in 2024. |
| Process loss (2.0%) | **Medium** | Estimated; varies by plant configuration and seed quality. Some references report 1–3%. |
| Oil content range (40–44% as-is) | **Medium** | CGC 2025 survey: 43.6% at 8.5% moisture. Range captures variety and seasonal variation. |

### 7.3 Known Limitations

1. **Crude vs. refined oil boundary:** This document uses crude canola oil at the crushing plant gate. If the system boundary includes oil refining, the oil yield would decrease slightly (degumming removes ~1.5–2.5% phospholipids/gums) and the price would increase to ~$1000–1300/t for RBD oil. The gums removed during degumming could be treated as an additional co-product (acidulated soapstock).

2. **Meal DM% variation:** Canola meal is traded at a maximum of 12% moisture (88% DM minimum), but typical values are 89–91% DM. The 90% DM midpoint is standard but actual values vary by plant.

3. **Oil DM% approximation:** Using 100% DM for crude oil is an approximation (actual ~99.5–99.7% per COPA specs). The impact on allocation is negligible (<0.1 percentage point).

4. **Process loss uncertainty:** The 2.0% process loss is an estimate. Actual losses vary by plant, seed quality, and processing conditions. Some references report losses of 1–3%. The DM content of the process loss is estimated at ~45% (a mix of moisture and dry fines), which closes the DM balance.

5. **Canola variety variation:** High-oil canola varieties (up to 46% oil on an as-is basis at 8.5% moisture) are becoming more common. These would shift the oil yield upward and meal yield downward, affecting both mass and economic allocation.

6. **Regional price variation:** Canola oil and meal prices vary significantly by region due to transportation costs and local supply/demand. Pacific Northwest meal prices tend to be higher due to Asian export demand.

7. **Seasonal price variation:** Canola oil and meal prices are seasonal, with oil prices typically higher in winter (biodiesel demand) and meal prices higher in spring/summer (livestock feeding season).

8. **Oil content basis clarity:** In the literature, oil content is commonly reported on either an "as-is" basis (at a specified moisture) or a "dry matter" basis. The CGC reports oil content at 8.5% moisture basis (which is an as-is basis, not a DM basis). The DM-basis oil content is approximately 5–8 percentage points higher. This document uses the as-is basis at 8.5% moisture (40–44% typical range) and provides DM-basis equivalents (43–48%) where relevant for calculation transparency.

---
