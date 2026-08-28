# Flaxseed Crushing: Co-Product Allocation Methodology, Data Sources, and Calculations
**Document Version:** 1.0
**Date:** June 2026
**Basis:** 1 metric ton (t) of flaxseed (AKA linseed) at 8.9% moisture (industry trading reference)
**Price Period:** 2024–2025 average (unless otherwise noted)

## Table of Contents
- [1. Standard Basis and Conversions](#1-standard-basis-and-conversions)
- [2. Data Sources and References](#2-data-sources-and-references)
- [3. Flaxseed Crushing System](#3-flaxseed-crushing-system)
- [4. Co-Product Yields and Properties](#4-co-product-yields-and-properties)
- [5. Prices](#5-prices)
- [6. Allocation Methodology](#6-allocation-methodology)
- [7. Mass Balance Verification](#7-mass-balance-verification)
- [8. Complete Data Table](#8-complete-data-table)
- [9. Data Quality and Limitations](#9-data-quality-and-limitations)

## 1. Standard Basis and Conversions

### 1.1 Parent Input Definition
| Parameter | Value | Source |
| --- | --- | --- |
| Parent crop | Flaxseed / Linseed (*Linum usitatissimum*) | — |
| Input quantity | 1 metric ton (1,000 kg) | — |
| Moisture content | 8.9% | Industry trading reference for flaxseed, toward the lower end of the typical safe-storage and trading range of 8–10.5% [^1^]. Flaxseed has no official USDA standard moisture (see the note below), so a representative trading moisture is used as the basis. |
| Dry matter (DM) input | 0.911 t DM/t flaxseed | Calculated: 1.000 × (1 − 0.089) = 0.911 |
| Bushel equivalent | 39.37 bushels/t | 1,000 kg ÷ 25.401 kg/bu (56 lb at standard moisture) |
| Bushel weight | 56.0 lb (25.401 kg) | USDA standard for flaxseed [^1^] |
| Typical oil content | ~44–46% (dry matter basis) | Canadian Grain Commission harvest quality reports for No. 1 CW flaxseed [^10^]: 45.6% (2020), 46.7% (2019), 2010–2019 mean 45.7%, all reported on a dry matter basis |

### 1.2 Unit Conversions
| Conversion | Factor |
| --- | --- |
| 1 bushel flaxseed | 56.0 lb = 25.401 kg |
| 1 lb | 0.453592 kg = 0.000453592 t |
| 1 t flaxseed | 39.37 bushels |
| 1 short ton | 2,000 lb = 0.907185 metric ton |
| 1 metric ton | 2,204.62 lb = 1.10231 short tons |

### 1.3 Convention for Adopted Values

Every yield, price, and DM% in this document is reported as an adopted point value together with the range it was drawn from. **Unless a row states otherwise, the adopted value is the midpoint of its stated range**, and the range is the parameter that carries the evidence. Point values are given to the precision the underlying sources support and are not intended to imply plant-level accuracy. Derived quantities (DM outputs, revenues, allocation percentages) are carried at four decimals internally and reported to one decimal place.

*Note on naming:* "Flaxseed" and "linseed" refer to the same crop (*Linum usitatissimum*). The term "flaxseed" is more commonly used in North America when the grain is destined for food or crushing, while "linseed" is more common in industrial contexts and in Europe/Oceania. The co-products are universally called "linseed oil" and "linseed meal."

*Note on moisture basis:* Unlike wheat (13.0%) or corn (15.5%), flaxseed has no official USDA standard moisture for grading purposes; moisture is not a grading factor under the U.S. Standards for Flaxseed (7 CFR Part 810, Subpart E). In the absence of a trading standard, 8.9% is used as a representative moisture within the 8–10.5% band. Because there is no standard to anchor it, the input dry matter carries more uncertainty here than in the grain files, and the dry-matter balance in Section 7 should be read with that in mind.

## 2. Data Sources and References

### 2.1 Primary Sources
| Citation | Full Title | Type | URL |
| --- | --- | --- | --- |
| [^1^] | USDA AMS FGIS — Grain Standards for Flaxseed (formerly GIPSA) | Government (USDA) | https://ams.usda.gov/ |
| [^2^] | FAO. *Food Outlook: Oilseeds and Oils Chapter* (biannual) | International Organization | https://www.fao.org/ |
| [^3^] | USDA ERS. *Oil Crops Yearbook* (Tables 29–31: Flaxseed, Linseed Meal, Linseed Oil) | Government (USDA) | https://ers.usda.gov/ |
| [^4^] | USDA WASDE (February 2026). *World Agricultural Supply and Demand Estimates* | Government (USDA) | https://www.usda.gov/ |
| [^5^] | IndexMundi. *Linseed Oil Monthly Price* | Market Data | https://www.indexmundi.com/ |
| [^6^] | IndexBox (2025). *World Linseed Market Analysis* (seed and oil only) | Industry/Market | https://www.indexbox.io/ |
| [^7^] | Flax Council of Canada. *Flax Feed Industry Guide* | Industry Association | https://flaxcouncil.ca/ |
| [^8^] | Wanasundara, J.P.D. and Shahidi, F. (1994). "Functional properties and amino-acid composition of solvent-extracted flaxseed meals." *Food Chemistry*, 49(1), 45–51. | Academic | https://doi.org/10.1016/0308-8146(94)90235-6 |
| [^9^] | Tridge (2025). *Linseed Meal — Global Price and Market Data* | Industry/Market | https://dir.tridge.com/ |
| [^10^] | Canadian Grain Commission (2024). *Flaxseed Harvest Quality Report* | Government (Canada) | https://www.grainscanada.gc.ca/ |
| [^11^] | Feedstuffs (2025). *Ingredient Market: Linseed Meal Price Series* | Industry/Market | https://www.feedstuffs.com/ |

### 2.2 How Sources Were Used
- **Yield data:** USDA ERS [^3^], FAO [^2^], and Flax Council of Canada [^7^] provided flaxseed crush yield data. The ranges reflect variation across extraction methods (expeller vs. solvent) and flaxseed varieties (high-oil vs. standard). IndexBox [^6^] provided linseed (seed) and linseed oil market data but does not track linseed meal pricing; it is not cited for meal prices.
- **Price data (oil):** USDA ERS [^3^], WASDE [^4^], and IndexMundi [^5^] provided linseed oil price data. Prices reflect the industrial/food grade crude oil market.
- **Price data (meal):** USDA ERS [^3^] (Oil Crops Yearbook Table 10 includes linseed meal prices), Tridge [^9^] (linseed meal transaction prices), and Feedstuffs [^11^] (ingredient market price series) provided linseed meal (solvent-extracted, ~35% protein) price data. The $400/t meal price is an industry estimate informed by these sources.
- **Oil content data:** Canadian Grain Commission [^10^] provided annual flaxseed oil content data for No. 1 CW flaxseed on a dry matter basis (45.6% in 2020, 46.7% in 2019, 2010–2019 mean 45.7%), which sets the 44–46% DM oil content used in Section 1.1 and the composition check on the oil yield in Section 4.1.
- **DM contents:** Industry trading specifications for linseed meal (max 12% moisture = min 88% DM) [^8^] and linseed oil (negligible moisture = ~100% DM).

## 3. Flaxseed Crushing System

### 3.1 Process Description
Flaxseed crushing (also called "linseed processing") involves the following steps:
1. **Cleaning:** Foreign material (dirt, weed seeds, chaff) is removed.
2. **Conditioning:** Flaxseed is heated and tempered to improve oil extractability and reduce meal moisture.
3. **Flaking:** Seeds are rolled into thin flakes to rupture cell walls and increase surface area.
4. **Pressing (optional):** Some facilities use a mechanical screw press (expeller) to remove ~50–70% of the oil before solvent extraction. Others go directly to solvent extraction.
5. **Solvent extraction:** Hexane is used to extract the remaining oil from the pressed cake or flakes.
6. **Desolventizing:** Hexane is removed from the oil (miscella) and meal (marc) by steam stripping and distillation.
7. **Oil refining:** Crude oil is degummed, neutralized, bleached, and deodorized for food or industrial use.
8. **Meal processing:** Meal is dried, cooled, and ground to specification (typically ~35% protein, max 12% moisture).

**Co-products generated:**
- **Linseed oil:** The primary high-value product (industrial coatings, food/nutraceuticals, biodiesel).
- **Linseed meal:** The primary high-volume co-product (ruminant animal feed, protein source).

*Note on hulls:* Unlike soybeans, flaxseed hulls are not typically separated as a distinct co-product in commercial crushing. The hulls remain with the meal, contributing to its fiber content (~8–10% crude fiber). Some specialty operations may dehull flaxseed for food-grade products, but standard crushing does not produce a separate hulls stream.

### 3.2 Process Flow

    1 t flaxseed at 8.9% moisture (0.911 t DM)
            │
            ▼
      ┌─ FLAXSEED CRUSHING ───────────────────────────┐
      │                                                 │
      │  Processing losses: 0.015 t as-is (1.5%)       │
      │  (handling, residual solvent, moisture loss)    │
      │  DM surplus: +0.0038 t DM (see Section 7)      │
      │                                                 │
      │  Linseed oil: 0.40 t as-is (0.4000 t DM)    ◄── co-product
      │                                                 │
      │  Linseed meal: 0.585 t as-is (0.5148 t DM)   ◄── co-product
      │                                                 │
      └─────────────────────────────────────────────────┘

    TWO CO-PRODUCTS from 1 t flaxseed:
      Linseed oil:  0.40 t as-is,  0.4000 t DM
      Linseed meal: 0.585 t as-is,  0.5148 t DM
      Total:                      0.9148 t DM  (from 0.911 t input; +0.0038 t DM surplus, see Section 7)

## 4. Co-Product Yields and Properties

### 4.1 Yields (per tonne of flaxseed input)
| Co-product | Yield (t/t flaxseed) | Range | Source & Calculation |
| --- | --- | --- | --- |
| Linseed oil | 0.40 | 0.36–0.44 | Industry standard solvent extraction yield [^2^][^3^][^7^]. The lower bound (0.36) represents moderate-oil varieties with typical extraction efficiency; the upper bound (0.44) represents high-oil varieties with efficient extraction. See the reconciliation note below for how the adopted 0.40 relates to seed composition. |
| Linseed meal | 0.585 | 0.55–0.62 | Industry reported yield range for solvent-extracted linseed meal [^3^][^7^]. Taken from industry data rather than derived as a residual. Solvent-extracted linseed meal yields vary with oil extraction efficiency: higher oil extraction means lower meal yield. |

*Reconciling the oil yield with seed composition:* Two independent routes give the oil yield, and they are close but not identical.
- **Seed composition route.** At the Canadian Grain Commission oil content for No. 1 CW flaxseed [^10^] — 45.7% of dry matter as a ten-year mean — 1 t of seed at 8.9% moisture carries 0.911 × 0.457 = 0.416 t of oil. Commercial solvent extraction recovers roughly 96–98% of it, giving **0.400–0.408 t/t**.
- **Reported crush yields.** Industry and USDA ERS crush data [^2^][^3^][^7^] give a range of **0.36–0.44 t/t** across varieties and extraction methods, midpoint 0.40.

The adopted value, **0.40 t/t**, is the midpoint of the reported crush range and also the lower end of the composition route, so the two agree. The upper bound of the reported range (0.44 t/t) would require about 48.4% oil on a dry matter basis, which is above anything the CGC harvest surveys record; it should be read as an optimistic bound rather than a typical value.

*Note on yield relationship:* Oil and meal yields are inversely related. When more oil is extracted (higher oil yield), less meal is produced (lower meal yield). The values in this table (0.40 oil, 0.585 meal) are each the midpoint of its own literature range and are therefore not constrained to satisfy that inverse relationship jointly; see Section 7 for the resulting dry-matter surplus. If oil yield were set higher (e.g., 0.42), meal yield would fall correspondingly (e.g., 0.565) to preserve the mass balance at ~1.5% processing losses.

*Methodological note on yield sourcing:* Both co-product yields are taken independently from industry and USDA ERS data [^3^][^7^], each at the midpoint of its own reported range, and neither is derived as a residual from the dry-matter balance. The input basis is 1 t of flaxseed at 8.9% moisture (0.911 t DM), a representative trading moisture within the 8–10.5% band. Because the two yields are not mutually reconciled, the dry-matter outputs do not close against the input: their sum exceeds input DM by 0.0038 t (0.42%). This is reported rather than removed. Section 7.2 gives the balance assessment, the residual-derived alternative, and the effect of the choice on the reported factors.

**Why Yields Do Not Sum to 1.0**
The as-is yields sum to 0.985 t/t flaxseed (0.40 + 0.585), which is less than the 1.0 t input. The ~1.5% shortfall represents real processing losses:
- **Handling and spillage:** ~0.5–1.0% lost during transport, transfer, and cleaning.
- **Residual solvent in meal:** Trace hexane (regulated to <500 ppm) adds negligible mass.
- **Moisture loss:** Flaxseed is conditioned and dried during processing, losing ~0.5–1.0% moisture.
- **Fines and dust:** ~0.2–0.5% lost as fines during flaking and handling.
The 1.5% total loss is consistent with industry data for solvent extraction plants [^2^][^7^].

### 4.2 Dry Matter Contents
| Co-product | DM (%) | Basis |
| --- | --- | --- |
| Linseed oil | 100.0% | Crude and refined linseed oil are essentially pure lipid (triglycerides) with negligible moisture (<0.1%). |
| Linseed meal | 88.0% | Standard trading specification: maximum 12% moisture = minimum 88% DM [^8^]. Solvent-extracted meal is typically delivered at 10–12% moisture. The 88% DM value represents the standard trading basis. |

### 4.3 DM Output per Tonne of Flaxseed
| Co-product | Calculation | DM Output (t/t flaxseed) |
| --- | --- | --- |
| Linseed oil | 0.40 × 1.00 | 0.4000 |
| Linseed meal | 0.585 × 0.88 | 0.5148 |
| **Total** | | **0.9148** |

## 5. Prices

### 5.1 Price Table
| Co-product | Price (USD/t) | Range | Source | Notes |
| --- | --- | --- | --- | --- |
| Linseed oil | 1,300 | 1,000–1,600 | USDA ERS [^3^]; WASDE [^4^]; IndexMundi [^5^] | 2024–2025 average. Linseed oil prices are volatile, driven by industrial demand (coatings, linoleum) and food/nutraceutical markets. Range captures market variability. |
| Linseed meal | 400 | 300–500 | USDA ERS [^3^]; Tridge [^9^]; Feedstuffs [^11^] | 2024–2025 average for solvent-extracted meal (~35% protein). Prices vary with protein content and regional demand. Range captures market variability. |

### 5.2 Price Verification
**Linseed oil:** adopted $1,300/t, the midpoint of the $1,000–1,600 range.
- USDA ERS (2025): ~$1,250-1,350/t (crude, FOB)
- IndexMundi (2025 avg): ~$1,280/t
- Historical range (2020-2025): $900-1,800/t

**Linseed meal:** adopted $400/t, the midpoint of the $300–500 range.
- USDA ERS (2025): ~$350-420/t (solvent-extracted, 35% protein)
- Tridge (2025): ~$380-420/t
- Feedstuffs (2025): ~$350-450/t
- Historical range (2020-2025): $250-550/t

### 5.3 Revenue per Tonne of Flaxseed
| Co-product | Calculation | Revenue (USD/t flaxseed) |
| --- | --- | --- |
| Linseed oil | 0.40 × 1,300 | $520.00 |
| Linseed meal | 0.585 × 400 | $234.00 |
| **Total** | | **$754.00** |

## 6. Allocation Methodology

### 6.1 Economic Allocation
Economic allocation distributes environmental burdens among co-products based on their relative market value.
**Formula:**
`Economic allocation (%) = (Revenue of co-product i ÷ Total revenue of all co-products) × 100`

| Co-product | Calculation | Allocation |
| --- | --- | --- |
| Linseed oil | (520.00 ÷ 754.00) × 100 | 69.0% |
| Linseed meal | (234.00 ÷ 754.00) × 100 | 31.0% |
| **Total** | | **100.0%** |

*Rounding note:* The raw calculations yield 68.966% (oil) and 31.034% (meal), which round to 69.0% and 31.0% at one decimal place so that the sum is exactly 100.0%.

### 6.2 Mass Allocation
Mass allocation distributes burdens based on the dry matter content of each co-product.
**Formula:**
`Mass allocation (%) = (DM output of co-product i ÷ Total DM output of all co-products) × 100`

| Co-product | Calculation | Allocation |
| --- | --- | --- |
| Linseed oil | (0.4000 ÷ 0.9148) × 100 | 43.7% |
| Linseed meal | (0.5148 ÷ 0.9148) × 100 | 56.3% |
| **Total** | | **100.0%** |

*Rounding note:* The raw calculations yield 43.73% (oil) and 56.27% (meal) at two decimal places. These are rounded to 43.7% and 56.3% so that the sum is exactly 100.0%.

### 6.3 Comparison: Economic vs. Mass Allocation
| Co-product | Economic Allocation | Mass Allocation | Difference |
| --- | --- | --- | --- |
| Linseed oil | 69.0% | 43.7% | +25.3 pp |
| Linseed meal | 31.0% | 56.3% | −25.3 pp |

The large difference reflects the high value-to-mass ratio of linseed oil. Oil commands $1,300/t (3.25× the meal price) but contains only 43.7% of the DM, giving it a much larger economic allocation than mass allocation. This pattern is typical of oilseed crushing, where oil is the high-value, low-mass product and meal is the high-mass, lower-value product.

## 7. Mass Balance Verification

### 7.1 Input-Output Reconciliation
| Check | Value | Status |
| --- | --- | --- |
| Input: Flaxseed at 8.9% moisture | 1.000 t | — |
| Input moisture | 8.9% | — |
| Input DM | 0.911 t | — |
| Output: Linseed oil (as-is) | 0.400 t | ✓ |
| Output: Linseed meal (as-is) | 0.585 t | ✓ |
| Total as-is output | 0.985 t | 98.5% of input |
| Processing losses (as-is) | 0.015 t | 1.5% of input ✓ |
| Output DM: Oil | 0.4000 t | ✓ |
| Output DM: Meal | 0.5148 t | ✓ |
| Total DM output | 0.9148 t | — |
| DM surplus | +0.0038 t | +0.42% of input DM |

### 7.2 DM Balance Detail
| Item | Value | Notes |
| --- | --- | --- |
| Input DM (1 t flaxseed at 8.9% moisture) | 0.9110 t | 1.000 × (1 − 0.089) |
| Output DM — co-products: | | |
| Linseed oil | 0.4000 t | 0.40 t × 100% DM |
| Linseed meal | 0.5148 t | 0.585 t × 88% DM |
| Total co-product DM | 0.9148 t | |
| DM balance gap (surplus) | +0.0038 t | +0.42% of input DM |

*Balance assessment:* The DM output (0.9148 t) exceeds the DM input (0.9110 t) by 0.0038 t, a surplus of 0.42%. Dry matter cannot be created, so this is an accounting result, not a physical one: the oil and meal yields are each drawn independently from its own literature range and are not mutually reconciled to a closed unit-process balance. The surplus is small relative to the width of those ranges (oil 0.36–0.44, meal 0.55–0.62) and to the uncertainty in the input moisture, which has no trading standard to anchor it.

*Effect of closing the balance:* The surplus can be removed by deriving the meal yield as the residual, in the manner of the canola methodology. Holding oil at 0.40 t/t and allowing 0.5% of input DM for processing losses gives a meal yield of **0.575 t/t** — comfortably inside the stated 0.55–0.62 range — and a total DM output of 0.9060 t, which closes. The effect on the reported factors is small:

| | As published (meal 0.585) | Residual-derived (meal 0.575) |
| --- | --- | --- |
| Mass allocation, oil / meal | 43.7% / 56.3% | 44.2% / 55.8% |
| Economic allocation, oil / meal | 69.0% / 31.0% | 69.3% / 30.7% |

The difference is under half a percentage point on any factor, which is well below the spread introduced by the price and yield ranges themselves and immaterial for ration-level or footprint-level use. The published values retain the independently sourced meal yield; users who require a closed balance can substitute 0.575 t/t and the factors above.

### 7.3 As-Is Mass Balance
| Item | Value | Notes |
| --- | --- | --- |
| Input (flaxseed) | 1.000 t | — |
| Output: | | |
| Linseed oil | 0.400 t | — |
| Linseed meal | 0.585 t | — |
| Total output | 0.985 t | |
| Processing losses | 0.015 t | 1.5%: handling, moisture loss, fines |
| **Balance** | **1.000 t** | **✓ Exact** |

## 8. Complete Data Table
| Parent Crop | Crop System | Stage | USDA Standard | Standard Moisture | Parent Input Basis | Co-product Stream | Yield (t/t) | Yield Range | Price (USD/t) | Price Range | DM (%) | DM Output (t/t) | Revenue (USD/t) | Econ Alloc (%) | Mass Alloc (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Flaxseed | Flaxseed crushing | Single | 56 lb/bushel | 8.9% | 1 t flaxseed at 8.9% moisture | Linseed oil | 0.40 | 0.36–0.44 | 1,300 | 1,000–1,600 | 100.0 | 0.4000 | 520.00 | 69.0 | 43.7 |
| Flaxseed | Flaxseed crushing | Single | 56 lb/bushel | 8.9% | 1 t flaxseed at 8.9% moisture | Linseed meal | 0.585 | 0.55–0.62 | 400 | 300–500 | 88.0 | 0.5148 | 234.00 | 31.0 | 56.3 |

*Note on allocation rounding:* Raw economic allocations are 68.97% (oil) and 31.03% (meal), rounded to 69.0% and 31.0% to sum to exactly 100.0%. Raw mass allocations are 43.73% (oil) and 56.27% (meal), rounded to 43.7% and 56.3% to sum to exactly 100.0%.

## 9. Data Quality and Limitations

### 9.1 High-Confidence Data
| Data Point | Confidence | Source |
| --- | --- | --- |
| Oil yield (0.40 t/t) | High | Midpoint of the reported crush range 0.36–0.44 [^2^][^3^][^7^], and independently reproduced by the seed-composition route (Section 4.1) |
| Meal yield (0.585 t/t) | Medium-High | Independently sourced from industry data [^3^][^7^]; not reconciled against the oil yield, giving the +0.42% DM surplus reported in Section 7.2 |
| Meal DM% (88%) | High | Industry trading specification (max 12% moisture) [^8^] |
| Oil DM% (100%) | High | Pure lipid with negligible moisture |
| Oil price ($1,300/t) | Medium-High | USDA ERS [^3^]; WASDE [^4^]; IndexMundi [^5^]. Quoted values cluster near $1,250–1,350/t, but the market is volatile |
| Meal price ($400/t) | Medium-High | USDA ERS [^3^]; Tridge [^9^]; Feedstuffs [^11^]. Quoted values cluster near $350–450/t |

### 9.2 Medium-Confidence Data
| Data Point | Confidence | Source |
| --- | --- | --- |
| Oil yield range (0.36–0.44) | Medium | The upper end (0.44) requires ~48.4% oil content on a DM basis, above the 45–47% recorded in CGC harvest surveys [^10^] |
| Meal yield range (0.55–0.62) | Medium | Wide range reflects variety and extraction method differences |
| Price ranges | Medium | Based on historical volatility; actual prices may exceed ranges during market shocks |
| Processing losses (1.5%) | Medium | Estimated from industry norms; not directly measured |

### 9.3 Known Limitations
- **Optimistic upper bound on oil yield:** The stated range runs to 0.44 t/t, which would require about 48.4% oil on a dry matter basis. CGC harvest surveys for No. 1 CW flaxseed record 45.6–46.7% [^10^], so 0.44 should be treated as an optimistic bound reachable only by high-oil seed with very efficient extraction, not as a typical value. The adopted 0.40 t/t is supported by both the reported crush range and the seed-composition route (Section 4.1).
- **Meal yield independently sourced:** The meal yield of 0.585 t/t is taken from industry data [^3^][^7^] rather than derived as a residual. The advantage is that neither co-product yield is a plug; the cost is that the two yields are not mutually reconciled, which is what produces the small dry-matter surplus reported in Section 7.2. Section 7.2 gives the residual-derived alternative and shows that the choice moves the allocation factors by less than half a percentage point.
- **No separate hulls co-product:** Unlike soybean crushing, flaxseed hulls are not typically separated as a distinct co-product. If a specific crushing facility does separate hulls, an additional co-product line would need to be added, and the allocation would change.
- **Expeller vs. solvent extraction:** This table represents solvent extraction, which yields more oil and less meal than mechanical expeller pressing. Expeller-pressed flaxseed typically yields about 0.30–0.33 t/t oil and 0.64–0.67 t/t meal, at a higher residual oil content in the meal (~6–8% vs. ~1% for solvent-extracted). Oil and meal are inversely related, so they cannot both be taken at the top of their ranges: any expeller pair must satisfy oil + meal ≤ 0.97–0.98 t/t to leave room for the 2–3% processing loss, and must also satisfy oil + 0.90 × meal ≤ 0.911 t on a dry matter basis. A pairing of 0.31 oil with 0.65 meal (0.96 t/t as-is, 0.895 t DM) satisfies both.
- **Regional price variation:** Linseed oil and meal prices vary significantly by region (European prices tend to be higher due to transportation costs and quality premiums for food-grade oil).
- **Industrial vs. food-grade oil:** Linseed oil has two distinct markets: industrial (coatings, linoleum, ~$1,000–1,300/t) and food/nutraceutical (cold-pressed, organic, ~$2,000–5,000/t). This table uses the industrial/crude oil price ($1,300/t). If food-grade oil is the intended product, the price and allocation would change dramatically.
- **Allocation sensitivity:** The economic allocation is very sensitive to the oil-to-meal price ratio. If oil prices drop from $1,300 to $1,000/t, oil's economic allocation drops from 69.0% to 63.1% (calculated: 0.40 × $1,000 = $400; 0.585 × $400 = $234; total = $634; oil alloc = $400 ÷ $634 = 63.1%). If meal prices rise from $400 to $500/t, oil's economic allocation drops from 69.0% to 64.0% (calculated: 0.40 × $1,300 = $520; 0.585 × $500 = $292.50; total = $812.50; oil alloc = $520 ÷ $812.50 = 64.0%).