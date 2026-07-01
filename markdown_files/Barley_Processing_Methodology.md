# Barley Processing: Co-Product Allocation Methodology, Data Sources, and Calculations

**Document Version:** 1.0
**Date:** May 2026  
**Basis:** 1 metric ton (t) of barley at 12% moisture (common storage moisture; USDA trading standard is 14.5%)  
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

---

## 1. Standard Basis and Conversions

### 1.1 Parent Input Definition

| Parameter | Value | Source |
|-----------|-------|--------|
| **Parent crop** | Barley (*Hordeum vulgare*) | — |
| **Input quantity** | 1 metric ton (1,000 kg) | — |
| **Moisture content** | 12.0% | Common storage moisture for calculation basis. USDA trading standard is 14.5% per 7 CFR Part 1421 [^1^] |
| **Dry matter (DM) input** | 0.880 t DM/t barley | Calculated: 1.000 × (1 − 0.12) = 0.880 |
| **Bushel equivalent** | 45.93 bushels/t | 1,000 kg ÷ 21.772 kg/bu (48 lb at standard moisture) |
| **Bushel weight** | 48.0 lb (21.772 kg) | USDA standard test weight for barley [^1^] |

### 1.2 Unit Conversions

| Conversion | Factor |
|------------|--------|
| 1 bushel barley | 48.0 lb = 21.772 kg (standard; varies 45–50 lb by type and grade) |
| 1 lb | 0.453592 kg = 0.000453592 t |
| 1 t barley | 45.93 bushels (at 48 lb/bu) |

> **Note on barley types:** Two main types are used in malting: **2-row barley** (higher starch, lower protein, preferred for brewing) and **6-row barley** (higher protein, higher enzyme activity, used in some North American brewing with adjuncts). USDA grade minimum test weights: 2-row U.S. No. 1 = 50 lb/bu, No. 2+ = 48 lb/bu; 6-row U.S. No. 1 = 47 lb/bu, No. 2 = 45 lb/bu (7 CFR §810.204–205) [^1^]. The 48 lb/bu standard is used here for consistency.

---

## 2. Data Sources and References

### 2.1 Primary Sources

| Citation | Full Title | Type | URL |
|----------|-----------|------|-----|
| [^1^] | USDA AMS/FGIS — Grain Standards for Barley (formerly GIPSA) | Government (USDA) | https://www.ams.usda.gov/grades-standards/barley-standards |
| [^2^] | Brewers Association. *Malting Barley Characteristics for Craft Brewers* (and related barley resources at /resource-hub/barley/) | Industry | https://www.brewersassociation.org/resource-hub/barley/ |
| [^3^] | Briggs, D.E., Hough, J.S., Stevens, R. & Young, T.W. (1981). *Malting and Brewing Science*, 2nd ed. Vols. 1 & 2. Chapman & Hall/Springer. | Academic textbook | https://link.springer.com/book/10.1007/978-1-4615-1743-1 |
| [^4^] | Mussatto, S.I., Dragone, G. & Roberto, I.C. (2006). "Brewers' spent grain: generation, characteristics and potential applications." *Journal of Cereal Science*, 43(1), 1–14. | Academic | https://doi.org/10.1016/j.jcs.2005.06.001 |
| [^5^] | IndexBox (2025). *World Malt Market Analysis* | Industry/Market | https://www.indexbox.io/store/world-malt-market-analysis-forecast-size-trends-and-insights |
| [^6^] | IndexMundi. *Barley Monthly Price* | Market Data | https://www.indexmundi.com/commodities/?commodity=barley |
| [^7^] | USDA FAS (2026). *Grain: World Markets and Trade* | Government (USDA) | https://apps.fas.usda.gov/psdonline/circulars/grain.pdf |
| [^8^] | Thomas, K.R. & Rahman, P.K.S.M. (2006). "Brewery wastes. Strategies for sustainability. A review." *Aspects of Applied Biology*, 80, 155–162. | Academic | Available via CABI Digital Library |
| [^9^] | Tridge (2025). *Barley Malt Price in United States* | Industry/Market | https://dir.tridge.com/prices/barley-malt/US |
| [^10^] | Briggs, D.E., Boulton, C.A., Brookes, P.A. & Stevens, R. (2004). *Brewing: Science and Practice*. Woodhead Publishing (now Elsevier). | Academic textbook | https://www.elsevier.com/books/brewing-science-and-practice/briggs/978-1-85573-906-1 |

