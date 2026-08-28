# Oat Milling: Co-Product Allocation Methodology, Data Sources, and Calculations

**Document Version:** 1.0
**Date:** May 2026
**Basis:** 1 metric ton (t) of oats at 12% moisture (industry trading convention)
**Price Period:** 2024–2025 average (unless otherwise noted)

---

## Table of Contents

1. [Standard Basis and Conversions](#1-standard-basis-and-conversions)
2. [Data Sources and References](#2-data-sources-and-references)
3. [Oat Milling System](#3-oat-milling-system)
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
| **Parent crop** | Oat (*Avena sativa*) | — |
| **Input quantity** | 1 metric ton (1,000 kg) | — |
| **Moisture content** | 12.0% | Industry trading convention for oat delivery [^1^]. Note: USDA grain grading standards for oats (7 CFR 810 Subpart G) do NOT include moisture as a grade-determining factor. Moisture is reported on inspection certificates but is not a grading criterion. The 12% figure is a common buyer/mill delivery specification, not a USDA standard. |
| **Dry matter (DM) input** | 0.880 t DM/t oats | Calculated: 1.000 × (1 − 0.12) = 0.880 |
| **Standard bushel equivalent** | 68.9 bushels/t | 1,000 kg ÷ 14.515 kg/bu (32 lb standard bushel weight) |
| **Standard bushel weight** | 32 lb (14.515 kg) | USDA standard bushel weight for oats, used for trading and reporting. Distinct from test weight. |
| **Typical test weight** | ~34 lb/bu (range 27–40 lb/bu) | Average commodity oat density at 12% moisture. USDA minimum test weight for No. 1 oats: 36 lb/bu; No. 4: 27 lb/bu (7 CFR 810.1004) [^1^]. Actual test weight varies by variety, growing conditions, and hull content. Hulless varieties approach 48 lb/bu but are rarely traded as commodity oats. |
| **Typical groat content** | ~70–78% of seed weight | Complement of the hull fraction (22–30%) [^2^][^6^]. Groat and hull are the two parts of the seed, so the two ranges are stated as complements. |

> **Note on bushel weight vs. test weight:** The standard bushel weight (32 lb) is used for bushel equivalent calculations, as this is the legal definition used in USDA reporting and grain trading. The typical test weight (~34 lb/bu) is reported separately as a descriptive statistic. The standard bushel for oats is 32 lb, compared to 60 lb for wheat, 56 lb for corn, and 48 lb for barley.

> **Note on moisture specification:** USDA oat grading standards (7 CFR 810 Subpart G) grade oats on test weight, heat-damaged kernels, wild oats, and foreign material — moisture is NOT a grade-determining factor. The 12% moisture figure is an industry trading convention and common buyer specification, not a USDA standard. For safe storage, the widely cited maximum is 13–14%.

### 1.2 Convention for Adopted Values

Every yield, price, and DM% in this document is reported as an adopted point value together with the range it was drawn from. **Unless a row states otherwise, the adopted value is the midpoint of its stated range**, and the range is the parameter that carries the evidence. Point values are given to the precision the underlying sources support and are not intended to imply plant-level accuracy. Derived quantities (DM outputs, revenues, allocation percentages) are carried at four decimals internally and reported to one decimal place.

### 1.3 Unit Conversions

| Conversion | Factor |
|------------|--------|
| 1 bushel oats (standard) | 32 lb = 14.515 kg (USDA standard bushel weight) |
| 1 lb | 0.453592 kg = 0.000453592 t |
| 1 t oats | ~68.9 bushels (at 32 lb/bu standard) |
| 1 short ton | 2,000 lb = 0.907185 metric ton |
| 1 metric ton | 2,204.62 lb = 1.10231 short tons |

---

## 2. Data Sources and References

### 2.1 Primary Sources

| Citation | Full Title | Type | URL |
|----------|-----------|------|-----|
| [^1^] | USDA AMS-FGIS — United States Standards for Oats, 7 CFR 810.1001–810.1005 | Government (USDA) | https://www.ams.usda.gov/grades-standards/oat-standards |
| [^2^] | Welch, R.W. (Ed.) (1995). *The Oat Crop: Production and Utilization*. Springer Dordrecht. DOI: 10.1007/978-94-011-0015-1 | Academic/Book | https://link.springer.com/book/10.1007/978-94-011-0015-1 |
| [^3^] | USDA NASS — Oats: Area, Yield, Production, and Price | Government (USDA) | https://www.nass.usda.gov/ |
| [^4^] | Girardet, N. & Webster, F.H. (2011). "Oat Milling: Specifications, Storage, and Processing." Chapter 14 in *OATS: Chemistry and Technology* (2nd ed.), AACC International, pp. 301–319. DOI: 10.1094/9781891127649.014 | Academic/Book Chapter | https://www.aaccnet.org/ |
| [^5^] | IndexMundi — Oats Futures Price | Market Data | https://www.indexmundi.com/commodities/?commodity=oats |
| [^6^] | Feedipedia — Oat hulls (INRAE/CIRAD/AFZ/FAO) | Scientific Database | https://www.feedipedia.org/node/707 |
| [^7^] | Feedipedia — Oat mill feed (INRAE/CIRAD/AFZ/FAO) | Scientific Database | https://www.feedipedia.org/node/708 |
| [^8^] | University of Minnesota Extension — Feed Ingredient Market Reports | University Extension | https://extension.umn.edu/ |

### 2.2 How Sources Were Used

- **Yield data:** Welch [^2^] and Girardet & Webster [^4^] provided oat milling yield data. The ranges reflect variation across oat varieties (hull content varies from 22–30%), mill configurations, and product specifications.
- **Price data (food oats):** USDA NASS [^3^] and IndexMundi [^5^] provided oat grain and product price data. Food oat prices reflect the value of processed groats/rolled oats.
- **Price data (hulls):** Feedipedia [^6^] and university extension feed reports [^8^] provided oat hull price data. Hulls are a low-value byproduct with limited markets and low price transparency.
- **Price data (mill feed):** Feedipedia [^7^] and university extension feed reports [^8^] provided oat mill feed price data. Mill feed is a mid-value byproduct used in animal feed.
- **DM contents and composition:** Feedipedia [^6^][^7^] and academic literature [^2^][^4^] for oat product composition data.

> **Note on URL specificity:** References [^3^] (USDA NASS) and [^8^] (Univ. of MN Extension) currently link to organizational homepages rather than specific report pages. This is because specific annual NASS reports and extension PDFs rotate URLs with each publication cycle. Specific annual NASS Oats reports (e.g., "Crop Production" and "Agricultural Prices" summaries) and extension feed ingredient market reports were consulted; homepage URLs are provided for general navigation as specific report URLs are not persistent.

---

## 3. Oat Milling System

### 3.1 Process Description

Oat milling converts raw oats into food-grade oat products and co-products through the following steps:

1. **Cleaning:** Foreign material (dirt, weed seeds, chaff, other grains) is removed using screens, aspirators, and disc separators. This removes ~1–3% of input mass.
2. **Dehulling:** Oat hulls are removed using impact or stone dehullers. The hull represents 22–30% of the oat seed weight (higher for covered varieties, lower for "naked" varieties). Dehulling efficiency is typically 92–96%, meaning some groats remain with the hulls and some hull fragments remain with the groats. The **recovered hull yield per tonne of oats received is therefore lower than the hull fraction of the seed**, because cleaning removes 1–3% of the mass first and part of the hull leaves with the groat stream.
3. **Kilning (heat treatment):** Groats are heated to develop flavor, inactivate lipase enzymes (which cause rancidity), and reduce moisture. Kilning reduces moisture from ~12% to ~9–11% and is essential for shelf stability. This is a key step that distinguishes oat milling from other grain milling.
4. **Cutting/flaking/grinding:** Kilned groats are processed into various food products:
   - **Steel-cut oats:** Groats cut into 2–4 pieces
   - **Rolled oats (old-fashioned):** Groats steamed and rolled flat
   - **Quick oats:** Groats cut before rolling (thinner flakes)
   - **Instant oats:** Groats cut very fine and rolled very thin (often with added ingredients)
   - **Oat flour:** Ground groats
5. **Sifting and grading:** Mill stream is sifted to separate product sizes. Fine particles that don't meet product specifications are collected as "oat mill feed."

**Co-products generated:**
- **Food oats:** The primary product (groats, rolled oats, steel-cut, oat flour). Includes all products destined for human consumption.
- **Oat hulls:** The fibrous outer husk, removed during dehulling. Used as animal feed roughage, boiler fuel, or as a source of dietary fiber.
- **Oat mill feed:** A mixture of bran particles, endosperm fines, short pieces, and other mill fractions that don't meet food oat specifications. Higher in protein and energy than hulls; used in animal feed.

### 3.2 Process Flow

```
1 t oats at 12% moisture (0.880 t DM)
        │
        ▼
  ┌─ OAT MILLING ──────────────────────────────────┐
  │                                                 │
  │  Cleaning: ~0.02 t removed (foreign material)  │
  │  Kilning: moisture reduced from ~12% to ~10%   │
  │  Processing losses: ~0.03 t (~3%)              │
  │  (fines, spillage, incomplete dehulling)        │
  │                                                 │
  │  Food oats: 0.60 t as-is (0.540 t DM)       ◄── co-product
  │                                                 │
  │  Oat hulls: 0.25 t as-is (0.225 t DM)      ◄── co-product
  │                                                 │
  │  Oat mill feed: 0.10 t as-is (0.090 t DM)  ◄── co-product
  │                                                 │
  └─────────────────────────────────────────────────┘

THREE CO-PRODUCTS from 1 t oats:
  Food oats:      0.60 t as-is,  0.540 t DM
  Oat hulls:      0.25 t as-is,  0.225 t DM
  Oat mill feed:  0.10 t as-is,  0.090 t DM
  Total:                        0.855 t DM  (from 0.880 t input; ~0.025 t losses)
```

---

## 4. Co-Product Yields and Properties

### 4.1 Yields (per tonne of oats input)

| Co-product | Yield (t/t oats) | Range | Source & Calculation |
|------------|-----------------|-------|---------------------|
| **Food oats** | 0.60 | 0.58–0.62 | Milling literature [^2^][^4^]. The fraction of groats, after dehulling, that meets food-grade specifications. Varies with oat variety (groat content 70–78%), dehulling efficiency (92–96%), and mill configuration. |
| **Oat hulls** | 0.25 | 0.22–0.28 | Milling literature [^2^][^6^]. Recovered hull stream. Hull is 22–30% of seed weight depending on variety; Feedipedia [^6^] gives "up to 25% of the weight of the grain." The recovered yield is lower than the seed hull fraction — see the reconciliation note below. |
| **Oat mill feed** | 0.10 | 0.08–0.12 | Milling literature [^4^][^7^]. Bran particles, endosperm fines, and short pieces that do not meet food oat specifications. Varies with mill configuration and product mix. |

*Reconciling the hull yield with seed composition:* The hull yield can be derived from seed composition, and doing so reproduces the adopted value. Cleaning removes 1–3% of the delivered mass before dehulling, leaving ~0.98 t of seed; of that, 22–30% is hull; and dehulling recovers 92–96% of it into the hull stream, the balance leaving with the groats.

| Hull fraction of cleaned seed | Dehulling recovery | Hull yield (t/t oats) |
|---|---|---|
| 26% | 96% | 0.245 |
| 28% | 92% | 0.252 |
| 30% | 90% | 0.265 |

The adopted **0.25 t/t** sits within this band and within the reported yield range of 0.22–0.28.

> **Note on yield relationship:** The three yields are interdependent. The seed is groat plus hull; the food oats yield then depends on how much of the groat stream meets food specifications, with the remainder going to mill feed. Higher food oat yields mean less mill feed.

### 4.2 Dry Matter Contents

| Co-product | DM (%) | Basis |
|------------|--------|-------|
| Food oats | 90.0% | Kilned and processed food oats (groats, rolled oats, steel-cut) typically have 9–11% moisture [^2^][^4^]; kilning reduces moisture from ~12% to ~9–11%. The adopted 90% DM corresponds to 10% moisture, the midpoint of that range. |
| Oat hulls | 90.0% | Dried oat hulls are typically 88–93% DM [^6^]. Feedipedia data (88 samples): average 90.3%, range 88.4–92.7%. Hulls are relatively dry after dehulling and may be further dried for storage. The 90% DM value is consistent with the Feedipedia average. |
| Oat mill feed | 90.0% | Oat mill feed (bran, fines, shorts) is typically 88–93% DM [^7^]. Moisture depends on processing conditions. The 90% DM value is the midpoint of the typical range. |



### 4.3 DM Output per Tonne of Oats

| Co-product | Calculation | DM Output (t/t oats) |
|------------|-------------|---------------------|
| **Food oats** | 0.60 × 0.90 | **0.5400** |
| **Oat hulls** | 0.25 × 0.90 | **0.2250** |
| **Oat mill feed** | 0.10 × 0.90 | **0.0900** |
| **Total** | | **0.8550** |

---

## 5. Prices

### 5.1 Price Table

| Co-product | Price (USD/t) | Range | Source | Notes |
|------------|--------------|-------|--------|-------|
| **Food oats** | 375 | 300–450 | USDA NASS [^3^]; IndexMundi [^5^] | 2024–2025 average for processed oat groats/rolled oats (wholesale). Raw oat grain: $150–220/t [^3^]. The milling margin adds ~$130–230/t. Range reflects the verified price range for wholesale processed food oats (Section 5.2). |
| **Oat hulls** | 80 | 50–110 | Feedipedia [^6^]; university extension feed reports [^8^] | 2024–2025 average. Oat hulls are a low-value byproduct used as animal feed roughage, boiler fuel at milling plants, or as a source of oat fiber (after further processing). Loose bulk: $40–70/t; pelleted: $90–120/t. |
| **Oat mill feed** | 180 | 140–220 | Feedipedia [^7^]; university extension feed reports [^8^] | 2024–2025 average. Oat mill feed is a mid-value byproduct used in animal feed (primarily ruminants). Higher in protein and energy than hulls (~8–13% protein vs. ~3–6% for hulls). |


> **Note on byproduct price transparency:** Oat hulls and oat mill feed are niche industrial byproducts with limited public price data. The values here come from Feedipedia indicative market values [^6^][^7^] and university extension feed ingredient reports [^8^]. Both price ranges carry more uncertainty than the food oats price, which is reflected in the confidence ratings in Section 9.2.

### 5.2 Price Verification

**Food oats:**

```
USDA NASS (2025): raw oat grain ~$170-220/t
Milling margin: ~$130-230/t (includes dehulling, kilning, rolling)
Processed food oats: $300-450/t (groats, rolled, steel-cut)
Instant oat products: $500-800/t (retail, with added ingredients)

Adopted: $375/t, the midpoint of the $300–450 range (wholesale, commodity processed oats)
```

**Oat hulls:**

```
Feedipedia indicative value: ~$50-90/t (loose, bulk)
Pelleted hulls: ~$90-120/t
Boiler fuel value: ~$30-50/t (energy content basis)
Oat fiber (processed from hulls): $200-400/t (after extraction and purification)

Adopted: $80/t, the midpoint of the $50–110 range (loose/pelleted mix, bulk)
```

**Oat mill feed:**

```
Feedipedia indicative value: ~$140-190/t
University extension feed reports: ~$150-210/t
Comparable feed ingredients: wheat middlings ~$140-190/t

Adopted: $180/t, the midpoint of the $140–220 range
```

### 5.3 Revenue per Tonne of Oats

| Co-product | Calculation | Revenue (USD/t oats) |
|------------|-------------|---------------------|
| **Food oats** | 0.60 × 375 | **$225.00** |
| **Oat hulls** | 0.25 × 80 | **$20.00** |
| **Oat mill feed** | 0.10 × 180 | **$18.00** |
| **Total** | | **$263.00** |

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
| Food oats | (225.00 ÷ 263.00) × 100 | **85.6%** |
| Oat hulls | (20.00 ÷ 263.00) × 100 | **7.6%** |
| Oat mill feed | (18.00 ÷ 263.00) × 100 | **6.8%** |
| **Total** | | **100.0%** |


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
| Food oats | (0.5400 ÷ 0.8550) × 100 | **63.2%** |
| Oat hulls | (0.2250 ÷ 0.8550) × 100 | **26.3%** |
| Oat mill feed | (0.0900 ÷ 0.8550) × 100 | **10.5%** |
| **Total** | | **100.0%** |

> **Rounding note:** The raw calculations yield 63.16% (food oats), 26.32% (hulls), and 10.53% (mill feed). These round to 63.2%, 26.3%, and 10.5%, which sum to exactly 100.0%.

> **Note on the mass allocation for oat milling:** All three streams carry the same dry matter content (90%), so the mass allocation reduces to the as-is yield split (0.60 / 0.25 / 0.10 divided by 0.95). Unlike systems whose co-products differ sharply in moisture — citrus juice against citrus pulp, for example — the mass column here adds no information beyond the yields themselves. Users comparing methods across crops should keep that in mind.

### 6.3 Comparison: Economic vs. Mass Allocation

| Co-product | Economic Allocation | Mass Allocation | Difference |
|------------|-------------------|----------------|------------|
| Food oats | 85.6% | 63.2% | +22.4 pp |
| Oat hulls | 7.6% | 26.3% | −18.7 pp |
| Oat mill feed | 6.8% | 10.5% | −3.7 pp |

Food oats receive a much larger economic allocation than mass allocation because of their high value per unit mass ($375/t vs. $80/t for hulls and $180/t for mill feed). Oat hulls, which carry 26.3% of the DM, receive only 7.6% of the economic allocation, reflecting their low market value as a roughage/fuel byproduct.

---

## 7. Mass Balance Verification

### 7.1 Input-Output Reconciliation

| Check | Value | Status |
|-------|-------|--------|
| Input: Oats at 12% moisture | 1.000 t | — |
| Input moisture | 12.0% | — |
| Input DM | 0.880 t | — |
| Output: Food oats (as-is) | 0.600 t | ✓ |
| Output: Oat hulls (as-is) | 0.250 t | ✓ |
| Output: Oat mill feed (as-is) | 0.100 t | ✓ |
| Total as-is output | 0.950 t | 95.0% of input |
| Processing losses (as-is) | 0.050 t | 5.0% of input |
| Output DM: Food oats | 0.540 t | ✓ |
| Output DM: Oat hulls | 0.225 t | ✓ |
| Output DM: Oat mill feed | 0.090 t | ✓ |
| Total DM output | 0.855 t | 97.2% of input DM |

### 7.2 DM Balance Detail

| Item | Value | Notes |
|------|-------|-------|
| Input DM (1 t oats at 12% moisture) | 0.8800 t | 1.000 × (1 − 0.12) |
| **Output DM — co-products:** | | |
| Food oats | 0.5400 t | 0.60 t × 90% DM |
| Oat hulls | 0.2250 t | 0.25 t × 90% DM |
| Oat mill feed | 0.0900 t | 0.10 t × 90% DM |
| Total co-product DM | **0.8550 t** | |
| DM balance gap | −0.0250 t | −2.8% of input DM |

> **Balance assessment:** The DM output is 2.8% below the DM input. This gap represents processing losses and is physically valid (output < input). The losses are attributed to:

| Loss type | Estimated magnitude | Basis |
|-----------|-------------------|-------|
| Cleaning (foreign material removal) | ~0.5–1.5% of input DM | Screen and aspiration rejects [^4^] |
| Kilning (thermal decomposition) | ~0.1–0.3% of input DM | Moisture reduction from ~12% to ~10% is captured in the 90% DM value for food oats; only minor thermal decomposition and volatilization contribute to DM loss |
| Milling fines not captured in mill feed | ~0.3–0.5% of input DM | Very fine particles lost in aspiration systems |
| Incomplete dehulling (groat in hull stream) | ~0.5–1.0% of input DM | 92–96% dehulling efficiency [^2^] |
| **Total estimated** | **~1.4–3.3%** | Consistent with the 2.8% gap |

> The 2.8% DM gap is within the expected range of processing losses for oat milling. It is well within the uncertainty of the yield coefficients (each of which has a ±2–3% range); the gap is documented as processing losses.

### 7.3 As-Is Mass Balance

| Item | Value | Notes |
|------|-------|-------|
| Input (oats) | 1.000 t | — |
| **Output:** | | |
| Food oats | 0.600 t | — |
| Oat hulls | 0.250 t | — |
| Oat mill feed | 0.100 t | — |
| **Total output** | **0.950 t** | |
| **Processing losses** | **0.050 t** | 5.0%: cleaning rejects, moisture loss, fines |
| **Balance** | **1.000 t** | ✓ Exact |

---

## 8. Complete Data Table

| Parent Crop | Crop System | Stage | USDA Standard | Standard Moisture | Parent Input Basis | Co-product Stream | Yield (t/t) | Yield Range | Price (USD/t) | Price Range | DM (%) | DM Output (t/t) | Revenue (USD/t) | Econ Alloc (%) | Mass Alloc (%) |
|-------------|-------------|-------|---------------|-------------------|-------------------|-------------------|-------------|-------------|---------------|-------------|--------|-----------------|-----------------|----------------|----------------|
| Oat | Oat milling | Single | 36 lb/bu min test weight (No. 1) | 12% (trading convention) | 1 t oats at 12% moisture | Food oats | 0.60 | 0.58–0.62 | 375 | 300–450 | 90.0 | 0.540 | 225.00 | 85.6 | 63.2 |
| Oat | Oat milling | Single | 36 lb/bu min test weight (No. 1) | 12% (trading convention) | 1 t oats at 12% moisture | Oat hulls | 0.25 | 0.22–0.28 | 80 | 50–110 | 90.0 | 0.225 | 20.00 | 7.6 | 26.3 |
| Oat | Oat milling | Single | 36 lb/bu min test weight (No. 1) | 12% (trading convention) | 1 t oats at 12% moisture | Oat mill feed | 0.10 | 0.08–0.12 | 180 | 140–220 | 90.0 | 0.090 | 18.00 | 6.8 | 10.5 |

> **Note on allocation rounding:** Raw economic allocations are 85.55% (food oats), 7.60% (hulls), and 6.84% (mill feed), rounding to 85.6%, 7.6%, and 6.8% to sum to exactly 100.0% with no adjustment needed. Raw mass allocations are 63.16% (food oats), 26.32% (hulls), and 10.53% (mill feed), rounding to 63.2%, 26.3%, and 10.5% to sum to exactly 100.0%.



---

## 9. Data Quality and Limitations

### 9.1 High-Confidence Data

| Data Point | Confidence | Source |
|------------|-----------|--------|
| Food oats yield (0.60 t/t) | **High** | Milling literature [^2^][^4^]; consistent with the dehulling reconciliation in Section 4.1 |
| Oat hulls yield (0.25 t/t) | **High** | Milling literature [^2^][^6^]; reproduced by the dehulling reconciliation in Section 4.1 |
| Oat hulls DM% (90%) | **High** | Feedipedia [^6^]: 90.3% average across 88 samples, range 88.4–92.7% |
| Food oats DM% (90%) | **High** | Post-kilning food oat specification, 9–11% moisture [^2^][^4^] |
| Oat mill feed yield (0.10 t/t) | **Medium-High** | Milling literature [^4^][^7^]; varies with mill configuration and product mix |
| Oat mill feed DM% (90%) | **Medium-High** | Industry specification [^7^]; typical range 88–93% |
| USDA test weight grades (36 lb/bu No. 1, 27 lb/bu No. 4) | **High** | Confirmed by 7 CFR 810.1004 [^1^] |
| Standard bushel weight (32 lb/bu) | **High** | USDA standard for trading and reporting |

### 9.2 Medium-Confidence Data

| Data Point | Confidence | Source |
|------------|-----------|--------|
| Food oats price ($375/t) | **Medium** | Depends on product mix (groats vs. rolled vs. instant) and market conditions |
| Oat hulls price ($80/t) | **Medium** | Small market with limited price transparency; varies with form (loose vs. pelleted) |
| Oat mill feed price ($180/t) | **Medium** | Niche product; limited market data |
| Processing losses (2.8% DM) | **Medium** | Estimated from yield balance; not directly measured |

### 9.3 Known Limitations

1. **DM gap (2.8%):** The DM output (0.855 t) is 2.8% below the DM input (0.880 t). This gap represents processing losses (cleaning, fines, incomplete dehulling, minor thermal decomposition) and is documented in Section 7.2. The gap is within the expected range for oat milling. 

2. **"Food oats" is an aggregate category:** The table treats all food-grade oat products (groats, rolled oats, steel-cut oats, oat flour) as a single co-product. In reality, these products have different prices (groats ~$300/t, rolled oats ~$400/t, instant oats ~$600/t) and slightly different yields. The $375/t price is a weighted average for commodity food oats at the midpoint of the verified wholesale range.

3. **Oat hulls value varies with use:** Hulls sold as animal feed roughage ($50–70/t) are worth much less than hulls used for oat fiber extraction ($200–400/t after processing). The $80/t price reflects the most common bulk use. If a milling plant extracts fiber from hulls, the hulls allocation would increase significantly.

4. **Byproduct price uncertainty:** Oat hulls and oat mill feed are niche products with limited public price data. The prices cited here are based on Feedipedia indicative values and university extension feed reports, supplemented by industry knowledge. Actual transaction prices may vary significantly from these estimates.

5. **Hulless oats:** Hulless (naked) oat varieties have very low hull content (~5–10% vs. 22–30% for covered oats) and higher groat yields. The yields and allocations in this table would be significantly different for hulless oats. A separate table would be needed.

6. **Dehulling efficiency:** The 0.60 t/t food oats yield assumes 92–96% dehulling efficiency. Incomplete dehulling means some groat material is lost with the hulls (reducing food oats yield) and some hull fragments remain with the groats (reducing food oats quality). This is a source of yield variability captured in the ranges.

7. **Seasonal and regional variation:** Oat quality (test weight, groat percentage, moisture) varies significantly by growing region and harvest conditions. Northern-grown oats tend to have higher groat content than southern-grown oats.

8. **Oat hulls protein content:** Feedipedia [^6^] reports an average crude protein of 5.2% DM across 107 samples, range 2.5–8.4%. Well-cleaned hulls sit at the low end; commercial hulls carry some adhering endosperm and typically run 5–6% DM. The ~3–6% figure quoted in Section 5.1 is used to contrast hulls with mill feed on feeding value, not as a specification.

9. **Oat mill feed protein content:** Feedipedia [^7^] describes oat mill feed as "typically a little richer in protein (8%)" with 25% starch and 22% fibre. This document uses **8–13% CP (DM basis)**: 8% is the Feedipedia figure and 13% represents mill feed carrying a higher proportion of bran. Mill feed composition depends heavily on how a given mill splits its sifting streams, so this is a wider band than for hulls.

---
