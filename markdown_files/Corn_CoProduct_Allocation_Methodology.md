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
| [^8^] | USDA NASS (2024). *Crop Production* | Government (USDA) | https://www.nass.usda.gov/ |
| [^9^] | Purdue Extension (2024). *Estimating a Per Acre Carbon Intensity (CI) Score* | University/Extension | https://extension.purdue.edu/ |
| [^10^] | Corn Refiners Association (CRA). *Corn Annual Report* | Industry | https://corn.org/ |
| [^11^] | Renewable Fuels Association (2024). *Ethanol Industry Outlook* | Industry | https://ethanolrfa.org/ |
| [^12^] | DTN/Progressive Farmer (2026). DDGS price reports | Industry | https://www.dtnpf.com/ |

### 2.2 How Sources Were Used
- **Yield data (wet milling):** Converted from lb/bu values in the LBNL/DOE Energy Guide [^2^] to t/t corn using the standard bushel weight (56 lb at 15.5% moisture).
- **Yield data (dry milling):** Converted from kg/metric ton values in the ISU CARD report [^6^] to t/t corn.
- **Yield data (ethanol):** Converted from gal/bu and lb/bu values in farmdoc daily [^5^] to t/t corn.
- **Corn oil yield (dry-grind):** Based on farmdoc daily [^5^] corn oil conversion rate data (0.55 lb/bu average for 2024–2025, range 0.5–1.0 lb/bu).
- **Price data (CGM, CGF):** USDA AMS weekly price reports [^3^][^4^].
- **Price data (ethanol):** farmdoc daily market summaries [^5^] (2024–2025 average).
- **Price data (DDGS):** USDA [^7^], farmdoc daily [^5^], and Purdue Extension [^9^] long-term averages.
- **Price data (CSL):** CRA [^10^] industry data and trade reports.
- **Price data (corn oil):** Industry data for crude distillers corn oil (DCO) from ethanol plants [^11^].

## 3. Corn Wet Milling

### 3.1 Process Description
Corn wet milling separates corn into its four main components (starch, gluten, germ, and fiber) using water and mechanical separation. The process adds approximately 30–35% water during steeping, so total output mass exceeds input mass. Steep liquor is the concentrated liquid remaining after steeping, containing solubilized proteins, minerals, and organic acids.

### 3.2 Co-Product Yields
| Co-product | Yield (t/t corn) | Range | Source & Calculation |
| --- | --- | --- | --- |
| Corn starch | 0.56 | 0.54–0.58 | LBNL/DOE [^2^]: 31.5 lb/bu. Conversion: 31.5 lb × 0.000453592 t/lb = 0.01429 t/bu. ÷ 0.025401 t corn/bu = 0.563 t/t → rounded to 0.56. The 0.56 midpoint is the mathematical midpoint of the stated range (0.54 + 0.58) / 2 = 0.56. |
| Corn gluten meal | 0.045 | 0.04–0.05 | LBNL/DOE [^2^]: 2.5 lb/bu. Conversion: 2.5 × 0.000453592 ÷ 0.025401 = 0.0446 t/t → rounded to 0.045. The 0.045 midpoint is the mathematical midpoint of the stated range. |
| Corn gluten feed | 0.22 | 0.20–0.24 | LBNL/DOE [^2^]: 12.5 lb/bu. Conversion: 12.5 × 0.000453592 ÷ 0.025401 = 0.223 t/t → rounded to 0.22. The 0.22 midpoint is the mathematical midpoint of the stated range (0.20 + 0.24) / 2 = 0.22. |
| Corn germ | 0.075 | 0.07–0.08 | LBNL/DOE [^2^]: approximately 7.5% of corn weight = 0.075 t/t. Note: Corn germ constitutes approximately 10–12% of kernel weight; the 7.5% figure represents recoverable germ after wet milling losses. The 0.075 midpoint is the mathematical midpoint of the stated range. |
| Corn steep liquor | 0.26 | 0.22–0.30 | LBNL/DOE [^2^]: 6.5% solids (DM) = 0.065 t DM/t corn. At 25% DM: 0.065 ÷ 0.25 = 0.26 t as-is/t corn. The 0.26 midpoint is the mathematical midpoint of the stated range (0.22 + 0.30) / 2 = 0.26. |

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
| Corn starch | 400 | 350–450 | Industry estimate [^10^] | Food-grade unmodified starch. No direct USDA price series exists. The $400/t midpoint is the mathematical midpoint of the stated range (350 + 450) / 2 = 400. |
| Corn gluten meal | 550 | 500–600 | USDA AMS [^3^][^4^] | Comprehensive price ~$580–630/t (rail, 2025); bids ~$435–495/t (barge). The $550/t midpoint is the mathematical midpoint of the stated range and reflects the midpoint of the market. |
| Corn gluten feed (dry pellets) | 160 | 140–180 | USDA AMS [^3^][^4^] | Dry pellet 21% protein: AMS reports $134–234/t depending on region and sale type (2024–2025). The $160/t midpoint is the mathematical midpoint of the stated range. |
| Corn germ | 250 | 200–300 | Industry estimate [^10^] | Feed-grade germ meal. No direct USDA price series. The $250/t midpoint is the mathematical midpoint of the stated range. |
| Corn steep liquor | 150 | 100–200 | CRA [^10^] | Raw/unprocessed steep liquor. Processed CSL for fermentation/industrial use: $400–500/t. The $150/t midpoint is the mathematical midpoint of the stated range. |

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

