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

### 1.2 Convention for Adopted Values

Every yield, price, and DM% in this document is reported as an adopted point value together with the range it was drawn from. **Unless a row states otherwise, the adopted value is the midpoint of its stated range**, and the range is the parameter that carries the evidence. Because barley processing is a two-stage system, the treatment of the intermediate product (malt) also has to be stated explicitly; Section 6.1 does that, sets out the alternative, and shows what each implies. Derived quantities (DM outputs, revenues, allocation percentages) are carried at four decimals internally and reported to one decimal place.

### 1.3 Unit Conversions

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
  │  Total malting loss: 0.045 t DM              │
  │  (respiration ~4-5% + steeping/screening)    │
  │                                               │
  │  Malt sprouts: 0.04 t as-is (0.037 t DM)  ◄── final co-product
  │                                               │
  │  Malt: 0.84 t as-is (0.798 t DM)          ◄── intermediate
  │                                               │
  └───────────────┬───────────────────────────────┘
                  │ 0.84 t malt (0.798 t DM)
                  ▼
  ┌─ STAGE 2: BREWING ──────────────────────────┐
  │                                               │
  │  + ~4.80 t water                              │
  │  CO₂ loss: ~0.172 t DM                        │
  │                                               │
  │  BSG (dried): 0.16 t as-is (0.146 t DM)   ◄── final co-product
  │                                               │
  │  Beer: 4.60 t as-is (0.391 t DM)          ◄── final co-product
  │                                               │
  └───────────────────────────────────────────────┘

THREE FINAL CO-PRODUCTS from 1 t barley:
  Beer:         4.60 t as-is,  0.391 t DM
  BSG (dried):  0.16 t as-is, 0.146 t DM
  Malt sprouts: 0.04 t as-is, 0.037 t DM
  Total:                      0.574 t DM  (from 0.880 t input; 0.306 t lost to malting loss, fermentation CO₂, and other brewing losses)
