# Soybean Crushing: Co-Product Allocation Methodology, Data Sources, and Calculations
**Document Version:** 1
**Date:** June 2026
**Basis:** 1 metric ton (t) of soybeans at 13% moisture (USDA standard trading basis)
**Price Period:** MY 2024/25 season average (unless otherwise noted)

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

### 1.2 Convention for Adopted Values

Every yield, price, and DM% in this document is reported as an adopted point value together with the range it was drawn from. **Unless a row states otherwise, the adopted value is the midpoint of its stated range**, and the range is the parameter that carries the evidence. Point values are given to the precision the underlying sources support and are not intended to imply plant-level accuracy. Derived quantities (DM outputs, revenues, allocation percentages) are carried at four decimals internally and reported to one decimal place.

### 1.3 Unit Conversions
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
| [^13^] | USDA AMS. *National Feedstuff Wholesale Prices* — 44% and 48% protein soybean meal quotations, used to establish the protein premium | Government (USDA) | https://www.ams.usda.gov/market-news/livestock-poultry-grain |

### 2.2 How Sources Were Used
- **Yield data:** NOPA LCI [^3^] provided weighted average yields from 52 crushing facilities (89% of USDA-reported crush volume, Jan–Dec 2023): 0.198 t/t oil, 0.750 t/t meal, 0.056 t/t hulls. This document adopts the midpoints of the reported ranges (0.195 and 0.055) rather than the NOPA point estimates, for consistency of treatment across all crop processing systems in this work. That is a convention, not a judgement that the midpoint is more accurate — NOPA's figures are measured across most of the U.S. industry and are the stronger evidence. Section 7.3 gives the allocation factors that result from using the NOPA values instead; the difference is under half a percentage point.
- **Price data:** USDA ERS [^5^], WASDE [^6^], and YCharts [^7^] provided government and market price data, from which the adopted midpoints ($1,050/t oil, $370/t meal, $140/t hulls) are taken.
- **Price data (meal):** USDA ERS [^5^], WASDE [^6^], UkrAgroConsult [^10^], and Fastmarkets [^11^] provided 44% protein meal prices. The premium for 48% protein dehulled meal is taken from the spread between the two grades in USDA AMS feedstuff quotations [^13^].
- **Price data (hulls):** USDA AMS data via Business Research Insights [^9^] provided Q1 2025 whole and pelleted hull prices.
- **Oil content context:** Iowa Soybean Association [^12^] provides recent quality survey data showing 21.7% average oil content, which is higher than the NOPA survey figure of 19.82%.
- **Industry context:** farmdoc daily [^4^] documents the long-run rise in U.S. crush capacity and oil extraction driven by renewable diesel demand, which is the background to the price volatility noted in Section 7.3.
- **Hull composition and feeding value:** K-State Extension MF2438 [^8^] provided composition and ruminant feeding-value context for soybean hulls.

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
| Soybean oil | 0.195 | 0.19–0.20 | Midpoint of the reported range. NOPA LCI [^3^] reports 0.198 kg/kg as the measured industry average across 52 plants; the midpoint is adopted here for consistency of treatment across crops, not because it is better evidence. See Section 7.3. |
| Soybean meal | 0.750 | 0.74–0.76 | NOPA LCI [^3^]: 0.750 kg/kg (as-produced basis). The midpoint of 0.74–0.76 is 0.75, which matches the NOPA average. |
| Soybean hulls | 0.055 | 0.05–0.06 | Midpoint of the reported range. NOPA LCI [^3^] reports 0.056 kg/kg as the measured industry average; the midpoint is adopted here for consistency of treatment across crops. |

**As-Is Yield Sum**
The adopted yields sum to 1.000 t/t soybeans (0.195 + 0.750 + 0.055). This is a consequence of rounding each yield to the midpoint of its range and should not be read as a mass balance that closes: NOPA's measured as-produced yields sum to **1.004** [^3^], and the CME crush convention allows about 1 lb/bu (0.017 t/t) of waste [^2^]. Crushing also removes moisture — beans enter at 13% and meal and hulls leave at about 11% — so on a physically consistent basis the as-is output would be roughly 0.95 t/t rather than 1.00. Section 5 reports the dry-matter balance, which is the check that carries information here.