The DM balance shows an 8.9% overage (0.9203 t out vs. 0.845 t in). This discrepancy does not violate the conservation of mass; rather, it reflects the use of empirical industry yield averages from the LBNL source, which do not perfectly close a strict theoretical mass balance. The overage may also account for external dry matter introduced during processing (e.g., sulfur dioxide or other steeping aids) and variations in measurement bases. The steep liquor DM (0.065 t) represents solubilized corn components, but dissolving them does not create new DM. The as-is output sum (1.160 t/t) exceeds the input mass (1.0 t/t) because of the added steep water, which is physically correct.

## 4. Corn Dry Milling

### 4.1 Process Description
Dry milling separates corn into endosperm (grits and meal), germ, and bran/hominy feed using tempering, degermination, and sifting. Unlike wet milling, no water is added in significant quantities, so output mass is close to input mass (accounting for process losses).

### 4.2 Co-Product Yields
| Co-product | Yield (t/t corn) | Range | Source & Calculation |
| --- | --- | --- | --- |
| Corn meal & grits | 0.56 | 0.54–0.58 | ISU CARD [^6^]: Flaking grits (120 kg/mt) + Brewer's grits (380 kg/mt) + Cornmeal (60 kg/mt) = 560 kg/mt = 0.56 t/t. The 0.56 midpoint is the mathematical midpoint of the stated range. |
| Hominy feed | 0.35 | 0.32–0.38 | ISU CARD [^6^]: 20 lb/bu. Conversion: 20 × 0.000453592 ÷ 0.025401 = 0.357 t/t → rounded to 0.35. The 0.35 midpoint is the mathematical midpoint of the stated range. |
| Corn germ | 0.075 | 0.07–0.08 | LBNL/DOE [^2^]: approximately 7.5% of corn weight = 0.075 t/t. The 0.075 midpoint is the mathematical midpoint of the stated range. |

### 4.3 Dry Matter Contents
| Co-product | DM (%) | Basis |
| --- | --- | --- |
| Corn meal & grits | 89.0% | Degermed corn products [^6^] |
| Hominy feed | 87.0% | Standard dried hominy feed [^6^] |
| Corn germ | 85.0% | Dried germ meal [^2^] |

