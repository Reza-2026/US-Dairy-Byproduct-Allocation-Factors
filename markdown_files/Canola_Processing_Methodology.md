# Canola Processing: Co-Product Allocation Methodology, Data Sources, and Calculations
**Document Version:** 1.0
**Date:** June 2026
**Basis:** 1 metric ton (t) of canola seed at 8.5% moisture (CGC reporting basis for oil and protein content)
**Price Period:** 2024–2025 average (unless otherwise noted)

## Table of Contents
- [1. Standard Basis and Conversions](#1-standard-basis-and-conversions)
- [2. Data Sources and References](#2-data-sources-and-references)
- [3. Canola Crushing](#3-canola-crushing)
- [4. Allocation Methodology](#4-allocation-methodology)
- [5. Mass Balance Verification](#5-mass-balance-verification)
- [6. Complete Data Table](#6-complete-data-table)
- [7. Data Quality and Limitations](#7-data-quality-and-limitations)

## 1. Standard Basis and Conversions

### 1.1 Parent Input Definition
| Parameter | Value | Source |
| --- | --- | --- |
| Parent crop | Canola (*Brassica napus*, low-erucic acid rapeseed) | — |
| Input quantity | 1 metric ton (1,000 kg) | — |
| Moisture content | 8.5% | Canadian Grain Commission (CGC) constant moisture basis for reporting oil and protein content [^1^]. This is an analytical reporting convention, not a trading standard; see the note below. |
| Dry matter (DM) input | 0.915 t DM/t canola | Calculated: 1.000 × (1 − 0.085) = 0.915 |
| Bushel equivalent | 44.09 bushels/t | 1,000 kg ÷ 22.68 kg/bu (50 lb at standard moisture) |
| Bushel weight | 50.0 lb (22.68 kg) | USDA/CGC standard for No. 1 Canada canola [^1^] |

*Note on moisture basis:* This document uses 8.5% moisture as the calculation basis, which is the CGC's constant moisture basis for reporting oil and protein content in quality surveys. This is NOT the same as a "trading standard" moisture — the CGC does not set a specific moisture percentage as a trading standard for canola. The CGC grading system uses moisture thresholds: straight (<10%), tough (10–12.5%), and damp (>12.5%). The Canola Council of Canada recommends ≤8% moisture for safe long-term storage. The 8.5% basis gives DM input = 0.915 t/t (instead of 0.910 t/t at 9% moisture). The 0.5% difference affects the DM balance slightly but does not materially change the allocation results.

### 1.2 Unit Conversions
| Conversion | Factor |
| --- | --- |
| 1 bushel canola | 50.0 lb = 22.68 kg (standard) |
| 1 lb | 0.453592 kg = 0.000453592 t |
| 1 t canola | 44.09 bushels (at 50 lb/bu) |

*Note on canola vs. rapeseed:* "Canola" refers to cultivars of rapeseed (*Brassica napus* or *B. rapa*) with low erucic acid (<2%) and low glucosinolates (<30 μmol/g). In Europe and Australia, the equivalent crop is typically called "rapeseed" or "oilseed rape" and may have slightly different oil content (42–45% on an as-is basis vs. 40–44% for canola). This document uses North American canola specifications.

## 2. Data Sources and References

### 2.1 Primary Sources
| Citation | Full Title | Type | URL |
| --- | --- | --- | --- |
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

## 3. Canola Crushing

### 3.1 Process Description
Canola crushing extracts oil from canola seed through a combination of mechanical pressing and solvent extraction:
1.  **Cleaning:** Remove foreign material, weed seeds, and dockage.
2.  **Pre-conditioning:** Heat and flake the seed to rupture cell walls and increase oil availability.
3.  **Pre-pressing:** Mechanically extract approximately 60–70% of the oil using a screw press (expeller). This produces press cake (still containing ~15–20% oil).
4.  **Solvent extraction:** The press cake is washed with hexane to extract the remaining oil. The defatted material (marc) is then toasted to remove residual hexane.
5.  **Desolventizing/Toasting:** The marc is heated to evaporate hexane and toast the meal, improving protein digestibility and reducing glucosinolates.
6.  **Oil refining (optional):** Crude oil may be refined (degummed, neutralized, bleached, deodorized) to produce RBD canola oil.

**Co-products generated:**
-   **Canola oil:** The primary product — either crude (unrefined) or refined (RBD). This document uses crude canola oil as the primary product at the crushing plant gate.
-   **Canola meal:** The primary co-product — the defatted, toasted seed residue, used primarily as a high-protein animal feed ingredient.

### 3.2 Co-Product Yields
| Co-product | Yield (t/t canola) | Range | Source & Calculation |
| --- | --- | --- | --- |
| Canola oil (crude) | 0.42 | 0.40–0.44 | COPA [^2^]: Canadian industry average ~0.415–0.430 t/t (2023–2025; calculated from 11.6 MMT seed crushed → 4.9 MMT oil = 0.422 t/t). Canola Council [^4^]: typical range 40–44%. USDA ERS [^3^]: US crush yields ~0.410–0.425 t/t. The 0.42 midpoint is the mathematical midpoint of the stated range and represents a modern Canadian crush plant processing No. 1 canola. |
| Canola meal | 0.56 | 0.54–0.58 | Derived from mass balance: 1.000 − 0.42 (oil) − 0.02 (process loss) = 0.56. Canola Council [^4^]: meal yield typically 55–58% at 88–90% DM. COPA [^2^]: meal production consistent with ~0.56 t/t. Range 0.54–0.58 captures variation. |

**Yield Calculation Rationale**
*Oil yield:*
Canola seed typically contains 40–44% oil on an as-is basis at 8.5% moisture (approximately 43–48% on a DM basis). The CGC 2025 harvest survey reports 43.6% oil at 8.5% moisture basis, which equals 47.7% on a DM basis (43.6% ÷ 0.915 = 47.7%). The extraction rate (proportion of oil in the seed that is recovered) is typically 97–99% in modern plants using pre-press/solvent extraction.
- Oil content of seed (as-is, 8.5% moisture basis): ~43.6% (CGC 2025 survey)
- Oil as-is per t seed: 0.436 t
- Extraction rate: 98%
- Oil recovered (as-is): 0.436 × 0.98 = 0.427 t/t

Three independent estimates of the oil yield are therefore available: 0.427 t/t from the composition-and-extraction route above, 0.422 t/t from COPA's reported Canadian crush data [^2^], and 0.420 t/t as the midpoint of the 0.40–0.44 range. All three fall within the stated range and differ by less than 2%. This document adopts **0.420 t/t**, the range midpoint, for consistency with the treatment of every other parameter in the database; the two higher estimates indicate that this is a marginally conservative choice for oil and correspondingly generous for meal.

*Meal yield (derived from mass balance):*
- Input: 1.000 t canola seed
- Oil output: 0.420 t
- Process loss: 0.020 t (moisture adjustment, fines, hexane recovery residue)
- Meal output: 1.000 − 0.420 − 0.020 = 0.560 t

The 2% process loss accounts for:
- Moisture loss during pre-conditioning and toasting (~0.5–1.0%)
- Fines and screenings lost during cleaning (~0.3–0.5%)
- Hexane absorption and recovery residue (~0.1–0.3%)
- Miscellaneous handling losses (~0.2–0.5%)

### 3.3 Dry Matter Contents
| Co-product | DM (%) | Basis |
| --- | --- | --- |
| Canola oil (crude) | 100.0% | Crude canola oil contains ~0.3% moisture and volatile matter per COPA trading specifications. For allocation purposes and strict mass balance modeling, 100% DM is used as a standard approximation for vegetable oils. |
| Canola meal (dried) | 88.0% | Standard specification for traded canola meal requires a maximum of 12% moisture (minimum 88% DM) for safe storage and transport [^4^]. While some plant-gate samples test at 90% DM, the 88% DM (12% moisture) trading boundary is used here because it is the specification traded against and because a higher figure cannot be reconciled with the process loss stream (see Section 7.3). |

### 3.4 Prices
| Co-product | Price (USD/t) | Range | Source | Notes |
| --- | --- | --- | --- | --- |
| Canola oil (crude) | 950 | 800–1100 | USDA FAS [^6^]; IndexBox [^5^] | Crude canola oil FOB: $800–1100/t (2024–2025). RBD canola oil: $1000–1300/t. The $950/t midpoint is the mathematical midpoint of the stated range ($800 + $1100) / 2 = $950. Prices are volatile and influenced by global vegetable oil markets (palm, soy, sunflower). |
| Canola meal | 310 | 250–370 | USDA ERS [^3^]; Tridge [^7^] | Canola meal (34–36% protein [^8^]): $250–370/t (2024–2025). Prices vary by region, protein content, and proximity to livestock operations. Midpoint $310/t is the mathematical midpoint of the stated range ($250 + $370) / 2 = $310. |

### 3.5 Revenue and Allocation Calculations

**Step 1: Calculate Revenue per Co-Product**
`Revenue (USD/t parent input) = Yield (t/t) × Price (USD/t)`

| Co-product | Calculation | Revenue |
| --- | --- | --- |
| Canola oil | 0.42 × 950 | $399.00 |
| Canola meal | 0.56 × 310 | $173.60 |
| **Total** | | **$572.60** |

**Step 2: Calculate DM Output per Co-Product**
`DM output (t DM/t parent input) = Yield (t/t) × DM (%)`

| Co-product | Calculation | DM Output |
| --- | --- | --- |
| Canola oil | 0.42 × 1.00 | 0.4200 |
| Canola meal | 0.56 × 0.88 | 0.4928 |
| **Total** | | **0.9128** |

**Step 3: Economic Allocation**
`Economic allocation (%) = (Co-product revenue ÷ Total revenue) × 100`

| Co-product | Calculation | Allocation |
| --- | --- | --- |
| Canola oil | (399.00 ÷ 572.60) × 100 | 69.7% |
| Canola meal | (173.60 ÷ 572.60) × 100 | 30.3% |
| **Total** | | **100.0%** |

*Rounding note:* The raw calculations yield 69.68% (oil) and 30.32% (meal). These are rounded to 69.7% and 30.3% so that the sum is exactly 100.0%.

**Step 4: Mass Allocation**
`Mass allocation (%) = (Co-product DM output ÷ Total DM output) × 100`

| Co-product | Calculation | Allocation |
| --- | --- | --- |
| Canola oil | (0.4200 ÷ 0.9128) × 100 | 46.0% |
| Canola meal | (0.4928 ÷ 0.9128) × 100 | 54.0% |
| **Total** | | **100.0%** |

*Rounding note:* The raw calculations yield 46.01% (oil) and 53.99% (meal). These are rounded to 46.0% and 54.0% so that the sum is exactly 100.0%.

### 3.6 Mass Balance Check
The as-is, dry-matter and water balances all close against the 1.000 t input. The full reconciliation, including the derivation of the dry-matter and water content of the process loss stream, is given in Section 5.

## 4. Allocation Methodology

### 4.1 Economic Allocation
Economic allocation distributes environmental burdens (or revenues) among co-products based on their relative market value.
**Formula:**
`Economic allocation (%) = (Revenue of co-product i ÷ Total revenue of all co-products) × 100`

### 4.2 Mass Allocation
Mass allocation distributes burdens based on the dry matter content of each co-product.
**Formula:**
`Mass allocation (%) = (DM output of co-product i ÷ Total DM output of all co-products) × 100`

### 4.3 Comparison: Economic vs. Mass Allocation
| System | Primary Product | Primary Alloc (Econ) | Primary Alloc (Mass) | Gap |
| --- | --- | --- | --- | --- |
| Canola crushing | Canola oil | 69.7% | 46.0% | 23.7 pp |

The large gap between economic and mass allocation reflects the fact that canola oil is a high-value, concentrated product (100% DM, $950/t) while canola meal is a lower-value bulk product (88% DM, $310/t). On a per-kg-DM basis:
-   Oil: $950 per t DM
-   Meal: $310 / 0.88 = $352 per t DM
Oil is worth 2.70× more per kg DM than meal, so economic allocation strongly favors oil, while mass allocation gives meal a slight majority (54.0%) because it represents more than half of the DM output.

## 5. Mass Balance Verification

### 5.1 Summary
| Item | Value | Notes |
| --- | --- | --- |
| Input As-Is | 1.000 t/t | — |
| Input DM (8.5% moisture) | 0.915 t/t | — |
| Output As-Is (oil + meal) | 0.980 t/t | — |
| Output DM (oil + meal) | 0.9128 t/t | — |
| As-is process loss | 0.020 t/t | 2.0% of input |
| Process loss DM | 0.0022 t/t | Derived from water balance closure |
| Process loss Water | 0.0178 t/t | Derived from water balance closure |

The dry-matter and water content of the process loss stream are not measured; they are derived from the water balance. Input water (0.085 t) less the water leaving in the meal (0.56 × 0.12 = 0.0672 t) leaves 0.0178 t of water in the loss stream, so the loss carries 0.020 − 0.0178 = 0.0022 t of dry matter, an 11% DM stream consistent with a mixture of evaporated moisture and dry fines.

### 5.2 Input-Output Reconciliation
**As-is balance:**
  Input:       1.0000 t
  Oil output:  0.4200 t
  Meal output: 0.5600 t
  Loss:        0.0200 t (moisture adjustment, fines, hexane residue)
  Total:       1.0000 t ✓

**DM balance:**
  Input DM:    0.9150 t
  Oil DM:      0.4200 t
  Meal DM:     0.4928 t
  Loss DM:     0.0022 t
  Total out:   0.9150 t ✓ (100.0% of input)

**Water balance:**
  Input Water: 0.0850 t
  Oil Water:   0.0000 t
  Meal Water:  0.0672 t (0.56 t × 12% moisture)
  Loss Water:  0.0178 t
  Total out:   0.0850 t ✓ (100.0% of input)

## 6. Complete Data Table
| Parent Crop | Crop System | Stage | USDA Standard | Standard Moisture | Parent Input Basis | Co-product Stream | Yield (t/t) | Yield Range | Price (USD/t) | Price Range | DM (%) | DM Output (t/t) | Revenue (USD/t) | Econ Alloc (%) | Mass Alloc (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Canola | Canola crushing | Single | CGC No. 1 Canada, 50 lb/bushel | 8.5% (CGC analytical basis) | 1 t canola seed at 8.5% moisture | Canola oil (crude) | 0.42 | 0.40–0.44 | 950 | 800–1100 | 100.0 | 0.4200 | 399.00 | 69.7 | 46.0 |
| Canola | Canola crushing | Single | CGC No. 1 Canada, 50 lb/bushel | 8.5% (CGC analytical basis) | 1 t canola seed at 8.5% moisture | Canola meal | 0.56 | 0.54–0.58 | 310 | 250–370 | 88.0 | 0.4928 | 173.60 | 30.3 | 54.0 |

## 7. Data Quality and Limitations

### 7.1 High-Confidence Data
| Data Point | Confidence | Source |
| --- | --- | --- |
| Oil yield (0.42 t/t) | High | COPA [^2^] (calculated from crush data: 0.422 t/t); Canola Council [^4^] |
| Meal yield (0.56 t/t) | High | Derived from mass balance; consistent with COPA [^2^] and Canola Council [^4^] |
| DM contents (oil 100%, meal 88%) | High | Industry specifications [^4^]; COPA trading rules. 88% DM is the standard maximum 12% moisture trading threshold. |
| Bushel weight (50 lb) | High | CGC [^1^] conversion tables |

### 7.2 Medium-Confidence Data
| Data Point | Confidence | Source |
| --- | --- | --- |
| Oil price ($950/t crude) | Medium | Volatile commodity; varies by $200/t+ annually. Canadian export prices exceeded $1100/t in 2024. |
| Meal price ($310/t) | Medium | Regional variation; protein content affects price. Tridge shows US export prices up to $430/t in 2024. |
| Process loss (2.0%) | Medium | Estimated; varies by plant configuration and seed quality. Some references report 1–3%. |
| Oil content range (40–44% as-is) | Medium | CGC 2025 survey: 43.6% at 8.5% moisture. Range captures variety and seasonal variation. |

### 7.3 Known Limitations
-   **Crude vs. refined oil boundary:** This document uses crude canola oil at the crushing plant gate. If the system boundary includes oil refining, the oil yield would decrease slightly (degumming removes ~1.5–2.5% phospholipids/gums) and the price would increase to ~$1000–1300/t for RBD oil. The gums removed during degumming could be treated as an additional co-product (acidulated soapstock).
-   **Meal DM% variation:** Canola meal is traded at a maximum of 12% moisture (88% DM minimum), but typical values at the plant gate may be 89–91% DM. This document strictly utilizes the 88% DM (12% moisture) boundary. Using a higher DM% (e.g., 90%) without adjusting the process loss parameters creates a physical impossibility where the water content of the waste stream exceeds the total mass of the waste stream. 
-   **Process loss uncertainty:** The 2.0% process loss is an estimate. Actual losses vary by plant, seed quality, and processing conditions. The DM content of the process loss is mathematically derived at ~11% (0.0022 t DM / 0.020 t As-Is), representing a mix of moisture evaporation and dry fines.
-   **Canola variety variation:** High-oil canola varieties (up to 46% oil on an as-is basis at 8.5% moisture) are becoming more common. These would shift the oil yield upward and meal yield downward, affecting both mass and economic allocation.
-   **Regional price variation:** Canola oil and meal prices vary significantly by region due to transportation costs and local supply/demand. Pacific Northwest meal prices tend to be higher due to Asian export demand.
-   **Seasonal price variation:** Canola oil and meal prices are seasonal, with oil prices typically higher in winter (biodiesel demand) and meal prices higher in spring/summer (livestock feeding season).
-   **Oil content basis clarity:** In the literature, oil content is commonly reported on either an "as-is" basis (at a specified moisture) or a "dry matter" basis. The CGC reports oil content at 8.5% moisture basis (which is an as-is basis, not a DM basis). The DM-basis oil content is approximately 5–8 percentage points higher. This document uses the as-is basis at 8.5% moisture (40–44% typical range) and provides DM-basis equivalents (43–48%) where relevant for calculation transparency.