### 2.2 How Sources Were Used

- **Yield data (malting):** Brewers Association [^2^] and Briggs et al. [^3^] provided malting yield data and malt loss factors (respiration, rootlet removal, steeping/screening losses).
- **Yield data (brewing):** Mussatto et al. [^4^] provided brewers spent grain (BSG) yield and composition data. Briggs et al. [^10^] provided beer yield data from malt.
- **Price data (malt):** USDA FAS [^7^] and IndexBox [^5^] provided barley and malt price data from global markets.
- **Price data (beer):** Industry estimates and market data from IndexBox [^5^] informed brewery-gate bulk beer prices.
- **Price data (BSG):** Thomas & Rahman [^8^] and Mussatto et al. [^4^] provided BSG price estimates for dried feed-grade material.
- **Price data (malt sprouts):** Comparable feed ingredients (DDGS, corn gluten feed) informed malt sprouts pricing [^9^].
- **DM contents:** Briggs et al. [^3^][^10^] provided malt and beer DM specifications. Mussatto et al. [^4^] provided BSG DM content.
- **Bushel weight and grading:** USDA AMS/FGIS [^1^] provided barley grade standards and test weight requirements.
---

## 3. Process Description

Barley processing involves two sequential stages: **malting** followed by **brewing**. Both stages produce co-products, and the final allocation must assign the original barley grain's environmental burden across all three final co-products: **beer, brewers spent grain (BSG), and malt sprouts**.

### 3.1 Stage 1: Malting

Barley malting converts raw barley into malt through controlled germination and kilning:

1. **Steeping:** Soak barley in water to raise moisture from ~12% to ~44–48% [^3^][^10^].
2. **Germination:** Allow barley to germinate for 4–6 days. Rootlets (sprouts) grow, and enzymes develop [^3^].
3. **Kilning:** Dry the germinated barley (green malt) to reduce moisture to 3–6%, producing finished malt [^3^][^10^].
4. **Deculming:** Remove rootlets (malt sprouts/culms) from the kilned malt.

**Stage 1 products:**
- **Malt** (intermediate product — input to Stage 2)
- **Malt sprouts** (final co-product)

### 3.2 Stage 2: Brewing

Barley brewing converts malt into beer through mashing, fermentation, and conditioning:

1. **Milling:** Malt is crushed to expose the endosperm.
2. **Mashing:** Milled malt is mixed with heated water to convert starch to fermentable sugars. Produces wort and BSG.
3. **Lautering:** Wort is separated from BSG.
4. **Boiling:** Wort is boiled with hops.
5. **Fermentation:** Yeast converts sugars to ethanol and CO₂.
6. **Conditioning:** Beer is aged, filtered, and packaged.

**Stage 2 products:**
- **Beer** (final co-product)
- **Brewers spent grain** (final co-product)

### 3.3 Overall Flow