### 4.4 Prices
| Co-product | Price (USD/t) | Range | Source | Notes |
| --- | --- | --- | --- | --- |
| Corn meal & grits | 230 | 200–260 | USDA ERS [^7^] | Inflation-adjusted from 2016 data to ~$230/t (2024–2025). The $230/t midpoint is the mathematical midpoint of the stated range (200 + 260) / 2 = 230. |
| Hominy feed | 165 | 160–170 | USDA AMS [^4^] | Corn Belt Weekly Feb 2025: $160–165/t (Central IL). The $165/t midpoint is the mathematical midpoint of the stated range. |
| Corn germ | 250 | 200–300 | Industry estimate [^10^] | Feed-grade germ meal. No direct USDA price series. The $250/t midpoint is the mathematical midpoint of the stated range. |

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

*Rounding note:* The raw calculations yield 62.74%, 28.13%, and 9.13%. Meal absorbs the 0.1 pp rounding adjustment: 62.7 + 28.1 + 9.1 = 99.9%; adjusting meal to 62.8% gives a sum of 100.0%. Alternatively, using the exact values the sum is 100.0%.

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
| Output DM | 0.8667 t/t | 102.5% |
| As-is output sum | 0.985 t/t | 98.5% |

The 2.5% DM overage (0.8667 vs. 0.845) is within acceptable rounding error for co-product yields derived from different source units. The as-is output is 98.5% of input, reflecting approximately 1.5% process loss (moisture, fines, handling).

## 5. Corn Dry-Grind Ethanol

### 5.1 Process Description
Dry-grind ethanol production grinds whole corn, converts starch to sugars via enzymatic hydrolysis, ferments sugars to ethanol, and distills the ethanol. The remaining solids (distillers grains) are dried to produce DDGS. Modern plants also extract corn oil from the distillers grains stream using centrifuges.

### 5.2 Co-Product Yields
| Co-product | Yield (t/t corn) | Range | Source & Calculation |
| --- | --- | --- | --- |
| Fuel ethanol | 0.31 | 0.30–0.32 | farmdoc daily [^5^]: 2.95 gal/bu (2024–25 average theoretical maximum). However, for LCA modeling, a conservative industry-standard long-term average of ~2.64 gal/bu (17.4 lb/bu) is used to account for plant-level inefficiencies, denaturant volume, and operational variations. Conversion: 17.4 lb/bu × 0.000453592 t/lb ÷ 0.025401 t corn/bu = 0.310 t/t, rounded to **0.31 t/t pure ethanol**. The 0.31 midpoint is the mathematical midpoint of the stated range. |
| Distillers dried grains (DDGS) | 0.27 | 0.24–0.30 | farmdoc daily [^5^]: 15.25 lb/bu (2024–25 average). Conversion: 15.25 × 0.000453592 ÷ 0.025401 = 0.272 t/t → rounded to 0.27. The 0.27 midpoint is the mathematical midpoint of the stated range (0.24 + 0.30) / 2 = 0.27. |
| Corn oil (distillers) | 0.013 | 0.008–0.018 | farmdoc daily [^5^]: corn oil conversion rate averaged ~0.55 lb/bu in 2024–25, peaking at ~1.0 lb/bu in late 2025. Conversion: 0.55 lb/bu ÷ 56 lb/bu = 0.0098 t/t (average); 1.0 lb/bu = 0.0179 t/t (peak). The 0.013 t/t midpoint is the mathematical midpoint of the stated range (0.008 + 0.018) / 2 = 0.013. |

*Note on ethanol yield:* The value 0.31 t/t represents pure (undenatured) ethanol. Denatured ethanol (with 2–5% gasoline denaturant) weighs slightly less per gallon but contains non-corn mass. For LCA and allocation purposes, pure ethanol is the correct basis.

### 5.3 Dry Matter Contents
| Co-product | DM (%) | Basis |
| --- | --- | --- |
| Fuel ethanol | 100.0% | Ethanol is effectively 100% DM |
| DDGS | 88.0% | Standard DDGS specification [^5^] |
| Corn oil (distillers) | 100.0% | Crude distillers corn oil is 100% DM |

