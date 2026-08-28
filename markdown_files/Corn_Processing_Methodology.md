# Corn Processing Co-Product Allocation: Methodology, Data Sources, and Calculation Documentation
**Document Version:** 1.0
**Date:** June 2026
**Basis:** 1 metric ton (t) of field corn at 15.5% moisture (USDA standard)
**Price Period:** 2024–2025 average (unless otherwise noted)

## Table of Contents
- [1. Standard Basis and Conversions](#1-standard-basis-and-conversions)
- [2. Data Sources and References](#2-data-sources-and-references)
- [3. Corn Wet Milling](#3-corn-wet-milling)
- [4. Corn Dry Milling](#4-corn-dry-milling)
- [5. Corn Dry-Grind Ethanol](#5-corn-dry-grind-ethanol)
- [6. Allocation Methodology](#6-allocation-methodology)
- [7. Mass Balance Verification](#7-mass-balance-verification)
- [8. Data Quality and Limitations](#8-data-quality-and-limitations)
- [9. Complete Data Table](#9-complete-data-table)

## 1. Standard Basis and Conversions

### 1.1 Parent Input Definition
| Parameter | Value | Source |
| --- | --- | --- |
| Parent crop | Field corn (No. 2 yellow dent corn) | USDA Grain Standards [^1^] |
| Input quantity | 1 metric ton (1,000 kg) | — |
| Moisture content | 15.5% | USDA standard test weight basis for corn trading [^1^] |
| Dry matter (DM) input | 0.845 t DM/t corn | Calculated: 1.000 × (1 − 0.155) = 0.845 |
| Bushel equivalent | 39.37 bushels/t | 1,000 kg ÷ 25.401 kg/bu (56 lb at 15.5% moisture) [^1^] |
| Bushel weight | 56.0 lb (25.401 kg) | USDA standard reference bushel weight for corn [^1^] |

*Note on moisture standard:* The 15.5% moisture content is the USDA standard for corn test weight determination and trading. The maximum eligible moisture for USDA loan programs is 15.5%. The standard reference bushel weight of 56 lb is defined at this moisture basis. Note: USDA grade standards specify minimum test weights of 56 lb/bu for No. 1 and 54 lb/bu for No. 2 yellow corn; the 56 lb figure used here is the standard bushel definition, not a grade requirement.

### 1.2 Unit Conversions
| Conversion | Factor |
| --- | --- |
| 1 bushel (bu) | 56.0 lb = 25.401 kg |
| 1 lb | 0.453592 kg = 0.000453592 t |
| 1 t corn | 39.37 bushels |
| 1 gallon ethanol (undenatured) | ~6.58 lb (at 0.789 g/mL density) |
| 1 gallon ethanol (denatured) | ~6.55 lb (with 2–5% gasoline denaturant, which is less dense than ethanol) |
| 1 t ethanol (undenatured) | ~334.8 gallons |

### 1.3 Convention for Adopted Values

Every yield, price, and DM% in this document is reported as an adopted point value together with the range it was drawn from. **Unless a row states otherwise, the adopted value is the midpoint of its stated range**, and the range is the parameter that carries the evidence. Point values are given to the precision that the underlying sources support — generally two or three significant figures — and are not intended to imply plant-level accuracy. Derived quantities (DM outputs, revenues, allocation percentages) are carried at four decimals internally and reported to one decimal place.

*Note on ethanol density:* Pure ethanol has a density of 0.789 g/mL at 20°C, giving 6.58 lb per US gallon (3.7854 L × 0.789 kg/L = 2.987 kg = 6.586 lb). One metric ton of pure ethanol therefore equals approximately 334.8 gallons (1,000 kg ÷ 2.987 kg/gal = 334.8 gal). The document uses 6.58 lb/gal for undenatured ethanol; denatured ethanol is slightly lighter (~6.55 lb/gal) because the gasoline denaturant (~6.15 lb/gal) is less dense than pure ethanol.

## 2. Data Sources and References

### 2.1 Primary Sources
| Citation | Full Title | Type | URL |
| --- | --- | --- | --- |
| [^1^] | USDA Agricultural Marketing Service (AMS). *Grain Standards — Corn* (formerly GIPSA) | Government | https://www.ams.usda.gov/grades-standards/corn-standards |
| [^2^] | Galitsky, C., Worrell, E., & Ruth, M. (2003). *Energy Efficiency Improvement and Cost Saving Opportunities for the Corn Wet Milling Industry.* LBNL-52307. | Government (DOE/LBNL) | https://eta-publications.lbl.gov/sites/default/files/lbnl-52307.pdf |
| [^3^] | USDA AMS (2025). *Corn Gluten Meal & Corn Gluten Feed Prices* (SJ_GR225) | Government (USDA) | https://www.ams.usda.gov/mnreports/sj_gr225.txt |
| [^4^] | USDA AMS (2025). *Corn Co-Products Report* (SJ_GR310) | Government (USDA) | https://www.ams.usda.gov/mnreports/sj_gr310.txt |
| [^5^] | farmdoc daily, University of Illinois (2024–2025). Ethanol yield and price data | University/Extension | https://farmdocdaily.illinois.edu/ |
| [^6^] | CARD, Iowa State University (2024). *Cedar Rapids Food and Bioprocessor Manufacturing Report* (24-SR-124) | University/Extension | https://www.card.iastate.edu/publications/24-sr-124 |
| [^7^] | USDA ERS. *Feed Grains Database: Yearbook Tables* | Government (USDA) | https://www.ers.usda.gov/data-products/feed-grains-database.aspx |
| [^8^] | Purdue Extension (2024). *Estimating a Per Acre Carbon Intensity (CI) Score* | University/Extension | https://extension.purdue.edu/ |
| [^9^] | Corn Refiners Association (CRA). *Corn Annual Report* | Industry | https://corn.org/ |
| [^10^] | Renewable Fuels Association (2024). *Ethanol Industry Outlook* | Industry | https://ethanolrfa.org/ |
| [^11^] | DTN/Progressive Farmer (2026). DDGS price reports | Industry | https://www.dtnpf.com/ |

### 2.2 How Sources Were Used
- **Yield data (wet milling):** Converted from lb/bu values in the LBNL/DOE Energy Guide [^2^] to t/t corn using the standard bushel weight (56 lb at 15.5% moisture).
- **Yield data (dry milling):** Converted from kg/metric ton values in the ISU CARD report [^6^] to t/t corn.
- **Yield data (ethanol):** Converted from gal/bu and lb/bu values in farmdoc daily [^5^] to t/t corn.
- **Corn oil yield (dry-grind):** Based on farmdoc daily [^5^] corn oil conversion rates, which rise across the period from roughly 0.5 lb/bu in the mid-2010s to 0.95 lb/bu assumed for 2025.
- **Price data (CGM, CGF):** USDA AMS weekly price reports [^3^][^4^].
- **Price data (ethanol):** farmdoc daily market summaries [^5^] (2024–2025 average).
- **Price data (DDGS):** USDA [^7^], farmdoc daily [^5^], Purdue Extension [^8^] long-term averages, and DTN/Progressive Farmer [^11^] market reports.
- **Price data (CSL):** CRA [^9^] industry data and trade reports.
- **Price data (corn oil):** Industry data for crude distillers corn oil (DCO) from ethanol plants [^10^].

## 3. Corn Wet Milling

### 3.1 Process Description
Corn wet milling separates corn into its four main components (starch, gluten, germ, and fiber) using water and mechanical separation. Water is added during steeping and part of it is retained in the co-products (about 0.16 t/t corn in the configuration modelled here), so the as-is output mass exceeds the input mass. Steep liquor is the concentrated liquid remaining after steeping, containing solubilized proteins, minerals, and organic acids.

> **Note on steep liquor and corn gluten feed — important for reading the mass balance:** In most U.S. wet mills the concentrated steep liquor is added back to the fiber stream and dried into corn gluten feed. The corn gluten feed yield reported by industry sources, including LBNL/DOE [^2^] ("corn steep liquor is added to the moist fiber and the mixture is dried to yield corn gluten feed"), therefore already contains the steep solids. This document nevertheless reports corn steep liquor as a separate stream, because it is separately traded and separately fed — condensed steep liquor is used as a liquid protein supplement in dairy rations, and a mill that sells it does not put it into its gluten feed. The consequence is that the two streams overlap: the steep solids are counted once inside the corn gluten feed yield and again as corn steep liquor. Section 3.6 quantifies this and Section 8.3 gives the alternative factors for a strictly closed balance.

### 3.2 Co-Product Yields
| Co-product | Yield (t/t corn) | Range | Source & Calculation |
| --- | --- | --- | --- |
| Corn starch | 0.56 | 0.54–0.58 | LBNL/DOE [^2^]: 31.5 lb/bu. Conversion: 31.5 lb × 0.000453592 t/lb = 0.01429 t/bu. ÷ 0.025401 t corn/bu = 0.563 t/t → rounded to 0.56. |
| Corn gluten meal | 0.045 | 0.04–0.05 | LBNL/DOE [^2^]: 2.5 lb/bu. Conversion: 2.5 × 0.000453592 ÷ 0.025401 = 0.0446 t/t → rounded to 0.045. |
| Corn gluten feed | 0.22 | 0.20–0.24 | LBNL/DOE [^2^]: 12.5 lb/bu. Conversion: 12.5 × 0.000453592 ÷ 0.025401 = 0.223 t/t → rounded to 0.22. |
| Corn germ | 0.075 | 0.07–0.08 | LBNL/DOE [^2^]: approximately 7.5% of corn weight = 0.075 t/t. Note: Corn germ constitutes approximately 10–12% of kernel weight; the 7.5% figure represents recoverable germ after wet milling losses. |
| Corn steep liquor | 0.26 | 0.22–0.30 | LBNL/DOE [^2^]: 6.5% solids (DM) = 0.065 t DM/t corn. At 25% DM: 0.065 ÷ 0.25 = 0.26 t as-is/t corn. |

**Yield Calculation Formula**

    Yield (t/t corn) = (lb/bu) × (0.000453592 t/lb) ÷ (0.025401 t corn/bu)
                     = (lb/bu) × 0.01786

### 3.3 Dry Matter Contents
| Co-product | DM (%) | Basis |
| --- | --- | --- |
| Corn starch | 99.5% | Commercial food-grade starch is dried to >99% DM [^2^] |
| Corn gluten meal | 90.5% | Standard CGM specification [^2^] |
| Corn gluten feed (dry pellets) | 88.0% | Standard dry pellet specification [^2^][^4^]. Note: Wet feed is 40–60% DM; dry pellets are 88–90% DM. This document uses dry pellets as the standard traded form. |
| Corn germ | 85.0% | Dried germ meal after oil extraction [^2^] |
| Corn steep liquor | 25.0% | Concentrated steep liquor (evaporated from ~5–7% to 20–30% solids) [^2^] |

*Note on CGF DM%: Corn gluten feed is modeled as dry pellets at 88% DM with a corresponding dry pellet price ($160/t), which is the standard traded form. If wet feed is modeled instead, both the DM% and the price must be adjusted accordingly (wet feed: 40–60% DM, $60–80/t).

### 3.4 Prices
| Co-product | Price (USD/t) | Range | Source | Notes |
| --- | --- | --- | --- | --- |
| Corn starch | 400 | 350–450 | Industry estimate [^9^] | Food-grade unmodified starch. No direct USDA price series exists. |
| Corn gluten meal | 550 | 500–600 | USDA AMS [^3^][^4^] | Comprehensive price ~$580–630/t (rail, 2025); bids ~$435–495/t (barge). The adopted $550/t sits between the rail and barge quotations above. |
| Corn gluten feed (dry pellets) | 160 | 140–180 | USDA AMS [^3^][^4^] | Dry pellet 21% protein: AMS reports $134–234/t depending on region and sale type (2024–2025). |
| Corn germ | 250 | 200–300 | Industry estimate [^9^] | Feed-grade germ meal. No direct USDA price series. |
| Corn steep liquor | 150 | 100–200 | CRA [^9^] | Raw/unprocessed steep liquor. Processed CSL for fermentation/industrial use: $400–500/t. |

### 3.5 Revenue and Allocation Calculations

**Step 1: Calculate Revenue per Co-Product**
`Revenue (USD/t parent input) = Yield (t/t) × Price (USD/t)`

| Co-product | Calculation | Revenue |
| --- | --- | --- |
| Corn starch | 0.56 × 400 | $224.00 |
| Corn gluten meal | 0.045 × 550 | $24.75 |
| Corn gluten feed | 0.22 × 160 | $35.20 |
| Corn germ | 0.075 × 250 | $18.75 |
| Corn steep liquor | 0.26 × 150 | $39.00 |
| **Total** | | **$341.70** |

**Step 2: Calculate DM Output per Co-Product**
`DM output (t DM/t parent input) = Yield (t/t) × DM (%)`

| Co-product | Calculation | DM Output |
| --- | --- | --- |
| Corn starch | 0.56 × 0.995 | 0.5572 |
| Corn gluten meal | 0.045 × 0.905 | 0.0407 |
| Corn gluten feed | 0.22 × 0.880 | 0.1936 |
| Corn germ | 0.075 × 0.850 | 0.0638 |
| Corn steep liquor | 0.26 × 0.250 | 0.0650 |
| **Total** | | **0.9203** |

**Step 3: Economic Allocation**
`Economic allocation (%) = (Co-product revenue ÷ Total revenue) × 100`

| Co-product | Calculation | Allocation |
| --- | --- | --- |
| Corn starch | (224.00 ÷ 341.70) × 100 | 65.6% |
| Corn gluten meal | (24.75 ÷ 341.70) × 100 | 7.2% |
| Corn gluten feed | (35.20 ÷ 341.70) × 100 | 10.3% |
| Corn germ | (18.75 ÷ 341.70) × 100 | 5.5% |
| Corn steep liquor | (39.00 ÷ 341.70) × 100 | 11.4% |

*Rounding note:* The raw calculations yield 65.55% (starch), 7.24% (CGM), 10.30% (CGF), 5.49% (germ), and 11.41% (CSL). These are rounded to one decimal place so that the sum is 100.0%.

**Step 4: Mass Allocation**
`Mass allocation (%) = (Co-product DM output ÷ Total DM output) × 100`

| Co-product | Calculation | Allocation |
| --- | --- | --- |
| Corn starch | (0.5572 ÷ 0.9203) × 100 | 60.6% |
| Corn gluten meal | (0.0407 ÷ 0.9203) × 100 | 4.4% |
| Corn gluten feed | (0.1936 ÷ 0.9203) × 100 | 21.0% |
| Corn germ | (0.0638 ÷ 0.9203) × 100 | 6.9% |
| Corn steep liquor | (0.0650 ÷ 0.9203) × 100 | 7.1% |

*Rounding note:* The raw calculations yield 60.55%, 4.43%, 21.04%, 6.93%, and 7.06%. These are rounded so that the sum is 100.0%: starch absorbs the 0.1 pp rounding adjustment to 60.6%.

### 3.6 Mass Balance Check
| Check | Value | Status |
| --- | --- | --- |
| Input DM (15.5% moisture) | 0.845 t/t | — |
| Output DM (sum of co-products) | 0.9203 t/t | 108.9% |
| As-is output sum | 1.160 t/t | — |

The summed DM output (0.9203 t) exceeds the DM input (0.845 t) by 8.9%. Dry matter is not created in wet milling, so this is an accounting overlap, not a physical result, and its cause is the one described in Section 3.1: the corn gluten feed yield taken from LBNL/DOE [^2^] already includes the steep solids that are also reported here as corn steep liquor. The overlap is the full steep liquor DM, 0.0650 t. Excluding it, the DM output is 0.8553 t, or **101.2% of input DM** — ordinary rounding for coefficients converted from lb/bu.

The overlap is disclosed rather than removed because both streams are genuinely marketed and both are fed to dairy cattle, and because the yields and ranges in this table are the ones used throughout this work. Practitioners who require a strictly closed balance should use the alternative factors in Section 8.3.

The as-is output sum (1.160 t/t) exceeds the input mass (1.0 t/t) because of steep water retained in the co-products, chiefly in the steep liquor itself (0.26 t at 25% DM) and in the gluten feed. That part is physically correct.

## 4. Corn Dry Milling

### 4.1 Process Description
Dry milling separates corn into endosperm (grits and meal), germ, and bran/hominy feed using tempering, degermination, and sifting. Unlike wet milling, no water is added in significant quantities, so output mass is close to input mass (accounting for process losses).

### 4.2 Co-Product Yields
| Co-product | Yield (t/t corn) | Range | Source & Calculation |
| --- | --- | --- | --- |
| Corn meal & grits | 0.56 | 0.54–0.58 | ISU CARD [^6^]: Flaking grits (120 kg/mt) + Brewer's grits (380 kg/mt) + Cornmeal (60 kg/mt) = 560 kg/mt = 0.56 t/t. |
| Hominy feed | 0.35 | 0.32–0.38 | ISU CARD [^6^]: 20 lb/bu. Conversion: 20 × 0.000453592 ÷ 0.025401 = 0.357 t/t → rounded to 0.35. |
| Corn germ | 0.075 | 0.07–0.08 | Carried over from the wet-milling basis, LBNL/DOE [^2^]: approximately 7.5% of corn weight = 0.075 t/t. Dry-mill degermination is expected to recover less than this; see Section 4.6 and Section 8.3. |

### 4.3 Dry Matter Contents
| Co-product | DM (%) | Basis |
| --- | --- | --- |
| Corn meal & grits | 89.0% | Degermed corn products [^6^] |
| Hominy feed | 87.0% | Standard dried hominy feed [^6^] |
| Corn germ | 85.0% | Dried germ meal [^2^] |

### 4.4 Prices
| Co-product | Price (USD/t) | Range | Source | Notes |
| --- | --- | --- | --- | --- |
| Corn meal & grits | 230 | 200–260 | USDA ERS [^7^] | Inflation-adjusted from 2016 data to ~$230/t (2024–2025). |
| Hominy feed | 165 | 160–170 | USDA AMS [^4^] | Corn Belt Weekly Feb 2025: $160–165/t (Central IL). |
| Corn germ | 250 | 200–300 | Industry estimate [^9^] | Feed-grade germ meal. No direct USDA price series. |

### 4.5 Revenue and Allocation Calculations

**Revenue**
| Co-product | Calculation | Revenue |
| --- | --- | --- |
| Corn meal & grits | 0.56 × 230 | $128.80 |
| Hominy feed | 0.35 × 165 | $57.75 |
| Corn germ | 0.075 × 250 | $18.75 |
| **Total** | | **$205.30** |

**DM Output**
| Co-product | Calculation | DM Output |
| --- | --- | --- |
| Corn meal & grits | 0.56 × 0.89 | 0.4984 |
| Hominy feed | 0.35 × 0.87 | 0.3045 |
| Corn germ | 0.075 × 0.85 | 0.0638 |
| **Total** | | **0.8667** |

**Economic Allocation**
| Co-product | Calculation | Allocation |
| --- | --- | --- |
| Corn meal & grits | (128.80 ÷ 205.30) × 100 | 62.8% |
| Hominy feed | (57.75 ÷ 205.30) × 100 | 28.1% |
| Corn germ | (18.75 ÷ 205.30) × 100 | 9.1% |

*Rounding note:* The raw calculations yield 62.74%, 28.13%, and 9.13%, which sum to 99.9% when each is rounded independently. Corn meal & grits absorbs the 0.1 pp adjustment to 62.8% so that the reported values sum to 100.0%.

**Mass Allocation**
| Co-product | Calculation | Allocation |
| --- | --- | --- |
| Corn meal & grits | (0.4984 ÷ 0.8667) × 100 | 57.5% |
| Hominy feed | (0.3045 ÷ 0.8667) × 100 | 35.1% |
| Corn germ | (0.0638 ÷ 0.8667) × 100 | 7.4% |

### 4.6 Mass Balance Check
| Check | Value | Status |
| --- | --- | --- |
| Input DM | 0.845 t/t | — |
| Output DM | 0.8667 t/t | 102.6% |
| As-is output sum | 0.985 t/t | 98.5% |

The summed DM output (0.8667 t) exceeds the DM input (0.845 t) by 2.6%. As in wet milling this is an accounting artefact rather than a physical result. The main contributor is the germ yield: 0.075 t/t is carried over from the wet-milling basis [^2^] rather than taken from the dry-milling source [^6^], and dry-mill degermination recovers less germ than wet milling does. Substituting a dry-mill germ yield of about 0.05 t/t would bring the DM output to roughly 0.845 t and close the balance. The remainder is rounding in coefficients converted from different source units (kg/mt vs. lb/bu). The as-is output is 98.5% of input, reflecting approximately 1.5% process loss (moisture, fines, handling).

## 5. Corn Dry-Grind Ethanol

### 5.1 Process Description
Dry-grind ethanol production grinds whole corn, converts starch to sugars via enzymatic hydrolysis, ferments sugars to ethanol, and distills the ethanol. The remaining solids (distillers grains) are dried to produce DDGS. Modern plants also extract corn oil from the distillers grains stream using centrifuges.

### 5.2 Co-Product Yields
| Co-product | Yield (t/t corn) | Range | Source & Calculation |
| --- | --- | --- | --- |
| Fuel ethanol | 0.31 | 0.30–0.32 | Adopted as 17.4 lb/bu (~2.64 gal/bu) of pure ethanol. Conversion: 17.4 lb/bu × 0.000453592 t/lb ÷ 0.025401 t corn/bu = 0.310 t/t → **0.31 t/t pure ethanol**. This is a deliberately conservative, long-term value and is below current best practice: farmdoc daily [^5^] assumes 2.95 gal/bu of denatured ethanol for 2023–2025, plus 0.10 gal/bu of cellulosic ethanol in 2025. On a pure-ethanol basis farmdoc's rate is roughly 2.9 gal/bu ≈ 0.34 t/t. The lower value used here reflects plant-level variation and older plant vintages; see the note below for the effect of the choice. |
| Distillers dried grains (DDGS) | 0.27 | 0.24–0.30 | farmdoc daily [^5^]: 15.25 lb/bu (2024–25 average). Conversion: 15.25 × 0.000453592 ÷ 0.025401 = 0.272 t/t → rounded to 0.27. |
| Corn oil (distillers) | 0.013 | 0.008–0.018 | farmdoc daily [^5^]: extraction rates have risen over the period, from roughly 0.5 lb/bu in the mid-2010s to an assumed 0.95 lb/bu for 2025. Conversion: 0.5 lb/bu ÷ 56 lb/bu = 0.0089 t/t; 1.0 lb/bu = 0.0179 t/t. The adopted 0.013 t/t (~0.73 lb/bu) sits between the older and current rates and represents a mid-vintage plant over 2024–2025. |

*Note on ethanol yield:* The value 0.31 t/t represents pure (undenatured) ethanol. Denatured ethanol (with 2–5% gasoline denaturant) weighs slightly less per gallon but contains non-corn mass. For LCA and allocation purposes, pure ethanol is the correct basis. Reported industry conversion rates are normally quoted for denatured ethanol and must be converted before comparison.

*Effect of the ethanol yield choice:* Because the yield adopted here is conservative, it is worth stating what a current-practice yield would do. At 0.34 t/t instead of 0.31 t/t, with all other parameters unchanged, the economic allocation moves from 75.4 / 19.7 / 4.9 to approximately 77.1 / 18.3 / 4.6 (ethanol / DDGS / corn oil) and the mass allocation from 55.3 / 42.4 / 2.3 to approximately 57.6 / 40.2 / 2.2. The direction is intuitive — a higher ethanol yield shifts burden toward ethanol — and the magnitude, under 2.5 percentage points, is small relative to the spread introduced by the price and yield ranges themselves. The conservative value is retained for consistency across this work.

### 5.3 Dry Matter Contents
| Co-product | DM (%) | Basis |
| --- | --- | --- |
| Fuel ethanol | 100.0% | Ethanol is effectively 100% DM |
| Distillers grains (total) | 88.0% | Standard DDGS specification [^5^] |
| Corn oil (distillers) | 100.0% | Crude distillers corn oil is 100% DM |

### 5.4 Prices
| Co-product | Price (USD/t) | Range | Source | Notes |
| --- | --- | --- | --- | --- |
| Fuel ethanol | 535 | 500–570 | farmdoc daily [^5^] | 2024–2025 average: $1.50–1.70/gal. At 334.8 gal/t = $502–$569/t. |
| Distillers grains (total) | 160 | 140–180 | USDA [^7^], farmdoc [^5^], Purdue [^8^], DTN [^11^] | 2024 spot: ~$146/t (USDA AMS). Long-term average $173/t (Purdue, 2007–2024). farmdoc reports 2025 trading in a narrow $125–150/t band, below the adopted range; the adopted $160/t is weighted toward the long-term average rather than the 2025 spot market. |
| Corn oil (distillers, crude) | 830 | 660–1,000 | Industry data [^10^] | Crude distillers corn oil (DCO) from ethanol plants. This is NOT refined food-grade corn oil, which trades at $1,100–1,540/t. |

*Note on corn oil price:* For dry-grind ethanol co-product allocation, the relevant product is crude distillers corn oil (DCO), which trades at $660–1,000/t — substantially below refined food-grade corn oil.

### 5.5 Revenue and Allocation Calculations

**Revenue**
| Co-product | Calculation | Revenue |
| --- | --- | --- |
| Fuel ethanol | 0.31 × 535 | $165.85 |
| Distillers grains (total) | 0.27 × 160 | $43.20 |
| Corn oil | 0.013 × 830 | $10.79 |
| **Total** | | **$219.84** |

**DM Output**
| Co-product | Calculation | DM Output |
| --- | --- | --- |
| Fuel ethanol | 0.31 × 1.00 | 0.3100 |
| Distillers grains (total) | 0.27 × 0.88 | 0.2376 |
| Corn oil | 0.013 × 1.00 | 0.0130 |
| **Total** | | **0.5606** |

**Economic Allocation**
| Co-product | Calculation | Allocation |
| --- | --- | --- |
| Fuel ethanol | (165.85 ÷ 219.84) × 100 | 75.4% |
| Distillers grains (total) | (43.20 ÷ 219.84) × 100 | 19.7% |
| Corn oil | (10.79 ÷ 219.84) × 100 | 4.9% |

**Mass Allocation**
| Co-product | Calculation | Allocation |
| --- | --- | --- |
| Fuel ethanol | (0.3100 ÷ 0.5606) × 100 | 55.3% |
| Distillers grains (total) | (0.2376 ÷ 0.5606) × 100 | 42.4% |
| Corn oil | (0.0130 ÷ 0.5606) × 100 | 2.3% |

### 5.6 Mass Balance Check
| Check | Value | Status |
| --- | --- | --- |
| Input DM | 0.845 t/t | — |
| Output DM | 0.5606 t/t | 66.3% |
| As-is output sum | 0.593 t/t | — |
| Missing mass | ~0.407 t/t | CO₂ gas (~0.30 t/t), water losses, process losses |

The as-is output sum (0.593 t/t) is only ~59% of input mass. The remaining ~41% is primarily CO₂ released during fermentation and water. Using stoichiometry (C₆H₁₂O₆ → 2C₂H₅OH + 2CO₂), the CO₂ produced is approximately 0.297 t CO₂ per t corn (0.31 t ethanol × 88/92 = 0.297 t CO₂). The remaining ~0.11 t/t is water vapor and other process losses. The calculated CO₂ mass slightly exceeds the "missing" corn DM because of fermentation stoichiometry: the oxygen and hydrogen from the **added process water** (which is not counted as input corn DM) become chemically bound into the ethanol and CO₂ molecules (which *are* counted as output DM). Therefore, the output DM of fermentation products naturally exceeds the mass of the consumed corn starch DM. CO₂ is typically vented and excluded from allocation unless captured and sold as a co-product.

## 6. Allocation Methodology

### 6.1 Economic Allocation
Economic allocation distributes environmental burdens (or revenues) among co-products based on their relative market value. Under the ISO 14044 hierarchy it sits at the third tier: allocation should first be avoided by subdivision or system expansion; where it cannot be avoided, inputs and outputs should be partitioned on a physical relationship; and where no physical relationship can be established, they may be partitioned on another relationship such as economic value. This document reports economic and mass allocation side by side and ranks neither.

**Formula:**

    Economic allocation (%) = (Revenue of co-product i ÷ Total revenue of all co-products) × 100
    
    where:
      Revenue of co-product i = Yield_i (t/t) × Price_i (USD/t)

### 6.2 Mass Allocation
Mass allocation distributes burdens based on the dry matter content of each co-product. It is one of the physical relationships contemplated at the second tier of the ISO 14044 hierarchy, and it is the physical basis most often used for feed co-products, where dry matter is the unit in which rations are formulated.

*Note on regulatory frameworks:* Mass allocation should not be confused with the allocation rule in the EU Renewable Energy Directive. RED II (Annex V, Part C) requires emissions to be divided between a fuel and its co-products **in proportion to their energy content, using the lower heating value on a wet basis** — that is, energy allocation, not mass allocation. Energy allocation is reported separately in this work, in the companion *Gross Energy Reference* document; note that it is computed on gross energy (higher heating value, dry basis), so it answers the same question as RED II's rule but is not numerically identical to it.

**Formula:**

    Mass allocation (%) = (DM output of co-product i ÷ Total DM output of all co-products) × 100
    
    where:
      DM output of co-product i = Yield_i (t/t) × DM_i (%)

### 6.3 Why Both Methods Are Reported
| Method | Use Case | Standard |
| --- | --- | --- |
| Economic allocation | LCA studies, corporate sustainability reporting | ISO 14044 (third tier), GHG Protocol Product Standard |
| Mass allocation | Feed and ration accounting; studies preferring a physical basis | ISO 14044 (second tier, physical basis) |

*Note:* ISO 14044 does not mandate either method. The hierarchy is: (1) avoid allocation by subdivision or system expansion, (2) partition on a physical relationship, (3) partition on another relationship such as economic value. Both methods are reported here so that users can apply whichever their study objective or reporting framework requires, and can see how much the choice matters. Users working to the EU Renewable Energy Directive need energy allocation rather than either of these; see Section 6.2 and the companion *Gross Energy Reference* document.

### 6.4 Comparison: Economic vs. Mass Allocation
| System | Primary Product | Primary Alloc (Econ) | Primary Alloc (Mass) | Gap |
| --- | --- | --- | --- | --- |
| Corn wet milling | Corn starch | 65.6% | 60.6% | 5.0 pp |
| Corn dry milling | Corn meal & grits | 62.8% | 57.5% | 5.3 pp |
| Corn dry-grind ethanol | Fuel ethanol | 75.4% | 55.3% | 20.1 pp |

The dry-grind ethanol system shows the largest gap between economic and mass allocation, reflecting the high value of ethanol relative to its DM share. Wet and dry milling show smaller gaps because their primary products (starch and meal) have values closer to the co-products on a per-kg-DM basis.

## 7. Mass Balance Verification

### 7.1 Summary Across All Systems
| System | Input DM (t/t) | Output DM (t/t) | Balance | As-is Output (t/t) | Notes |
| --- | --- | --- | --- | --- | --- |
| Wet milling | 0.845 | 0.9203 | 108.9% | 1.160 | Steep solids counted both in corn gluten feed and as corn steep liquor; 101.2% excluding the overlap |
| Dry milling | 0.845 | 0.8667 | 102.6% | 0.985 | ~1.5% process loss; 2.6% DM overage, mainly the germ yield carried over from the wet-milling basis |
| Dry-grind ethanol | 0.845 | 0.5606 | 66.3% | 0.593 | CO₂ (~0.30 t/t) and water losses not allocated |

### 7.2 Input-Output Reconciliation

**Wet Milling:**
- **Input:** 1.0 t corn at 15.5% moisture = 0.845 t DM
- **Output DM:** 0.9203 t (108.9% of input)
The 8.9% DM overage is an accounting overlap: the corn gluten feed yield reported by LBNL/DOE [^2^] already contains the steep solids that this table also reports separately as corn steep liquor (see Sections 3.1 and 3.6). Excluding the 0.0650 t of overlapping steep DM gives 0.8553 t, or 101.2% of input. Dissolving corn solids into steep water does not create dry matter, and no external dry matter of any consequence is added — sulphur dioxide used in steeping amounts to roughly 1–2 kg per tonne of corn, against a 75 kg gap.
- **As-is mass** (1.160 t) exceeds input (1.0 t) because ~0.16 t of added steep water is retained in the co-products (primarily in CSL and wet CGF).

**Dry Milling:**
- **Input:** 0.845 t DM
- **Output DM:** 0.8667 t (102.6% of input)
The 2.6% overage arises mainly from the germ yield, which is carried over from the wet-milling basis [^2^]; a dry-mill-specific value near 0.05 t/t would close the balance. The remainder is rounding in coefficients derived from different source units (kg/mt vs. lb/bu).
- **As-is mass** is 0.985 t (98.5% of input), reflecting ~1.5% process loss.

**Dry-Grind Ethanol:**
- **Input:** 0.845 t DM
- **Output DM:** 0.5606 t (66.3% of input)
- **Missing DM:** 0.2844 t is converted to CO₂ gas (~0.297 t CO₂/t corn from stoichiometry) and lost as water vapor. The CO₂ mass slightly exceeds the missing corn DM because oxygen and hydrogen from added process water (not counted as input DM) are incorporated into the ethanol and CO₂ molecules (counted as output DM). This is biochemically correct for ethanol fermentation.

## 8. Data Quality and Limitations

### 8.1 High-Confidence Data (Government/Peer-Reviewed Sources)
| Data Point | Confidence | Source |
| --- | --- | --- |
| Wet milling yields (starch, gluten, germ, steep liquor) | High | LBNL/DOE Energy Guide [^2^] |
| Dry milling yields (grits, meal, hominy) | High | ISU CARD report [^6^] |
| Ethanol yields (gal/bu, lb DDGS/bu) | High | farmdoc daily [^5^] |
| CGM prices | High | USDA AMS weekly reports [^3^][^4^] |
| Ethanol prices | High | farmdoc daily [^5^] |
| DDGS prices (long-term average) | High | Purdue [^8^]; USDA [^7^] |
| Corn oil conversion rate | High | farmdoc daily [^5^] (~0.5–1.0 lb/bu, 2014–2025) |

### 8.2 Medium-Confidence Data (Industry Estimates)
| Data Point | Confidence | Source |
| --- | --- | --- |
| Corn starch price ($400/t) | Medium | Industry estimate [^9^]; no USDA price series |
| Corn germ/germ meal price ($250/t) | Medium | Industry estimate [^9^]; no USDA price series |
| Corn steep liquor price ($150/t) | Medium | CRA [^9^]; highly variable by region and product form |
| CGF dry pellet price ($160/t) | Medium | USDA AMS [^3^][^4^]; wide regional variation ($134–234/t) |
| Crude distillers corn oil price ($830/t) | Medium | Industry data [^10^]; varies with vegetable oil markets |

### 8.3 Known Limitations
- **Steep liquor overlap in wet milling (affects the wet-milling factors):** The corn gluten feed yield used here is an industry average in which the steep solids have been dried back into the gluten feed, while this table also reports corn steep liquor as a separate marketed stream. The two therefore overlap by 0.0650 t DM/t corn, which is why the wet-milling DM output sums to 108.9% of input rather than ~100%. Both streams are retained because both are separately traded and separately fed. A user who requires a closed balance should drop corn steep liquor and use the following wet-milling factors, which are computed on the same prices and DM contents: corn starch 74.0% economic / 65.1% mass; corn gluten meal 8.2% / 4.8%; corn gluten feed 11.6% / 22.6%; corn germ 6.2% / 7.5% (total revenue $302.70/t, total DM output 0.8553 t/t = 101.2% of input DM).
- **Germ yield in dry milling:** The 0.075 t/t germ yield in Section 4 is carried over from the wet-milling basis [^2^] because the dry-milling source [^6^] does not report germ separately. Dry-mill degermination recovers less, and this is the main reason the dry-milling DM output sums to 102.6% of input. A dry-mill-specific value near 0.05 t/t would close the balance; the higher value is retained for consistency with the rest of this work, and its effect on the dry-milling factors is under 2 percentage points.
- **Ethanol yield is conservative:** The adopted 0.31 t/t (~2.64 gal/bu pure ethanol) is below current industry practice; farmdoc daily [^5^] assumes 2.95 gal/bu denatured for 2023–2025. Section 5.2 gives the effect of using a current-practice yield instead, which is under 2.5 percentage points on any allocation factor.
- **Regional variation:** Prices vary significantly by location (Corn Belt vs. coastal markets). CGF pellet prices vary from $134/t to $234/t depending on region.
- **Temporal variation:** Prices are volatile. The 2024–2025 average may not represent future markets. Ethanol prices ranged from $1.40 to $2.00/gal over the past several years.
- **Product form consistency:** Corn gluten feed can be wet (40–60% DM) or dry pellets (88–90% DM). This document uses dry pellets at 88% DM with a corresponding dry pellet price. If wet feed is used, both the DM% and price must be adjusted together.
- **Corn oil yield variability:** Corn oil extraction rates vary significantly by plant technology and vintage. Older plants may extract only 0.3–0.5 lb/bu, while current plants reach ~0.95–1.0 lb/bu. The adopted 0.013 t/t (~0.73 lb/bu) represents a mid-vintage plant over 2024–2025 and is below the rate assumed for 2025 by farmdoc daily [^5^].
- **Starch yield interpretation:** The 31.5 lb/bu starch yield from LBNL/DOE [^2^] represents recoverable starch after wet milling losses, not the total starch content of the corn kernel (which is ~60–65% or ~33–36 lb/bu). The difference is accounted for in the gluten meal, gluten feed, and steep liquor fractions.
- **Germ yield interpretation:** The 7.5% germ yield represents recoverable germ after wet milling, not the total germ content of the corn kernel (which is ~10–12%). The difference is accounted for in other co-product fractions.
- **CO₂ from ethanol fermentation:** CO₂ is typically vented and excluded from allocation. If a plant captures and sells CO₂ as a co-product (for beverage carbonation, dry ice, or enhanced oil recovery), it should be included as an additional co-product with its own yield, price, and DM content.
- **Denaturant in fuel ethanol:** The denaturant (2–5% gasoline) adds mass and value to denatured ethanol but is not a corn-derived product. For LCA purposes, pure (undenatured) ethanol is the correct basis, as the denaturant should be allocated to the petroleum system.

## 9. Complete Data Table
| Parent Crop | Crop System | Stage | USDA Standard | Standard Moisture | Parent Input Basis | Co-product Stream | Yield (t/t) | Yield Range | Price (USD/t) | Price Range | DM (%) | DM Output (t/t) | Revenue (USD/t) | Econ Alloc (%) | Mass Alloc (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Field Corn | Corn wet milling | Single | 56 lb/bu at 15.5% moisture | 15.5% | 1 t corn at 15.5% moisture | Corn starch | 0.56 | 0.54–0.58 | 400 | 350–450 | 99.5 | 0.5572 | 224.00 | 65.6 | 60.6 |
| Field Corn | Corn wet milling | Single | 56 lb/bu at 15.5% moisture | 15.5% | 1 t corn at 15.5% moisture | Corn gluten meal | 0.045 | 0.04–0.05 | 550 | 500–600 | 90.5 | 0.0407 | 24.75 | 7.2 | 4.4 |
| Field Corn | Corn wet milling | Single | 56 lb/bu at 15.5% moisture | 15.5% | 1 t corn at 15.5% moisture | Corn gluten feed | 0.22 | 0.20–0.24 | 160 | 140–180 | 88.0 | 0.1936 | 35.20 | 10.3 | 21.0 |
| Field Corn | Corn wet milling | Single | 56 lb/bu at 15.5% moisture | 15.5% | 1 t corn at 15.5% moisture | Corn germ | 0.075 | 0.07–0.08 | 250 | 200–300 | 85.0 | 0.0638 | 18.75 | 5.5 | 6.9 |
| Field Corn | Corn wet milling | Single | 56 lb/bu at 15.5% moisture | 15.5% | 1 t corn at 15.5% moisture | Corn steep liquor | 0.26 | 0.22–0.30 | 150 | 100–200 | 25.0 | 0.0650 | 39.00 | 11.4 | 7.1 |
| Field Corn | Corn dry milling | Single | 56 lb/bu at 15.5% moisture | 15.5% | 1 t corn at 15.5% moisture | Corn meal & grits | 0.56 | 0.54–0.58 | 230 | 200–260 | 89.0 | 0.4984 | 128.80 | 62.8 | 57.5 |
| Field Corn | Corn dry milling | Single | 56 lb/bu at 15.5% moisture | 15.5% | 1 t corn at 15.5% moisture | Hominy feed | 0.35 | 0.32–0.38 | 165 | 160–170 | 87.0 | 0.3045 | 57.75 | 28.1 | 35.1 |
| Field Corn | Corn dry milling | Single | 56 lb/bu at 15.5% moisture | 15.5% | 1 t corn at 15.5% moisture | Corn germ | 0.075 | 0.07–0.08 | 250 | 200–300 | 85.0 | 0.0638 | 18.75 | 9.1 | 7.4 |
| Field Corn | Corn dry-grind ethanol | Single | 56 lb/bu at 15.5% moisture | 15.5% | 1 t corn at 15.5% moisture | Fuel ethanol | 0.31 | 0.30–0.32 | 535 | 500–570 | 100.0 | 0.3100 | 165.85 | 75.4 | 55.3 |
| Field Corn | Corn dry-grind ethanol | Single | 56 lb/bu at 15.5% moisture | 15.5% | 1 t corn at 15.5% moisture | Distillers grains (total) | 0.27 | 0.24–0.30 | 160 | 140–180 | 88.0 | 0.2376 | 43.20 | 19.7 | 42.4 |
| Field Corn | Corn dry-grind ethanol | Single | 56 lb/bu at 15.5% moisture | 15.5% | 1 t corn at 15.5% moisture | Corn oil | 0.013 | 0.008–0.018 | 830 | 660–1,000 | 100.0 | 0.0130 | 10.79 | 4.9 | 2.3 |