```
1 t barley (0.880 t DM)
        │
        ▼
  ┌─ STAGE 1: MALTING ──────────────────────────┐
  │                                               │
  │  Total malting loss: 0.083 t DM              │
  │  (respiration ~4-5% + steeping/screening)    │
  │                                               │
  │  Malt sprouts: 0.04 t as-is (0.037 t DM)  ◄── final co-product
  │                                               │
  │  Malt: 0.80 t as-is (0.760 t DM)          ◄── intermediate
  │                                               │
  └───────────────┬───────────────────────────────┘
                  │ 0.80 t malt (0.760 t DM)
                  ▼
  ┌─ STAGE 2: BREWING ──────────────────────────┐
  │                                               │
  │  + ~4.60 t water                              │
  │  CO₂ loss: ~0.164 t DM                        │
  │                                               │
  │  BSG (dried): 0.16 t as-is (0.146 t DM)   ◄── final co-product
  │                                               │
  │  Beer: 4.40 t as-is (0.374 t DM)          ◄── final co-product
  │                                               │
  └───────────────────────────────────────────────┘

THREE FINAL CO-PRODUCTS from 1 t barley:
  Beer:         4.40 t as-is,  0.374 t DM
  BSG (dried):  0.16 t as-is, 0.146 t DM
  Malt sprouts: 0.04 t as-is, 0.037 t DM
  Total:                      0.557 t DM  (from 0.880 t input; 0.247 t lost to malting loss, fermentation CO₂, and other brewing losses)
```

---

## 4. Co-Product Yields and Properties

### 4.1 Yields (per tonne of barley input)

| Co-product | Stage | Yield (t/t barley) | Range | Source & Calculation |
|------------|-------|-------------------|-------|---------------------|
| **Malt** | 1 (intermediate) | 0.80 | 0.78–0.90 | Industry standard malting yield [^2^][^3^]. Conservative estimate; modern operations achieve 0.82–0.90. Losses through respiration (~4–5% DM), rootlet removal (~3–5%), and steeping/screening (~1–2%) total ~8–12% of barley mass. |
| **Malt sprouts** | 1 (final) | 0.04 | 0.03–0.05 | [^3^]: rootlets constitute 3–5% of malt produced after kilning (≈ 2.4–4.0% of original barley mass). |
| **Beer** | 2 (final) | 4.40 | 4.0–5.2 | Calculated: 5.50 t beer/t malt × 0.80 t malt/t barley = 4.40 t/t barley. Beer yield per t malt [^10^]: 4.5–6.0 t/t depending on beer strength and brewhouse efficiency. Midpoint 5.50 t/t malt. |
| **Brewers spent grain (dried)** | 2 (final) | 0.16 | 0.14–0.18 | Calculated: 0.20 t BSG/t malt × 0.80 t malt/t barley = 0.16 t/t barley. BSG yield per t malt [^4^]: 0.18–0.22 t/t dried. Midpoint 0.20 t/t malt. |

### 4.2 Dry Matter Contents

| Co-product | DM (%) | Basis |
|------------|--------|-------|
| Malt (intermediate) | 95.0% | Kilned malt: 94–96% DM (3–6% moisture) [^3^][^10^]. |
| Malt sprouts | 93.0% | Kilned sprouts: 92–95% DM [^4^]. Dried with malt during kilning; comparable to malt DM%. |
| Beer | 8.5% | Beer at ~5% ABV: ~3.9% ethanol (ABW) + ~4% residual extract + ~0.5% protein/ash = ~8.5% DM (range 8–9%) [^10^]. Note: the original extract (e.g., 12°P = 12% dissolved solids in wort) is NOT the same as beer DM%. |
| Brewers spent grain (dried) | 91.0% | Dried BSG: 90–93% DM [^4^]. Wet BSG at lautering is ~20–28% DM; dried for storage and transport. |

### 4.3 DM Output per Tonne of Barley

| Co-product | Calculation | DM Output (t/t barley) |
|------------|-------------|----------------------|
| **Malt** (intermediate) | 0.80 × 0.95 | **0.7600** |
| **Malt sprouts** | 0.04 × 0.93 | **0.0372** |
| Stage 1 total | | **0.7972** |
| **Beer** | 4.40 × 0.085 | **0.3740** |
| **Brewers spent grain** | 0.16 × 0.91 | **0.1456** |
| Stage 2 total | | **0.5196** |
| **All final co-products** | 0.374 + 0.146 + 0.037 | **0.5568** |

---

## 5. Prices

### 5.1 Price Table