```

---

## 4. Co-Product Yields and Properties

### 4.1 Yields (per tonne of barley input)

| Co-product | Stage | Yield (t/t barley) | Range | Source & Calculation |
|------------|-------|-------------------|-------|---------------------|
| **Malt** | 1 (intermediate) | 0.84 | 0.78–0.90 | Midpoint of the stated range. Industry standard malting yield [^2^][^3^]; modern operations achieve 0.82–0.90. Losses through respiration (~4–5% DM), rootlet removal (~3–5%), and steeping/screening (~1–2%) total ~8–12% of barley mass. |
| **Malt sprouts** | 1 (final) | 0.04 | 0.03–0.05 | Briggs et al. [^3^] report rootlets at 3–5% of the malt produced after kilning. At the 0.84 t/t malting yield that is **0.025–0.042 t/t barley**, so the adopted 0.04 sits near the top of the composition-derived band while remaining the midpoint of the stated 0.03–0.05 range. The two bands overlap but are not identical; the stated range is the wider of the two and is the one carried through this document. |
| **Beer** | 2 (final) | 4.60 | 4.0–5.2 | Midpoint of the stated range, equivalent to 5.48 t beer per t malt at the 0.84 t/t malting yield. Beer yield per t malt [^10^]: 4.5–6.0 t/t depending on beer strength and brewhouse efficiency. |
| **Brewers spent grain (dried)** | 2 (final) | 0.16 | 0.14–0.18 | Midpoint of the stated range, equivalent to 0.19 t BSG per t malt at the 0.84 t/t malting yield. BSG yield per t malt [^4^]: 0.18–0.22 t/t dried. |

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
| **Malt** (intermediate) | 0.84 × 0.95 | **0.7980** |
| **Malt sprouts** | 0.04 × 0.93 | **0.0372** |
| Stage 1 total | | **0.8352** |
| **Beer** | 4.60 × 0.085 | **0.3910** |
| **Brewers spent grain** | 0.16 × 0.91 | **0.1456** |
| Stage 2 total | | **0.5366** |
| **All final co-products** | 0.391 + 0.146 + 0.037 | **0.5738** |

---

## 5. Prices

### 5.1 Price Table

| Co-product | Price (USD/t) | Range | Source | Notes |
|------------|--------------|-------|--------|-------|
| **Malt** (intermediate) | 375 | 250–500 | USDA FAS [^7^]; IndexBox [^5^] | Standard 2-row brewers malt; the adopted $375/t is the midpoint of the stated range, which reflects regional and quality variation. For context, feed barley runs $180–230/t and malting barley $250–350/t [^7^][^6^]. See the note below on how the malt price relates to the barley price. |
| **Malt sprouts** | 200 | 150–250 | Comparable to DDGS and corn gluten feed [^9^] | Animal feed, primarily dairy/beef cattle. Niche, thin-market product with limited price transparency. The adopted $200/t is the midpoint of the stated range. |
| **Beer (commodity, brewery-gate bulk)** | 400 | 300–500 | Industry estimate | Brewery-gate bulk liquid price (ex-works, unpackaged). Wholesale/distribution prices are $700–1,200/t. Craft beer: $600–1,200/t at brewery gate. The adopted $400/t is the midpoint of the stated range, for standard commercial lager at brewery gate. |
| **Brewers spent grain (dried)** | 185 | 150–220 | Thomas & Rahman [^8^]; Mussatto et al. [^4^] | Dried BSG for animal feed: $150–220/t. Wet BSG: $30–80/t. The adopted $185/t is the midpoint of the stated range, for dried BSG. |

> **Note on the malt price relative to the barley price:** These two prices are drawn from independent sources and are not forced to be mutually consistent, and the arithmetic is worth stating openly. At the 0.84 t/t malting yield, one tonne of malt requires 1.19 t of barley, so malting barley at $250–350/t costs $298–417 per tonne of malt produced. Against the adopted malt price of $375/t that implies a gross margin over barley cost of **+$77/t of malt at the bottom of the barley range and −$42/t at the top**; at the midpoints ($375 malt, $300 barley) it is about +$18/t of malt, or +$15 per tonne of barley. The adopted malt price is therefore at the conservative end of what a malting margin would imply, and the stated barley and malt ranges overlap in a way that a single consistent market snapshot would not. Section 9.2 quantifies what this means for the result: the Stage 1 split is the only allocation affected, and moving the malt price to $250/t changes malt sprouts from 2.5% to 3.7%.

### 5.2 Revenue per Tonne of Barley

| Co-product | Calculation | Revenue (USD/t barley) |
|------------|-------------|----------------------|
| **Beer** | 4.60 × 400 | **$1,840.00** |
| **Brewers spent grain** | 0.16 × 185 | **$29.60** |
| **Malt sprouts** | 0.04 × 200 | **$8.00** |
| **Total** | | **$1,877.60** |

> **Note:** Malt does not appear in this final-co-product revenue total because it is an intermediate, not an output of the system. Malt's value enters the allocation at Stage 1 (Section 6.2), where the barley burden is split between malt and malt sprouts; the split between beer and BSG is then computed within the malt block at Stage 2. This sequential treatment applies allocation at each unit process and is appropriate here because malt is an independently traded commodity with an observable transfer price at the point of separation. Section 6.1 sets out why that convention is used and Section 6.7 sets it against the direct end-of-chain calculation, in which the final-product revenues above form the sole denominator.

---

## 6. Two-Stage Allocation

### 6.1 Treatment of the Intermediate Product

Barley processing has an intermediate — malt — that is sold between the two stages, so Stage 1 cannot be allocated without deciding what malt is worth. Two conventions are possible, and they give materially different answers.

**Market-price cascade (used here).** Malt is valued at the price it actually transacts at between maltster and brewer ($375/t, Section 5.1). Stage 1 divides the barley burden between malt and malt sprouts on that basis; Stage 2 divides malt's burden between beer and BSG; the two stage allocations are then multiplied along each product's path.

**Derived valuation (not used here).** Malt is instead valued at the total revenue of the products it becomes ($1,869.60/t barley).

These are not two independent options plus a third. **Valuing the intermediate at its derived value makes the cascade collapse algebraically to the direct end-of-chain calculation**, because the derived value cancels out of the multiplication:

```
Stage 1 malt share x Stage 2 beer share
  = D / (D + sprouts)  x  beer / D
  = beer / (D + sprouts)
  = beer / (beer + BSG + sprouts)        <- the direct calculation