**Oil Yield vs. Oil Content**
NOPA reports incoming soybeans at **19.82% lipid** and a crude oil yield of **0.198 kg/kg** [^3^]. Taken at face value that is 99.9% recovery, which no extraction process achieves, so the two figures are not measuring the same material. Analytical lipid content is determined by solvent (ether) extract on the seed, while crude oil as weighed at the plant also carries phospholipids, gums, free fatty acids and unsaponifiable matter that are removed later during degumming and refining. The crude oil stream is therefore slightly heavier than the seed's triglyceride content, which is also why Section 3.2's note on refining losses reduces the saleable RBD oil to ~0.191–0.193 t/t. Practitioners comparing an oil yield against a seed oil analysis should expect the yield to be the larger of the two, not the smaller.

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
| Soybean hulls | 89.0% | Dried hulls are typically 88–90% DM [^8^]. Whole hulls may be slightly higher in moisture if not fully dried. NOPA's paired as-produced and dry-basis figures imply ~90.8% [^3^]. |

### 3.5 Prices
| Co-product | Price (USD/t) | Range | Source | Notes |
| --- | --- | --- | --- | --- |
| Soybean oil | 1,050 | 900–1,200 | USDA ERS [^5^]; WASDE [^6^]; YCharts [^7^] | Midpoint of the reported range. MY 2024/25 season average. USDA WASDE MY 2024/25 forecast: ~42-43 cents/lb = ~$926-948/t. YCharts MY 2024/25 average: ~$979–1,077/t. |
| Soybean meal (48% protein) | 370 | 340–400 | USDA ERS [^5^]; WASDE [^6^]; UkrAgroConsult [^10^]; Fastmarkets [^11^]; USDA AMS [^13^] | Midpoint of the reported range. Derived from 44% protein meal baseline: $295/short ton = $325/metric ton (WASDE Feb 2026). 48% protein premium: +$35–50/metric ton. |
| Soybean hulls (whole) | 140 | 110–170 | USDA AMS; Business Research Insights [^9^] | Midpoint of the reported range. USDA AMS FOB Midwest Q1 2025: whole hulls $105–130/short ton = $115–143/metric ton. |

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
| **Total** | | **0.91145** |

*Note on the dry matter total:* The DM output sum (0.91145 t) exceeds the 13%-basis DM input (0.870 t) by 4.76%. Section 5.3 sets out where that comes from. It does not affect the allocation factors below, which are ratios among the co-products: dividing each co-product's DM by the co-product total gives the same percentages as any proportional rescaling of all three. Rescaling the three DM outputs so that they sum to the DM input would leave every allocation percentage exactly as it stands, so no such rescaling is applied here; the excess is reported instead.

**Step 3: Economic Allocation**
`Economic allocation (%) = (Co-product revenue ÷ Total revenue) × 100`

| Co-product | Calculation | Allocation |
| --- | --- | --- |
| Soybean oil | (204.75 ÷ 489.95) × 100 | 41.8% |
| Soybean meal | (277.50 ÷ 489.95) × 100 | 56.6% |
| Soybean hulls | (7.70 ÷ 489.95) × 100 | 1.6% |

*Rounding note:* Raw calculations yield 41.79% (oil), 56.64% (meal), and 1.57% (hulls). Rounded: 41.8%, 56.6%, 1.6% (sum = 100.0%).

**Step 4: Mass Allocation**
`Mass allocation (%) = (Co-product DM output ÷ Total co-product DM output) × 100`

| Co-product | Calculation | Allocation |
| --- | --- | --- |
| Soybean oil | (0.1950 ÷ 0.91145) × 100 | 21.4% |
| Soybean meal | (0.6675 ÷ 0.91145) × 100 | 73.2% |
| Soybean hulls | (0.04895 ÷ 0.91145) × 100 | 5.4% |