| Co-product | Price (USD/t) | Range | Source | Notes |
|------------|--------------|-------|--------|-------|
| **Malt** (intermediate) | 300 | 250–500 | USDA FAS [^7^]; IndexBox [^5^] | Barley grain (feed): $180–230/t; barley grain (malting): $250–350/t [^7^]. Gross malting margin: $60–130/t (malt price minus barley cost; net margin after all costs is $10–40/t). Midpoint $300/t for standard 2-row brewers malt; range reflects regional and quality variation. |
| **Malt sprouts** | 200 | 150–250 | Comparable to DDGS and corn gluten feed [^9^] | Animal feed, primarily dairy/beef cattle. Niche, thin-market product with limited price transparency. Midpoint $200/t. |
| **Beer (commodity, brewery-gate bulk)** | 380 | 300–500 | Industry estimate | Brewery-gate bulk liquid price (ex-works, unpackaged). Wholesale/distribution prices are $700–1,200/t. Craft beer: $600–1,200/t at brewery gate. Midpoint $380/t for standard commercial lager at brewery gate. |
| **Brewers spent grain (dried)** | 180 | 150–220 | Thomas & Rahman [^8^]; Mussatto et al. [^4^] | Dried BSG for animal feed: $150–220/t. Wet BSG: $30–80/t. Midpoint $180/t for dried. |

### 5.2 Revenue per Tonne of Barley

| Co-product | Calculation | Revenue (USD/t barley) |
|------------|-------------|----------------------|
| **Beer** | 4.40 × 380 | **$1,672.00** |
| **Brewers spent grain** | 0.16 × 180 | **$28.80** |
| **Malt sprouts** | 0.04 × 200 | **$8.00** |
| **Total** | | **$1,708.80** |

> **Note:** Malt is not included in the final revenue calculation because it is an intermediate product, not a final co-product. The malt's value is realized through its conversion into beer and BSG. Using malt's intermediate price would distort the allocation by double-counting value (once at the malt stage, once at the beer stage).

---

## 6. Two-Stage Allocation

### 6.1 Allocation Approach

Because barley processing has two sequential stages, the allocation is performed in two steps:

**Stage 1 (Malting):** Allocate barley's burden between malt and malt sprouts.
**Stage 2 (Brewing):** Allocate malt's burden between beer and BSG.

The final allocation for each co-product is the product of the stage allocations along its path through the system:

```
Beer:       Stage 1 malt alloc × Stage 2 beer alloc
BSG:        Stage 1 malt alloc × Stage 2 BSG alloc
Sprouts:    Stage 1 sprouts alloc (no Stage 2)
```

> **Methodology note:** ISO 14044 (Section 4.3.4.2) requires allocation to be applied at each unit process separately, which naturally leads to a cascade (stepwise) approach when multi-stage processes have intermediate products. The term "cascade allocation" is a practitioner's term, not an ISO-defined concept, and should not be confused with ISO 14044's "stepwise allocation procedure" (which refers to the hierarchy of allocation methods: avoid → physical → economic).

### 6.2 Stage 1: Malting Allocation

**Mass allocation:**

| Co-product | DM Output | Calculation | Stage 1 Allocation |
|------------|-----------|-------------|-------------------|
| Malt | 0.7600 t | (0.7600 ÷ 0.7972) × 100 | **95.3%** |
| Malt sprouts | 0.0372 t | (0.0372 ÷ 0.7972) × 100 | **4.7%** |

**Economic allocation:**

| Co-product | Revenue | Calculation | Stage 1 Allocation |
|------------|---------|-------------|-------------------|
| Malt | $240.00 | (240.00 ÷ 248.00) × 100 | **96.8%** |
| Malt sprouts | $8.00 | (8.00 ÷ 248.00) × 100 | **3.2%** |

### 6.3 Stage 2: Brewing Allocation

**Mass allocation:**

| Co-product | DM Output (per t barley) | Calculation | Stage 2 Allocation |
|------------|-------------------------|-------------|-------------------|
| Beer | 0.3740 t | (0.3740 ÷ 0.5196) × 100 | **72.0%** |
| BSG | 0.1456 t | (0.1456 ÷ 0.5196) × 100 | **28.0%** |