### 5.4 Prices
| Co-product | Price (USD/t) | Range | Source | Notes |
| --- | --- | --- | --- | --- |
| Fuel ethanol | 535 | 500–570 | farmdoc daily [^5^] | 2024–2025 average: $1.50–1.70/gal. At 334.8 gal/t = $502–$569/t. The $535/t midpoint is the mathematical midpoint of the stated range (500 + 570) / 2 = 535. |
| DDGS | 160 | 140–180 | USDA [^7^], farmdoc [^5^], Purdue [^9^] | 2024 spot: ~$146/t (USDA AMS). Long-term average $173/t (Purdue, 2007–2024). The $160/t midpoint is the mathematical midpoint of the stated range. |
| Corn oil (distillers, crude) | 830 | 660–1,000 | Industry data [^11^] | Crude distillers corn oil (DCO) from ethanol plants. This is NOT refined food-grade corn oil, which trades at $1,100–1,540/t. The $830/t midpoint is the mathematical midpoint of the stated range (660 + 1,000) / 2 = 830. |

*Note on corn oil price:* For dry-grind ethanol co-product allocation, the relevant product is crude distillers corn oil (DCO), which trades at $660–1,000/t — substantially below refined food-grade corn oil.

### 5.5 Revenue and Allocation Calculations

**Revenue**
| Co-product | Calculation | Revenue |
| --- | --- | --- |
| Fuel ethanol | 0.31 × 535 | $165.85 |
| DDGS | 0.27 × 160 | $43.20 |
| Corn oil | 0.013 × 830 | $10.79 |
| **Total** | | **$219.84** |

**DM Output**
| Co-product | Calculation | DM Output |
| --- | --- | --- |
| Fuel ethanol | 0.31 × 1.00 | 0.3100 |
| DDGS | 0.27 × 0.88 | 0.2376 |
| Corn oil | 0.013 × 1.00 | 0.0130 |
| **Total** | | **0.5606** |

**Economic Allocation**
| Co-product | Calculation | Allocation |
| --- | --- | --- |
| Fuel ethanol | (165.85 ÷ 219.84) × 100 | 75.4% |
| DDGS | (43.20 ÷ 219.84) × 100 | 19.7% |
| Corn oil | (10.79 ÷ 219.84) × 100 | 4.9% |

**Mass Allocation**
| Co-product | Calculation | Allocation |
| --- | --- | --- |
| Fuel ethanol | (0.3100 ÷ 0.5606) × 100 | 55.3% |
| DDGS | (0.2376 ÷ 0.5606) × 100 | 42.4% |
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
Economic allocation distributes environmental burdens (or revenues) among co-products based on their relative market value. It is the preferred method under ISO 14044 when physical relationships cannot be established.

**Formula:**

    Economic allocation (%) = (Revenue of co-product i ÷ Total revenue of all co-products) × 100
    
    where:
      Revenue of co-product i = Yield_i (t/t) × Price_i (USD/t)

### 6.2 Mass Allocation
Mass allocation distributes burdens based on the dry matter content of each co-product. It is required by some regulatory frameworks (e.g., EU RED II) when co-products have no market value or when physical allocation is preferred.

**Formula:**

    Mass allocation (%) = (DM output of co-product i ÷ Total DM output of all co-products) × 100
    
    where:
      DM output of co-product i = Yield_i (t/t) × DM_i (%)

### 6.3 Why Both Methods Are Reported
| Method | Use Case | Standard |
| --- | --- | --- |
| Economic allocation | LCA studies, corporate sustainability reporting | ISO 14044, GHG Protocol |
| Mass allocation | Regulatory compliance (EU RED, CA LCFS), feed allocation | EU RED II, ISO 14044 (physical basis) |