Numerically: 99.574% x 98.417% = 97.997%, which is exactly
             1840.00 / 1877.60 = 97.997%
```

So the choice is between the market-price cascade and the direct end-of-chain calculation, and Section 6.5 reports the direct result for comparison.

**Why the market-price cascade is used for barley:**

1. **Malt is not a final co-product in this work.** It is not a dairy feed; it exists here only as the input to brewing, and the sole reason it appears in the calculation is that it is the point at which the barley burden divides. The three co-products this document reports are beer, BSG and malt sprouts.
2. **The malt price is an arms-length transfer price into Stage 2.** It is what a brewer pays a maltster for the same stream that enters brewing, so it is the observable value at the point of separation — which is what applying allocation at each unit process requires.
3. **It keeps the field burden independent of downstream value-add.** Brewing multiplies the value of the stream roughly sixfold using water, hops, yeast and energy, none of which is agricultural. Under derived valuation that value-add would decide how the barley field's burden splits, moving malt sprouts from 2.5% to 0.4% without anything changing in the field.

**Where this convention does not apply.** A different treatment is warranted where the intermediate is itself a marketed final co-product of the system being studied — that is, where the study needs allocation factors for both the intermediate and the products it becomes, because both are genuine outputs. In that case the intermediate's quoted price is the price in a competing end use rather than a transfer price into the next stage, and the direct end-of-chain treatment is used so that all final products sit on one denominator. That situation does not arise for barley: malt has no use outside brewing in this system.

### 6.2 Allocation Approach

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

### 6.3 Stage 1: Malting Allocation

**Mass allocation:**

| Co-product | DM Output | Calculation | Stage 1 Allocation |
|------------|-----------|-------------|-------------------|
| Malt | 0.7980 t | (0.7980 ÷ 0.8352) × 100 | **95.5%** |
| Malt sprouts | 0.0372 t | (0.0372 ÷ 0.8352) × 100 | **4.5%** |

**Economic allocation:**

| Co-product | Revenue | Calculation | Stage 1 Allocation |
|------------|---------|-------------|-------------------|
| Malt | $315.00 | (315.00 ÷ 323.00) × 100 | **97.5%** |
| Malt sprouts | $8.00 | (8.00 ÷ 323.00) × 100 | **2.5%** |

### 6.4 Stage 2: Brewing Allocation

**Mass allocation:**

| Co-product | DM Output (per t barley) | Calculation | Stage 2 Allocation |
|------------|-------------------------|-------------|-------------------|
| Beer | 0.3910 t | (0.3910 ÷ 0.5366) × 100 | **72.9%** |
| BSG | 0.1456 t | (0.1456 ÷ 0.5366) × 100 | **27.1%** |

**Economic allocation:**

| Co-product | Revenue (per t barley) | Calculation | Stage 2 Allocation |
|------------|----------------------|-------------|-------------------|
| Beer | $1,840.00 | (1840.00 ÷ 1869.60) × 100 | **98.4%** |
| BSG | $29.60 | (29.60 ÷ 1869.60) × 100 | **1.6%** |

### 6.5 Final Cumulative Allocation

The final allocation of barley's environmental burden to each of the three final co-products is calculated by cascading the two stages:

**Mass allocation (cumulative):**

| Co-product | Calculation | Final Allocation |
|------------|-------------|-----------------|
| **Beer** | 95.5% × 72.9% | **69.6%** |
| **Brewers spent grain** | 95.5% × 27.1% | **25.9%** |
| **Malt sprouts** | 4.5% (Stage 1 only) | **4.5%** |
| **Total** | | **100.0%** |

**Economic allocation (cumulative):**

| Co-product | Calculation | Final Allocation |
|------------|-------------|-----------------|
| **Beer** | 97.5% × 98.4% | **96.0%** |
| **Brewers spent grain** | 97.5% × 1.6% | **1.5%** |
| **Malt sprouts** | 2.5% (Stage 1 only) | **2.5%** |
| **Total** | | **100.0%** |

### 6.6 Verification: Direct Calculation

The cumulative allocation can be verified by calculating directly from the three final co-products' DM and revenue values per tonne of barley, bypassing the intermediate malt stage:

**Direct mass allocation:**

| Co-product | DM Output (t/t barley) | Calculation | Final Allocation |
|------------|----------------------|-------------|-----------------|
| Beer | 0.3910 | (0.3910 ÷ 0.5738) × 100 | **68.1%** |
| BSG | 0.1456 | (0.1456 ÷ 0.5738) × 100 | **25.4%** |
| Malt sprouts | 0.0372 | (0.0372 ÷ 0.5738) × 100 | **6.5%** |
| **Total** | **0.5738** | | **100.0%** |

**Direct economic allocation:**

| Co-product | Revenue (USD/t barley) | Calculation | Final Allocation |
|------------|----------------------|-------------|-----------------|
| Beer | $1,840.00 | (1840.00 ÷ 1877.60) × 100 | **98.0%** |
| BSG | $29.60 | (29.60 ÷ 1877.60) × 100 | **1.6%** |
| Malt sprouts | $8.00 | (8.00 ÷ 1877.60) × 100 | **0.4%** |
| **Total** | **$1,877.60** | | **100.0%** |

### 6.7 Reconciliation: Cascade vs. Direct

The cascade and direct methods give different results because they handle the DM losses differently:

| Co-product | Mass (cascade) | Mass (direct) | Econ (cascade) | Econ (direct) |
|------------|---------------|---------------|----------------|---------------|
| Beer | 69.6% | 68.1% | 96.0% | 98.0% |
| BSG | 25.9% | 25.4% | 1.5% | 1.6% |
| Sprouts | 4.5% | 6.5% | 2.5% | 0.4% |

**Why the differences exist:**

- **Mass allocation:** The cascade method calculates Stage 1 allocation using only the Stage 1 DM total (0.8352 t, which excludes total malting loss), then Stage 2 allocation using only the Stage 2 DM total (0.5366 t). The direct method uses the combined total of the three final co-products (0.5738 t). Neither denominator contains losses; the difference is that the cascade measures sprouts against the Stage 1 pool, before fermentation removes dry matter, whereas the direct method measures them against a pool already reduced by it. Sprouts therefore carry a larger share under the direct method (6.5% against 4.5%), while beer and BSG shift by no more than 1.5 percentage points.

- **Economic allocation:** The cascade values the intermediate at malt's own transfer price ($375/t), so malt sprouts compete against malt revenue of $315.00/t barley. The direct calculation places sprouts against the total revenue of all three final co-products ($1,877.60/t barley), nearly six times the Stage 1 total, because brewing adds substantial non-agricultural value. Sprouts therefore fall from 2.5% under the cascade to 0.4% under the direct calculation, and beer rises from 96.0% to 98.0%. The difference (2.0 pp for beer, 2.1 pp for sprouts) is larger than on the mass side because economic value is transformed across stages whereas mass is conserved. As shown in Section 6.1, the direct column is also what would result from valuing malt at the revenue of the products it becomes — the two are the same calculation.

**Which method to use:**

- The **cascade method** applies allocation at each unit process separately, which is appropriate when the intermediate crosses a system boundary and is independently traded, as malt is. It reflects the transaction at each processing stage and prevents brewing value-add from determining how the barley field burden is split.
- The **direct calculation** is simpler and uses a single denominator, but it collapses the two-stage structure and lets the value added in Stage 2 govern the Stage 1 split. It is the more appropriate treatment where the intermediate is itself a marketed final co-product of the system, which malt is not.

Both results are reported here. The **cascade method is the primary allocation** for this document, for the reasons set out in Section 6.1: malt is not a final co-product of this system, its price is an arms-length transfer price into brewing, and the cascade keeps the split of the field burden independent of the value that brewing adds using non-agricultural inputs. The direct result is reported so that a user who prefers an end-of-chain denominator can apply it.

### 6.8 Recommended Final Allocation

| Co-product | Mass Allocation | Economic Allocation |
|------------|----------------|-------------------|
| **Beer** | **69.6%** | **96.0%** |
| **Brewers spent grain** | **25.9%** | **1.5%** |
| **Malt sprouts** | **4.5%** | **2.5%** |
| **Total** | **100.0%** | **100.0%** |

---

## 7. Mass Balance Verification

### 7.1 Overall DM Balance

| Item | Value | Notes |
|------|-------|-------|
| Input DM (1 t barley at 12% moisture) | 0.880 t | — |
| **Output DM — final co-products:** | | |
| Beer | 0.391 t | 4.60 t × 8.5% DM |
| Brewers spent grain (dried) | 0.146 t | 0.16 t × 91% DM |
| Malt sprouts | 0.037 t | 0.04 t × 93% DM |
| Total co-product DM | **0.574 t** | |
| **Losses:** | | |
| Total malting DM loss (respiration + steeping + screening) | 0.045 t | 5.1% of input DM; consistent with literature respiration loss of ~4–5% plus small steeping and screening losses |
| CO₂ from fermentation | 0.172 t | Stoichiometric: ethanol in beer (~0.179 t at 5% ABV) × 88/92 |
| **Total accounted** | **0.791 t** | |
| Unaccounted | 0.089 t | 10.1% of input; includes yeast biomass (~0.02–0.03 t), evaporation during boiling, trub loss, and minor inconsistencies in independently-sourced yield parameters |

### 7.2 Stage-by-Stage Balance

**Stage 1: Malting**

| Item | Value | Notes |
|------|-------|-------|
| Input DM | 0.880 t | 1 t barley at 12% moisture |
| Malt DM | 0.798 t | 0.84 t × 95% DM |
| Sprouts DM | 0.037 t | 0.04 t × 93% DM |
| Total malting DM loss | 0.045 t | 0.880 − 0.798 − 0.037 |
| **Total accounted** | **0.880 t** | ✓ Exact |

> **Note on malting loss composition:** The 0.045 t total malting DM loss (5.1% of input) comprises respiration loss (~4–5% of input DM, primarily starch oxidized to CO₂ and H₂O), rootlet growth beyond the 0.037 t recovered as sprouts (included in respiration accounting), steeping loss (fine particles and soluble materials washed away, ~0.5–1%), and screening/cleaning losses (~1–2%). Literature consistently reports respiration alone at ~4–5% of input DM (Maule, 1971; Wiley-VCH Technology of Malting), which is consistent with the 5.1% total obtained here.

**Stage 2: Brewing**

| Item | Value | Notes |
|------|-------|-------|
| Input DM (malt) | 0.798 t | From Stage 1 |
| Beer DM | 0.391 t | 4.60 t × 8.5% DM |
| BSG DM | 0.146 t | 0.16 t × 91% DM |
| CO₂ from fermentation | 0.172 t | Ethanol in beer (~0.179 t at 5% ABV) × 88/92 |
| **Total accounted** | **0.709 t** | |
| Unaccounted | 0.089 t | 11.2% of malt DM; see note below |

> The 0.089 t DM gap in brewing arises because the beer yield (5.48 t/t malt) and BSG yield (0.19 t/t malt) are independently estimated from industry data and are not forced to close stoichiometrically. The gap represents: (1) yeast biomass production (~0.02–0.03 t DM/t barley from malt sugars, not captured as a co-product), (2) evaporation losses during boiling (~0.01–0.02 t DM equivalent), (3) trub loss (hot break, cold break — partially recovered with BSG), and (4) minor inconsistencies between independently-sourced yield parameters. A fully consistent set would require adjusting either the beer yield or the BSG yield. The allocation results are not highly sensitive to this gap because the relative proportions of beer, BSG, and sprouts DM are robust.

### 7.3 As-Is Mass Balance

| Item | Value | Notes |
|------|-------|-------|
| Input (barley) | 1.000 t | — |
| Water added during steeping | +0.400 t | Absorbed then removed by kilning (net zero) |
| Water added during mashing/brewing | +4.800 t | Becomes part of beer |
| Malting mass loss (CO₂ + H₂O from respiration and steeping) | −0.094 t | Stoichiometric: complete oxidation of 0.045 t DM produces ~0.067 t CO₂ + ~0.027 t H₂O |
| Fermentation CO₂ loss | −0.172 t | CO₂ from sugar fermentation |
| Water removed by kilning and by evaporation during the boil | −1.134 t | The balancing term: steeping water plus the barley's own moisture driven off during kilning (malt leaves at 3–6% moisture), plus wort evaporation during boiling. Obtained as the residual of this table, not measured independently |
| **Output:** | | |
| Beer | 4.600 t | — |
| BSG (dried) | 0.160 t | — |
| Malt sprouts | 0.040 t | — |
| **Total output** | **4.800 t** | |
| **Net water addition** | **3.800 t** | 5.200 added (steeping + brewing) − 1.400 lost (malting respiration + CO₂ + kilning water removal) |

> **Note:** The as-is balance is complex because water is added at two stages (steeping, mashing) and removed at two others (kilning, evaporation during the boil). With the kilning and evaporation term included the rows now sum to the stated output: 1.000 + 0.400 + 4.800 − 0.094 − 0.172 − 1.134 = 4.800 t. That term is the residual of the table rather than an independent measurement, so it absorbs any rounding in the other rows. The net water addition of ~3.80 t is consistent with a beer output of 4.60 t, which is predominantly water.

---

## 8. Complete Data Table

### 8.1 Final Co-Product Allocation (per 1 t barley at 12% moisture)

| Parent Crop | Crop System | Stage | USDA Standard | Standard Moisture | Parent Input Basis | Co-product Stream | Yield (t/t barley) | Yield Range | Price (USD/t) | Price Range | DM (%) | DM Output (t/t barley) | Revenue (USD/t barley) | Econ Alloc — Cascade (%) | Econ Alloc — Direct (%) | Mass Alloc — Cascade (%) | Mass Alloc — Direct (%) |
|-------------|-------------|-------|---------------|-------------------|-------------------|-------------------|-------------------|-------------|---------------|-------------|--------|----------------------|----------------------|------------------------|------------------------|------------------------|------------------------|
| Barley | Barley malting/brewing | 2 | 48 lb/bushel at 12% moisture | 12% | 1 t barley at 12% moisture | Beer | 4.60 | 4.0–5.2 | 400 | 300–500 | 8.5 | 0.391 | 1840.00 | 96.0 | 98.0 | 69.6 | 68.1 |
| Barley | Barley malting/brewing | 2 | 48 lb/bushel at 12% moisture | 12% | 1 t barley at 12% moisture | Brewers spent grain (dried) | 0.16 | 0.14–0.18 | 185 | 150–220 | 91.0 | 0.146 | 29.60 | 1.5 | 1.6 | 25.9 | 25.4 |
| Barley | Barley malting/brewing | 2 | 48 lb/bushel at 12% moisture | 12% | 1 t barley at 12% moisture | Malt sprouts | 0.04 | 0.03–0.05 | 200 | 150–250 | 93.0 | 0.037 | 8.00 | 2.5 | 0.4 | 4.5 | 6.5 |

### 8.2 Intermediate Product (for cascade calculation reference only)

| Parent Crop | Crop System | Stage | USDA Standard | Standard Moisture | Parent Input Basis | Co-product Stream | Yield (t/t barley) | Yield Range | Price (USD/t) | Price Range | DM (%) | DM Output (t/t barley) | Revenue (USD/t barley) | Stage 1 Econ Alloc (%) | Stage 1 Mass Alloc (%) |
|-------------|-------------|-------|---------------|-------------------|-------------------|-------------------|-------------------|-------------|---------------|-------------|--------|----------------------|----------------------|------------------------|------------------------|
| Barley | Barley malting | 1 | 48 lb/bushel at 12% moisture | 12% | 1 t barley at 12% moisture | Malt (intermediate) | 0.84 | 0.78–0.90 | 375 | 250–500 | 95.0 | 0.798 | 315.00 | 97.5 | 95.5 |

---

## 9. Data Quality and Limitations

### 9.1 High-Confidence Data

| Data Point | Confidence | Source |
|------------|-----------|--------|
| Malt yield (0.84 t/t barley) | **High** | Brewers Association [^2^]; Briggs et al. [^3^] |
| Malt sprouts yield (0.04 t/t barley) | **High** | Briggs et al. [^3^] |
| DM contents (malt 95%, sprouts 93%, BSG 91%) | **High** | Industry specifications; peer-reviewed literature [^3^][^4^] |
| Malt price ($375/t) | **High** | USDA FAS [^7^]; IndexBox [^5^] |
| Barley grain prices | **High** | USDA FAS [^7^] |

### 9.2 Medium-Confidence Data

| Data Point | Confidence | Source |
|------------|-----------|--------|
| Beer yield (5.48 t/t malt) | **Medium** | Varies by beer style; derived from extract yield and specific gravity [^10^] |
| Beer DM% (8.5%) | **Medium** | Varies with ABV and residual extract; range 8–9% at 5% ABV [^10^] |
| Beer price ($400/t) | **Medium** | Brewery-gate bulk liquid price; highly variable by type (commodity vs. craft) and distribution level |
| BSG yield dried (0.19 t/t malt) | **Medium** | Depends on malt analysis and brewhouse efficiency [^4^] |
| BSG price dried ($185/t) | **Medium** | Regional market with limited price transparency [^8^] |

### 9.3 Known Limitations

1. **Cascade vs. direct allocation:** The two methods give different results (mass: 69.6% vs. 68.1% for beer; economic: 96.0% vs. 98.0%). The cascade method is recommended as the primary allocation per ISO 14044's per-unit-process requirement, but the direct method is shown for comparison.

2. **Economic allocation sensitivity:** Under the cascade the Stage 1 split is driven by the malt price, not the beer price, so beer's final allocation is comparatively insensitive to the beer price: at $300/t instead of $400/t, beer's cascaded economic allocation falls only from 96.0% to ~95.5%. The Stage 1 split is more sensitive: at a malt price of $250/t instead of $375/t, malt sprouts rise from 2.5% to ~3.7%.

3. **Water addition in brewing:** The brewing process adds ~4.8 t of water per t of barley. This water becomes part of the beer product. The as-is mass balance reflects this large water input, which dominates the total mass flow but does not affect DM-based allocation.

4. **DM reconciliation gap in brewing:** The independently-sourced beer and BSG yields create a ~0.089 t DM gap per t barley (10.1% of input). This gap is explainable by yeast biomass, evaporation losses, trub, and minor yield parameter inconsistencies. It is documented in Section 7.2 and does not materially affect allocation results because the relative DM proportions are robust.

5. **Wet vs. dried BSG:** This table uses dried BSG (91% DM, 0.16 t/t barley). Many breweries sell wet BSG (20–28% DM, ~0.96 t/t barley) directly to nearby farms. The choice of wet vs. dried BSG affects the as-is yield and price but not the DM-based allocation (same DM mass either way).

6. **Missing co-products:** Brewing also produces spent hops (~0.01 t/t malt) and spent yeast (~0.04 t/t malt). These are typically low-value and often excluded from allocation.

7. **Regional variation:** Malt and beer prices vary significantly by region. European malt prices tend to be higher than North American due to energy costs and regulatory differences.

8. **Moisture basis:** This document uses 12% moisture as the calculation basis, which is a common storage moisture for barley. The USDA trading standard is 14.5% (per 7 CFR Part 1421). Using 14.5% would change the DM input to 0.855 t (instead of 0.880 t) and proportionally adjust all DM-based calculations.

---