**Economic allocation:**

| Co-product | Revenue (per t barley) | Calculation | Stage 2 Allocation |
|------------|----------------------|-------------|-------------------|
| Beer | $1,672.00 | (1672.00 ÷ 1700.80) × 100 | **98.3%** |
| BSG | $28.80 | (28.80 ÷ 1700.80) × 100 | **1.7%** |

### 6.4 Final Cumulative Allocation

The final allocation of barley's environmental burden to each of the three final co-products is calculated by cascading the two stages:

**Mass allocation (cumulative):**

| Co-product | Calculation | Final Allocation |
|------------|-------------|-----------------|
| **Beer** | 95.3% × 72.0% | **68.6%** |
| **Brewers spent grain** | 95.3% × 28.0% | **26.7%** |
| **Malt sprouts** | 4.7% (Stage 1 only) | **4.7%** |
| **Total** | | **100.0%** |

**Economic allocation (cumulative):**

| Co-product | Calculation | Final Allocation |
|------------|-------------|-----------------|
| **Beer** | 96.8% × 98.3% | **95.2%** |
| **Brewers spent grain** | 96.8% × 1.7% | **1.6%** |
| **Malt sprouts** | 3.2% (Stage 1 only) | **3.2%** |
| **Total** | | **100.0%** |

### 6.5 Verification: Direct Calculation

The cumulative allocation can be verified by calculating directly from the three final co-products' DM and revenue values per tonne of barley, bypassing the intermediate malt stage:

**Direct mass allocation:**

| Co-product | DM Output (t/t barley) | Calculation | Final Allocation |
|------------|----------------------|-------------|-----------------|
| Beer | 0.3740 | (0.3740 ÷ 0.5568) × 100 | **67.2%** |
| BSG | 0.1456 | (0.1456 ÷ 0.5568) × 100 | **26.1%** |
| Malt sprouts | 0.0372 | (0.0372 ÷ 0.5568) × 100 | **6.7%** |
| **Total** | **0.5568** | | **100.0%** |

**Direct economic allocation:**

| Co-product | Revenue (USD/t barley) | Calculation | Final Allocation |
|------------|----------------------|-------------|-----------------|
| Beer | $1,672.00 | (1672.00 ÷ 1708.80) × 100 | **97.8%** |
| BSG | $28.80 | (28.80 ÷ 1708.80) × 100 | **1.7%** |
| Malt sprouts | $8.00 | (8.00 ÷ 1708.80) × 100 | **0.5%** |
| **Total** | **$1,708.80** | | **100.0%** |

### 6.6 Reconciliation: Cascade vs. Direct

The cascade and direct methods give different results because they handle the DM losses differently:

| Co-product | Mass (cascade) | Mass (direct) | Econ (cascade) | Econ (direct) |
|------------|---------------|---------------|----------------|---------------|
| Beer | 68.6% | 67.2% | 95.2% | 97.8% |
| BSG | 26.7% | 26.1% | 1.6% | 1.7% |
| Sprouts | 4.7% | 6.7% | 3.2% | 0.5% |

**Why the differences exist:**

- **Mass allocation:** The cascade method calculates Stage 1 allocation using only the Stage 1 DM total (0.7972 t, which excludes total malting loss), then Stage 2 allocation using only the Stage 2 DM total (0.5196 t). The direct method uses the combined total (0.5568 t) which includes both malting and fermentation losses in the denominator. The difference reflects different accounting treatments of DM losses. Mass is conserved across stages, so the differences are moderate (≤1.5 percentage points for beer and BSG, 2.0 pp for sprouts).

- **Economic allocation:** The cascade method uses malt's price ($300/t) for Stage 1, which is lower than beer's price ($380/t). This means the cascade method assigns a larger share of barley's burden to the malt intermediate (via malt's revenue) than the direct method assigns to the final products. The direct method captures the full value chain (barley → beer at $380/t), giving beer 97.8% instead of 95.2%. The economic difference (2.6 pp for beer) is larger than the mass difference because economic value is transformed across stages (unlike mass, which is conserved).