*Rounding note:* Raw calculations yield 21.39% (oil), 73.23% (meal), and 5.37% (hulls). Rounded: 21.4%, 73.2%, 5.4% (sum = 100.0%).

## 4. Allocation Methodology

### 4.1 Economic Allocation
Economic allocation distributes environmental burdens (or revenues) among co-products based on their relative market value.
**Formula:**
`Economic allocation (%) = (Revenue of co-product i ÷ Total revenue of all co-products) × 100`

### 4.2 Mass Allocation
Mass allocation distributes burdens based on the dry matter content of each co-product.
**Formula:**
`Mass allocation (%) = (DM output of co-product i ÷ Total DM output of all co-products) × 100`

### 4.3 Summary of Allocations
| Co-product | Economic | Mass |
| --- | --- | --- |
| Soybean oil | 41.8% | 21.4% |
| Soybean meal | 56.6% | 73.2% |
| Soybean hulls | 1.6% | 5.4% |
| **Total** | **100.0%** | **100.0%** |

> **Note on energy allocation:** Gross-energy allocation is reported for this crop system in the companion *Gross Energy Reference* document, which is the single source for GE values and their uncertainty ranges, and in the Monte Carlo script `monte_carlo_uncertainty_v11.py`. GE data are deliberately not duplicated here.

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
| Total DM output | 0.91145 t | 104.76% of input DM |

### 5.2 Reconciliation Using Delivered Moisture Basis
| Check | Value | Status |
| --- | --- | --- |
| Input: Soybeans at 10.75% moisture | 1.000 t | — |
| Input DM (delivered basis) | 0.893 t | — |
| Total DM output (from yields) | 0.91145 t | 102.1% of input DM |
| Residual excess | ~0.0185 t | ~2.1% |

### 5.3 Where the Dry Matter Excess Comes From

The DM output (0.91145 t) exceeds the 13%-basis DM input (0.870 t) by 4.76%. Dry matter is not created in crushing, so this is an accounting result. It has three separable causes, and NOPA's own data identifies the largest of them.

| Component | Contribution | Explanation |
| --- | --- | --- |
| Trading basis vs delivered moisture | ~2.6 pp | Yields are applied to 1 t of beans at the 13% trading basis (0.870 t DM), but the beans the yields were measured on averaged 10.75% moisture (0.893 t DM) [^3^] |
| Inherent in the source survey | ~1.7 pp | See below |
| Dry matter contents adopted here | ~0.4 pp | This document uses 89% DM for both meal and hulls; NOPA's paired as-produced and dry-basis figures imply about 87.8% for meal and 90.8% for hulls |

**The survey does not close either, and says why.** NOPA reports each yield twice — as produced and on a dry weight basis. The dry-basis figures are 0.222 (oil), 0.738 (meal) and 0.057 (hulls) kg per kg of soybean dry matter [^3^], which sum to **1.017**. The survey therefore shows 1.7% more dry matter leaving than entering, and NOPA notes the reason directly: *"Materials added during crushing and refining can be added back to the meal."* Degumming and refining residues, and processing aids, return to the meal stream and are weighed as meal, so a mass balance drawn only across seed in and products out will not close. The same effect explains why NOPA's as-produced yields sum to 1.004 rather than 1.000.

**Effect on the results: none.** All three allocation methods are ratios among the co-products, so a proportional excess spread across the outputs leaves the percentages unchanged. The excess is reported here rather than removed, because it is a real property of the industry data this table is built on and users should be able to see it.

