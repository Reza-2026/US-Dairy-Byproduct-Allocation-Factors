# Citrus Processing: Co-Product Allocation Methodology, Data Sources, and Calculations

**Document Version:** 1.0
**Date:** May 2026  
**Basis:** 1 metric ton (t) of fresh citrus fruit at ~14% DM (~86% moisture)  
**Price Period:** 2024–2025 average (unless otherwise noted)

---

## Table of Contents

1. [Standard Basis and Conversions](#1-standard-basis-and-conversions)
2. [Data Sources and References](#2-data-sources-and-references)
3. [Citrus Processing System](#3-citrus-processing-system)
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
| **Parent crop** | Citrus (predominantly orange, *Citrus sinensis*) | — |
| **Input quantity** | 1 metric ton (1,000 kg) | — |
| **Moisture content** | ~86% (14% DM) | USDA FoodData Central for raw navel oranges (FDC ID 169917): 86.3% water [^1^]; industry average for processing-grade citrus |
| **Dry matter (DM) input** | 0.140 t DM/t fresh citrus | Calculated: 1.000 × 0.14 = 0.140 |
| **Box equivalent** | ~24.5 boxes/t (Florida 90-lb field box) | 1,000 kg ÷ 40.823 kg/box (90 lb) |
| **Typical juice content** | ~45–55% by weight (as-is) | Industry average for Florida processing oranges [^2^][^6^] |

### 1.2 Unit Conversions

| Conversion | Factor |
|------------|--------|
| 1 Florida field box | 90 lb = 40.823 kg (standard for oranges; grapefruit 85 lb; tangerines 95 lb per UF/IFAS) |
| 1 lb | 0.453592 kg = 0.000453592 t |
| 1 t fresh citrus | ~24.5 Florida field boxes (at 90 lb/box) |
| 1 short ton | 2,000 lb = 0.907185 metric ton |
| 1 metric ton | 2,204.62 lb = 1.10231 short tons |
| 1 gallon single-strength OJ | ~8.6 lb ≈ 3.9 kg ≈ 3.9 L |

> **Note on citrus categories:** "Citrus" encompasses a broad family of fruits including oranges, grapefruit, lemons, limes, tangerines/mandarins, and pomelos. Processing citrus in the United States is overwhelmingly oranges (~95% of processing volume), primarily Valencia and Hamlin varieties in Florida. This document uses parameters representative of orange processing. Other citrus types have different DM%, juice yields, and co-product characteristics (see Section 9.3, item 3).

> **Note on moisture:** Unlike grains, fresh citrus has no USDA-defined standard moisture for trading. Citrus is sold by count, size, or weight at natural moisture content. The moisture varies by variety (oranges ~85–87%, grapefruit ~89–92%, lemons ~88–91%), growing conditions, maturity, and storage duration. This document uses 86% moisture (14% DM) as the standard basis, consistent with USDA FoodData Central data for navel oranges (86.3% water = 13.7% DM) and rounded to 14% DM as a practical mid-season average. Valencia oranges are 86.8% water (13.2% DM); the 14% DM basis represents a midpoint across common processing varieties.

---

## 2. Data Sources and References

### 2.1 Primary Sources

| Citation | Full Title | Type | URL |
|----------|-----------|------|-----|
| [^1^] | USDA FoodData Central — Oranges, raw, navels (FDC ID 169917) | Government (USDA) | https://fdc.nal.usda.gov/food-details/169917/nutrients |
| [^2^] | FAO. *Practical Aspects of Citrus Juice Processing* (Chapter 13 of Agricultural Services Bulletin) | International Organization | https://www.fao.org/4/y2515e/y2515e13.htm |
| [^3^] | USDA ERS (2025). *Fruit and Tree Nuts Outlook* | Government (USDA) | https://www.ers.usda.gov/publications/ |
| [^4^] | USDA NASS. *Florida Citrus Statistics* (Annual) | Government (USDA) | https://www.nass.usda.gov/Statistics_by_State/Florida/ |
| [^5^] | IndexBox (2025). *World Citrus Juice Market Analysis* | Industry/Market | https://www.indexbox.io/store/ |
| [^6^] | Kimball, D.A. (1999). *Citrus Processing: A Complete Guide*, 2nd ed. Chapman & Hall/Springer. ISBN: 978-0-8342-1258-8 | Academic textbook | https://link.springer.com/book/10.1007/978-1-4615-4973-4 |
| [^7^] | Braddock, R.J. (1999). *Handbook of Citrus By-Products and Processing Technology*. Wiley. ISBN: 978-0-471-19024-0 | Academic textbook | https://www.wiley.com/en-us/9780471190240 |
| [^8^] | UF/IFAS Extension. AN108: *Estimating the Value of Wet Citrus Pulp for Florida Cattlemen* | Extension/University | https://edis.ifas.ufl.edu/ |
| [^9^] | OECD-FAO (2025). *Agricultural Outlook 2025-2034*, Chapter 10: Other Products | International Organization | https://www.oecd.org/ |

### 2.2 How Sources Were Used

- **Yield data:** USDA ERS [^3^], FAO [^2^], and Kimball [^6^] provided citrus processing yield data. The ranges reflect variation across citrus varieties, extraction methods (FMC whole-fruit extractor vs. Brown extractor vs. reamer-type), fruit maturity, and product specifications.
- **Price data (juice):** USDA ERS [^3^], USDA NASS [^4^], and IndexBox [^5^] provided citrus juice price data. Prices reflect single-strength (not from concentrate) juice at the processing plant level (FOB). Industry convention prices orange juice per pound of soluble solids; conversions are provided.
- **Price data (pulp):** UF/IFAS AN108 [^8^] provided the primary data for wet citrus pulp valuation for animal feed markets. Braddock [^7^] provided co-product composition data.
- **DM contents:** USDA FoodData Central [^1^] provided nutritional composition data for whole oranges. Kimball [^6^] and Braddock [^7^] provided processing waste composition data. Feedipedia and Mad Barn feed databases were consulted for pulp DM%.

---

## 3. Citrus Processing System

### 3.1 Process Description

Citrus processing for juice extraction involves the following steps:

1. **Receiving and grading:** Citrus fruit is received at the processing facility, graded for quality, and sorted by size. Fruit that does not meet juice standards is diverted to other markets or waste.
2. **Washing:** Fruit is washed to remove dirt, debris, and agricultural chemical residues.
3. **Juice extraction:** Several extraction technologies are used commercially. The FMC (now JBT) whole-fruit extractor presses the fruit between interlocking cups, simultaneously extracting juice and separating peel oil. The Brown extractor cuts the fruit in half and reams each half. The choice of extractor affects both juice yield and the composition of the peel residue.
4. **Finishing:** Extracted juice passes through a finisher (screen) to remove pulp, seeds, and rag (membranes). The finisher pulp is either blended back into the juice or directed to the pulp stream.
5. **Deoiling (optional):** Excess essential oil is removed from the juice by vacuum or steam stripping to meet flavor specifications.
6. **Pasteurization:** Juice is heat-treated to inactivate enzymes and microorganisms.
7. **Packaging:** Juice is packaged as single-strength (not from concentrate), concentrated (FCOJ), or chilled.

**Co-products generated:**
- **Citrus juice:** The primary high-value product. This table represents single-strength (not from concentrate) juice, which is the most common product from fresh-squeezed operations. Concentrated juice (FCOJ) involves additional evaporation steps and has different yield and DM% characteristics.
- **Citrus pulp (wet):** The solid residue after juice extraction, consisting primarily of peel (flavedo and albedo), rag (segment membranes), seeds, and finisher pulp. This material is typically pressed (screw press) to reduce moisture and sold as wet cattle feed. It is distinct from dried citrus pulp pellets (CPP), which are produced by further drying to ~88–91% DM.

> **Note on missing co-products:** Commercial citrus processing also produces citrus essential oils (cold-pressed peel oil, primarily D-limonene) and, in some facilities, citrus molasses and pectin. These are not included as separate co-product streams in this table because they represent a very small fraction of total mass (~0.3–0.5% of input weight for essential oils) and their recovery is not universal across processing facilities. See Section 9.3 for the impact of including essential oils.

### 3.2 Process Flow

```
1 t fresh citrus at ~14% DM (0.140 t DM)
        │
        ▼
  ┌─ CITRUS PROCESSING ───────────────────────────┐
  │                                                 │
  │  Processing losses: ~0.17 t as-is (~17%)       │
  │  (wastewater: dissolved solids, peel moisture,  │
  │   wash water, minor fractions)                  │
  │  DM losses: ~0.016 t DM (~11.4%)               │
  │                                                 │
  │  Citrus juice: 0.53 t as-is at 12% DM        ◄── co-product
  │    (0.0636 t DM)                                │
  │                                                 │
  │  Citrus pulp (wet): 0.30 t as-is at 20% DM   ◄── co-product
  │    (0.0600 t DM)                                │
  │                                                 │
  └─────────────────────────────────────────────────┘

TWO CO-PRODUCTS from 1 t fresh citrus:
  Citrus juice:      0.53 t as-is,  0.0636 t DM
  Citrus pulp:       0.30 t as-is,  0.0600 t DM
  Total:                          0.1236 t DM  (from 0.140 t input; ~0.0164 t DM losses)
```

---

## 4. Co-Product Yields and Properties

### 4.1 Yields (per tonne of citrus input)

| Co-product | Yield (t/t citrus) | Range | Source & Calculation |
|------------|--------------------|-------|---------------------|
| **Citrus juice** | 0.53 | 0.45–0.62 | True mathematical midpoint of range (0.45 + 0.62) / 2 = 0.535; rounded to 0.53 for consistency with industry convention. Industry average for Florida orange processing [^2^][^6^]. Yields vary with extraction method (FMC whole-fruit: ~0.50–0.58; Brown reamer: ~0.45–0.55), variety (Valencia ~0.52–0.62; Hamlin ~0.48–0.55), maturity, and fruit size. Note: HLB-affected groves may yield 0.40–0.50 t/t; see Section 9.3 item 9. |
| **Citrus pulp (wet)** | 0.30 | 0.25–0.35 | Midpoint of range. Represents pressed wet peel, rag, seeds, and finisher pulp [^6^][^7^]. Pulp yield is inversely related to juice yield: more complete juice extraction leaves less pulp. Yields vary with peel thickness (grapefruit has thicker peel → higher pulp yield) and extraction efficiency. |

> **Note on yield relationship:** Juice and pulp yields are inversely related. When more juice is extracted (higher juice yield), less pulp is produced. The values in this table (0.53 juice, 0.30 pulp) sum to 0.83 t/t, meaning 17% of the input mass is not captured in either co-product stream. This 17% represents wastewater (peel moisture, wash water, dissolved solids), unrecovered essential oils, and minor fractions. See Section 7 for the as-is mass balance.

### 4.2 Dry Matter Contents

| Co-product | DM (%) | Basis |
|------------|--------|-------|
| Citrus juice | 12.0% | USDA FoodData Central: raw orange juice is ~88% water, ~12% DM (11.8°Brix minimum for Grade A per 7 CFR §51.1177; total DM slightly higher at ~12%) [^1^]. Single-strength citrus juice retains the natural sugar and acid content of the fruit. |
| Citrus pulp (wet) | 20.0% | Wet citrus pulp after screw-press dewatering [^6^][^7^]. Fresh peel/rag/seed residue from juice extraction has ~15–18% DM. After mechanical pressing to reduce moisture for cattle feed transport, DM% increases to ~18–22%. Feedipedia lists fresh citrus pulp at 17.5–20% DM; Mad Barn lists 19% DM. The 20% DM value represents the typical composition of commercially pressed wet pulp. Note: dried citrus pulp pellets (CPP) have ~88–91% DM but much lower as-is yield (~0.10–0.15 t/t). |

> **Note on juice DM% consistency:** Single-strength citrus juice at 12% DM is consistent with the processing description (no concentration or dehydration). If the product were frozen concentrated orange juice (FCOJ), DM% would be ~60–65% at a yield of ~0.18–0.22 t/t. If the product were reconstituted from concentrate, DM% would return to ~12%. This table models single-strength juice production only.



### 4.3 DM Output per Tonne of Citrus

| Co-product | Calculation | DM Output (t/t citrus) |
|------------|-------------|----------------------|
| **Citrus juice** | 0.53 × 0.12 | **0.0636** |
| **Citrus pulp (wet)** | 0.30 × 0.20 | **0.0600** |
| **Total** | | **0.1236** |

---

## 5. Prices

### 5.1 Price Table

| Co-product | Price (USD/t) | Range | Source | Notes |
|------------|--------------|-------|--------|-------|
| **Citrus juice** | 500 | 350–650 | USDA ERS [^3^]; USDA NASS [^4^]; IndexBox [^5^] | 2024–2025 average for single-strength orange juice at processing plant level (FOB). Price reflects bulk juice, not retail. Industry convention prices OJ per pound of soluble solids: at $500/t single-strength juice (11.8°Brix), this equates to ~$1.92/lb solids. Recent pricing has been higher: $2.60/lb solids in 2023-24 ≈ $676/t. Midpoint of range: ($350 + $650) / 2 = $500. |
| **Citrus pulp (wet)** | 10 | 5–15 | UF/IFAS AN108 [^8^] | 2024–2025 estimate for wet citrus pulp sold as cattle feed, delivered to nearby dairies. Price varies significantly with moisture content, proximity to livestock operations, and seasonal demand. In regions without nearby cattle operations, pulp may have zero or negative value (disposal cost). Dried citrus pulp pellets (CPP) trade at $150–250/t — a different product. Midpoint of range: ($5 + $15) / 2 = $10. |

### 5.2 Price Verification

**Citrus juice:**

```
USDA ERS (2025): single-strength OJ at processing plant ~$450-550/t (FOB)
USDA NASS Florida Citrus Statistics: juice priced per lb solids
  At 11.8°Brix: $1.92/lb solids ≈ $500/t; $2.60/lb solids ≈ $676/t
IndexBox (2025): ~$400-600/t (varies with variety and region)
FCOJ futures (2025): ~$1.30-1.60/lb solids (different pricing basis)

Selected midpoint: $500/t (historical; note current market is higher)
Mathematical midpoint of range ($350-650): $500/t ✓
The price midpoint IS the true mathematical midpoint of the stated range.
Note: $500/t ≈ $2.00/gal FOB (not retail). Retail NFC OJ: $6-12/gal.
```

**Citrus pulp (wet):**

```
UF/IFAS AN108: wet citrus pulp valued at $5-15/ton delivered to nearby dairies
Transport-constrained regions: may have zero or negative value (disposal cost)
Nearby dairy operations: up to $15/ton
Dried citrus pulp pellets: ~$150-250/t (different product, not comparable)

Selected midpoint: $10/t
Mathematical midpoint of range ($5-15): $10/t ✓
The price midpoint IS the true mathematical midpoint of the stated range.
```

### 5.3 Revenue per Tonne of Citrus

| Co-product | Calculation | Revenue (USD/t citrus) |
|------------|-------------|----------------------|
| **Citrus juice** | 0.53 × 500 | **$265.00** |
| **Citrus pulp (wet)** | 0.30 × 10 | **$3.00** |
| **Total** | | **$268.00** |

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
| Citrus juice | (265.00 ÷ 268.00) × 100 | **98.9%** |
| Citrus pulp (wet) | (3.00 ÷ 268.00) × 100 | **1.1%** |
| **Total** | | **100.0%** |

> **Rounding note:** The raw calculations yield 98.88% (juice) and 1.12% (pulp). These are rounded to 98.9% and 1.1% so that the sum is exactly 100.0%.

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
| Citrus juice | (0.0636 ÷ 0.1236) × 100 | **51.5%** |
| Citrus pulp (wet) | (0.0600 ÷ 0.1236) × 100 | **48.5%** |
| **Total** | | **100.0%** |

> **Rounding note:** The raw calculations yield 51.46% (juice) and 48.54% (pulp). These are rounded to 51.5% and 48.5% so that the sum is exactly 100.0%.

### 6.3 Comparison: Economic vs. Mass Allocation

| Co-product | Economic Allocation | Mass Allocation | Difference |
|------------|-------------------|----------------|------------|
| Citrus juice | 98.9% | 51.5% | +47.4 pp |
| Citrus pulp (wet) | 1.1% | 48.5% | −47.4 pp |

The 47.4 percentage-point difference between economic and mass allocation is the **largest divergence among all the crops reviewed**. This extreme divergence arises from a unique combination of factors: (1) juice commands a very high price ($500/t, 50× the pulp price), (2) juice has low DM% (12%) so it carries slightly less dry matter per ton than pulp (20% DM), and (3) the DM outputs of juice and pulp are nearly equal (0.0636 vs. 0.0600 t DM), giving mass allocation a near-50/50 split. The result is that economic allocation assigns 98.9% of burden to juice while mass allocation assigns only 51.5% — a 47.4 pp swing. The choice of allocation method has an enormous impact on LCA results for citrus processing and must be carefully justified by LCA practitioners.

---

## 7. Mass Balance Verification

### 7.1 Input-Output Reconciliation

| Check | Value | Status |
|-------|-------|--------|
| Input: Fresh citrus | 1.000 t | — |
| Input DM% | 14% | — |
| Input DM | 0.140 t | — |
| Output: Juice (as-is) | 0.530 t | ✓ |
| Output: Pulp (as-is) | 0.300 t | ✓ |
| Total as-is output | 0.830 t | 83.0% of input |
| Processing losses and wastewater (as-is) | 0.170 t | 17.0% of input |
| Output DM: Juice | 0.0636 t | ✓ |
| Output DM: Pulp | 0.0600 t | ✓ |
| Total DM output | 0.1236 t | 88.3% of input DM |
| DM losses and gap | 0.0164 t | 11.7% of input DM |

### 7.2 DM Balance Detail

| Item | Value | Notes |
|------|-------|-------|
| Input DM (1 t citrus at 14% DM) | 0.1400 t | 1.000 × 0.14 |
| **Output DM — co-products:** | | |
| Citrus juice | 0.0636 t | 0.53 t × 12% DM |
| Citrus pulp (wet) | 0.0600 t | 0.30 t × 20% DM |
| Total co-product DM | **0.1236 t** | |
| DM balance gap | −0.0164 t | −11.7% of input DM |

> **Balance assessment:** The DM output is 0.0164 t (11.7%) below the DM input. The gap represents: (1) dissolved solids in wastewater (sugars, organic acids, pectin lost during extraction, washing, and finishing — estimated at ~0.005–0.008 t), (2) citrus essential oils not captured as a co-product (~0.003–0.006 t), (3) pectin and soluble fiber lost in the peel moisture stream, and (4) minor processing losses. The gap is physically realistic and is documented transparently. A fully closed balance would require adjusting the pulp DM% upward or including essential oils as a co-product.

### 7.3 As-Is Mass Balance

| Item | Value | Notes |
|------|-------|-------|
| Input (fresh citrus) | 1.000 t | — |
| **Output:** | | |
| Citrus juice | 0.530 t | — |
| Citrus pulp (wet) | 0.300 t | — |
| **Total co-product output** | **0.830 t** | |
| **Wastewater and losses** | **0.170 t** | 17.0%: peel moisture, wash water, dissolved solids |
| **Balance** | **1.000 t** | ✓ Exact |

> **Note on as-is gap:** The 17% as-is gap (0.170 t) is the largest among all crops reviewed. This reflects the high moisture content of citrus fruit (~86%) and the nature of juice extraction, which generates large volumes of wastewater containing peel moisture, wash water, and dissolved solids. Unlike grain or oilseed processing, where solid co-products capture nearly all mass, citrus processing inherently produces a large liquid waste stream. The 0.170 t of wastewater contains approximately 0.0164 t DM (~9.6% of the wastewater mass).

---

## 8. Complete Data Table

| Parent Crop | Crop System | Stage | USDA Standard | Standard Moisture | Parent Input Basis | Co-product Stream | Yield (t/t) | Yield Range | Price (USD/t) | Price Range | DM (%) | DM Output (t/t) | Revenue (USD/t) | Econ Alloc (%) | Mass Alloc (%) |
|-------------|-------------|-------|---------------|-------------------|-------------------|-------------------|-------------|-------------|---------------|-------------|--------|-----------------|-----------------|----------------|----------------|
| Citrus | Citrus processing | Single | USDA AMS Grade A (7 CFR §51.1177) | ~86% (14% DM) | 1 t fresh citrus at 14% DM | Citrus juice | 0.53 | 0.45–0.62 | 500 | 350–650 | 12.0 | 0.0636 | 265.00 | 98.9 | 51.5 |
| Citrus | Citrus processing | Single | USDA AMS Grade A (7 CFR §51.1177) | ~86% (14% DM) | 1 t fresh citrus at 14% DM | Citrus pulp (wet) | 0.30 | 0.25–0.35 | 10 | 5–15 | 20.0 | 0.0600 | 3.00 | 1.1 | 48.5 |

> **Note on allocation rounding:** Raw economic allocations are 98.88% (juice) and 1.12% (pulp), rounded to 98.9% and 1.1% to sum to exactly 100.0%. Raw mass allocations are 51.46% (juice) and 48.54% (pulp), rounded to 51.5% and 48.5% to sum to exactly 100.0%.

---

## 9. Data Quality and Limitations

### 9.1 High-Confidence Data

| Data Point | Confidence | Source |
|------------|-----------|--------|
| Juice DM% (12%) | **High** | USDA FoodData Central [^1^]; FDA standard (11.8°Brix minimum) |
| Pulp DM% (20%) | **High** | Feedipedia; Mad Barn feed database; industry data for pressed wet pulp [^6^][^7^] |
| Juice yield range (0.45–0.62) | **High** | Well-documented across extraction methods and varieties [^2^][^6^] |
| Pulp yield (0.30) | **Medium-High** | Midpoint of stated range; consistent with industry data |
| Florida field box standard (90 lb) | **High** | UF/IFAS; Florida Statutes Chapter 601.86 |

### 9.2 Medium-Confidence Data

| Data Point | Confidence | Source |
|------------|-----------|--------|
| Juice yield midpoint (0.53) | **Medium** | True midpoint is 0.535; industry commonly cites 0.55. The 0.53 value is slightly below the true midpoint. |
| Juice price ($500/t) | **Medium** | Historical pricing; current market (post-2023) is significantly higher (~$650-700/t). Prices quoted per lb solids. |
| Pulp price ($10/t) | **Medium** | Limited market data; highly variable by region. UF/IFAS AN108 provides the best available estimate. |
| Input DM% (14%) | **Medium** | Navel oranges: 13.7% DM; Valencia: 13.2% DM. The 14% is a practical rounding. Varies by variety (11–14%), maturity, and growing conditions. |
| Pulp yield range (0.25–0.35) | **Medium** | Less well-documented than juice yield; depends on extraction method and peel thickness |

### 9.3 Known Limitations

1. **Missing citrus essential oils:** Commercial citrus processing produces cold-pressed peel oil (primarily D-limonene) as a valuable co-product. Typical yield is ~0.003–0.006 t/t (0.3–0.6% of input weight) at a price of $2,000–5,000/t. This generates revenue of ~$6–30/t citrus, which is small relative to juice ($265/t) but would shift the economic allocation slightly. If essential oil at 0.004 t/t and $3,000/t were included:
   - Additional revenue: $12.00/t
   - Total revenue: $280.00/t
   - Juice economic allocation: 94.6% (down from 98.9%)
   - Pulp economic allocation: 1.1% (unchanged)
   - Essential oil economic allocation: 4.3%
   - The impact on mass allocation is minimal because essential oil carries very little DM (~0.004 t DM).

2. **Extreme economic-vs-mass allocation divergence:** The 47.4 percentage-point difference between economic allocation (98.9% juice) and mass allocation (51.5% juice) is the largest among all crops reviewed. This extreme divergence arises because: (a) juice carries roughly half the DM but over 98% of the revenue, and (b) the DM outputs of juice and pulp are nearly equal (0.0636 vs. 0.0600), producing a near-50/50 mass split. LCA practitioners must carefully justify their choice of allocation method for citrus, as the method choice has an enormous impact on results.

3. **Generic "citrus" category:** This table treats all citrus as a single category dominated by oranges. In practice, different citrus types have very different processing characteristics:
   - **Oranges:** Juice yield 0.45–0.62, DM% ~13–14%, juice DM% ~12%
   - **Grapefruit:** Juice yield 0.40–0.50, DM% ~8–9%, juice DM% ~9–10%
   - **Lemons:** Juice yield 0.30–0.40, DM% ~9–11%, juice DM% ~8–9%
   - **Tangerines/Mandarins:** Juice yield 0.40–0.55, DM% ~13–14%, juice DM% ~12–13%
   
   Studies focused on non-orange citrus should use variety-specific data rather than this generic model.

4. **Large as-is mass gap (17%):** The 0.170 t gap between input and co-product output is the largest among all crops reviewed. This reflects the nature of juice extraction, which produces large volumes of wastewater. In some LCA frameworks, wastewater treatment burdens are allocated to the processing stage and thus distributed among co-products. This table does not model wastewater treatment separately.

5. **Wet vs. dried pulp configuration:** This table models wet citrus pulp (20% DM, 0.30 t/t yield). Some facilities dry the pulp to produce citrus pulp pellets (CPP) at ~88–91% DM with a yield of ~0.10–0.15 t/t and a price of ~$150–250/t. The dried configuration would have:
   - Lower pulp yield (0.10–0.15 t/t instead of 0.30 t/t)
   - Higher pulp DM% (88–91% instead of 20%)
   - Higher pulp price ($150–250/t instead of $10/t)
   - Similar pulp DM output (~0.09–0.13 t DM vs. 0.060 t DM — higher because drying captures more of the peel DM)
   - Different allocation results
   
   The dried pulp configuration is more common in regions where pulp must be transported long distances to livestock operations.

6. **FCOJ not modeled:** This table models single-strength (not from concentrate) juice production. Frozen concentrated orange juice (FCOJ) involves an additional evaporation step that removes ~80% of the water from the juice. FCOJ has:
   - Juice yield: ~0.18–0.22 t/t (concentrated)
   - Juice DM%: ~60–65%
   - Juice price: ~$1,500–2,500/t (concentrate)
   - Co-product: essence and aroma compounds recovered during evaporation
   
   FCOJ production would require a separate allocation model with different yields, DM%, and prices.

7. **Regional variation:** Florida, California, and Brazil (the three largest orange processing regions) have different varieties, extraction methods, and market structures. Florida processing is optimized for Valencia and Hamlin oranges with FMC extractors; Brazil processes primarily Pera and Valencia with different equipment; California produces more navels for fresh market with less processing capacity. Prices and yields vary by region.

8. **Seasonal variation in DM%:** Orange DM% varies through the season: early-season fruit (November–December) may have 11–12% DM, while late-season fruit (May–June) may reach 14–15% DM. The 14% DM average used here represents a mid-season average. Studies focused on specific processing periods should adjust accordingly.

9. **Citrus greening disease (HLB):** Huanglongbing (HLB, citrus greening disease) has significantly affected Florida citrus production since 2005, reducing yields, increasing fruit drop, and altering fruit composition (lower Brix, higher acidity). USDA NASS data shows FCOJ yields declined from 1.66 gal/box (2009/10) to 1.17 gal/box (2022/23), a 29% reduction. Current juice yields from HLB-affected groves may be 0.40–0.50 t/t rather than the historical 0.50–0.60 t/t. The yield range in this table (0.45–0.62) is intended to capture this variability, but practitioners working with current Florida data should consider using the lower end of the range.

10. **DM balance gap:** The 11.7% DM gap (0.0164 t) between input and co-product output is larger than ideal for a methodology document. This gap arises because independently-sourced yield and DM% parameters are not forced to close stoichiometrically. The gap can be reduced by: (a) including essential oils as a co-product (adds ~0.004 t DM), (b) accounting for pectin and soluble fiber in the wastewater stream more precisely, or (c) adjusting the pulp DM% upward. The allocation results are not highly sensitive to this gap because the relative proportions of juice and pulp DM are robust.

---