**Which method to use:**

- The **cascade method** is consistent with ISO 14044's requirement that allocation be applied at each unit process separately when a unit process has intermediate products that cross system boundaries (i.e., malt could be sold independently). It reflects the economic reality at each processing stage.
- The **direct method** is simpler and more transparent, but it obscures the two-stage nature of the process and can give misleading results if the intermediate product (malt) has a very different value than the final product (beer).

For this document, we report both methods and recommend the **cascade method** as the primary allocation for LCA purposes, consistent with ISO 14044.

### 6.7 Recommended Final Allocation

| Co-product | Mass Allocation | Economic Allocation |
|------------|----------------|-------------------|
| **Beer** | **68.6%** | **95.2%** |
| **Brewers spent grain** | **26.7%** | **1.6%** |
| **Malt sprouts** | **4.7%** | **3.2%** |
| **Total** | **100.0%** | **100.0%** |

---

## 7. Mass Balance Verification

### 7.1 Overall DM Balance

| Item | Value | Notes |
|------|-------|-------|
| Input DM (1 t barley at 12% moisture) | 0.880 t | — |
| **Output DM — final co-products:** | | |
| Beer | 0.374 t | 4.40 t × 8.5% DM |
| Brewers spent grain (dried) | 0.146 t | 0.16 t × 91% DM |
| Malt sprouts | 0.037 t | 0.04 t × 93% DM |
| Total co-product DM | **0.557 t** | |
| **Losses:** | | |
| Total malting DM loss (respiration + steeping + screening) | 0.083 t | 9.4% of input DM; includes respiration (~4–5%), steeping loss, and screening loss |
| CO₂ from fermentation | 0.164 t | Stoichiometric: ethanol in beer (~0.172 t at 5% ABV) × 88/92 |
| **Total accounted** | **0.804 t** | |
| Unaccounted | 0.076 t | 8.6% of input; includes yeast biomass (~0.02–0.03 t), evaporation during boiling, trub loss, and minor inconsistencies in independently-sourced yield parameters |

### 7.2 Stage-by-Stage Balance

**Stage 1: Malting**

| Item | Value | Notes |
|------|-------|-------|
| Input DM | 0.880 t | 1 t barley at 12% moisture |
| Malt DM | 0.760 t | 0.80 t × 95% DM |
| Sprouts DM | 0.037 t | 0.04 t × 93% DM |
| Total malting DM loss | 0.083 t | 0.880 − 0.760 − 0.037 |
| **Total accounted** | **0.880 t** | ✓ Exact |

> **Note on malting loss composition:** The 0.083 t total malting DM loss (9.4% of input) comprises respiration loss (~4–5% of input DM, primarily starch oxidized to CO₂ and H₂O), rootlet growth beyond the 0.037 t recovered as sprouts (included in respiration accounting), steeping loss (fine particles and soluble materials washed away, ~0.5–1%), and screening/cleaning losses (~1–2%). Literature consistently reports respiration alone at ~4–5% of input DM (Maule, 1971; Wiley-VCH Technology of Malting), not the full 9.4%.

**Stage 2: Brewing**

| Item | Value | Notes |
|------|-------|-------|
| Input DM (malt) | 0.760 t | From Stage 1 |
| Beer DM | 0.374 t | 4.40 t × 8.5% DM |
| BSG DM | 0.146 t | 0.16 t × 91% DM |
| CO₂ from fermentation | 0.164 t | Ethanol in beer (~0.172 t at 5% ABV) × 88/92 |
| **Total accounted** | **0.684 t** | |
| Unaccounted | 0.076 t | 10.0% of malt DM; see note below |

