# Rice Milling: Co-Product Allocation Methodology, Data Sources, and Calculations

**Document Version:** 1.0 
**Date:** June 2026  
**Basis:** 1 metric ton (t) of rough rice (paddy) at 13% moisture  
**Price Period:** 2024–2025 average (unless otherwise noted)

---

## Table of Contents

1. [Standard Basis and Conversions](#1-standard-basis-and-conversions)
2. [Data Sources and References](#2-data-sources-and-references)
3. [Process Description](#3-process-description)
4. [Co-Product Yields and Properties](#4-co-product-yields-and-properties)
5. [Prices](#5-prices)
6. [Two-Stage Allocation](#6-two-stage-allocation)
7. [Mass Balance Verification](#7-mass-balance-verification)
8. [Complete Data Table](#8-complete-data-table)
9. [Data Quality and Limitations](#9-data-quality-and-limitations)

---

## 1. Standard Basis and Conversions

### 1.1 Parent Input Definition

| Parameter | Value | Source |
|-----------|-------|--------|
| **Parent crop** | Rough rice / paddy rice (*Oryza sativa*) | — |
| **Input quantity** | 1 metric ton (1,000 kg) | — |
| **Moisture content** | 13.0% | Typical trade/storage moisture target for long-grain rough rice [^1^]. Note: moisture is not a USDA FGIS grade-determining factor for rough rice; 13% is the industry standard target for safe storage and milling. |
| **Dry matter (DM) input** | 0.870 t DM/t rough rice | Calculated: 1.000 × (1 − 0.13) = 0.870 |
| **Bushel equivalent** | 49.0 bushels/t | 1,000 kg ÷ 20.412 kg/bu (45 lb/bu at standard test weight) |
| **Cwt equivalent** | 22.05 cwt/t | 1,000 kg ÷ 45.359 kg/cwt (100 lb/cwt) |
| **Bushel weight** | 45.0 lb (20.412 kg) | USDA standard test weight for rough rice (No. 1 minimum: 45 lb/bu for long grain) [^1^] |
| **Typical whole-grain yield** | ~45–60% (head rice, as-is from rough rice) | Industry average for well-milled long-grain rice [^2^]. Pure head rice yield (HRY) is 45–60% for long-grain; total milled rice yield (MRY, including brokens) is 65–72%. |

### 1.2 Convention for Adopted Values

Every yield, price, and DM% in this document is reported as an adopted point value together with the range it was drawn from. **Unless a row states otherwise, the adopted value is the midpoint of its stated range**, and the range is the parameter that carries the evidence. Because rice milling is a two-stage system, the treatment of the intermediate product (brown rice) also has to be stated explicitly; Section 6.1 does that and sets out the alternative. Cumulative allocations are computed from unrounded stage values and then rounded once, as described in Section 6.5.

### 1.3 Unit Conversions

| Conversion | Factor |
|------------|--------|
| 1 bushel rough rice | 45.0 lb ≈ 20.41 kg (at 13% moisture, long grain) |
| 1 cwt rough rice | 100 lb ≈ 45.36 kg |
| 1 lb | 0.453592 kg = 0.000453592 t |
| 1 t rough rice | ~49.0 bushels (at 45 lb/bu) |
| 1 t rough rice | ~22.05 cwt (at 100 lb/cwt) |
| 1 short ton | 2,000 lb = 0.907185 metric ton |
| 1 metric ton | 2,204.62 lb = 1.10231 short tons |

> **Note on rice types:** Three main grain types are grown in the US: **long-grain** (slender kernel, ~65% of US production, typically Southern states), **medium-grain** (shorter and wider, ~30%, California and Southern), and **short-grain** (round kernel, ~5%, California). Milling yields vary by type: long-grain typically yields 45–60% head rice, medium-grain 55–68%, and short-grain 58–72%. Total milled rice yield (including brokens) is higher: long-grain 65–70%, medium-grain 68–72%, short-grain 70–74%. This document uses long-grain as the reference type, consistent with the largest US production share.

> **Note on rough rice moisture:** The 13% moisture used here is the typical trade and storage moisture target for long-grain rough rice, not a USDA FGIS grade standard. USDA FGIS rough rice grading standards (7 CFR Part 868 Subpart C) do not specify moisture as a grade-determining factor; moisture is measured and reported on certificates but is not one of the grade requirements. Medium- and short-grain rough rice is typically dried to ~14% moisture for storage. Rough rice is typically harvested at 18–22% moisture and dried to the target moisture for storage and milling.

---

## 2. Data Sources and References

### 2.1 Primary Sources

| Citation | Full Title | Type | URL |
|----------|-----------|------|-----|
| [^1^] | USDA AMS — United States Standards for Rice (formerly FGIS) | Government (USDA) | https://www.ams.usda.gov/grades-standards/rough-rice |
| [^2^] | USDA ERS (August 2025). *Rice Yearbook* | Government (USDA) | https://ers.usda.gov/ |
| [^3^] | USDA WASDE (February 2026). *World Agricultural Supply and Demand Estimates* | Government (USDA) | https://www.usda.gov/ |
| [^4^] | FAO (1999). *RICE: Post-harvest Operations* (INPhO Post-Harvest Compendium) | International Organization | https://www.fao.org/fileadmin/user_upload/inpho/docs/Post_Harvest_Compendium_-_RICE.pdf |
| [^5^] | IndexMundi. *Rice Monthly Price — US Dollars per Metric Ton* | Market Data | https://www.indexmundi.com/commodities/?commodity=rice |
| [^6^] | IndexBox (2024). *World - Rice - Market Analysis, Forecast, Size, Trends and Insights* | Industry/Market | https://www.indexbox.io/ |
| [^7^] | USA Rice. *Understanding Rice Varieties, Types, and Forms* | Industry Association | https://www.usarice.com/ |
| [^8^] | Champagne (2004). *Rice: Chemistry and Technology*, 3rd ed. | Academic | https://www.cerealsgrains.org/ |
| [^9^] | Tridge. *Rice Bran Price in United States* | Industry/Market | https://dir.tridge.com/prices/rice-bran/US |
| [^10^] | OECD-FAO (2025). *OECD-FAO Agricultural Outlook 2025-2034*, Chapter 2: Cereals | International Organization | https://www.oecd.org/ |

### 2.2 How Sources Were Used

- **Yield data:** USDA ERS [^2^], FAO [^4^], and USA Rice [^7^] provided rice milling yield data. The ranges reflect variation across grain types, milling precision, and equipment.
- **Hull fraction:** Industry data [^7^][^8^] indicates rice hulls represent 18–22% of rough rice weight. The 0.20 t/t midpoint is the industry standard for long-grain rice.
- **Price data (white rice):** USDA ERS [^2^], WASDE [^3^], and IndexMundi [^5^] provided milled rice price data.
- **Price data (bran):** USDA ERS [^2^], Tridge [^9^], and IndexBox [^6^] provided rice bran price data. Stabilized rice bran commands a significant premium over raw bran.
- **Price data (hulls):** Industry estimates provided rice hull price data. Hulls are a low-value byproduct used as animal feed, mulch, or industrial filler. Market data is limited.
- **Price data (mill feed):** USDA ERS [^2^] and industry estimates provided rice mill feed (brokens + fines) price data.
- **DM contents:** Commercial trading specifications for white rice (typically 12% moisture = 88% DM), rice bran (10–12% moisture), rice hulls (8–12% moisture), and rice mill feed (10–12% moisture).
- **Production and trade outlook:** OECD-FAO [^10^] provides global cereal market projections, contextualizing the methodology within broader market trends.

---

## 3. Process Description

Rice milling involves two sequential stages: **hulling** followed by **milling/whitening**. Both stages produce co-products, and the final allocation must assign the original rough rice's environmental burden across all four final co-products: **white rice, rice bran, rice hulls, and rice mill feed**.

### 3.1 Stage 1: Hulling

Rice hulling (also called "shelling") removes the outer husk from rough rice:

1. **Cleaning:** Foreign material (dirt, straw, weed seeds) is removed.
2. **Hulling:** Rough rice passes through rubber-roll or stone hullers that crack and remove the hulls. The hulls are separated by aspiration.
3. **Paddy separation:** Any remaining unhulled rough rice (paddy) is separated from brown rice using gravity or oscillating paddy separators and recycled through the huller.

**Stage 1 products:**
- **Brown rice** (intermediate product — input to Stage 2)
- **Rice hulls** (final co-product)

### 3.2 Stage 2: Milling / Whitening

Rice milling converts brown rice into white rice by removing the bran layer:

1. **Whitening:** Brown rice passes through abrasive or friction whiteners that remove the bran layer (pericarp, germ, and some sub-aleurone).
2. **Polishing (optional):** A gentle polishing step removes residual bran particles and produces a glossy finish.
3. **Sizing/grading:** Milled rice is separated into whole kernels (head rice), large brokens, and small brokens/fines by sieve graders.
4. **Color sorting (optional):** Discolored kernels are removed by optical sorters.

**Stage 2 products:**
- **White rice** (head rice + large brokens — final co-product)
- **Rice bran** (final co-product)
- **Rice mill feed** (small brokens + fines — final co-product)

### 3.3 Overall Flow

```
1 t rough rice at 13% moisture (0.870 t DM)
        │
        ▼
  ┌─ STAGE 1: HULLING ──────────────────────────┐
  │                                               │
  │  Processing losses: ~0.002 t DM (0.23%)      │
  │  (dust, fines, incomplete dehulling)          │
  │                                               │
  │  Rice hulls: 0.20 t as-is (0.180 t DM)    ◄── final co-product
  │                                               │
  │  Brown rice: 0.80 t as-is (0.688 t DM)    ◄── intermediate
  │                                               │
  └───────────────┬───────────────────────────────┘
                  │ 0.80 t brown rice (0.688 t DM)
                  ▼
  ┌─ STAGE 2: MILLING / WHITENING ──────────────┐
  │                                               │
  │  Processing losses: ~0.0003 t DM (0.04%)     │
  │  (polishing dust, residual bran)              │
  │                                               │
  │  White rice: 0.65 t as-is (0.572 t DM)    ◄── final co-product
  │                                               │
  │  Rice bran: 0.08 t as-is (0.071 t DM)     ◄── final co-product
  │                                               │
  │  Rice mill feed: 0.05 t as-is (0.045 t DM)◄── final co-product
  │                                               │
  └───────────────────────────────────────────────┘

FOUR FINAL CO-PRODUCTS from 1 t rough rice:
  White rice:     0.65 t as-is,  0.572 t DM
  Rice bran:      0.08 t as-is,  0.071 t DM
  Rice hulls:     0.20 t as-is,  0.180 t DM
  Rice mill feed: 0.05 t as-is,  0.045 t DM
  Total:                        0.868 t DM  (from 0.870 t input; ~0.002 t losses)
```

---

## 4. Co-Product Yields and Properties

### 4.1 Yields (per tonne of rough rice input)

| Co-product | Stage | Yield (t/t rough rice) | Range | Source & Calculation |
|------------|-------|----------------------|-------|---------------------|
| **Brown rice** | 1 (intermediate) | 0.80 | 0.78–0.82 | Industry standard hulling yield [^4^][^7^]. Rough rice yields ~78–82% brown rice after hull removal. The 0.80 midpoint represents long-grain rice. |
| **Rice hulls** | 1 (final) | 0.20 | 0.18–0.22 | Industry standard [^4^][^8^]. Hulls represent 18–22% of rough rice weight for long-grain varieties. The adopted 0.20 is the midpoint of the stated range. |
| **White rice (head rice + large brokens)** | 2 (final) | 0.65 | 0.58–0.72 | Industry standard for well-milled long-grain rice [^2^][^7^]. This yield includes head rice plus large brokens graded as whole-kernel equivalent. Pure head rice yield (HRY, whole kernels only) from rough rice is 45–60% for long-grain; total milled rice yield (MRY, including all brokens) is 65–72%. The 0.65 value represents the common industry practice of combining head rice with large brokens. |
| **Rice bran** | 2 (final) | 0.08 | 0.06–0.10 | Industry standard [^4^][^8^]. Bran represents 6–10% of rough rice weight (including polish and germ fractions; bran alone without polish is 6–8%). IRRI and academic sources consistently report ~8% for well-milled rice. The adopted 0.08 is the midpoint of the stated range. |
| **Rice mill feed (brokens + fines)** | 2 (final) | 0.05 | 0.03–0.07 | Industry standard [^7^]. Mill feed includes small brokens, brewer's rice, and fines. The adopted 0.05 is the midpoint of the stated range. Note: "mill feed" here excludes bran and hulls. |

> **Note on yield relationships:** The Stage 2 yields from brown rice are white rice 0.65/0.80 = 81.25%, bran 0.08/0.80 = 10.0% and mill feed 0.05/0.80 = 6.25%, summing to 97.5% — an apparent 2.5% milling loss on an as-is basis. Almost all of that is water, not dry matter. Brown rice enters at 14% moisture and the three products leave at 11–12%, so of the 0.020 t as-is loss, **0.0197 t is water and only 0.0003 t is dry matter** (0.04% of the brown rice DM, Section 7.2). The as-is and dry matter views of Stage 2 look very different for that reason and are not in conflict.

#### Total Recovery and Losses

The as-is yields sum to 0.98 t/t rough rice (0.65 + 0.08 + 0.20 + 0.05), which is less than the 1.0 t input. The ~2% shortfall represents real processing losses:

1. **Stage 1 losses (~0%):** Hulling is a mechanical separation with minimal mass loss. Some dust and fines are generated but are minor (<0.5%).
2. **Stage 2 losses (~2%):** Milling and polishing generate fine bran dust, residual material in the whitener, and minor moisture loss during polishing.

### 4.2 Dry Matter Contents

| Co-product | DM (%) | Basis |
|------------|--------|-------|
| Brown rice (intermediate) | 86.0% | Brown rice at 14% moisture [^8^], typical for brown rice entering the whitener. This is slightly wetter than the rough rice it came from (13%), which is correct rather than anomalous: hulls are the driest fraction of the grain, so removing them concentrates the remaining water in the kernel. The water balance confirms it — see the check below the DM output table in Section 4.3. |
| White rice (head rice + large brokens) | 88.0% | Commercial standard for milled rice: typically 12% moisture = 88% DM. USDA sample grade threshold is 15% moisture; well-milled rice is typically traded at 11–13% moisture [^1^]. |
| Rice bran | 89.0% | Rice bran typically at 10–12% moisture [^8^]. Stabilized rice bran (heat-treated) is at 10–11% moisture. |
| Rice hulls | 90.0% | Rice hulls at 8–12% moisture [^8^]. Hulls are the driest fraction; their high silica content limits moisture absorption. |
| Rice mill feed (brokens + fines) | 89.0% | Similar to milled rice, at 10–12% moisture. Broken kernels have the same composition as whole kernels. |

### 4.3 DM Output per Tonne of Rough Rice

| Co-product | Calculation | DM Output (t/t rough rice) |
|------------|-------------|--------------------------|
| **Brown rice** (intermediate) | 0.80 × 0.86 | **0.6880** |
| **Rice hulls** | 0.20 × 0.90 | **0.1800** |
| Stage 1 total | | **0.8680** |
| **White rice** | 0.65 × 0.88 | **0.5720** |
| **Rice bran** | 0.08 × 0.89 | **0.0712** |
| **Rice mill feed** | 0.05 × 0.89 | **0.0445** |
| Stage 2 total | | **0.6877** |
| **All final co-products** | 0.5720 + 0.0712 + 0.1800 + 0.0445 | **0.8677** |

---

> **Water balance check on Stage 1:** The brown rice moisture used in this table is not an independent assumption — it follows from the rough rice and hull moistures. One tonne of rough rice at 13% moisture carries 0.130 t of water. Hulls, at 90% DM, take 0.20 × 0.10 = 0.020 t of it, leaving 0.110 t in 0.80 t of brown rice, or **13.75% moisture**. The adopted 14% (86% DM) follows directly, and the small residual is the 0.002 t of Stage 1 DM loss shown in Section 7.2.

---

## 5. Prices

### 5.1 Price Table

| Co-product | Price (USD/t) | Range | Source | Notes |
|------------|--------------|-------|--------|-------|
| **Brown rice** (intermediate) | 480 | 380–580 | USDA ERS [^2^]; IndexBox [^6^] | Brown rice intermediate for Stage 1 allocation. Priced between rough rice (~$250–350/t) and milled rice (~$400–700/t). |
| **White rice (head rice + large brokens)** | 550 | 400–700 | USDA ERS [^2^]; WASDE [^3^]; IndexMundi [^5^] | 2024–2025 average for US long-grain milled rice. Prices vary by grade, variety, and crop year. |
| **Rice bran** | 220 | 140–300 | USDA ERS [^2^]; Tridge [^9^]; IndexBox [^6^] | 2024–2025 average for stabilized rice bran. Raw bran: ~$90–170/t (USDA AMS Weekly Rice Summary reports domestic bulk at $85–120/short ton ≈ $94–132/t); stabilized: $180–320/t. |
| **Rice hulls** | 40 | 20–60 | Industry estimates | 2024–2025 average. Rice hulls are a low-value byproduct used as animal feed roughage, mulch, bedding, or industrial filler. Market data is limited; hulls are often consumed on-site. |
| **Rice mill feed (brokens + fines)** | 160 | 100–220 | USDA ERS [^2^]; industry estimates | 2024–2025 average. Brokens and brewer's rice sold as animal feed or for brewing. Priced well below head rice. |

### 5.2 Price Verification

**White rice (head rice + large brokens):**

```
USDA ERS (2025): ~$500-600/t (long-grain, milled, FOB)
IndexMundi (2025 avg): ~$530/t
WASDE (Feb 2026): 12-14 ¢/lb = $265-309/t (rough rice, not milled)
Milled rice premium over rough rice: typically 2.0-2.5× rough rice price

Adopted: $550/t, the midpoint of the stated range
```

**Rice bran:**

```
USDA AMS Weekly Rice Summary: raw bran ~$85-120/short ton bulk (~$94-132/t)
Tridge: ~$200-260/t (stabilized)
IndexBox: ~$180-300/t
Raw bran: ~$90-170/t; stabilized: $180-320/t

Adopted: $220/t, the midpoint of the stated range
```

**Rice hulls:**

```
Industry estimates: ~$30-50/t (bulk, loose)
Pelleted hulls: ~$60-100/t
Boiler fuel value: ~$20-40/t (energy content basis)

Adopted: $40/t, the midpoint of the stated range
```

**Rice mill feed:**

```
USDA ERS (2025): ~$140-180/t (brokens, feed grade)
Brewer's rice: ~$160-220/t
Second heads (large brokens): ~$200-300/t

Adopted: $160/t, the midpoint of the stated range
```

### 5.3 Revenue per Tonne of Rough Rice

| Co-product | Calculation | Revenue (USD/t rough rice) |
|------------|-------------|--------------------------|
| **White rice** | 0.65 × 550 | **$357.50** |
| **Rice bran** | 0.08 × 220 | **$17.60** |
| **Rice hulls** | 0.20 × 40 | **$8.00** |
| **Rice mill feed** | 0.05 × 160 | **$8.00** |
| **Total** | | **$391.10** |

> **Note:** Brown rice is not included in the final revenue calculation because it is an intermediate product, not a final co-product. The brown rice's value is realized through its conversion into white rice, bran, and mill feed. Using brown rice's intermediate price in the final allocation would distort the result by double-counting value (once at the brown rice stage, once at the milling stage). Brown rice's price ($480/t) is used only for Stage 1 economic allocation.

---

## 6. Two-Stage Allocation

### 6.1 Treatment of the Intermediate Product

Rice milling has an intermediate — brown rice — that is sold between the two stages, so Stage 1 cannot be allocated without deciding what brown rice is worth. Two conventions are possible.

**Market-price cascade (used here).** Brown rice is valued at the price it transacts at between huller and miller ($480/t, Section 5.1). Stage 1 divides the rough rice burden between brown rice and hulls on that basis; Stage 2 divides brown rice's burden among white rice, bran and mill feed; the two stage allocations are then multiplied along each product's path.

**Derived valuation (not used here).** Brown rice is instead valued at the total revenue of the products it becomes ($383.10/t rough rice).

These are not two options plus a third. **Valuing the intermediate at its derived value makes the cascade collapse algebraically to the direct end-of-chain calculation**, because the derived value cancels out of the multiplication:

```
Stage 1 brown rice share x Stage 2 white rice share
  = D / (D + hulls)  x  white / D
  = white / (D + hulls)
  = white / (white + bran + mill feed + hulls)   <- the direct calculation
```

So the choice is between the market-price cascade and the direct end-of-chain calculation, and Section 6.6 reports the direct result. For rice the two agree to within 0.01 percentage point (Section 6.7), so the choice is immaterial here — but it is stated explicitly because it is not immaterial in every two-stage system.

**Why the market-price cascade is used for rice:**

1. **Brown rice is not a final co-product in this work.** It is not a dairy feed; within this system it exists only as the input to whitening. The four co-products this document reports are white rice, rice bran, rice hulls and rice mill feed.
2. **The brown rice price is an arms-length transfer price into Stage 2.** It is what a miller pays for the same stream that enters whitening, so it is the observable value at the point of separation, which is what applying allocation at each unit process requires.
3. **It keeps the split of the field burden independent of downstream value-add.** Whitening adds relatively little value in rice, which is why the two calculations converge; the convention nonetheless holds the Stage 1 split to the transaction that actually occurs there.

**Where this convention does not apply.** A different treatment is warranted where the intermediate is itself a marketed final co-product of the system being studied — that is, where the study needs allocation factors for both the intermediate and the products it becomes, because both are genuine outputs. In that case the intermediate's quoted price is the price in a competing end use rather than a transfer price into the next stage, and the direct end-of-chain treatment is used so that all final products sit on one denominator. That situation does not arise for rice: brown rice sold as a retail food product leaves the system as a final product in its own right and is outside the scope of this table, which models the whitening pathway.

### 6.2 Allocation Approach

Because rice milling has two sequential stages, the allocation is performed in two steps:

**Stage 1 (Hulling):** Allocate rough rice's burden between brown rice and rice hulls.  
**Stage 2 (Milling):** Allocate brown rice's burden between white rice, rice bran, and rice mill feed.

The final allocation for each co-product is the product of the stage allocations along its path through the system:

```
White rice:   Stage 1 brown rice alloc × Stage 2 white rice alloc
Rice bran:    Stage 1 brown rice alloc × Stage 2 bran alloc
Rice hulls:   Stage 1 hulls alloc (no Stage 2)
Rice mill feed: Stage 1 brown rice alloc × Stage 2 mill feed alloc
```

### 6.3 Stage 1: Hulling Allocation

**Mass allocation:**

| Co-product | DM Output | Calculation | Stage 1 Allocation |
|------------|-----------|-------------|-------------------|
| Brown rice | 0.6880 t | (0.6880 ÷ 0.8680) × 100 | **79.3%** |
| Rice hulls | 0.1800 t | (0.1800 ÷ 0.8680) × 100 | **20.7%** |

**Economic allocation:**

| Co-product | Revenue | Calculation | Stage 1 Allocation |
|------------|---------|-------------|-------------------|
| Brown rice | $384.00 | (384.00 ÷ 392.00) × 100 | **98.0%** |
| Rice hulls | $8.00 | (8.00 ÷ 392.00) × 100 | **2.0%** |

> **Stage 1 revenue:** Brown rice: 0.80 × $480 = $384.00; Rice hulls: 0.20 × $40 = $8.00; Total: $392.00.

### 6.4 Stage 2: Milling Allocation

**Mass allocation:**

| Co-product | DM Output (per t rough rice) | Calculation | Stage 2 Allocation |
|------------|-------------------------|-------------|-------------------|
| White rice | 0.5720 t | (0.5720 ÷ 0.6877) × 100 | **83.2%** |
| Rice bran | 0.0712 t | (0.0712 ÷ 0.6877) × 100 | **10.3%** |
| Rice mill feed | 0.0445 t | (0.0445 ÷ 0.6877) × 100 | **6.5%** |

> **Rounding note:** Raw calculations yield 83.18%, 10.35%, and 6.47%. These are rounded to 83.2%, 10.3%, and 6.5% so that the sum is exactly 100.0%.

**Economic allocation:**

| Co-product | Revenue (per t rough rice) | Calculation | Stage 2 Allocation |
|------------|----------------------|-------------|-------------------|
| White rice | $357.50 | (357.50 ÷ 383.10) × 100 | **93.3%** |
| Rice bran | $17.60 | (17.60 ÷ 383.10) × 100 | **4.6%** |
| Rice mill feed | $8.00 | (8.00 ÷ 383.10) × 100 | **2.1%** |

> **Rounding note:** Raw calculations yield 93.32%, 4.59%, and 2.09%. These are rounded to 93.3%, 4.6%, and 2.1% so that the sum is exactly 100.0%.

### 6.5 Final Cumulative Allocation

The final allocation of rough rice's environmental burden to each of the four final co-products is calculated by cascading the two stages:

**Mass allocation (cumulative):**

| Co-product | Calculation | Final Allocation |
|------------|-------------|-----------------|
| **White rice** | 79.263% × 83.176% | **65.9%** |
| **Rice bran** | 79.263% × 10.353% | **8.2%** |
| **Rice hulls** | 20.737% (Stage 1 only) | **20.7%** |
| **Rice mill feed** | 79.263% × 6.471% | **5.2%** |
| **Total** | | **100.0%** |

> **Rounding note:** The cumulative values are computed from the **unrounded** stage allocations, not from the one-decimal figures displayed in Sections 6.3 and 6.4. Multiplying rounded percentages inflates the result: 79.3% × 83.2% gives 65.98%, whereas the unrounded product is 65.93%. The unrounded cumulative values are 65.927%, 8.206%, 20.737% and 5.129%, which sum to exactly 100%. Rounded to one decimal place they give 65.9, 8.2, 20.7 and 5.1, summing to 99.9%; rice mill feed carries the +0.1 pp adjustment, being the stream whose value sits closest to the next decimal. Rice hulls is not adjusted because its cumulative allocation is its Stage 1 allocation by construction.

**Economic allocation (cumulative):**

| Co-product | Calculation | Final Allocation |
|------------|-------------|-----------------|
| **White rice** | 97.959% × 93.317% | **91.4%** |
| **Rice bran** | 97.959% × 4.594% | **4.5%** |
| **Rice hulls** | 2.041% (Stage 1 only) | **2.0%** |
| **Rice mill feed** | 97.959% × 2.088% | **2.1%** |
| **Total** | | **100.0%** |

> **Rounding note:** As above, computed from the unrounded stage allocations. The unrounded cumulative values are 91.413%, 4.500%, 2.041% and 2.046%, summing to exactly 100%; rice mill feed carries the +0.1 pp adjustment.

### 6.6 Verification: Direct Calculation

The cumulative allocation can be verified by calculating directly from the four final co-products' DM and revenue values per tonne of rough rice, bypassing the intermediate brown rice stage:

**Direct mass allocation:**

| Co-product | DM Output (t/t rough rice) | Calculation | Final Allocation |
|------------|----------------------|-------------|-----------------|
| White rice | 0.5720 | (0.5720 ÷ 0.8677) × 100 | **65.9%** |
| Rice bran | 0.0712 | (0.0712 ÷ 0.8677) × 100 | **8.2%** |
| Rice hulls | 0.1800 | (0.1800 ÷ 0.8677) × 100 | **20.7%** |
| Rice mill feed | 0.0445 | (0.0445 ÷ 0.8677) × 100 | **5.2%** |
| **Total** | **0.8677** | | **100.0%** |

> **Rounding note:** Unrounded values are 65.921%, 8.206%, 20.744% and 5.129%. Rounded independently they sum to 99.9%, so rice mill feed carries the +0.1 pp adjustment, as in Section 6.5.

**Direct economic allocation:**

| Co-product | Revenue (USD/t rough rice) | Calculation | Final Allocation |
|------------|----------------------|-------------|-----------------|
| White rice | $357.50 | (357.50 ÷ 391.10) × 100 | **91.4%** |
| Rice bran | $17.60 | (17.60 ÷ 391.10) × 100 | **4.5%** |
| Rice hulls | $8.00 | (8.00 ÷ 391.10) × 100 | **2.0%** |
| Rice mill feed | $8.00 | (8.00 ÷ 391.10) × 100 | **2.1%** |
| **Total** | **$391.10** | | **100.0%** |

> **Rounding note:** Rice hulls and rice mill feed both earn $8.00/t rough rice, so their unrounded allocations are identical at 2.046%. Rounded independently the four values sum to 99.9%; rice mill feed carries the +0.1 pp adjustment, matching the treatment in Section 6.5.

### 6.7 Reconciliation: Cascade vs. Direct

The cascade and direct methods give very similar results for rice milling:

| Co-product | Mass (cascade) | Mass (direct) | Econ (cascade) | Econ (direct) |
|------------|---------------|---------------|----------------|---------------|
| White rice | 65.9% | 65.9% | 91.4% | 91.4% |
| Rice bran | 8.2% | 8.2% | 4.5% | 4.5% |
| Rice hulls | 20.7% | 20.7% | 2.0% | 2.0% |
| Rice mill feed | 5.2% | 5.2% | 2.1% | 2.1% |

**Why the two agree so closely:** For rice milling the cascade and direct calculations agree to within 0.01 percentage point on every stream — closer than the displayed precision — so they are identical once rounded. Two reasons. On the mass side, the processing losses are very small (0.26% of input DM in total), so the cascade denominators and the direct denominator are nearly the same pool. On the economic side, the brown rice intermediate is priced at $480/t while its products run $550/t (white rice), $220/t (bran) and $160/t (mill feed); the intermediate price is close to the revenue-weighted average of what it becomes ($383.10 of revenue from 0.80 t of brown rice is $479/t), so valuing the intermediate at its own price and valuing it at its derived value give nearly the same Stage 1 split.

This convergence is a property of rice milling, not a general result. Where a downstream stage adds a large multiple of value, the two calculations diverge substantially.

**Which method to use:**

- The **cascade method** applies allocation at each unit process separately, which is appropriate when the intermediate crosses a system boundary and is independently traded, as brown rice is. It reflects the transaction that actually occurs at each stage. Note that ISO 14044 requires allocation to be applied at each unit process; it does not define or mandate a "cascade", which is a practitioner's term and should not be confused with ISO's stepwise allocation *hierarchy* (avoid → physical → economic).
- The **direct calculation** uses a single end-of-chain denominator. It is simpler, but it collapses the two-stage structure and lets value added in Stage 2 govern the Stage 1 split.

Both are reported. The **cascade is the primary allocation** for this document, for the reasons in Section 6.1. For rice the two agree to within 0.01 pp, so the choice does not affect the published factors.

### 6.8 Recommended Final Allocation

| Co-product | Mass Allocation | Economic Allocation |
|------------|----------------|-------------------|
| **White rice** | **65.9%** | **91.4%** |
| **Rice bran** | **8.2%** | **4.5%** |
| **Rice hulls** | **20.7%** | **2.0%** |
| **Rice mill feed** | **5.2%** | **2.1%** |
| **Total** | **100.0%** | **100.0%** |

---

## 7. Mass Balance Verification

### 7.1 Overall DM Balance

| Item | Value | Notes |
|------|-------|-------|
| Input DM (1 t rough rice at 13% moisture) | 0.8700 t | 1.000 × (1 − 0.13) |
| **Output DM — final co-products:** | | |
| White rice | 0.5720 t | 0.65 t × 88% DM |
| Rice bran | 0.0712 t | 0.08 t × 89% DM |
| Rice hulls | 0.1800 t | 0.20 t × 90% DM |
| Rice mill feed | 0.0445 t | 0.05 t × 89% DM |
| Total co-product DM | **0.8677 t** | |
| DM balance gap | −0.0023 t | 0.26% of input DM |

> **Balance assessment:** The DM output is 0.0023 t (0.26%) below the DM input. This small deficit represents processing losses (dust from hulling, polishing fines, moisture adjustment) and is well within the acceptable range.

### 7.2 Stage-by-Stage Balance

**Stage 1: Hulling**

| Item | Value | Notes |
|------|-------|-------|
| Input DM | 0.8700 t | 1 t rough rice at 13% moisture |
| Brown rice DM | 0.6880 t | 0.80 t × 86% DM |
| Hulls DM | 0.1800 t | 0.20 t × 90% DM |
| **Total accounted** | **0.8680 t** | |
| Stage 1 losses | 0.0020 t | 0.23% of input; dust and fines from hulling |

**Stage 2: Milling / Whitening**

| Item | Value | Notes |
|------|-------|-------|
| Input DM (brown rice) | 0.6880 t | From Stage 1 |
| White rice DM | 0.5720 t | 0.65 t × 88% DM |
| Bran DM | 0.0712 t | 0.08 t × 89% DM |
| Mill feed DM | 0.0445 t | 0.05 t × 89% DM |
| **Total accounted** | **0.6877 t** | |
| Stage 2 losses | 0.0003 t | 0.04% of input; polishing dust, residual bran |

### 7.3 As-Is Mass Balance

| Item | Value | Notes |
|------|-------|-------|
| Input (rough rice) | 1.000 t | — |
| **Output:** | | |
| White rice | 0.650 t | — |
| Rice bran | 0.080 t | — |
| Rice hulls | 0.200 t | — |
| Rice mill feed | 0.050 t | — |
| **Total output** | **0.980 t** | |
| **Processing losses** | **0.020 t** | 2.0%: chiefly moisture removed during whitening and polishing (see Section 4.1), plus dust and fines — the residual of the balance, not an independent measurement |
| **Balance** | **1.000 t** | Closes by construction, since the loss term is the residual |

---

## 8. Complete Data Table

### 8.1 Final Co-Product Allocation (per 1 t rough rice at 13% moisture)

| Parent Crop | Crop System | Stage | USDA Standard | Standard Moisture | Parent Input Basis | Co-product Stream | Yield (t/t rough rice) | Yield Range | Price (USD/t) | Price Range | DM (%) | DM Output (t/t rough rice) | Revenue (USD/t rough rice) | Econ Alloc — Cascade (%) | Econ Alloc — Direct (%) | Mass Alloc — Cascade (%) | Mass Alloc — Direct (%) |
|-------------|-------------|-------|---------------|-------------------|-------------------|-------------------|----------------------|-------------|---------------|-------------|--------|--------------------------|--------------------------|------------------------|------------------------|------------------------|------------------------|
| Rice | Rice milling | 2 | 45 lb/bu min test weight (long grain) | 13% | 1 t rough rice at 13% moisture | White rice (head rice + large brokens) | 0.65 | 0.58–0.72 | 550 | 400–700 | 88.0 | 0.572 | 357.50 | 91.4 | 91.4 | 65.9 | 65.9 |
| Rice | Rice milling | 2 | 45 lb/bu min test weight (long grain) | 13% | 1 t rough rice at 13% moisture | Rice bran | 0.08 | 0.06–0.10 | 220 | 140–300 | 89.0 | 0.071 | 17.60 | 4.5 | 4.5 | 8.2 | 8.2 |
| Rice | Rice milling | 2 | 45 lb/bu min test weight (long grain) | 13% | 1 t rough rice at 13% moisture | Rice hulls | 0.20 | 0.18–0.22 | 40 | 20–60 | 90.0 | 0.180 | 8.00 | 2.0 | 2.0 | 20.7 | 20.7 |
| Rice | Rice milling | 2 | 45 lb/bu min test weight (long grain) | 13% | 1 t rough rice at 13% moisture | Rice mill feed | 0.05 | 0.03–0.07 | 160 | 100–220 | 89.0 | 0.045 | 8.00 | 2.1 | 2.1 | 5.2 | 5.2 |

### 8.2 Intermediate Product (for cascade calculation reference only)

| Parent Crop | Crop System | Stage | USDA Standard | Standard Moisture | Parent Input Basis | Co-product Stream | Yield (t/t rough rice) | Yield Range | Price (USD/t) | Price Range | DM (%) | DM Output (t/t rough rice) | Revenue (USD/t rough rice) | Stage 1 Econ Alloc (%) | Stage 1 Mass Alloc (%) |
|-------------|-------------|-------|---------------|-------------------|-------------------|-------------------|----------------------|-------------|---------------|-------------|--------|--------------------------|--------------------------|------------------------|------------------------|
| Rice | Rice hulling | 1 | 45 lb/bu min test weight (long grain) | 13% | 1 t rough rice at 13% moisture | Brown rice (intermediate) | 0.80 | 0.78–0.82 | 480 | 380–580 | 86.0 | 0.688 | 384.00 | 98.0 | 79.3 |

---

## 9. Data Quality and Limitations

### 9.1 High-Confidence Data

| Data Point | Confidence | Source |
|------------|-----------|--------|
| Rice hulls yield (0.20 t/t) | **High** | Industry standard; hull fraction is well-characterized at 18–22% [^4^][^7^] |
| Rice bran yield (0.08 t/t) | **High** | Well-established at ~8% of rough rice; IRRI consistently reports ~8% [^8^] |
| Brown rice yield (0.80 t/t) | **High** | Consistent with 78–82% hulling yield [^4^] |
| White rice DM% (88%) | **High** | Commercial standard for milled rice; well-milled rice typically 11–13% moisture |
| White rice price ($550/t) | **High** | USDA ERS [^2^]; IndexMundi [^5^] quote ~$500–600/t and ~$530/t respectively |

### 9.2 Medium-Confidence Data

| Data Point | Confidence | Source |
|------------|-----------|--------|
| White rice yield (0.65 t/t) | **Medium** | This includes head rice + large brokens. Pure HRY for long-grain is 45–60%; MRY is 65–72%. The 0.65 value represents common industry practice but depends on how brokens are classified. |
| Rice mill feed yield (0.05 t/t) | **Medium** | Depends on milling precision and how brokens are classified. Some mills include large brokens with head rice; others sell them separately. |
| Brown rice price ($480/t) | **Medium** | Brown rice is not as widely traded as white rice; price estimated from relationship with rough rice and milled rice prices |
| Hulls price ($40/t) | **Medium** | Limited market data; hulls are often consumed on-site or disposed of rather than sold |
| Price ranges | **Medium** | Based on historical volatility; actual prices may exceed ranges during market shocks |

### 9.3 Known Limitations

1. **Grain type variation:** This document uses long-grain rice as the reference type. Medium- and short-grain rice have higher head rice yields (up to 0.58–0.72 t/t for the head rice + large brokens metric) and may have slightly different bran and hull fractions. Users working with medium- or short-grain rice should adjust yields accordingly within the stated ranges.

2. **Head rice yield vs. total milled rice yield:** The "white rice" co-product in this methodology includes head rice plus large brokens graded as whole-kernel equivalent (0.65 t/t). Pure head rice yield (HRY, whole kernels ≥3/4 length only) would be significantly lower (0.45–0.60 t/t for long-grain). The choice to include large brokens with head rice is common in industry but differs from the strict USDA definition of head rice. LCA practitioners should be aware of this distinction and adjust if their study requires pure HRY.

3. **Economic allocation dominance by white rice:** White rice commands 91.4% of the economic allocation, making the economic allocation very stable (insensitive to price changes) but also making the other co-products' allocations very small. This is a common feature of cereal processing where one product (the primary food) dominates the value.

4. **Broken rice classification:** The boundary between "white rice" (head rice + large brokens at $550/t) and "rice mill feed" (small brokens + fines at $160/t) is somewhat arbitrary. Some mills sell second heads (large brokens) at $250–350/t as a separate product. Reclassifying large brokens from mill feed to white rice would increase white rice yield and shift allocations.

5. **Hull value variability:** Rice hulls have limited markets and are sometimes treated as waste (zero value). If hulls are assigned zero revenue, Stage 1 assigns the whole burden to brown rice and the economic allocation becomes the Stage 2 split: **white rice 93.3%, bran 4.6%, mill feed 2.1%**. That is a 1.9 pp increase for white rice relative to the $40/t hull scenario.

6. **Rough rice moisture:** The 13% moisture used here is a typical trade and storage target for long-grain rough rice, not a USDA FGIS grade standard. Medium- and short-grain rough rice is typically stored at ~14% moisture. The DM input changes from 0.870 (13% moisture) to 0.860 (14% moisture), which would slightly affect mass allocation proportions. The choice of moisture target should match the grain type being modeled.

7. **Brown rice intermediate price:** The Stage 1 economic allocation depends on the brown rice price ($480/t), which is less well established than the white rice price. In this system that dependency turns out not to matter: $480/t is close to the revenue-weighted value of what brown rice becomes ($383.10 of revenue from 0.80 t of brown rice is $479/t), so the cascade and direct calculations agree to within 0.01 pp (Section 6.7). The brown rice price would matter materially only if it diverged substantially from the value of its products, which is not the case here.

8. **Stabilized vs. raw rice bran:** The $220/t price assumes stabilized rice bran (heat-treated to deactivate lipase, extending shelf life from days to months). Raw rice bran sells for ~$90–170/t but deteriorates rapidly. The choice affects bran's economic allocation share.

---