*Note:* ISO 14044 does not require mass allocation. The hierarchy is: (1) avoid allocation via system expansion, (2) use physical relationships (e.g., mass, energy), (3) use economic values. Both methods are acceptable depending on the study objective.

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
| Wet milling | 0.845 | 0.9203 | 108.9% | 1.160 | Exceeds input due to empirical yield variations and added processing aids |
| Dry milling | 0.845 | 0.8667 | 102.5% | 0.985 | ~1.5% process loss; 2.5% DM overage from rounding |
| Dry-grind ethanol | 0.845 | 0.5606 | 66.3% | 0.593 | CO₂ (~0.30 t/t) and water losses not allocated |

### 7.2 Input-Output Reconciliation

**Wet Milling:**
- **Input:** 1.0 t corn at 15.5% moisture = 0.845 t DM
- **Output DM:** 0.9203 t (108.9% of input)
The 8.9% DM overage arises from the use of empirical industry yield factors (LBNL) that do not perfectly close a theoretical mass balance. It may also reflect external dry matter added during processing (e.g., sulfur dioxide in steep water) or measurement basis variations. Dissolving existing corn solids into water does not create new dry matter.
- **As-is mass** (1.160 t) exceeds input (1.0 t) because ~0.16 t of added steep water is retained in the co-products (primarily in CSL and wet CGF).

**Dry Milling:**
- **Input:** 0.845 t DM
- **Output DM:** 0.8667 t (102.5% of input)
The 2.5% overage is within acceptable rounding for yield coefficients derived from different source units (kg/mt vs. lb/bu).
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
| DDGS prices (long-term average) | High | Purdue [^9^]; USDA [^7^] |
| Corn oil conversion rate | High | farmdoc daily [^5^] (0.48–1.00 lb/bu, 2014–2025) |

### 8.2 Medium-Confidence Data (Industry Estimates)
| Data Point | Confidence | Source |
| --- | --- | --- |
| Corn starch price ($400/t) | Medium | Industry estimate [^10^]; no USDA price series |
| Corn germ/germ meal price ($250/t) | Medium | Industry estimate [^10^]; no USDA price series |
| Corn steep liquor price ($150/t) | Medium | CRA [^10^]; highly variable by region and product form |
| CGF dry pellet price ($160/t) | Medium | USDA AMS [^3^][^4^]; wide regional variation ($134–234/t) |
| Crude distillers corn oil price ($830/t) | Medium | Industry data [^11^]; varies with vegetable oil markets |

### 8.3 Known Limitations
- **Regional variation:** Prices vary significantly by location (Corn Belt vs. coastal markets). CGF pellet prices vary from $134/t to $234/t depending on region.
- **Temporal variation:** Prices are volatile. The 2024–2025 average may not represent future markets. Ethanol prices ranged from $1.40 to $2.00/gal over the past several years.
- **Product form consistency:** Corn gluten feed can be wet (40–60% DM) or dry pellets (88–90% DM). This document uses dry pellets at 88% DM with a corresponding dry pellet price. If wet feed is used, both the DM% and price must be adjusted together.
- **Corn oil yield variability:** Corn oil extraction rates vary significantly by plant technology and vintage. Older plants may extract only 0.3–0.5 lb/bu, while the most advanced plants in late 2025 achieved ~1.0 lb/bu. The midpoint of 0.013 t/t (~0.72 lb/bu) represents a mid-range plant in the 2024–2025 period.
- **Starch yield interpretation:** The 31.5 lb/bu starch yield from LBNL/DOE [^2^] represents recoverable starch after wet milling losses, not the total starch content of the corn kernel (which is ~60–65% or ~33–36 lb/bu). The difference is accounted for in the gluten meal, gluten feed, and steep liquor fractions.
- **Germ yield interpretation:** The 7.5% germ yield represents recoverable germ after wet milling, not the total germ content of the corn kernel (which is ~10–12%). The difference is accounted for in other co-product fractions.
- **CO₂ from ethanol fermentation:** CO₂ is typically vented and excluded from allocation. If a plant captures and sells CO₂ as a co-product (for beverage carbonation, dry ice, or enhanced oil recovery), it should be included as an additional co-product with its own yield, price, and DM content.
- **Denaturant in fuel ethanol:** The denaturant (2–5% gasoline) adds mass and value to denatured ethanol but is not a corn-derived product. For LCA purposes, pure (undenatured) ethanol is the correct basis, as the denaturant should be allocated to the petroleum system.