> The 0.076 t DM gap in brewing arises because the beer yield (5.50 t/t malt) and BSG yield (0.20 t/t malt) are independently estimated from industry data and are not forced to close stoichiometrically. The gap represents: (1) yeast biomass production (~0.02–0.03 t DM/t barley from malt sugars, not captured as a co-product), (2) evaporation losses during boiling (~0.01–0.02 t DM equivalent), (3) trub loss (hot break, cold break — partially recovered with BSG), and (4) minor inconsistencies between independently-sourced yield parameters. A fully consistent set would require adjusting either the beer yield or the BSG yield. The allocation results are not highly sensitive to this gap because the relative proportions of beer, BSG, and sprouts DM are robust.

### 7.3 As-Is Mass Balance

| Item | Value | Notes |
|------|-------|-------|
| Input (barley) | 1.000 t | — |
| Water added during steeping | +0.400 t | Absorbed then removed by kilning (net zero) |
| Water added during mashing/brewing | +4.600 t | Becomes part of beer |
| Malting mass loss (CO₂ + H₂O from respiration and steeping) | −0.173 t | Stoichiometric: complete oxidation of 0.083 t DM produces ~0.123 t CO₂ + ~0.050 t H₂O |
| Fermentation CO₂ loss | −0.164 t | CO₂ from sugar fermentation |
| **Output:** | | |
| Beer | 4.400 t | — |
| BSG (dried) | 0.160 t | — |
| Malt sprouts | 0.040 t | — |
| **Total output** | **4.600 t** | |
| **Net water addition** | **3.663 t** | 5.000 added (steeping + brewing) − 1.337 lost (malting respiration + CO₂ + kilning water removal) |

> **Note:** The as-is mass balance is complex because water is added at multiple stages (steeping, mashing) and removed at others (kilning, evaporation during boiling). The net water addition of ~3.66 t is consistent with the beer output of 4.40 t (which is primarily water). Small discrepancies arise from rounding and from unmeasured evaporation losses during boiling and cooling.

---

## 8. Complete Data Table

### 8.1 Final Co-Product Allocation (per 1 t barley at 12% moisture)

| Parent Crop | Crop System | Stage | USDA Standard | Standard Moisture | Parent Input Basis | Co-product Stream | Yield (t/t barley) | Yield Range | Price (USD/t) | Price Range | DM (%) | DM Output (t/t barley) | Revenue (USD/t barley) | Econ Alloc — Cascade (%) | Econ Alloc — Direct (%) | Mass Alloc — Cascade (%) | Mass Alloc — Direct (%) |
|-------------|-------------|-------|---------------|-------------------|-------------------|-------------------|-------------------|-------------|---------------|-------------|--------|----------------------|----------------------|------------------------|------------------------|------------------------|------------------------|
| Barley | Barley malting/brewing | 2 | 48 lb/bushel at 12% moisture | 12% | 1 t barley at 12% moisture | Beer | 4.40 | 4.0–5.2 | 380 | 300–500 | 8.5 | 0.374 | 1672.00 | 95.2 | 97.8 | 68.6 | 67.2 |
| Barley | Barley malting/brewing | 2 | 48 lb/bushel at 12% moisture | 12% | 1 t barley at 12% moisture | Brewers spent grain (dried) | 0.16 | 0.14–0.18 | 180 | 150–220 | 91.0 | 0.146 | 28.80 | 1.6 | 1.7 | 26.7 | 26.1 |
| Barley | Barley malting/brewing | 2 | 48 lb/bushel at 12% moisture | 12% | 1 t barley at 12% moisture | Malt sprouts | 0.04 | 0.03–0.05 | 200 | 150–250 | 93.0 | 0.037 | 8.00 | 3.2 | 0.5 | 4.7 | 6.7 |

### 8.2 Intermediate Product (for cascade calculation reference only)