## 6. Complete Data Table
| Parent Crop | Crop System | Stage | USDA Standard | Standard Moisture | Parent Input Basis | Co-product Stream | Yield (t/t) | Yield Range | Price (USD/t) | Price Range | DM (%) | DM Output (t/t) | Revenue (USD/t) | Econ Alloc (%) | Mass Alloc (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Soybean | Soybean crushing | Single | 60 lb/bushel at 13% moisture | 13% | 1 t soybeans at 13% moisture | Soybean oil | 0.195 | 0.19–0.20 | 1,050 | 900–1,200 | 100.0 | 0.1950 | 204.75 | 41.8 | 21.4 |
| Soybean | Soybean crushing | Single | 60 lb/bushel at 13% moisture | 13% | 1 t soybeans at 13% moisture | Soybean meal (48% protein) | 0.750 | 0.74–0.76 | 370 | 340–400 | 89.0 | 0.6675 | 277.50 | 56.6 | 73.2 |
| Soybean | Soybean crushing | Single | 60 lb/bushel at 13% moisture | 13% | 1 t soybeans at 13% moisture | Soybean hulls (whole) | 0.055 | 0.05–0.06 | 140 | 110–170 | 89.0 | 0.04895 | 7.70 | 1.6 | 5.4 |

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
| Oil yield (0.195 t/t) | Medium | Midpoint of the range; NOPA's measured average is 0.198 [^3^] |
| Hull yield (0.055 t/t) | Medium | Midpoint of the range; NOPA's measured average is 0.056 [^3^] |
| Oil price ($1,050/t) | Medium | Midpoint of the range; quoted values cluster nearer ~$1,020 (WASDE ~$926–948/t, YCharts ~$979–1,077/t) |
| Meal price ($370/t) | Medium | Midpoint of the range; derived value from the 44% baseline plus premium is ~$369 |
| 48% protein premium ($35–50/MT) | Medium | Spread between 44% and 48% grades in USDA AMS feedstuff quotations [^13^]; consistent with the $295/short ton 44% baseline and the $340–400/t range adopted for 48% meal |

### 7.3 Known Limitations
- **Midpoint convention:** Adopted values are the midpoints of their reported ranges (0.195, 0.055, $1,050, $370, $140), applied consistently across every crop in this work. Substituting the NOPA measured yields (0.198, 0.056) and the survey-derived prices (~$1,020, ~$369) — all of which fall inside the stated ranges — gives oil at ~41.5% economic and ~21.6% mass, against 41.8% and 21.4% here. The convention therefore costs less than half a percentage point on any factor.
- **Protein content configuration:** This table models 48% protein dehulled meal with hulls reported as a separate co-product, which is the CME board-crush specification [^2^]. A plant producing 44% protein meal blends the hulls back into the meal instead. Modelling that configuration means **merging the hulls line into the meal line**, not separating it: meal yield becomes roughly 0.805 t/t, protein falls to 44%, and the meal price falls to about $325/t (WASDE Feb 2026, converted from $295/short ton). The hulls co-product disappears, and the allocation is then a two-way split between oil and meal.
- **Regional price variation:** Soybean product prices vary significantly by location.
- **Temporal volatility:** The renewable diesel boom has increased price volatility and shifted value between oil and meal; farmdoc daily [^4^] tracks this shift and the accompanying expansion in U.S. crush capacity.
- **Hull form:** Whole hulls ($140/t) vs. pelleted hulls ($175/t) vs. ground hulls ($130/t) have different prices.
- **Waste not allocated:** The CME standard [^2^] includes 1 lb/bu (0.017 t/t) of waste. This is not allocated because it has no market value.
- **Refining losses:** The 0.195 t/t oil yield is crude oil. Further refining incurs ~1–2% loss, which is not captured.
- **Dry matter excess:** The DM output exceeds the 13%-basis DM input by 4.76%. Section 5.3 decomposes this into the trading-versus-delivered moisture basis (~2.6 pp), an excess inherent in the NOPA survey itself (~1.7 pp, arising from refining materials returned to the meal stream), and the DM contents adopted here (~0.4 pp). Because all three allocation methods are ratios among the co-products, the excess does not affect the reported factors.
- **Oil content variance:** The NOPA LCI [^3^] reports 19.82% average oil content, but the Iowa Soybean Association [^12^] reports 21.7% average.