# Peanut Processing: Co-Product Allocation Methodology, Data Sources, and Calculations
**Document Version:** 1.0
**Date:** June 2026
**Basis:** 1 metric ton (t) of in-shell peanuts at 10% moisture
**Price Period:** 2024–2025 average (unless otherwise noted)

## Table of Contents
- [1. Standard Basis and Conversions](#1-standard-basis-and-conversions)
- [2. Data Sources and References](#2-data-sources-and-references)
- [3. Process Description](#3-process-description)
- [4. Co-Product Yields and Properties](#4-co-product-yields-and-properties)
- [5. Prices](#5-prices)
- [6. Two-Stage Allocation](#6-two-stage-allocation)
- [7. Mass Balance Verification](#7-mass-balance-verification)
- [8. Complete Data Table](#8-complete-data-table)
- [9. Data Quality and Limitations](#9-data-quality-and-limitations)

## 1. Standard Basis and Conversions

### 1.1 Parent Input Definition
| Parameter | Value | Source |
| --- | --- | --- |
| Parent crop | In-shell peanuts / farmer-stock peanuts (*Arachis hypogaea*) | — |
| Input quantity | 1 metric ton (1,000 kg) | — |
| Moisture content | 10.0% | USDA FGIS standard for in-shell peanuts; maximum moisture for storage and marketing [^1^] |
| Dry matter (DM) input | 0.900 t DM/t in-shell peanuts | Calculated: 1.000 × (1 − 0.10) = 0.900 |
| Bushel equivalent | 27.56 bushels/t | 1,000 kg ÷ 36.288 kg/bu (80 lb at standard moisture) |
| Bushel weight | 80.0 lb (36.288 kg) | USDA standard bushel weight for in-shell peanuts (historically based on Virginia types). Note: Runner peanuts are smaller and typically test at 60–75 lb/bu, while Virginia types test closer to the 80 lb standard [^1^]. |
| Typical oil content | ~47% (dry matter basis, shelled kernels) | Industry average for runner-type peanuts [^2^] |

*Critical constraint on oil yield:* At 47% oil content (DM basis) and 92% DM for shelled kernels, the total oil present per tonne of kernels (as-is) is 0.47 × 0.920 = 0.4324 t. This is the absolute physical ceiling. Any oil yield claim exceeding 0.4324 t/t implies extraction efficiency >100%, which is physically impossible. At 95–98% solvent extraction recovery, the achievable range is 0.4108–0.4238 t/t at 47% oil content.

### 1.2 Convention for Adopted Values

Every yield, price, and DM% in this document is reported as an adopted point value together with the range it was drawn from. **Unless a row states otherwise, the adopted value is the midpoint of its stated range**, and the range is the parameter that carries the evidence. Two exceptions are stated where they appear: the oil yield is bounded by the physical oil content of the kernel (Sections 1.1 and 4.1), and the treatment of the intermediate product (shelled kernels) is set out in Section 6.1. Cumulative allocations are computed from unrounded stage values and rounded once, as described in Section 6.5.

### 1.3 Unit Conversions
| Conversion | Factor |
| --- | --- |
| 1 bushel in-shell peanuts | 80.0 lb ≈ 36.29 kg (at 10% moisture) |
| 1 lb | 0.453592 kg = 0.000453592 t |
| 1 t in-shell peanuts | ~27.6 bushels (at 80 lb/bu) |
| 1 short ton | 2,000 lb = 0.907185 metric ton |
| 1 metric ton | 2,204.62 lb = 1.10231 short tons |

*Note on peanut types:* Four main market types are grown in the US: Runner (~80% of production, medium kernel, used for peanut butter), Virginia (~15%, large kernel, used for in-shell roasting), Spanish (~4%, small kernel, high oil content), and Valencia (~1%, sweet flavor, three-plus kernels per pod). Runner peanuts are the reference type for this document. Oil content varies: Spanish (~48–52% oil), Runner (~44–50%), Virginia (~42–48%).

*Note on in-shell vs. shelled basis:* Peanut processing is inherently two-stage. The farmer delivers in-shell peanuts, which are first shelled to produce raw kernels, and the kernels are then crushed for oil extraction. **Yields in Stage 1 are per tonne of in-shell peanuts; yields in Stage 2 are per tonne of shelled kernels.** Every figure in this document states which basis it is on, and Section 7.1 shows why the distinction matters when combining stage losses.

## 2. Data Sources and References

### 2.1 Primary Sources
| Citation | Full Title | Type | URL |
| --- | --- | --- | --- |
| [^1^] | USDA AMS — United States Standards for Peanuts (formerly FGIS) | Government (USDA) | https://www.ams.usda.gov/ |
| [^2^] | USDA ERS (August 2025). *Peanut Outlook* | Government (USDA) | https://ers.usda.gov/ |
| [^3^] | USDA WASDE (February 2026). *World Agricultural Supply and Demand Estimates* | Government (USDA) | https://www.usda.gov/ |
| [^4^] | USDA ERS. *Oil Crops Yearbook: Peanut Section* | Government (USDA) | https://www.ers.usda.gov/data-products/oil-crops-yearbook/ |
| [^5^] | IndexMundi. *Peanut Oil Monthly Price* | Market Data | https://www.indexmundi.com/ |
| [^6^] | IndexBox (2025). *World Peanut Market Analysis* | Industry/Market | https://www.indexbox.io/ |
| [^7^] | American Peanut Council. *Processing and Products* | Industry Association | https://www.peanutsusa.com/ |
| [^8^] | USDA ARS National Peanut Research Laboratory. *Peanut Quality and Processing Research* | Government (USDA ARS) | https://www.ars.usda.gov/southeast-area/dawson-ga/national-peanut-research-laboratory/ |
| [^9^] | Feedipedia. *Peanut Meal* | Animal Feed Resources Information System (INRAE/CIRAD/FAO) | https://www.feedipedia.org/ |


### 2.2 How Sources Were Used
- **Yield data (shelling):** USDA ERS [^2^], USDA ERS Oil Crops Yearbook [^4^], and American Peanut Council [^7^] provided peanut shelling yield data. Kernel yields of 68–75% are standard for well-cleaned farmer-stock peanuts.
- **Yield data (crushing):** USDA ERS [^2^], USDA ERS Oil Crops Yearbook [^4^], and USDA ARS National Peanut Research Laboratory [^8^] provided peanut crushing yield data. Oil yield is constrained by the physical ceiling of oil content (see Section 1.1). Meal yield is independently established from industry data, not derived as a residual plug.
- **Hull fraction:** Industry data [^7^] indicates peanut hulls represent 20–26% of in-shell weight for runner-type peanuts.
- **Price data (oil):** USDA ERS [^2^], WASDE [^3^], and IndexMundi [^5^] provided peanut oil price data. Peanut oil is a premium cooking oil.
- **Price data (meal):** USDA ERS [^2^] and Feedipedia [^9^] provided peanut meal price data. Peanut meal at ~45% protein is a high-quality feed ingredient.
- **Price data (hulls):** Industry sources [^7^] provided peanut hull price data for loose bulk hulls. Hulls are a low-value byproduct.
- **DM contents:** Industry trading specifications for peanut meal (max 12% moisture = min 88% DM), peanut oil (negligible moisture = ~100% DM), and shelled kernels (8–10% moisture = 90–92% DM).

## 3. Process Description

Peanut processing involves two sequential stages: shelling followed by crushing (oil extraction). Both stages produce co-products, and the final allocation must assign the original in-shell peanuts' environmental burden across all three final co-products: peanut oil, peanut meal, and peanut hulls.

### 3.1 Stage 1: Shelling
Peanut shelling removes the hull (shell) from in-shell peanuts:
1. **Precleaning:** Foreign material (dirt, rocks, stems, vine material) is removed by screens and aspiration.
2. **Shelling:** In-shell peanuts pass through rotating drums or impact shellers that crack the hulls. The hulls are separated from the kernels by screens and air aspiration.
3. **Sizing:** Shelled kernels are separated by size through slotted screens. Oversized, medium, and undersized kernels are graded.
4. **Electronic sorting:** Discolored or damaged kernels are removed by optical sorters to meet food-grade standards.

**Stage 1 products:**
- **Shelled kernels** (intermediate product — input to Stage 2)
- **Peanut hulls** (final co-product)

*Note on shelling losses:* Peanut shelling generates 5–8% mass losses from foreign material removal, immature pods, damaged kernels, dust, and fines. These losses are higher than for cereal-grain hulling because farmer-stock peanuts carry more foreign material and a higher fraction of immature pods.

### 3.2 Stage 2: Crushing (Oil Extraction)
Peanut crushing converts shelled kernels into oil and meal:
1. **Cleaning:** Residual foreign material is removed.
2. **Conditioning:** Kernels are heated to ~60–80°C and adjusted to ~10–11% moisture to improve oil extractability.
3. **Flaking:** Kernels are rolled into thin flakes to rupture cell walls.
4. **Pre-pressing (expeller):** Flakes pass through a screw press that removes ~65–70% of the oil. This step produces expeller-pressed oil and a pressed cake with ~15–20% residual oil.
5. **Solvent extraction:** The pressed cake is extracted with hexane to remove the remaining oil. This step produces solvent-extracted oil and defatted meal.
6. **Desolventizing:** Hexane is removed from the meal by toasting.
7. **Oil refining:** Crude oil is degummed, neutralized, bleached, and deodorized.

**Stage 2 products:**
- **Peanut oil** (final co-product)
- **Peanut meal** (final co-product)

*Why solvent extraction is modelled here:* Full solvent extraction (expeller pre-press followed by solvent extraction) recovers 95–98% of the oil in peanut kernels, against roughly 65–75% for expeller-only pressing, and it is the standard method for commercial peanut crushing in the US. Expeller-only pressing is used for specialty and organic peanut oil but leaves 6–12% residual oil in the meal (typically 10–12% for standalone expellers); Section 9.3 gives the yields and prices for that configuration.

*Physical constraint on oil yield:* At 47% oil content (DM basis) and 92% DM for shelled kernels, the total extractable oil is limited to 0.4324 t per tonne of kernels (as-is) at 100% extraction. Solvent extraction at 95–98% recovery gives an achievable range of approximately 0.41–0.42 t/t at this oil content.

### 3.3 Overall Flow

    1 t in-shell peanuts at 10% moisture (0.900 t DM)
            │
            ▼
      ┌─ STAGE 1: SHELLING ─────────────────────────┐
      │                                               │
      │  Processing losses: ~0.047 t DM (5.2%)       │
      │  (FM, immature pods, dust, damaged kernels)   │
      │                                               │
      │  Peanut hulls: 0.23 t as-is (0.209 t DM)  ◄── final co-product
      │                                               │
      │  Shelled kernels: 0.70 t as-is (0.644 t DM)◄── intermediate
      │                                               │
      └───────────────┬───────────────────────────────┘
                      │ 0.70 t shelled kernels (0.644 t DM)
                      ▼
      ┌─ STAGE 2: CRUSHING (solvent extraction) ────┐
      │                                               │
      │  Processing losses: ~0.018 t DM (1.9% of      │
      │  in-shell input; 2.7% of kernels crushed)     │
      │  (handling, residual solvent, moisture loss)  │
      │                                               │
      │  Peanut oil: 0.42 t as-is (0.420 t DM)    ◄── final co-product
      │                                               │
      │  Peanut meal: 0.54 t as-is (0.475 t DM)   ◄── final co-product
      │                                               │
      └───────────────────────────────────────────────┘

    THREE FINAL CO-PRODUCTS from 1 t in-shell peanuts:
      Peanut oil:   0.294 t as-is,  0.294 t DM  (0.70 × 0.42)
      Peanut meal:  0.378 t as-is,  0.333 t DM  (0.70 × 0.54 × 0.88)
      Peanut hulls: 0.230 t as-is,  0.209 t DM
      Total:                      0.836 t DM  (from 0.900 t input; ~0.064 t losses)

## 4. Co-Product Yields and Properties

### 4.1 Yields (per tonne of in-shell peanuts and shelled kernels)
| Co-product | Stage | Yield basis | Yield (t/t) | Range | Source & Calculation |
| --- | --- | --- | --- | --- | --- |
| Shelled kernels | 1 (intermediate) | Per t in-shell peanuts | 0.70 | 0.68–0.72 | Industry standard shelling yield for runner peanuts [^4^][^7^]. Kernel yields of 68–75% are typical; the adopted 0.70 is the midpoint of the narrower range typical of well-cleaned farmer-stock peanuts. |
| Peanut hulls | 1 (final) | Per t in-shell peanuts | 0.23 | 0.20–0.26 | Industry standard [^4^][^7^]. Peanut hulls represent 20–26% of in-shell weight for runner varieties. |
| Peanut oil | 2 (final) | Per t shelled kernels | 0.42 | 0.39–0.45 | Physically constrained by oil content. At 47% oil (DM basis) and 92% DM: total oil = 0.4324 t/t. Solvent extraction at 96.5% recovery (midpoint of 95–98%) gives 0.417 t/t ≈ 0.42 t/t. Range spans 44% oil at 95% extraction (0.385) to 50% oil at 98% extraction (0.451), rounded to 0.39–0.45.. |
| Peanut meal | 2 (final) | Per t shelled kernels | 0.54 | 0.50–0.58 | Taken from industry data for solvent-extracted, dehulled meal at ~45% protein [^8^][^9^], **not** derived as the residual of the Stage 2 balance. Deriving it as a residual would not be improper, but sourcing it independently means the Stage 2 dry matter balance is a genuine check rather than an identity: the two yields are set separately and the 2.7% loss falls out of them. Reported meal yields run from 0.50 t/t (at higher oil recovery) to 0.58 t/t (at lower), and the adopted 0.54 is the midpoint. |

*Note on Stage 2 yield relationship:* Oil and meal yields are inversely related, as with all oilseeds. When more oil is extracted (higher oil yield), less meal is produced. The values in this table (0.42 oil, 0.54 meal) are independently established from physical constraints and industry data respectively, and are mutually consistent with the DM balance at ~2.7% processing losses.

**Total Recovery and Losses**
*Stage 1:* The as-is yields sum to 0.93 t/t in-shell peanuts (0.70 + 0.23), which is less than the 1.0 t input. The ~7% shortfall represents:
- Foreign material (FM): ~2–3% removed during precleaning (dirt, rocks, stems, vine material).
- Immature pods (pops): ~1–2% of in-shell weight are empty or immature pods that are separated during shelling.
- Damaged kernels: ~0.5–1% of kernels are damaged during shelling and removed by electronic sorting.
- Dust and fines: ~0.3–0.7% lost as dust during shelling and aspiration.

*Stage 2:* The as-is yields sum to 0.96 t/t shelled kernels (0.42 + 0.54), which is less than the 1.0 t input. The ~4% shortfall represents:
- Handling and spillage: ~0.5–1.0% lost during transport and transfer.
- Moisture loss: ~0.5–1.0% moisture evaporated during conditioning and toasting.
- Residual solvent in meal: Trace hexane (regulated to <500 ppm) adds negligible mass.
- Fines and dust: ~0.2–0.5% lost as fines during flaking and desolventizing.

### 4.2 Dry Matter Contents
| Co-product | DM (%) | Basis |
| --- | --- | --- |
| Shelled kernels (intermediate) | 92.0% | Raw shelled peanuts at 7–9% moisture [^8^]. Peanuts are dried to 8–10% moisture for storage; shelled edible peanuts are typically at 7–9%. The 92% DM value (8% moisture) is standard for shelled kernels entering the crusher. The adopted 92% DM corresponds to 8% moisture, the midpoint of that band. |
| Peanut oil | 100.0% | Crude and refined peanut oil are essentially pure lipid (triglycerides) with negligible moisture (<0.1%). |
| Peanut meal (solvent-extracted) | 88.0% | Standard trading specification: maximum 12% moisture = minimum 88% DM [^8^][^9^]. Solvent-extracted, toasted meal is typically delivered at 9–12% moisture. The 88% DM value represents the standard trading basis (conservative estimate using maximum moisture). |
| Peanut hulls | 91.0% | Peanut hulls at 7–11% moisture [^8^]. Hulls are drier than kernels due to their low hygroscopicity and high fiber content. The adopted 91% DM is the midpoint of the 89–93% band, corresponding to 9% moisture. |

### 4.3 DM Output per Tonne of In-Shell Peanuts
| Co-product | Calculation | DM Output (t/t in-shell peanuts) |
| --- | --- | --- |
| Shelled kernels (intermediate) | 0.70 × 0.92 | 0.644 |
| Peanut hulls | 0.23 × 0.91 | 0.209 |
| Stage 1 total | | 0.853 |
| Peanut oil | 0.70 × (0.42 × 1.00) | 0.294 |
| Peanut meal | 0.70 × (0.54 × 0.88) | 0.333 |
| Stage 2 total (from in-shell) | | 0.627 |
| All final co-products | 0.294 + 0.333 + 0.209 | 0.836 |

### 4.4 DM Output per Tonne of Shelled Kernels (Stage 2 internal basis)
| Co-product | Calculation | DM Output (t/t shelled kernels) |
| --- | --- | --- |
| Peanut oil | 0.42 × 1.00 | 0.420 |
| Peanut meal | 0.54 × 0.88 | 0.475 |
| Stage 2 total | | 0.895 |

## 5. Prices

### 5.1 Price Table
| Co-product | Price (USD/t) | Range | Source | Notes |
| --- | --- | --- | --- | --- |
| Shelled kernels (intermediate) | 800 | 600–1,000 | USDA ERS [^2^]; IndexBox [^6^] | Shelled runner peanuts for crushing. Farmer-stock peanuts: $350–500/t; shelling margin: $150–300/t. |
| Peanut oil | 1,600 | 1,400–1,800 | USDA ERS [^2^]; WASDE [^3^]; IndexMundi [^5^] | 2024–2025 average. Peanut oil is a premium cooking oil with high smoke point and distinctive flavor. Commands 1.5–2× the price of commodity vegetable oils. Range narrowed to match verification data. |
| Peanut meal | 250 | 200–300 | USDA ERS [^2^]; Feedipedia [^9^] | 2024–2025 average for solvent-extracted, 45% protein meal. Range narrowed to match verification data. Expeller-pressed meal with higher residual oil: $280–380/t. |
| Peanut hulls | 40 | 30–50 | American Peanut Council [^7^] | 2024–2025 average for loose bulk hulls (the primary co-product form from shelling). Pelleted hulls ($60–100/t) are a different product requiring additional processing. |

### 5.2 Price Verification
**Peanut oil:**
- USDA ERS (2025): ~$1,400-1,700/t (crude, FOB)
- IndexMundi (2025 avg): ~$1,500-1,650/t
- Specialty/expeller-pressed: $2,000-3,000/t
- Commodity vegetable oil baseline (soybean): ~$800-1,000/t
- *Adopted: $1,600/t, the midpoint of the stated range*

**Peanut meal:**
- USDA ERS (2025): ~$220-280/t (solvent-extracted, 45% protein)
- Feedipedia: indicative values $200-300/t (solvent-extracted meal)
- Expeller-pressed peanut meal: ~$280-380/t (higher residual oil)
- *Adopted: $250/t, the midpoint of the stated range*

**Peanut hulls:**
- American Peanut Council: ~$30-50/t (loose, bulk)
- Pelleted hulls: ~$60-100/t (different product — requires additional processing)
- Compost/mulch value: ~$20-40/t
- *Adopted: $40/t, the midpoint of the stated range (loose bulk hulls only)*

### 5.3 Revenue per Tonne of In-Shell Peanuts
| Co-product | Calculation | Revenue (USD/t in-shell peanuts) |
| --- | --- | --- |
| Peanut oil | 0.70 × 0.42 × 1,600 | $470.40 |
| Peanut meal | 0.70 × 0.54 × 250 | $94.50 |
| Peanut hulls | 0.23 × 40 | $9.20 |
| **Total** | | **$574.10** |

*Note:* Shelled kernels are not included in the final revenue calculation because they are an intermediate product, not a final co-product. The kernel's value is realized through its conversion into oil and meal. The kernel price ($800/t) is used only for Stage 1 economic allocation.

## 6. Two-Stage Allocation

### 6.1 Treatment of the Intermediate Product

Peanut processing has an intermediate — shelled kernels — that is sold between the two stages, so Stage 1 cannot be allocated without deciding what the kernels are worth. Two conventions are possible.

**Market-price cascade (used here).** Kernels are valued at the price they transact at between sheller and crusher ($800/t, Section 5.1). Stage 1 divides the in-shell peanut burden between kernels and hulls on that basis; Stage 2 divides the kernels' burden between oil and meal; the two stage allocations are then multiplied along each product's path.

**Derived valuation (not used here).** Kernels are instead valued at the total revenue of the products they become ($807/t of kernels).

These are not two options plus a third. **Valuing the intermediate at its derived value makes the cascade collapse algebraically to the direct end-of-chain calculation**, because the derived value cancels out of the multiplication:

```
Stage 1 kernel share x Stage 2 oil share
  = D / (D + hulls)  x  oil / D
  = oil / (D + hulls)
  = oil / (oil + meal + hulls)          <- the direct calculation
```

So the choice is between the market-price cascade and the direct end-of-chain calculation, and Section 6.6 reports the direct result. For peanuts the two agree to within 0.01 percentage point, because the kernel market price ($800/t) is within one percent of the kernels' derived value ($807/t).

**Why the market-price cascade is used for peanuts:**

1. **Shelled kernels are not a final co-product in this work.** Within this system they exist only as the input to crushing. The three co-products this document reports are peanut oil, peanut meal and peanut hulls.
2. **The $800/t price is specifically the transfer price into crushing.** This matters more for peanuts than for most crops, because shelled kernels have a much larger competing market: only about 15–20% of US shelled peanuts are crushed, with most going to food uses at $900–1,400/t (Section 9.3). The $800/t adopted here is the **crushing-grade** price — the price of the stream that actually enters Stage 2 — not the edible-grade price. Using the food-market price would value the kernels at a use they did not enter.
3. **It keeps the split of the in-shell burden independent of downstream value-add.** The Stage 1 split is held to the transaction that occurs at shelling.

**Where this convention does not apply.** A different treatment is warranted where the intermediate is itself a marketed final co-product of the system being studied — that is, where the study needs allocation factors for both the intermediate and the products it becomes, because both are genuine outputs. In that case the intermediate's quoted price is the price in a competing end use rather than a transfer price into the next stage, and the direct end-of-chain treatment is used so that all final products sit on one denominator. That situation does not arise here: edible shelled peanuts leave the system as a final food product and are outside the scope of this table, which models the crushing pathway.

### 6.2 Allocation Approach
Because peanut processing has two sequential stages, the allocation is performed in two steps:
1. **Stage 1 (Shelling):** Allocate in-shell peanuts' burden between shelled kernels and peanut hulls.
2. **Stage 2 (Crushing):** Allocate shelled kernels' burden between peanut oil and peanut meal.

The final allocation for each co-product is the product of the stage allocations along its path through the system:
- Peanut oil: Stage 1 kernel alloc × Stage 2 oil alloc
- Peanut meal: Stage 1 kernel alloc × Stage 2 meal alloc
- Peanut hulls: Stage 1 hulls alloc (no Stage 2)

### 6.3 Stage 1: Shelling Allocation
**Mass allocation:**
| Co-product | DM Output | Calculation | Stage 1 Allocation |
| --- | --- | --- | --- |
| Shelled kernels | 0.644 t | (0.644 ÷ 0.853) × 100 | 75.5% |
| Peanut hulls | 0.209 t | (0.209 ÷ 0.853) × 100 | 24.5% |

**Economic allocation:**
| Co-product | Revenue | Calculation | Stage 1 Allocation |
| --- | --- | --- | --- |
| Shelled kernels | $560.00 | (560.00 ÷ 569.20) × 100 | 98.4% |
| Peanut hulls | $9.20 | (9.20 ÷ 569.20) × 100 | 1.6% |

*Stage 1 revenue:* Shelled kernels: 0.70 × $800 = $560.00; Peanut hulls: 0.23 × $40 = $9.20; Total: $569.20.

### 6.4 Stage 2: Crushing Allocation
**Mass allocation:**
| Co-product | DM Output (per t shelled kernels) | Calculation | Stage 2 Allocation |
| --- | --- | --- | --- |
| Peanut oil | 0.420 t | (0.420 ÷ 0.895) × 100 | 46.9% |
| Peanut meal | 0.475 t | (0.475 ÷ 0.895) × 100 | 53.1% |

**Economic allocation:**
| Co-product | Revenue (per t shelled kernels) | Calculation | Stage 2 Allocation |
| --- | --- | --- | --- |
| Peanut oil | $672.00 | (672.00 ÷ 807.00) × 100 | 83.3% |
| Peanut meal | $135.00 | (135.00 ÷ 807.00) × 100 | 16.7% |

*Stage 2 revenue:* Peanut oil: 0.42 × $1,600 = $672.00; Peanut meal: 0.54 × $250 = $135.00; Total: $807.00.

### 6.5 Final Cumulative Allocation
The final allocation of in-shell peanuts' environmental burden to each of the three final co-products is calculated by cascading the two stages:

**Mass allocation (cumulative):**
| Co-product | Calculation | Final Allocation |
| --- | --- | --- |
| Peanut oil | 75.498% × 46.927% | 35.4% |
| Peanut meal | 75.498% × 53.073% | 40.1% |
| Peanut hulls | 24.502% (Stage 1 only) | 24.5% |
| **Total** | | **100.0%** |

**Economic allocation (cumulative):**
| Co-product | Calculation | Final Allocation |
| --- | --- | --- |
| Peanut oil | 98.384% × 83.271% | 81.9% |
| Peanut meal | 98.384% × 16.729% | 16.5% |
| Peanut hulls | 1.616% (Stage 1 only) | 1.6% |
| **Total** | | **100.0%** |

> **Rounding note:** Cumulative values are computed from the **unrounded** stage allocations, not from the one-decimal figures shown in Sections 6.3 and 6.4. Multiplying rounded percentages shifts the result: 98.4% × 83.3% gives 81.97%, whereas the unrounded product is 81.93%. The unrounded cumulative values are 81.925%, 16.458% and 1.616%, which sum to exactly 100% and round to 81.9%, 16.5% and 1.6%.

### 6.6 Verification: Direct Calculation
The cumulative allocation can be verified by calculating directly from the three final co-products' DM and revenue values per tonne of in-shell peanuts, bypassing the intermediate shelled kernels stage:

**Direct mass allocation:**
| Co-product | DM Output (t/t in-shell) | Calculation | Final Allocation |
| --- | --- | --- | --- |
| Peanut oil | 0.294 | (0.294 ÷ 0.836) × 100 | 35.2% |
| Peanut meal | 0.333 | (0.333 ÷ 0.836) × 100 | 39.8% |
| Peanut hulls | 0.209 | (0.209 ÷ 0.836) × 100 | 25.0% |
| **Total** | 0.836 | | **100.0%** |

**Direct economic allocation:**
| Co-product | Revenue (USD/t in-shell) | Calculation | Final Allocation |
| --- | --- | --- | --- |
| Peanut oil | $470.40 | (470.40 ÷ 574.10) × 100 | 81.9% |
| Peanut meal | $94.50 | (94.50 ÷ 574.10) × 100 | 16.5% |
| Peanut hulls | $9.20 | (9.20 ÷ 574.10) × 100 | 1.6% |
| **Total** | $574.10 | | **100.0%** |

### 6.7 Reconciliation: Cascade vs. Direct
The cascade and direct methods give similar results:
| Co-product | Mass (cascade) | Mass (direct) | Econ (cascade) | Econ (direct) |
| --- | --- | --- | --- | --- |
| Peanut oil | 35.4% | 35.2% | 81.9% | 81.9% |
| Peanut meal | 40.1% | 39.8% | 16.5% | 16.5% |
| Peanut hulls | 24.5% | 25.0% | 1.6% | 1.6% |

*Why the differences are small:* The shelled kernel price ($800/t) is close to the weighted average of its products ($807/t of kernels: 0.42 × $1,600 + 0.54 × $250 = $672 + $135 = $807), so the cascade and direct methods converge.

*Which method to use:* 
- The **cascade method** applies allocation at each unit process separately, which is appropriate when the intermediate crosses a system boundary and is independently traded, as shelled kernels are. Note that ISO 14044 requires allocation to be applied at each unit process; it does not define or mandate a "cascade", which is a practitioner's term and should not be confused with ISO's stepwise allocation *hierarchy* (avoid → physical → economic).
- The **direct calculation** uses a single end-of-chain denominator. It is simpler, but it collapses the two-stage structure and lets value added in Stage 2 govern the Stage 1 split.
- Both are reported. The **cascade is the primary allocation** for this document, for the reasons in Section 6.1. For peanuts the two agree to within 0.01 pp, so the choice does not affect the published factors.

### 6.8 Recommended Final Allocation
| Co-product | Mass Allocation | Economic Allocation |
| --- | --- | --- |
| Peanut oil | 35.4% | 81.9% |
| Peanut meal | 40.1% | 16.5% |
| Peanut hulls | 24.5% | 1.6% |
| **Total** | **100.0%** | **100.0%** |

## 7. Mass Balance Verification

### 7.1 Overall DM Balance
| Item | Value | Notes |
| --- | --- | --- |
| Input DM (1 t in-shell peanuts at 10% moisture) | 0.900 t | 1.000 × (1 − 0.10) |
| Output DM — final co-products: | | |
| Peanut oil | 0.294 t | 0.70 × 0.42 × 100% DM |
| Peanut meal | 0.333 t | 0.70 × 0.54 × 88% DM |
| Peanut hulls | 0.209 t | 0.23 × 91% DM |
| Total co-product DM | 0.836 t | |
| DM balance gap | −0.064 t | 7.1% of input DM |

*Balance assessment:* The DM output is 0.064 t (7.1%) below the DM input, and the two stages contribute unequally. Shelling loses 0.047 t DM — **5.2% of the in-shell input** — which is high for a hulling step because farmer-stock peanuts carry foreign material, immature pods and damaged kernels. Crushing loses 0.025 t DM per tonne of shelled kernels, but only 0.70 t of kernels is produced per tonne of in-shell peanuts, so on the in-shell basis that is 0.0175 t, or **1.9% of the input DM**. The two add to 0.064 t, or 7.1%. Care is needed with the basis: the crushing loss is 2.7% of kernels but 1.9% of in-shell peanuts, and only the latter is additive with the shelling loss.

### 7.2 Stage-by-Stage Balance
**Stage 1: Shelling**
| Item | Value | Notes |
| --- | --- | --- |
| Input DM | 0.900 t | 1 t in-shell peanuts at 10% moisture |
| Shelled kernels DM | 0.644 t | 0.70 t × 92% DM |
| Hulls DM | 0.209 t | 0.23 t × 91% DM |
| Total accounted | 0.853 t | |
| Stage 1 losses | 0.047 t | 5.2% of input; FM, immature pods, damaged kernels, dust |

**Stage 2: Crushing**
| Item | Value | Notes |
| --- | --- | --- |
| Input DM (shelled kernels) | 0.920 t | 1 t shelled kernels at 92% DM |
| Peanut oil DM | 0.420 t | 0.42 t × 100% DM |
| Peanut meal DM | 0.475 t | 0.54 t × 88% DM |
| Total accounted | 0.895 t | |
| Stage 2 losses | 0.025 t | 2.7% of input; handling, residual solvent, moisture loss |

### 7.3 As-Is Mass Balance
| Item | Value | Notes |
| --- | --- | --- |
| Input (in-shell peanuts) | 1.000 t | — |
| Output: | | |
| Peanut oil | 0.294 t | 0.70 × 0.42 |
| Peanut meal | 0.378 t | 0.70 × 0.54 |
| Peanut hulls | 0.230 t | — |
| Total output | 0.902 t | |
| Processing losses | 0.098 t | 9.8%: FM, immature pods, dust, handling, moisture loss — the residual of the balance, not an independent measurement |
| **Balance** | **1.000 t** | Closes by construction, since the loss term is the residual |

## 8. Complete Data Table

### 8.1 Final Co-Product Allocation (per 1 t in-shell peanuts at 10% moisture)
| Parent Crop | Crop System | Stage | USDA Standard | Standard Moisture | Parent Input Basis | Co-product Stream | Yield (t/t in-shell) | Yield Range | Price (USD/t) | Price Range | DM (%) | DM Output (t/t in-shell) | Revenue (USD/t in-shell) | Econ Alloc — Cascade (%) | Econ Alloc — Direct (%) | Mass Alloc — Cascade (%) | Mass Alloc — Direct (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Peanut | Peanut shelling/crushing | 2 | 80 lb/bu min test weight (runner) | 10% | 1 t in-shell peanuts at 10% moisture | Peanut oil | 0.294 | 0.27–0.32 | 1,600 | 1,400–1,800 | 100.0 | 0.294 | 470.40 | 81.9 | 81.9 | 35.4 | 35.2 |
| Peanut | Peanut shelling/crushing | 2 | 80 lb/bu min test weight (runner) | 10% | 1 t in-shell peanuts at 10% moisture | Peanut meal | 0.378 | 0.35–0.40 | 250 | 200–300 | 88.0 | 0.333 | 94.50 | 16.5 | 16.5 | 40.1 | 39.8 |
| Peanut | Peanut shelling/crushing | 2 | 80 lb/bu min test weight (runner) | 10% | 1 t in-shell peanuts at 10% moisture | Peanut hulls | 0.230 | 0.20–0.26 | 40 | 30–50 | 91.0 | 0.209 | 9.20 | 1.6 | 1.6 | 24.5 | 25.0 |

### 8.2 Intermediate Product (for cascade calculation reference only)
| Parent Crop | Crop System | Stage | USDA Standard | Standard Moisture | Parent Input Basis | Co-product Stream | Yield (t/t in-shell) | Yield Range | Price (USD/t) | Price Range | DM (%) | DM Output (t/t in-shell) | Revenue (USD/t in-shell) | Stage 1 Econ Alloc (%) | Stage 1 Mass Alloc (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Peanut | Peanut shelling | 1 | 80 lb/bu min test weight (runner) | 10% | 1 t in-shell peanuts at 10% moisture | Shelled kernels (intermediate) | 0.70 | 0.68–0.72 | 800 | 600–1,000 | 92.0 | 0.644 | 560.00 | 98.4 | 75.5 |

### 8.3 Stage 2 Internal Basis (per 1 t shelled kernels)
| Parent Crop | Crop System | Stage | USDA Standard | Standard Moisture | Parent Input Basis | Co-product Stream | Yield (t/t kernels) | Yield Range | Price (USD/t) | Price Range | DM (%) | DM Output (t/t kernels) | Revenue (USD/t kernels) | Stage 2 Econ Alloc (%) | Stage 2 Mass Alloc (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Peanut | Peanut crushing | 2 | — | 8% | 1 t shelled kernels at 92% DM | Peanut oil | 0.42 | 0.39–0.45 | 1,600 | 1,400–1,800 | 100.0 | 0.420 | 672.00 | 83.3 | 46.9 |
| Peanut | Peanut crushing | 2 | — | 8% | 1 t shelled kernels at 92% DM | Peanut meal | 0.54 | 0.50–0.58 | 250 | 200–300 | 88.0 | 0.475 | 135.00 | 16.7 | 53.1 |

## 9. Data Quality and Limitations

### 9.1 High-Confidence Data
| Data Point | Confidence | Source |
| --- | --- | --- |
| Kernel yield (0.70 t/t in-shell) | High | Industry standard for runner peanuts [^4^][^7^] |
| Hull fraction (~23% of in-shell) | High | Well-characterized at 20–26% [^7^] |
| Peanut oil DM% (100%) | High | Pure lipid with negligible moisture |
| Peanut meal DM% (88%) | High | Industry trading specification (max 12% moisture) |
| Oil price ($1,600/t) | Medium-High | USDA ERS [^2^] ~$1,400–1,700/t; IndexMundi [^5^] ~$1,500–1,650/t |
| Oil yield (0.42 t/t) | Medium-High | Physically constrained by oil content; matches extraction calculation at 47% oil / 96.5% recovery |

### 9.2 Medium-Confidence Data
| Data Point | Confidence | Source |
| --- | --- | --- |
| Meal yield (0.54 t/t kernels) | Medium | Independently established from industry data for solvent-extracted 45% protein meal [^8^][^9^]. Inversely related to oil yield. |
| Shelled kernels price ($800/t) | Medium | Peanut prices are volatile and depend heavily on quota/allocation system, crop quality, and aflatoxin levels. |
| Meal price ($250/t) | Medium | Peanut meal market is smaller than soybean meal; limited price transparency. |
| Hull price ($40/t) | Medium | Limited market data for loose bulk hulls; hulls are often consumed on-site or disposed of. Pelleted hulls command higher prices but are a different product. |

### 9.3 Known Limitations
- **Expeller vs. solvent extraction:** This document uses solvent extraction as the primary method (consistent with "highest standard"). An alternative expeller-only configuration would produce: Oil ~0.33 t/t kernels (range 0.28–0.35), Expeller cake/meal ~0.58 t/t at ~88% DM with 6–12% residual oil, priced at ~$200–300/t. The expeller-only meal has higher residual oil and thus higher energy value but lower protein concentration (~38–42% vs. 45% for solvent-extracted). The allocation would shift significantly: economic allocation to oil would decrease (lower oil yield, higher meal price per t).
- **Peanut variety variation:** Runner peanuts (~80% of US production) are the reference type. Spanish peanuts have higher oil content (~48–52%) and would yield more oil per t of kernels. Virginia peanuts have larger kernels and slightly lower oil content (~42–48%). The yield ranges should capture this variability.
- **Aflatoxin concerns:** Peanuts are susceptible to aflatoxin contamination (*Aspergillus flavus*), which can result in rejection of entire lots. Aflatoxin-contaminated peanuts are diverted to oil crushing (aflatoxin is not oil-soluble and remains in the meal). This can affect the effective kernel price and the proportion of kernels going to food vs. crushing.
- **Edible vs. crushing grade:** Not all shelled peanuts go to crushing. In the US, ~55–60% of shelled peanuts go to food uses (peanut butter, snacks, confections) and only ~15–20% are crushed for oil. The remaining ~20–25% are used for seed and other purposes. The price of shelled kernels for crushing ($600–1,000/t) is lower than for edible use ($900–1,400/t). The $800/t intermediate price reflects the crushing-grade market.
- **Hull value variability:** Peanut hulls have limited markets. Many shelling plants burn hulls on-site for energy or give them away for compost. If hulls are assigned zero revenue (waste), the economic allocation shifts to: Oil 83.3%, Meal 16.7%. This is a 1.3 pp increase for oil relative to the $40/t hull price scenario.
- **Economic allocation sensitivity:** Peanut oil's high price ($1,600/t) and meal's moderate price ($250/t) mean the economic allocation is dominated by oil (81.9%). If oil drops to $1,400/t, oil's economic allocation drops to ~80%. If meal price rises to $300/t, oil's economic allocation drops to ~79%.
- **Moisture variation:** In-shell peanuts are typically dried to 8–10% moisture for storage. At 8% moisture (DM = 0.920), the DM input is higher, and the mass allocation proportions shift slightly (more DM to allocate). The 10% standard is used for consistency with USDA marketing standards.