| Parent Crop | Crop System | Stage | USDA Standard | Standard Moisture | Parent Input Basis | Co-product Stream | Yield (t/t barley) | Yield Range | Price (USD/t) | Price Range | DM (%) | DM Output (t/t barley) | Revenue (USD/t barley) | Stage 1 Econ Alloc (%) | Stage 1 Mass Alloc (%) |
|-------------|-------------|-------|---------------|-------------------|-------------------|-------------------|-------------------|-------------|---------------|-------------|--------|----------------------|----------------------|------------------------|------------------------|
| Barley | Barley malting | 1 | 48 lb/bushel at 12% moisture | 12% | 1 t barley at 12% moisture | Malt (intermediate) | 0.80 | 0.78–0.90 | 300 | 250–500 | 95.0 | 0.760 | 240.00 | 96.8 | 95.3 |

---

## 9. Data Quality and Limitations

### 9.1 High-Confidence Data

| Data Point | Confidence | Source |
|------------|-----------|--------|
| Malt yield (0.80 t/t barley) | **High** | Brewers Association [^2^]; Briggs et al. [^3^] |
| Malt sprouts yield (0.04 t/t barley) | **High** | Briggs et al. [^3^] |
| DM contents (malt 95%, sprouts 93%, BSG 91%) | **High** | Industry specifications; peer-reviewed literature [^3^][^4^] |
| Malt price ($300/t) | **High** | USDA FAS [^7^]; IndexBox [^5^] |
| Barley grain prices | **High** | USDA FAS [^7^] |

### 9.2 Medium-Confidence Data

| Data Point | Confidence | Source |
|------------|-----------|--------|
| Beer yield (5.50 t/t malt) | **Medium** | Varies by beer style; derived from extract yield and specific gravity [^10^] |
| Beer DM% (8.5%) | **Medium** | Varies with ABV and residual extract; range 8–9% at 5% ABV [^10^] |
| Beer price ($380/t) | **Medium** | Brewery-gate bulk liquid price; highly variable by type (commodity vs. craft) and distribution level |
| BSG yield dried (0.20 t/t malt) | **Medium** | Depends on malt analysis and brewhouse efficiency [^4^] |
| BSG price dried ($180/t) | **Medium** | Regional market with limited price transparency [^8^] |

### 9.3 Known Limitations

1. **Cascade vs. direct allocation:** The two methods give different results (mass: 68.6% vs. 67.2% for beer; economic: 95.2% vs. 97.8%). The cascade method is recommended as the primary allocation per ISO 14044's per-unit-process requirement, but the direct method is shown for comparison.

2. **Economic allocation sensitivity:** The economic allocation is very sensitive to the beer price. If beer is priced at $300/t instead of $380/t, beer's economic allocation drops from 95.2% to ~92%, and sprouts and BSG each gain ~1–2 percentage points.

3. **Water addition in brewing:** The brewing process adds ~4.6 t of water per t of malt. This water becomes part of the beer product. The as-is mass balance reflects this large water input, which dominates the total mass flow but does not affect DM-based allocation.

4. **DM reconciliation gap in brewing:** The independently-sourced beer and BSG yields create a ~0.076 t DM gap per t barley (8.6% of input). This gap is explainable by yeast biomass, evaporation losses, trub, and minor yield parameter inconsistencies. It is documented in Section 7.2 and does not materially affect allocation results because the relative DM proportions are robust.

5. **Wet vs. dried BSG:** This table uses dried BSG (91% DM, 0.16 t/t barley). Many breweries sell wet BSG (20–28% DM, ~0.96 t/t barley) directly to nearby farms. The choice of wet vs. dried BSG affects the as-is yield and price but not the DM-based allocation (same DM mass either way).

6. **Missing co-products:** Brewing also produces spent hops (~0.01 t/t malt) and spent yeast (~0.04 t/t malt). These are typically low-value and often excluded from allocation.

7. **Regional variation:** Malt and beer prices vary significantly by region. European malt prices tend to be higher than North American due to energy costs and regulatory differences.

8. **Moisture basis:** This document uses 12% moisture as the calculation basis, which is a common storage moisture for barley. The USDA trading standard is 14.5% (per 7 CFR Part 1421). Using 14.5% would change the DM input to 0.855 t (instead of 0.880 t) and proportionally adjust all DM-based calculations.

---