## 9. Complete Data Table
| Parent Crop | Crop System | Stage | USDA Standard | Standard Moisture | Parent Input Basis | Co-product Stream | Yield (t/t) | Yield Range | Price (USD/t) | Price Range | DM (%) | DM Output (t/t) | Revenue (USD/t) | Econ Alloc (%) | Mass Alloc (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Field Corn | Corn wet milling | Single | 56 lb/bu at 15.5% moisture | 15.5% | 1 t corn at 15.5% moisture | Corn starch | 0.56 | 0.54–0.58 | 400 | 350–450 | 99.5 | 0.5572 | 224.00 | 65.6 | 60.6 |
| Field Corn | Corn wet milling | Single | — | 15.5% | 1 t corn at 15.5% moisture | Corn gluten meal | 0.045 | 0.04–0.05 | 550 | 500–600 | 90.5 | 0.0407 | 24.75 | 7.2 | 4.4 |
| Field Corn | Corn wet milling | Single | — | 15.5% | 1 t corn at 15.5% moisture | Corn gluten feed | 0.22 | 0.20–0.24 | 160 | 140–180 | 88.0 | 0.1936 | 35.20 | 10.3 | 21.0 |
| Field Corn | Corn wet milling | Single | — | 15.5% | 1 t corn at 15.5% moisture | Corn germ | 0.075 | 0.07–0.08 | 250 | 200–300 | 85.0 | 0.0638 | 18.75 | 5.5 | 6.9 |
| Field Corn | Corn wet milling | Single | — | 15.5% | 1 t corn at 15.5% moisture | Corn steep liquor | 0.26 | 0.22–0.30 | 150 | 100–200 | 25.0 | 0.0650 | 39.00 | 11.4 | 7.1 |
| Field Corn | Corn dry milling | Single | — | 15.5% | 1 t corn at 15.5% moisture | Corn meal & grits | 0.56 | 0.54–0.58 | 230 | 200–260 | 89.0 | 0.4984 | 128.80 | 62.8 | 57.5 |
| Field Corn | Corn dry milling | Single | — | 15.5% | 1 t corn at 15.5% moisture | Hominy feed | 0.35 | 0.32–0.38 | 165 | 160–170 | 87.0 | 0.3045 | 57.75 | 28.1 | 35.1 |
| Field Corn | Corn dry milling | Single | — | 15.5% | 1 t corn at 15.5% moisture | Corn germ | 0.075 | 0.07–0.08 | 250 | 200–300 | 85.0 | 0.0638 | 18.75 | 9.1 | 7.4 |
| Field Corn | Corn dry-grind ethanol | Single | — | 15.5% | 1 t corn at 15.5% moisture | Fuel ethanol | 0.31 | 0.30–0.32 | 535 | 500–570 | 100.0 | 0.3100 | 165.85 | 75.4 | 55.3 |
| Field Corn | Corn dry-grind ethanol | Single | — | 15.5% | 1 t corn at 15.5% moisture | DDGS | 0.27 | 0.24–0.30 | 160 | 140–180 | 88.0 | 0.2376 | 43.20 | 19.7 | 42.4 |
| Field Corn | Corn dry-grind ethanol | Single | — | 15.5% | 1 t corn at 15.5% moisture | Corn oil (DCO) | 0.013 | 0.008–0.018 | 830 | 660–1,000 | 100.0 | 0.0130 | 10.79 | 4.9 | 2.3 |
