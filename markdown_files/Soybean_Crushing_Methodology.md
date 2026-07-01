# Soybean Crushing: Co-Product Allocation Methodology, Data Sources, and Calculations
**Document Version:** 1
**Date:** June 2026
**Basis:** 1 metric ton (t) of soybeans at 13% moisture (USDA standard trading basis)
**Price Period:** MY 2024/25 season average (unless otherwise noted)
**Fact-Check Date:** June 2026

## Table of Contents
- [1. Standard Basis and Conversions](#1-standard-basis-and-conversions)
- [2. Data Sources and References](#2-data-sources-and-references)
- [3. Soybean Crushing System](#3-soybean-crushing-system)
- [4. Allocation Methodology](#4-allocation-methodology)
- [5. Mass Balance Verification](#5-mass-balance-verification)
- [6. Complete Data Table](#6-complete-data-table)
- [7. Data Quality and Limitations](#7-data-quality-and-limitations)

## 1. Standard Basis and Conversions

### 1.1 Parent Input Definition
| Parameter | Value | Source |
| --- | --- | --- |
| Parent crop | Soybean (*Glycine max*) | — |
| Input quantity | 1 metric ton (1,000 kg) | — |
| Moisture content (trading basis) | 13.0% | USDA trading weight basis for soybeans; 60 lb/bu defined at 13% moisture [^1^] |
| Moisture content (actual delivered) | ~10.75% | NOPA LCI survey [^3^] reports actual delivered moisture averages 10.75% across 52 facilities |
| Dry matter (DM) input — trading basis | 0.870 t DM/t soybeans | Calculated: 1.000 × (1 − 0.13) = 0.870 |
| Dry matter (DM) input — delivered basis | ~0.893 t DM/t soybeans | Calculated: 1.000 × (1 − 0.1075) = 0.893 |
| Bushel equivalent | 36.74 bushels/t | 1,000 kg ÷ 27.216 kg/bu (60 lb at 13% moisture) |
| Bushel weight | 60.0 lb (27.216 kg) | USDA standard No. 1 soybean; 60 lb/bu defined at 13% moisture [^1^][^2^] |
| Average oil content | 19.82% (lipids) | NOPA LCI survey [^3^]. Note: recent Iowa Soybean Association (2025) data reports 21.7% average (range 17.7–25.1%); the 19.82% figure is specific to the NOPA 2023 survey year. |

### 1.2 Unit Conversions
| Conversion | Factor |
| --- | --- |
| 1 bushel soybeans | 60.0 lb = 27.216 kg |
| 1 lb | 0.453592 kg = 0.000453592 t |
| 1 t soybeans | 36.74 bushels |
| 1 short ton | 2,000 lb = 0.907185 metric ton |
| 1 metric ton | 2,204.62 lb = 1.10231 short tons |

*Note on moisture standard:* Soybeans are traded at 13% moisture, which is lower than corn (15.5%) because soybeans are naturally lower in moisture at harvest and are more stable in storage. NOPA's industry survey [^3^] reports actual delivered moisture averages 10.75%, but 13% is the official USDA trading weight basis for bushel equivalence. The 13% figure is a trading convention, not a grade-determining factor under the U.S. Standards for Soybeans (7 CFR 810.1601-1604) [^1^].

*Important: Dual-basis approach.* This document presents mass balance on the 13% trading basis (DM input = 0.870 t) for consistency with the CME crush model and USDA reporting conventions. A secondary reconciliation using the 10.75% delivered moisture basis (DM input = 0.893 t) is provided in Section 5 to close the DM mass balance.

## 2. Data Sources and References

### 2.1 Primary Sources
| Citation | Full Title | Type | URL |
| --- | --- | --- | --- |
| [^1^] | USDA AMS — Soybean Standards (formerly GIPSA) | Government (USDA) | https://www.ams.usda.gov/grades-standards/soybean-standards |
| [^2^] | CME Group (formerly CBOT). *Soybean Crush Reference Guide* | Industry/Exchange | https://www.cmegroup.com/ |
| [^3^] | NOPA (2024). *Life Cycle Inventory Data of Soybean Processing* | Industry Association | https://www.nopa.org/ |
| [^4^] | farmdoc daily, University of Illinois (2025). 3-part series: (1) *The Long-Run Evolution of Oilseed Crushing* (Aug 2025); (2) *Squeezing More Oil from the Soybean Crush* (Sep 2025); (3) *The Value of Soybean Oil in the Soybean Crush* (Oct 2025) | University/Extension | https://farmdocdaily.illinois.edu/ |
| [^5^] | USDA ERS (August 2025). *Oil Crops Outlook*, OCS-25H | Government (USDA) | https://ers.usda.gov/ |
| [^6^] | USDA WASDE (February 2026). *World Agricultural Supply and Demand Estimates* | Government (USDA) | https://www.usda.gov/ |
| [^7^] | YCharts. *Soybean Oil Price (Any Origin)* | Market Data | https://ycharts.com/indicators/soybean_oil_price |
| [^8^] | K-State Extension. *MF2438: Soybean Hulls: Composition and Feeding Value for Beef and Dairy Cattle* (January 2000) | University/Extension | https://bookstore.ksre.ksu.edu/ |
| [^9^] | Business Research Insights. *Soybean Hulls Market Growth: Size, Trend & Insights 2035* | Industry/Market | https://www.businessresearchinsights.com/ |
| [^10^] | UkrAgroConsult (August 2025). *US soybean meal production to grow 4.5% next season, prices to fall* | Industry/Market | https://ukragroconsult.com/ |
| [^11^] | Fastmarkets (February 2025). *US corn, wheat export sales rise; soybean below estimates* | Industry/Market | https://www.fastmarkets.com/ |
| [^12^] | Iowa Soybean Association (2025). *Soybean Quality Survey Data* | Industry/Research | https://www.iasoybeans.com/ |
| [^13^] | Journal of Applied Poultry Research (2023). *Soybean meal protein premium analysis* | Academic | https://doi.org/10.1016/j.japr.2023 |

### 2.2 How Sources Were Used
- **Yield data:** NOPA LCI [^3^] provided weighted average yields from 52 crushing facilities (89% of USDA-reported crush volume, data from Jan–Dec 2023). The NOPA industry averages are 0.198 t/t for oil and 0.056 t/t for hulls. However, **this document uses the mathematical midpoints of the reported ranges** (0.195 t/t for oil, 0.055 t/t for hulls) for methodological consistency across all crop processing systems.
- **Price data:** USDA ERS [^5^], WASDE [^6^], and YCharts [^7^] provided government and market price data. **This document uses the mathematical midpoints of the reported price ranges** ($1,050/t for oil, $370/t for meal, $140/t for hulls) for full consistency with the midpoint-based approach.
- **Price data (meal):** USDA ERS [^5^], WASDE [^6^], UkrAgroConsult [^10^], and Fastmarkets [^11^] provided 44% protein meal prices. A premium was calculated for 48% protein dehulled meal using published academic data [^13^].
- **Price data (hulls):** USDA AMS data via Business Research Insights [^9^] provided Q1 2025 whole and pelleted hull prices.
- **Oil content context:** Iowa Soybean Association [^12^] provides recent quality survey data showing 21.7% average oil content, which is higher than the NOPA survey figure of 19.82%.

## 3. Soybean Crushing System

### 3.1 Process Description
Soybean crushing (also called "oilseed processing") involves the following steps:
1. **Cleaning:** Foreign material (dirt, stones, weed seeds) is removed.
2. **Dehulling:** Hulls are cracked and separated from the cotyledons (meats). Hulls may be removed partially or completely depending on desired meal protein content.
3. **Conditioning:** Meats are heated to improve oil extractability.
4. **Flaking:** Meats are rolled into thin flakes to increase surface area.
5. **Solvent extraction:** Hexane is used to extract oil from the flakes.
6. **Desolventizing:** Hexane is removed from the oil (miscella) and meal (marc).
7. **Oil refining:** Crude oil is degummed, neutralized, bleached, and deodorized.
8. **Meal processing:** Meal is dried, cooled, and ground to specification.
9. **Hull processing:** Hulls may be ground, pelleted, or blended back into meal.

**Co-products generated:**
- **Soybean oil:** The primary high-value product (food, biodiesel, industrial uses).
- **Soybean meal:** The primary high-volume co-product (animal feed, protein source).
- **Soybean hulls:** A fiber-rich byproduct used in ruminant feed.

### 3.2 Co-Product Yields
| Co-product | Yield (t/t soybeans) | Range | Source & Calculation |
| --- | --- | --- | --- |
| Soybean oil | 0.195 | 0.19–0.20 | **Mathematical midpoint** of reported range. NOPA LCI [^3^] reports 0.198 kg/kg as the industry average. This document uses the true midpoint (0.195) for methodological consistency. Midpoint: (0.19 + 0.20) / 2 = 0.195 ✓ |
| Soybean meal | 0.750 | 0.74–0.76 | NOPA LCI [^3^]: 0.750 kg/kg (as-produced basis). The midpoint of 0.74–0.76 is 0.75, which matches the NOPA average. |
| Soybean hulls | 0.055 | 0.05–0.06 | **Mathematical midpoint** of reported range. NOPA LCI [^3^] reports 0.056 kg/kg as the industry average. This document uses the true midpoint (0.055) for methodological consistency. Midpoint: (0.05 + 0.06) / 2 = 0.055 ✓ |

**As-Is Yield Sum**
The as-is yields sum to **1.000 t/t soybeans** (0.195 + 0.750 + 0.055 = 1.000), perfectly closing the mass balance at the as-is level.

**Oil Yield vs. Oil Content**
Soybeans contain ~19.82% oil (lipids) by weight per the NOPA LCI survey [^3^]. The reconciliation uses the NOPA physical average (0.198 t/t). The use of 0.195 t/t in this document is a methodological midpoint choice and does not alter the physical reconciliation.

*Note:* Refining losses (degumming, neutralization, bleaching, deodorization) of ~1–2% apply downstream of the 0.195 t crude oil yield and reduce the saleable RBD oil to ~0.191–0.193 t/t.

### 3.3 Protein Content and Meal Types
| Meal Type | Protein Content | Hulls | Typical Use | Price Premium |
| --- | --- | --- | --- | --- |
| 44% protein meal | 44% crude protein | Included (not removed) | Swine, poultry, general feed | Baseline |
| 48% protein meal | 48% crude protein | Removed (dehulled) | Poultry, aquaculture, high-performance diets | +$35–50/metric ton (~$32–45/short ton) |
| High-protein concentrate | >50% protein | Removed, further processed | Specialty feeds, pet food | +$50–100/short ton |

This table uses 48% protein dehulled meal as the primary meal product because:
1. It is the standard product for the CME "board crush" calculation [^2^].
2. It represents the higher-value product stream when hulls are separated.
3. It is more comparable to international soybean meal trading specifications.

### 3.4 Dry Matter Contents
| Co-product | DM (%) | Basis |
| --- | --- | --- |
| Soybean oil | 100.0% | Refined soybean oil is pure lipid (triglycerides) with negligible moisture. |
| Soybean meal | 89.0% | Standard trading specification: maximum 12% moisture = minimum 88% DM. The 89% midpoint reflects typical delivered moisture of 10–11%. |
| Soybean hulls | 89.0% | Dried hulls are typically 88–90% DM. Whole hulls may be slightly higher in moisture if not fully dried. |

### 3.5 Prices
| Co-product | Price (USD/t) | Range | Source | Notes |
| --- | --- | --- | --- | --- |
| Soybean oil | 1,050 | 900–1,200 | USDA ERS [^5^]; WASDE [^6^]; YCharts [^7^] | **Mathematical midpoint** of reported range. MY 2024/25 season average. USDA WASDE MY 2024/25 forecast: ~42-43 cents/lb = ~$926-948/t. YCharts MY 2024/25 average: ~$979–1,077/t. The true midpoint of the range ($900 + $1,200) / 2 = $1,050 is used for methodological consistency. |
| Soybean meal (48% protein) | 370 | 340–400 | USDA ERS [^5^]; WASDE [^6^]; UkrAgroConsult [^10^]; Fastmarkets [^11^]; J. Appl. Poult. Res. [^13^] | **Mathematical midpoint** of reported range. Derived from 44% protein meal baseline: $295/short ton = $325/metric ton (WASDE Feb 2026). 48% protein premium: +$35–50/metric ton. The true midpoint of the range ($340 + $400) / 2 = $370 is used for methodological consistency. |
| Soybean hulls (whole) | 140 | 110–170 | USDA AMS; Business Research Insights [^9^] | **Mathematical midpoint** of reported range. USDA AMS FOB Midwest Q1 2025: whole hulls $105–130/short ton = $115–143/metric ton. The true midpoint of the range ($110 + $170) / 2 = $140 is used for methodological consistency. |

### 3.6 Revenue and Allocation Calculations

**Step 1: Calculate Revenue per Co-Product**
`Revenue (USD/t parent input) = Yield (t/t) × Price (USD/t)`

| Co-product | Calculation | Revenue |
| --- | --- | --- |
| Soybean oil | 0.195 × 1,050 | $204.75 |
| Soybean meal | 0.750 × 370 | $277.50 |
| Soybean hulls | 0.055 × 140 | $7.70 |
| **Total** | | **$489.95** |

**Step 2: Calculate DM Output per Co-Product**
`DM output (t DM/t parent input) = Yield (t/t) × DM (%)`

| Co-product | Calculation | DM Output |
| --- | --- | --- |
| Soybean oil | 0.195 × 1.00 | 0.1950 |
| Soybean meal | 0.750 × 0.89 | 0.6675 |
| Soybean hulls | 0.055 × 0.89 | 0.04895 |
| **Total (raw)** | | **0.91145** |
| **Total (normalized to input DM)** | | **0.8700** |

*DM normalization:* The raw DM output sum (0.91145 t) exceeds the input DM (0.870 t) by 4.76%. For ISO 14044 compliance, DM outputs are normalized. The normalization factor is 0.8700 / 0.91145 = 0.95453.

| Co-product | Calculation | Normalized DM Output |
| --- | --- | --- |
| Soybean oil | 0.1950 × 0.95453 | 0.18613 |
| Soybean meal | 0.6675 × 0.95453 | 0.63715 |
| Soybean hulls | 0.04895 × 0.95453 | 0.04672 |
| **Total** | | **0.8700** |

**Step 3: Economic Allocation**
`Economic allocation (%) = (Co-product revenue ÷ Total revenue) × 100`

| Co-product | Calculation | Allocation |
| --- | --- | --- |
| Soybean oil | (204.75 ÷ 489.95) × 100 | 41.8% |
| Soybean meal | (277.50 ÷ 489.95) × 100 | 56.6% |
| Soybean hulls | (7.70 ÷ 489.95) × 100 | 1.6% |

*Rounding note:* Raw calculations yield 41.79% (oil), 56.64% (meal), and 1.57% (hulls). Rounded: 41.8%, 56.6%, 1.6% (sum = 100.0%).

**Step 4: Mass Allocation**
`Mass allocation (%) = (Co-product normalized DM output ÷ Total DM input) × 100`

| Co-product | Calculation | Allocation |
| --- | --- | --- |
| Soybean oil | (0.18613 ÷ 0.8700) × 100 | 21.4% |
| Soybean meal | (0.63715 ÷ 0.8700) × 100 | 73.2% |
| Soybean hulls | (0.04672 ÷ 0.8700) × 100 | 5.4% |

**Step 5: Energy Allocation**
`Energy output (MJ/t parent input) = DM output (raw) × GE (MJ/kg DM) × 1,000`

| Co-product | Calculation | Energy Output (MJ/t) | Allocation |
| --- | --- | --- | --- |
| Soybean oil | 0.1950 × 39.3 × 1,000 | 7,663.5 | (7,663.5 ÷ 21,699.245) × 100 = **35.3%** |
| Soybean meal | 0.6675 × 19.7 × 1,000 | 13,149.75 | (13,149.75 ÷ 21,699.245) × 100 = **60.6%** |
| Soybean hulls | 0.04895 × 18.1 × 1,000 | 885.995 | (885.995 ÷ 21,699.245) × 100 = **4.1%** |
| **Total** | | **21,699.245** | **100.0%** |

## 4. Allocation Methodology

### 4.1 Economic Allocation
Economic allocation distributes environmental burdens (or revenues) among co-products based on their relative market value.
**Formula:**
`Economic allocation (%) = (Revenue of co-product i ÷ Total revenue of all co-products) × 100`

### 4.2 Mass Allocation
Mass allocation distributes burdens based on the dry matter content of each co-product, normalized to ensure mass balance closure.
**Formula:**
`Mass allocation (%) = (Normalized DM output of co-product i ÷ Total DM input) × 100`

### 4.3 Energy Allocation
Energy allocation distributes burdens based on the gross energy content of each co-product.
**Formula:**
`Energy allocation (%) = (Energy output of co-product i ÷ Total energy output of all co-products) × 100`
`Energy output (MJ) = DM output (raw) × GE (MJ/kg DM) × 1,000`

### 4.4 Summary of Allocations
| Co-product | Economic | Mass | Energy |
| --- | --- | --- | --- |
| Soybean oil | 41.8% | 21.4% | 35.3% |
| Soybean meal | 56.6% | 73.2% | 60.6% |
| Soybean hulls | 1.6% | 5.4% | 4.1% |
| **Total** | **100.0%** | **100.0%** | **100.0%** |

### 4.5 Historical Context: The Shift in Economic Allocation
| Period | Oil Price ($/t) | Meal Price ($/t) | Oil Revenue ($/t) | Meal Revenue ($/t) | Oil Alloc | Meal Alloc |
| --- | --- | --- | --- | --- | --- | --- |
| Pre-2020 | ~$700 | ~$350 | $136.50 | $262.50 | ~34% | ~66% |
| 2020–2023 | ~$1,200 | ~$450 | $234.00 | $337.50 | ~41% | ~59% |
| MY 2024/25 | ~$1,050 | ~$370 | $204.75 | $277.50 | ~42% | ~58% |

## 5. Mass Balance Verification

### 5.1 Input-Output Reconciliation (13% Trading Basis)
| Check | Value | Status |
| --- | --- | --- |
| Input: Soybeans at 13% moisture | 1.000 t | — |
| Input moisture (trading basis) | 13.0% | — |
| Input DM (trading basis) | 0.870 t | — |
| Output: Soybean oil (as-is) | 0.195 t | ✓ |
| Output: Soybean meal (as-is) | 0.750 t | ✓ |
| Output: Soybean hulls (as-is) | 0.055 t | ✓ |
| Total as-is output | 1.000 t | 100.0% of input |
| Output DM: Oil | 0.1950 t | ✓ |
| Output DM: Meal | 0.6675 t | ✓ |
| Output DM: Hulls | 0.04895 t | ✓ |
| Total DM output (raw) | 0.91145 t | 104.76% of input DM |
| Total DM output (normalized) | 0.8700 t | 100.0% of input DM ✓ |

### 5.2 Reconciliation Using Delivered Moisture Basis
| Check | Value | Status |
| --- | --- | --- |
| Input: Soybeans at 10.75% moisture | 1.000 t | — |
| Input DM (delivered basis) | 0.893 t | — |
| Total DM output (raw, from yields) | 0.91145 t | 102.07% of input DM |
| Residual excess | ~0.0185 t | ~2.1% — within industry uncertainty range |
| Total DM output (normalized) | 0.893 t | 100.0% of input DM ✓ |

### 5.3 Explanation of Mass Balance
**As-is mass equals input (100.0%):** The yields sum to 1.000 t/t soybeans.

**DM output exceeds input DM on 13% basis (104.76%):** The DM output (0.91145 t) exceeds the 13%-basis DM input (0.870 t) by 4.76%. This is primarily caused by the mismatch between the 13% trading standard and the 10.75% actual delivered moisture. When recalculated on the 10.75% delivered basis, the excess reduces to approximately 2.1%, which is within the typical uncertainty range for aggregate industry data from 52 facilities.

## 6. Complete Data Table
| Parent Crop | Crop System | Stage | USDA Standard | Standard Moisture | Parent Input Basis | Co-product Stream | Yield (t/t) | Yield Range | Price (USD/t) | Price Range | DM (%) | DM Output Raw (t/t) | DM Output Norm (t/t) | Revenue (USD/t) | Econ Alloc (%) | Mass Alloc (%) | Energy Alloc (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Soybean | Soybean crushing | Single | 60 lb/bushel at 13% moisture | 13% | 1 t soybeans at 13% moisture | Soybean oil | 0.195 | 0.19–0.20 | 1,050 | 900–1,200 | 100.0 | 0.1950 | 0.1861 | 204.75 | 41.8 | 21.4 | 35.3 |
| Soybean | Soybean crushing | Single | 60 lb/bushel at 13% moisture | 13% | 1 t soybeans at 13% moisture | Soybean meal (48% protein, dehulled) | 0.750 | 0.74–0.76 | 370 | 340–400 | 89.0 | 0.6675 | 0.6372 | 277.50 | 56.6 | 73.2 | 60.6 |
| Soybean | Soybean crushing | Single | 60 lb/bushel at 13% moisture | 13% | 1 t soybeans at 13% moisture | Soybean hulls (whole) | 0.055 | 0.05–0.06 | 140 | 110–170 | 89.0 | 0.04895 | 0.0467 | 7.70 | 1.6 | 5.4 | 4.1 |

## 7. Data Quality and Limitations

### 7.1 High-Confidence Data (Industry/Government Sources)
| Data Point | Confidence | Source |
| --- | --- | --- |
| Oil yield range (0.19–0.20) | High | Well-documented; NOPA LCI [^3^] industry average 0.198 falls within this range |
| Meal yield (0.750 t/t) | High | NOPA LCI [^3^] (52 facilities, 89% of U.S. crush) |
| Hull yield range (0.05–0.06) | High | Well-documented; NOPA LCI [^3^] industry average 0.056 falls within this range |
| Price ranges | High | USDA WASDE [^6^]; YCharts [^7^] |
| DM contents (89% meal, 100% oil) | High | Industry trading specifications |

### 7.2 Medium-Confidence Data (Estimated or Derived)
| Data Point | Confidence | Source |
| --- | --- | --- |
| Oil yield (0.195 t/t) | Medium | Mathematical midpoint of range; NOPA average is 0.198 |
| Hull yield (0.055 t/t) | Medium | Mathematical midpoint of range; NOPA average is 0.056 |
| Oil price ($1,050/t) | Medium | Mathematical midpoint of range; market survey average is ~$1,020 |
| Meal price ($370/t) | Medium | Mathematical midpoint of range; market survey average is ~$369 |
| 48% protein premium ($35–50/MT) | Medium | Academic literature [^13^]; USB market view |
| DM normalization factor | Medium | Proportional normalization is the standard LCA approach |

### 7.3 Known Limitations
- **Midpoint-based approach:** This document uses mathematical midpoints for all yields and prices (0.195, 0.055, $1,050, $370, $140) for full methodological consistency across all crop processing systems. The NOPA industry averages (0.198, 0.056) and survey-derived prices (~$1,020, ~$369) fall within the reported ranges and would yield slightly different allocation factors (oil econ ~41.5%, oil mass ~21.6%).
- **Protein content ambiguity:** The table uses 48% protein meal. If 44% protein meal is required, the meal price should be ~$325/t and hulls should be removed as a separate co-product.
- **Regional price variation:** Soybean product prices vary significantly by location.
- **Temporal volatility:** The renewable diesel boom has increased price volatility.
- **Hull form:** Whole hulls ($140/t) vs. pelleted hulls ($175/t) vs. ground hulls ($130/t) have different prices.
- **Waste not allocated:** The CME standard [^2^] includes 1 lb/bu (0.017 t/t) of waste. This is not allocated because it has no market value.
- **Refining losses:** The 0.195 t/t oil yield is crude oil. Further refining incurs ~1–2% loss, which is not captured.
- **Mass balance normalization:** The ~4.76% DM excess on the 13% trading basis is a methodological artifact. DM outputs are proportionally normalized for ISO 14044 compliance.
- **Oil content variance:** The NOPA LCI [^3^] reports 19.82% average oil content, but the Iowa Soybean Association [^12^] reports 21.7% average.
