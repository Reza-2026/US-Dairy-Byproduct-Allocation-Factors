# Cotton Processing: Co-Product Allocation Methodology, Data Sources, and Calculations

**Document Version:** 1.0  
**Date:** May 2026  
**Basis:** 1 metric ton (t) of seed cotton at ~10% moisture (90% DM)  
**Price Period:** 2024–2025 average (unless otherwise noted)

---

## Table of Contents

1. [Standard Basis and Conversions](#1-standard-basis-and-conversions)
2. [Data Sources and References](#2-data-sources-and-references)
3. [Cotton Processing System](#3-cotton-processing-system)
4. [Co-Product Yields and Properties](#4-co-product-yields-and-properties)
5. [Prices](#5-prices)
6. [Allocation Methodology](#6-allocation-methodology)
7. [Mass Balance Verification](#7-mass-balance-verification)
8. [Complete Data Table](#8-complete-data-table)
9. [Data Quality and Limitations](#9-data-quality-and-limitations)
10. [System Boundary Assumption and the Alternative Sequential Treatment](#10-system-boundary-assumption-and-the-alternative-sequential-treatment)

---

## 1. Standard Basis and Conversions

### 1.1 Parent Input Definition

| Parameter | Value | Source |
|-----------|-------|--------|
| **Parent crop** | Seed cotton (unginned cotton, lint + seed) | — |
| **Input quantity** | 1 metric ton (1,000 kg) | — |
| **Moisture content** | ~10% (90% DM) | Industry average for seed cotton at the gin [^1^]; moisture varies 8–12% depending on harvest conditions and storage |
| **Dry matter (DM) input** | 0.900 t DM/t seed cotton | Calculated: 1.000 × 0.90 = 0.900 |
| **Bale equivalent** | ~1.75 bales/t seed cotton | The 480-lb bale is the statistical unit USDA reports cotton production in; actual net bale weights average ~495 lb [^1^]. At 480 lb (217.72 kg), 1 t of lint = 4.59 bales, so 0.38 t lint per t seed cotton = 1.75 bales. |
| **Typical lint turnout** | ~36–40% of seed cotton weight | Gin turnout for US upland cotton [^1^][^12^] |
| **Typical seed turnout** | ~45–51% of seed cotton weight | Ratio of seed to seed cotton at the gin [^11^][^12^]; see Section 4.1 |

### 1.2 Unit Conversions

| Conversion | Factor |
|------------|--------|
| 1 bale of cotton (US) | 480 lb gross weight ≈ 217.72 kg (net ~215 kg lint) |
| 1 lb | 0.453592 kg = 0.000453592 t |
| 1 t seed cotton | ~1.75 bales of lint (at 0.38 t lint/t seed cotton and 480 lb/bale) |
| 1 short ton | 2,000 lb = 0.907185 metric ton |
| 1 metric ton | 2,204.62 lb = 1.10231 short tons |

> **Note on seed cotton definition:** "Seed cotton" refers to the harvested, unginned product consisting of cotton lint (fiber) still attached to the cottonseed. It is the input to the ginning process (Stage 1). The term is distinct from "cotton lint" (the ginned fiber) and "whole cottonseed" (the seed after ginning), which are the co-products of Stage 1.

> **Note on cotton types:** This document models **upland cotton** (*Gossypium hirsutum*), which represents ~95% of US cotton production. Pima/ELS cotton (*Gossypium barbadense*) has different lint characteristics (longer staple, higher price) and is not covered here.

---

## 2. Data Sources and References

### 2.1 Primary Sources

| Citation | Full Title | Type | URL |
|----------|-----------|------|-----|
| [^1^] | USDA AMS — Cotton Varieties Planted and Ginning Reports | Government (USDA) | https://www.ams.usda.gov/ |
| [^2^] | ICAC (2024). *Cotton: Review of the World Situation* | Intergovernmental Organization | https://www.icac.org/ |
| [^3^] | USDA ERS (2025). *Cotton and Wool Outlook* | Government (USDA) | https://ers.usda.gov/ |
| [^4^] | USDA NASS (2025). *Cotton Ginning Annual Summary* | Government (USDA) | https://www.nass.usda.gov/ |
| [^5^] | ICE Futures U.S. — Cotton No. 2 Futures | Exchange/Market | https://www.theice.com/products/254/Cotton-No-2-Futures |
| [^6^] | Anthony, W.S. and Mayfield, W.D. (Eds.) (1994). *Cotton Ginners Handbook*. USDA Agricultural Handbook No. 503 | Academic/Government | https://www.cotton.org/tech/ginners/ |
| [^7^] | O'Brien, R.D., Jones, L.A., King, C.C., Wakelyn, P.J., and Wan, P.J. (2005). "Cottonseed Oil." Chapter 3 in *Bailey's Industrial Oil and Fat Products*, 6th ed., Vol. 2. Wiley-Interscience. DOI: 10.1002/0471678493.bio026 | Academic | — |
| [^8^] | Feedipedia — Cottonseed meal and hulls (INRAE/CIRAD/AFZ/FAO) | Research Consortium/Database | https://www.feedipedia.org/ |
| [^9^] | OECD-FAO (2025). *Agricultural Outlook: Cotton Chapter* | International Organization | https://www.oecd.org/ |
| [^10^] | National Cottonseed Products Association (2025). *Cottonseed Trading Rules, Bylaws & Charter* | Industry Association | https://www.cottonseed.com/ |
| [^11^] | USDA NASS. *Crop Production* and *Crop Production Annual Summary* — cotton and cottonseed production tables | Government (USDA) | https://www.nass.usda.gov/ |
| [^12^] | Texas A&M AgriLife Research and Extension (2025). *Texas High Plains RACE Trial Report* | Academic/Extension | https://varietytesting.tamu.edu/ |
| [^13^] | Albers, D. (Cotton Incorporated). *Perspectives on Cotton Seed Size in Cotton Varieties* | Industry Research | https://www.cottoninc.com/ |
| [^14^] | US EPA. *AP-42 Compilation of Air Pollutant Emission Factors*, Section 9.7: Cotton Ginning | Government (EPA) | https://www.epa.gov/air-emissions-factors-and-quantification/ap-42-compilation-air-emissions-factors |
| [^15^] | National Cotton Council. *Cotton: From Field to Fabric — Cottonseed* | Industry Association | https://www.cotton.org/pubs/cottoncounts/fieldtofabric/cottonseed.cfm |
| [^16^] | *Cotton Seed Size — What is the "Fuzz" All About?* Journal of Cotton Science 27:81–94 (2023) | Academic (peer-reviewed) | https://www.cotton.org/journal/2023-27/2/upload/JCS27-081.pdf |
| [^17^] | ICAC. *Report of an Expert Panel on Ginning Methods* | Intergovernmental Organization | https://icac.org/ |

### 2.2 How Sources Were Used

- **Yield data (Stage 1):** USDA NASS [^4^][^11^], Anthony and Mayfield [^6^], and ICAC [^2^] provided cotton ginning yield data. Lint turnout and seed yield ranges reflect variation across cotton varieties, growing conditions, harvest system, and ginning technology.
- **Seed-to-lint ratio (Stage 1):** The adopted seed yield is set from the ratio of marketed cottonseed to marketed lint. USDA NASS national production [^11^] and measured gin turnouts from the Texas High Plains RACE variety trials [^12^] provide the ratio; Cotton Incorporated [^13^] and the *Journal of Cotton Science* seed-size review [^16^] document the downward trend in that ratio. The National Cotton Council's long-standing figure [^15^] is retained as the sensitivity case (Section 4.1).
- **Gin trash fraction:** EPA AP-42 Section 9.7 [^14^] and the ICAC ginning panel [^17^] provide foreign-matter and gin-waste quantities by harvest system.
- **Yield data (Stage 2):** O'Brien et al. [^7^], NCPA [^10^], and ICAC [^2^] provided cottonseed crushing yield data. Ranges reflect variation across extraction methods (expeller vs. solvent) and seed dehulling configurations.
- **Price data (lint):** USDA ERS [^3^] and ICE Futures U.S. [^5^] provided cotton lint price data from futures and spot markets.
- **Price data (seed products):** USDA ERS [^3^], Feedipedia [^8^], and NCPA [^10^] provided cottonseed oil, meal, hulls, and linters price data.
- **DM contents:** USDA AMS [^1^] provided cotton moisture standards. NCPA [^10^] and O'Brien et al. [^7^] provided cottonseed product specifications.
- **Market outlook context:** OECD-FAO [^9^] provides cotton market outlook projections and long-term price trends that inform the selection of price ranges.

> **Note on URL specificity:** References [^1^] (USDA AMS), [^3^] (USDA ERS), and [^4^] (USDA NASS) currently link to organizational homepages rather than specific report pages. This is because specific annual reports and extension PDFs rotate URLs with each publication cycle. Specific annual NASS Cotton Ginning Annual Summary reports, ERS Cotton and Wool Outlook reports, and AMS cotton ginning reports were consulted; homepage URLs are provided for general navigation as specific report URLs are not persistent.

---

## 3. Cotton Processing System

### 3.1 Process Description

Cotton processing consists of two distinct stages: ginning (Stage 1) and cottonseed crushing (Stage 2).

**Stage 1: Cotton Ginning**

1. **Receiving and drying:** Seed cotton is received at the gin and dried to the optimal moisture level (~6–8%) for efficient ginning.
2. **Cleaning:** Foreign matter (burrs, sticks, leaves, sand, dust) is removed through a series of cylinders and screens.
3. **Ginning:** Seed cotton passes through gin stands where rotating saws pull the lint fibers away from the seed. The lint is separated from the seed.
4. **Lint cleaning:** Ginned lint passes through lint cleaners to remove remaining trash and short fibers (motes).
5. **Baling:** Cleaned lint is compressed into 480-lb bales for market.

**Stage 1 co-products:**
- **Cotton lint:** The primary high-value product — textile fiber.
- **Gin trash:** Burrs, sticks, leaves, motes, sand and fine debris removed during cleaning and lint cleaning. Gin trash is not treated as a co-product here — it carries no allocation — but it is a substantial mass stream and is accounted for explicitly in the mass balance (Section 7.1).
- **Whole cottonseed:** The seed with short fibers (linters) still attached. This is a **dual-pathway product**: it can be (a) used directly as cattle feed (high-energy, high-protein supplement for dairy rations) without further processing, OR (b) sent to Stage 2 (cottonseed crushing) to produce oil, meal, hulls, and linters. The allocation depends on which pathway is used (see Section 6).

**Stage 2: Cottonseed Crushing**

1. **Delinting:** Short fibers (linters) remaining on the seed after ginning are removed in one or two cuts using delinting saws.
2. **Dehulling:** Seed hulls are partially removed using bar knives or impact dehullers. In typical commercial practice, partial dehulling removes ~70–80% of hulls; the remainder stays with the kernel and ends up in the meal.
3. **Flaking and conditioning:** Dehulled kernels (meats) are flaked and heated to improve oil extractability.
4. **Pressing:** Mechanical screw presses (expellers) remove ~50–60% of the oil, producing a pressed cake.
5. **Solvent extraction:** Hexane extracts the remaining oil from the pressed cake.
6. **Desolventizing and toasting:** Meal is heated to remove residual hexane and toast the protein (reducing gossypol toxicity).
7. **Hull blending:** Some hulls may be added back to the meal to achieve the target protein specification (41% protein meal requires ~10–15% hull addition).

**Stage 2 co-products:**
- **Cottonseed oil:** The primary high-value product — cooking oil, shortening, soap, biodiesel.
- **Cottonseed meal:** Protein-rich animal feed (41–44% protein, solvent-extracted).
- **Cottonseed hulls:** Low-value roughage for cattle feed, mulch.
- **Cottonseed linters:** Cellulose fiber for chemical cellulose, medical pads, paper, batting.

> **Note on dual pathway for whole cottonseed:** Whole cottonseed is unusual among the intermediate products in this review because it is itself a marketed final product — a high-energy, high-protein dairy feed — as well as the feedstock for crushing. Part of the cottonseed produced at the gin is sold directly to dairy operations and the remainder is crushed. These are two distinct fates, and each requires its own allocation:
> - **Pathway A (cottonseed used directly):** Stage 1 only. Two final products: cotton lint and whole cottonseed.
> - **Pathway B (cottonseed crushed):** Stage 1 and Stage 2 together. Five final products: cotton lint, cottonseed oil, meal, hulls and linters, all reported on one seed cotton basis.
>
> A given tonne of cottonseed follows one pathway or the other, never both, so the two sets of factors are alternatives rather than a double count. A study covering a mixed system may weight them by the share of seed crushed in its region.
>
> Section 6.1 sets out how the intermediate is valued in Pathway B and why that treatment differs from the market-price cascade used for the other two-stage crops in this review.

### 3.2 Process Flow

```
STAGE 1: COTTON GINNING

1 t seed cotton at 90% DM (0.900 t DM)
        │
        ▼
  ┌─ COTTON GINNING ────────────────────────────────┐
  │                                                 │
  │  Gin trash: 0.140 t as-is (14.0%)               │
  │  (burrs, sticks, leaves, motes, sand, fines)    │
  │  DM in gin trash: 0.121 t DM (13.5% of DM in)   │
  │                                                 │
  │  Cotton lint: 0.380 t at 90% DM             ◄── co-product (final)
  │    (0.342 t DM)                                 │
  │                                                 │
  │  Whole cottonseed: 0.480 t at 91% DM        ◄── DUAL FATE:
  │    (0.437 t DM)                                   Pathway A: final product (dairy feed)
  │                                                   Pathway B: feedstock → Stage 2
  └─────────────────────────────────────────────────┘

PATHWAY A: COTTONSEED USED DIRECTLY (as dairy feed)
  → Two final products: lint + whole cottonseed
  → Economic: Lint 81.4%, Seed 18.6%
     Mass:     Lint 43.9%, Seed 56.1%

PATHWAY B: COTTONSEED CRUSHED (Stage 2)

0.480 t whole cottonseed (basis below is 1 t cottonseed at 91% DM = 0.910 t DM)
        │
        ▼
  ┌─ COTTONSEED CRUSHING ───────────────────────────┐
  │                                                 │
  │  Processing losses: ~0.010 t as-is (~1%)        │
  │  (handling, residual solvent, moisture, fines)  │
  │  DM losses: ~0.009 t DM (0.96%)                 │
  │                                                 │
  │  Cottonseed oil:     0.170 t at 100% DM     ◄── co-product (final)
  │  Cottonseed meal:    0.475 t at  88% DM     ◄── co-product (final)
  │  Cottonseed hulls:   0.275 t at  90% DM     ◄── co-product (final)
  │  Cottonseed linters: 0.070 t at  94% DM     ◄── co-product (final)
  │                                                 │
  └─────────────────────────────────────────────────┘

PATHWAY B — ALLOCATION OVER ALL FIVE FINAL PRODUCTS
  (per 1 t seed cotton; Stage 2 streams converted to the seed
   cotton basis by multiplying by 0.48 t seed/t seed cotton)

  ECONOMIC                          MASS (dry matter)

  Lint:     77.2%                   Lint:     44.2%
  Oil:      10.4%                   Oil:      10.5%
  Meal:      9.4%                   Meal:     25.9%
  Hulls:     1.5%                   Hulls:    15.3%
  Linters:   1.5%                   Linters:   4.1%
  ─────────────────                 ─────────────────
  Total:   100.0%                   Total:   100.0%
  (Seed-derived: 22.8%)             (Seed-derived: 55.8%)

  Lint's economic share is lower in Pathway B (77.2%) than in
  Pathway A (81.4%) because crushing turns $139.20 of whole
  cottonseed into $179.34 of oil, meal, hulls and linters, so the
  seed side of the denominator grows. See Section 6.1.
```

---

## 4. Co-Product Yields and Properties

### 4.1 Stage 1: Cotton Ginning Yields

| Co-product | Yield (t/t seed cotton) | Range | Source & Calculation |
|------------|------------------------|-------|---------------------|
| **Cotton lint** | 0.38 | 0.36–0.40 | Gin turnout for US upland cotton [^1^][^6^][^12^]. Turnout varies with variety, growing conditions, harvest system and gin efficiency; higher-micronaire cotton tends to gin out higher. |
| **Whole cottonseed** | 0.48 | 0.45–0.51 | Derived as lint yield × the current US seed-to-lint ratio of 1.26 (see note below): 0.38 × 1.26 = 0.479. The range spans the ratio range 1.23–1.29 observed across national production data and measured gin turnouts [^11^][^12^]. |
| **Gin trash (not allocated)** | 0.14 | 0.10–0.18 | Residual: 1.000 − 0.380 − 0.480. Consistent with measured gin waste for the US crop mix [^14^][^17^]. |

#### Note on the seed-to-lint ratio

This is the single most consequential parameter in Stage 1, because both the mass and the economic allocation depend on the ratio of lint to seed. It is set from current US data rather than from the ratio most often quoted in the cotton literature.

| Basis | Period | Seed : lint |
|-------|--------|-------------|
| USDA NASS national production (3,644 thousand t seed / 12,066 thousand bales) [^11^] | 2023 | 1.26 |
| USDA NASS national production (4,262 thousand t seed / 14,413 thousand bales) [^11^] | 2024 | 1.23 |
| USDA NASS national production (4,308 thousand t seed / 14,268 thousand bales) [^11^] | 2025 | 1.26 |
| Texas High Plains RACE trials, measured turnouts (lint ~34.5%, seed ~44.5% of seed cotton) [^12^] | 2025 | 1.29 |
| National Cotton Council, "about 162 lb of cottonseed per 100 lb of fiber" [^15^] | long-standing figure | 1.62 |

**Adopted: 1.26**, giving 0.48 t whole cottonseed per t seed cotton.

The gap between the current data and the long-standing 1.62 figure is not a measurement disagreement. Breeding has raised lint percent — the lint fraction of lint plus seed — from roughly 38% to roughly 44% across the commercial pipeline, which mechanically lowers the seed-to-lint ratio. Cotton Incorporated documents a 10–15% reduction in cottonseed per bale as lint percent rises [^13^], and the *Journal of Cotton Science* seed-size review states that the seed-to-lint ratio "has been decreasing considerably over the years" [^16^]. A ratio of 1.62 corresponds to a lint percent of 38.2%; the 2023–2025 NASS production data correspond to 44.2–44.8%. Because this document is built on 2024–2025 prices and yields, the current ratio is the consistent choice.

This is *not* a conventional-versus-transgenic distinction. High lint percent is characteristic of the modern commercial pipeline as a whole, including non-transgenic material; "conventional" is used elsewhere in this document (Section 9.3) in its usual sense of non-organic, non-GMO, and carries no implication about lint percent.

#### Sensitivity: the long-standing 1.62 ratio

Studies drawing on older literature, or on the National Cotton Council figure, will use 0.60 t whole cottonseed per t seed cotton. That case is reported here so results on either basis can be reconciled:

| | Adopted (seed 0.48, ratio 1.26) | Legacy (seed 0.60, ratio 1.58) |
|---|---|---|
| Pathway A — lint / seed, economic | 81.4% / 18.6% | 77.7% / 22.3% |
| Pathway A — lint / seed, mass | 43.9% / 56.1% | 38.5% / 61.5% |
| Pathway B — lint, economic | 77.2% | 73.1% |
| Pathway B — lint, mass | 44.2% | 38.7% |
| Implied gin trash | 14.0% | 2.0% |

The legacy case carries a second problem that is easy to miss: holding lint at 0.38 and seed at 0.60 leaves only 2.0% of the seed cotton for gin trash. Measured gin waste is far higher — EPA AP-42 reports roughly 150 lb of trash per 500-lb bale for spindle-picked cotton and about 1,000 lb per bale for stripper-harvested cotton [^14^], and ICAC puts foreign matter in seed cotton at 5–10% for spindle-harvested and 10–30% for stripper-harvested material [^17^]. The three Stage 1 figures sum to 1.000 by construction, so the seed yield and the gin trash fraction cannot be set independently; the adopted values satisfy both the seed-to-lint ratio and the measured trash range.

> **Note on the yield relationship:** Lint and seed yields are inversely related within a variety, but the two ranges in the table above are not independent — a run at the top of the lint range will not also sit at the top of the seed range. Each pairing must leave a physically sensible gin trash residual.

### 4.2 Stage 2: Cottonseed Crushing Yields

| Co-product | Yield (t/t whole cottonseed) | Range | Source & Calculation |
|------------|------------------------------|-------|---------------------|
| **Cottonseed oil** | 0.17 | 0.16–0.18 | Industry average for solvent extraction [^7^][^10^]. Expeller-only yields are ~0.13–0.16 t/t; solvent extraction achieves ~0.16–0.18 t/t. |
| **Cottonseed meal** | 0.475 | 0.45–0.50 | Represents 41% protein, solvent-extracted meal with some residual hulls [^7^][^10^]. Meal yield varies with protein specification (41% protein = higher yield with more hulls; 44% protein = lower yield with fewer hulls) and oil extraction efficiency. |
| **Cottonseed hulls** | 0.275 | 0.25–0.30 | Represents separated hulls after partial dehulling [^7^]. Hull yield depends on the degree of dehulling: more complete dehulling produces more separated hulls but reduces meal yield and meal protein content. |
| **Cottonseed linters** | 0.07 | 0.05–0.09 | Represents combined first-cut and second-cut linters [^7^][^10^]. Linters yield varies with delinting method (saw-type vs. abrasive), number of cuts, and seed variety. |

> **Note on yield relationships:** Oil and meal yields are inversely related (more oil extraction means less meal). Hull yield depends on the degree of dehulling. Linters are removed before dehulling and oil extraction. The four co-products sum to 0.99 t/t (0.17 + 0.475 + 0.275 + 0.07), with ~1% processing losses.

> **Note on basis for Pathway B:** Section 4.2 shows Stage 2 yields per tonne of whole cottonseed (the natural processing basis). For Pathway B calculations (Sections 6.3 and 8), these yields are converted to a seed cotton basis by multiplying by the cottonseed yield (0.48 t seed/t seed cotton): Oil 0.0816, Meal 0.2280, Hulls 0.1320, Linters 0.0336 t/t seed cotton. All Pathway B results are presented on this consistent seed cotton basis.

### 4.3 Dry Matter Contents

**Stage 1:**

| Co-product | DM (%) | Basis |
|------------|--------|-------|
| Cotton lint | 90.0% | Cotton lint at the gin typically has 8–12% moisture. The USDA marketing standard is 8.5% moisture (91.5% DM), but actual moisture varies significantly with harvesting conditions and gin drying. The 90% DM value is a reasonable industry average for lint at the gin [^1^]. |
| Whole cottonseed | 91.0% | Whole cottonseed (with linters attached) typically has 8–10% moisture. The 91% DM value is consistent with industry data for cottonseed entering the oil mill [^7^]. |

**Stage 2:**

| Co-product | DM (%) | Basis |
|------------|--------|-------|
| Cottonseed oil | 100.0% | Crude and refined cottonseed oil are essentially pure lipid with negligible moisture (<0.1%). |
| Cottonseed meal | 88.0% | Standard trading specification: maximum 12% moisture = minimum 88% DM [^10^]. Solvent-extracted, 41% protein meal is typically delivered at 10–12% moisture. |
| Cottonseed hulls | 90.0% | Cottonseed hulls are typically 89–91% DM (9–11% moisture). The 90% DM value represents the industry average [^10^]. |
| Cottonseed linters | 94.0% | Cotton linters are cellulose fibers with low moisture content (5–7% moisture, 93–95% DM). The 94% DM value represents the industry average for mechanically delinted linters [^7^]. |



### 4.4 DM Output per Tonne

**Stage 1 (per tonne of seed cotton):**

| Co-product | Calculation | DM Output (t/t seed cotton) |
|------------|-------------|----------------------------|
| **Cotton lint** | 0.38 × 0.90 | **0.3420** |
| **Whole cottonseed** | 0.48 × 0.91 | **0.4368** |
| **Total co-product DM** | | **0.7788** |
| *Gin trash DM (not a co-product)* | *0.9000 − 0.7788* | *0.1212* |

**Stage 2 (per tonne of whole cottonseed):**

| Co-product | Calculation | DM Output (t/t cottonseed) |
|------------|-------------|---------------------------|
| **Cottonseed oil** | 0.17 × 1.00 | **0.1700** |
| **Cottonseed meal** | 0.475 × 0.88 | **0.4180** |
| **Cottonseed hulls** | 0.275 × 0.90 | **0.2475** |
| **Cottonseed linters** | 0.07 × 0.94 | **0.0658** |
| **Total** | | **0.9013** |

**Pathway B: Cascade DM Output (per tonne of seed cotton):**

**Pathway B: DM Output of the Five Final Products (per tonne of seed cotton):**

All 5 final products on a common seed cotton basis. Stage 2 DM outputs are converted by multiplying by the cottonseed yield (0.48 t seed/t seed cotton).

| Co-product | Calculation | DM Output (t/t seed cotton) |
|------------|-------------|----------------------------|
| **Cotton lint** | 0.38 × 0.90 | **0.3420** |
| **Cottonseed oil** | 0.48 × 0.17 × 1.00 | **0.0816** |
| **Cottonseed meal** | 0.48 × 0.475 × 0.88 | **0.2006** |
| **Cottonseed hulls** | 0.48 × 0.275 × 0.90 | **0.1188** |
| **Cottonseed linters** | 0.48 × 0.07 × 0.94 | **0.0316** |
| **Total co-product DM** | | **0.7746** |
| *DM input (1 t seed cotton at 90% DM)* | | *0.9000* |
| *DM not in a co-product* | | *0.1254 (13.93%)* |

> **Note on the DM gap:** The 0.1254 t of dry matter that does not leave the system as a co-product is 0.1212 t of gin trash (13.47% of the DM input) plus 0.0042 t of Stage 2 processing losses (0.96% of cottonseed DM × 0.48 = 0.46% of the DM input). Gin trash dominates and is a real, quantified stream rather than an unexplained residual: 0.140 t as-is at about 87% DM. It carries no allocation, so it does not appear in the denominators of Section 6.
---

## 5. Prices

### 5.1 Stage 1 Prices

| Co-product | Price (USD/t) | Range | Source | Notes |
|------------|--------------|-------|--------|-------|
| **Cotton lint** | 1,600 | 1,200–2,000 | USDA ERS [^3^]; ICE Futures U.S. [^5^] | 2024–2025 average for US upland cotton (strict low middling 1-1/16" staple). Equivalent to ~$0.73/lb. Prices vary with quality (staple length, micronaire, strength, color grade) and market conditions. |
| **Whole cottonseed** | 290 | 200–380 | USDA ERS [^3^]; NCPA [^10^]; industry estimates | 2024–2025 average for whole cottonseed at the oil mill or feed lot. Used as cattle feed or sold for crushing. Price depends on proximity to oil mills, dairy demand, and seasonal supply. |

### 5.2 Stage 2 Prices

| Co-product | Price (USD/t) | Range | Source | Notes |
|------------|--------------|-------|--------|-------|
| **Cottonseed oil** | 1,000 | 800–1,200 | USDA ERS [^3^] | 2024–2025 average for crude cottonseed oil (FOB). Prices track other vegetable oils but at a discount to soybean oil. Used for cooking oil, shortening, soap, and biodiesel. |
| **Cottonseed meal** | 325 | 250–400 | USDA ERS [^3^]; Feedipedia [^8^]; NCPA [^10^] | 2024–2025 average for solvent-extracted, 41% protein meal. Prices vary with protein content and regional demand. 44% protein meal commands ~$30–50/t premium. |
| **Cottonseed hulls** | 90 | 60–120 | Feedipedia [^8^]; NCPA [^10^]; university extension feed reports | 2024–2025 average for cottonseed hulls used as cattle feed roughage. Low-value product; price varies with proximity to dairy operations. Some markets price hulls at $0 (given away) when transportation costs exceed value. |
| **Cottonseed linters** | 350 | 200–500 | NCPA [^10^]; O'Brien et al. [^7^]; industry estimates | 2024–2025 average across linter grades and end uses. First-cut linters (longer fibers, chemical cellulose): ~$300–600/t. Second-cut linters (shorter fibers, batting/paper): ~$150–350/t. Blended average: ~$350/t. |

### 5.3 Price Verification

**Cotton lint:**

```
ICE Futures U.S. Cotton No. 2 (2025): ~$0.65-0.85/lb = $1,430-1,875/t
USDA ERS (2025): average spot price ~$0.70-0.80/lb = $1,540-1,765/t
Historical range (2020-2025): $0.50-1.50/lb = $1,100-3,300/t

Adopted: $1,600/t
```

**Whole cottonseed:**

```
USDA ERS (2025): ~$220-320/t (at the oil mill)
NCPA (2025): ~$200-350/t
Feed value premium during drought: up to $380/t

Adopted: $290/t
```

**Cottonseed oil:**

```
USDA ERS (2025): crude cottonseed oil ~$850-1,050/t
Feedipedia indicative values: ~$800-1,100/t
Discount to soybean oil: typically $50-150/t

Adopted: $1,000/t
```

**Cottonseed meal:**

```
USDA ERS (2025): 41% protein meal ~$280-380/t
NCPA (2025): ~$250-400/t
Feedipedia indicative values: comparable to canola meal (~$250-350/t)

Adopted: $325/t
```

### 5.4 Revenue per Tonne

**Stage 1 (per tonne of seed cotton) — Pathway A:**

| Co-product | Calculation | Revenue (USD/t seed cotton) |
|------------|-------------|----------------------------|
| **Cotton lint** | 0.38 × 1,600 | **$608.00** |
| **Whole cottonseed** | 0.48 × 290 | **$139.20** |
| **Total** | | **$747.20** |

**Stage 2 (per tonne of whole cottonseed):**

| Co-product | Calculation | Revenue (USD/t cottonseed) |
|------------|-------------|---------------------------|
| **Cottonseed oil** | 0.17 × 1,000 | **$170.00** |
| **Cottonseed meal** | 0.475 × 325 | **$154.38** |
| **Cottonseed hulls** | 0.275 × 90 | **$24.75** |
| **Cottonseed linters** | 0.07 × 350 | **$24.50** |
| **Total** | | **$373.63** |

**Pathway B: Revenue of the Five Final Products (per tonne of seed cotton):**

All 5 final products on a common seed cotton basis. Stage 2 revenues are converted by multiplying by the cottonseed yield (0.48 t seed/t seed cotton).

| Co-product | Calculation | Revenue (USD/t seed cotton) |
|------------|-------------|----------------------------|
| **Cotton lint** | 0.38 × 1,600 | **$608.00** |
| **Cottonseed oil** | 0.0816 × 1,000 | **$81.60** |
| **Cottonseed meal** | 0.2280 × 325 | **$74.10** |
| **Cottonseed hulls** | 0.1320 × 90 | **$11.88** |
| **Cottonseed linters** | 0.0336 × 350 | **$11.76** |
| **Total** | | **$787.34** |

> **Note on the value of the intermediate:** Whole cottonseed sold as feed is worth $139.20/t seed cotton (0.48 × $290). The same seed crushed yields co-products worth $179.34/t seed cotton (0.48 × $373.63/t cottonseed), a difference of $40.14/t seed cotton ($83.63/t cottonseed) — the gross processing margin before crushing costs are deducted. Pathway A therefore has a revenue base of $747.20/t seed cotton and Pathway B a base of $787.34/t seed cotton. Because lint's revenue is the same in both, its economic share is lower in Pathway B (77.2%) than in Pathway A (81.4%), and the seed-derived products together carry 22.8% rather than the seed's 18.6%.

---

## 6. Allocation Methodology

### 6.1 Treatment of the Intermediate Product

Cotton is a two-stage chain, and whole cottonseed sits between the two stages. How that intermediate is valued determines the whole result, so the convention is stated here before any numbers are calculated.

**There are two conventions, not three.**

*Market-price cascade.* The intermediate is valued at the price it transacts at between the two stages. Stage 1 divides the parent burden between the final Stage 1 product and the intermediate on that basis; Stage 2 divides the intermediate's burden among its own products; the two stage allocations are multiplied along each path.

*Direct end-of-chain.* All final products are placed on a single denominator — one revenue total, or one dry matter total — and each takes its own share of it.

A third option is sometimes proposed: cascade, but value the intermediate at its **derived value** (the summed revenue of the products it becomes) instead of its market price. That is not a third convention. Writing $L$ for lint revenue and $x_1 \ldots x_4$ for the revenues of the four crush products, with $D = \sum x_i$, the derived-value cascade gives product $i$:

$$\frac{D}{L + D} \times \frac{x_i}{D} \;=\; \frac{x_i}{L + D}$$

which is exactly the direct end-of-chain calculation. The $D$ cancels. Valuing an intermediate at its derived value and cascading is the direct method under another name, and this document reports it as such.

**Cotton uses the direct end-of-chain treatment.** Three reasons:

1. **Whole cottonseed is itself a final product of this study, not only an intermediate.** It is a major dairy feed and this document reports an allocation factor for it in its own right (Pathway A, Section 6.2). Its quoted price of $290/t is therefore the price in a *competing end use* — what a dairy pays for the seed — and not a transfer price into the crush. That is the opposite of the situation for the other two-stage crops in this review, where the intermediate's quoted price is what the next stage actually pays and the intermediate leaves no factor of its own.

2. **Using $290/t as a cascade price would cap the seed's burden regardless of its fate.** It would fix the seed side at 18.6% whether the seed is fed whole or converted into $179.34 of oil, meal, hulls and linters. Under the direct treatment the seed side carries 22.8% when it is crushed, which is what the products it becomes are actually worth.

3. **The system boundary is a single integrated block.** Section 10 sets out the boundary: seed cotton enters the gin and five marketable co-products leave. Within one block, all final products compete for one denominator.

**Where this convention does not apply.** A study that models the gin and the crusher as two separate unit processes — because it holds distinct emission factors, energy sources and waste streams for each (gin trash versus hexane emissions) — should use the market-price cascade at $290/t instead. Section 10.2 gives that alternative and its result.

**Mass allocation.** For economic allocation the two conventions coincide exactly, as shown above. For mass they do not, because Stage 2 loses 0.96% of the cottonseed's dry matter: the direct method places all five products over the summed dry matter that actually leaves the system (0.7746 t), while a cascade holds lint at its Stage 1 share and splits the seed's share among four products, absorbing the Stage 2 loss inside the seed side. The difference is at most 0.24 percentage points:

| Final co-product | Mass — direct (used here) | Mass — cascade |
|-----------------|---------------------------|----------------|
| Cotton lint | 44.2% | 43.9% |
| Cottonseed oil | 10.5% | 10.6% |
| Cottonseed meal | 25.9% | 26.0% |
| Cottonseed hulls | 15.3% | 15.4% |
| Cottonseed linters | 4.1% | 4.1% |

The direct values are adopted so that one convention governs both the economic and the mass columns of the same table.

### 6.2 Pathway A: Cottonseed Used Directly (Stage 1 only)

Two final products: cotton lint and whole cottonseed, the seed valued at its market price of $290/t. Gin trash carries no allocation and does not appear in either denominator.

**Economic allocation:**

| Co-product | Calculation | Allocation |
|------------|-------------|------------|
| Cotton lint | (608.00 ÷ 747.20) × 100 | **81.4%** |
| Whole cottonseed | (139.20 ÷ 747.20) × 100 | **18.6%** |
| **Total** | | **100.0%** |

**Mass allocation:**

| Co-product | Calculation | Allocation |
|------------|-------------|------------|
| Cotton lint | (0.3420 ÷ 0.7788) × 100 | **43.9%** |
| Whole cottonseed | (0.4368 ÷ 0.7788) × 100 | **56.1%** |
| **Total** | | **100.0%** |

**Comparison:**

| Co-product | Economic | Mass | Difference |
|------------|----------|------|------------|
| Cotton lint | 81.4% | 43.9% | +37.5 pp |
| Whole cottonseed | 18.6% | 56.1% | −37.5 pp |

The 37.5 pp spread reflects lint's value-to-mass ratio: lint sells for $1,600/t against $290/t for the seed — 5.5 times the price — while carrying 43.9% of the dry matter.

### 6.3 Pathway B: Cottonseed Crushed (five final products)

All five final products are placed on one seed cotton basis and one denominator, following Section 6.1. Stage 2 streams are converted to that basis by multiplying by the cottonseed yield (0.48 t seed/t seed cotton).

**Economic allocation:**

| Final co-product | Revenue (USD/t seed cotton) | Calculation | Allocation |
|-----------------|----------------------------|-------------|------------|
| Cotton lint | $608.00 | (608.00 ÷ 787.34) × 100 | **77.2%** |
| Cottonseed oil | $81.60 | (81.60 ÷ 787.34) × 100 | **10.4%** |
| Cottonseed meal | $74.10 | (74.10 ÷ 787.34) × 100 | **9.4%** |
| Cottonseed hulls | $11.88 | (11.88 ÷ 787.34) × 100 | **1.5%** |
| Cottonseed linters | $11.76 | (11.76 ÷ 787.34) × 100 | **1.5%** |
| **Total** | **$787.34** | | **100.0%** |
| *Seed-derived subtotal* | *$179.34* | | *22.8%* |

**Mass allocation:**

| Final co-product | DM Output (t/t seed cotton) | Calculation | Allocation |
|-----------------|----------------------------|-------------|------------|
| Cotton lint | 0.3420 | (0.3420 ÷ 0.7746) × 100 | **44.2%** |
| Cottonseed oil | 0.0816 | (0.0816 ÷ 0.7746) × 100 | **10.5%** |
| Cottonseed meal | 0.2006 | (0.2006 ÷ 0.7746) × 100 | **25.9%** |
| Cottonseed hulls | 0.1188 | (0.1188 ÷ 0.7746) × 100 | **15.3%** |
| Cottonseed linters | 0.0316 | (0.0316 ÷ 0.7746) × 100 | **4.1%** |
| **Total** | **0.7746** | | **100.0%** |
| *Seed-derived subtotal* | *0.4326* | | *55.8%* |

**Comparison:**

| Final co-product | Economic | Mass | Difference |
|-----------------|----------|------|------------|
| Cotton lint | 77.2% | 44.2% | +33.0 pp |
| Cottonseed oil | 10.4% | 10.5% | −0.1 pp |
| Cottonseed meal | 9.4% | 25.9% | −16.5 pp |
| Cottonseed hulls | 1.5% | 15.3% | −13.8 pp |
| Cottonseed linters | 1.5% | 4.1% | −2.6 pp |

**Equivalence check.** The same economic figures arise from a derived-value cascade, confirming the identity in Section 6.1. The seed side takes 22.778% of the Stage 1 revenue; within Stage 2 the oil takes 45.500% of the seed's burden (Section 6.4); 22.778% × 45.500% = 10.364%, which is the direct result for oil to three decimals. The same holds for meal, hulls and linters.

### 6.4 Stage 2 Internal Allocation (per tonne of whole cottonseed)

These are the shares of the *cottonseed's* burden among its four products, on the natural per-cottonseed processing basis. They are reported for transparency and as the input to the equivalence check above; they are not the final allocations, which are given in Section 6.3.

**Economic:**

| Co-product | Calculation | Internal Allocation |
|------------|-------------|-------------------|
| Cottonseed oil | (170.00 ÷ 373.63) × 100 | **45.5%** |
| Cottonseed meal | (154.38 ÷ 373.63) × 100 | **41.3%** |
| Cottonseed hulls | (24.75 ÷ 373.63) × 100 | **6.6%** |
| Cottonseed linters | (24.50 ÷ 373.63) × 100 | **6.6%** |
| **Total** | | **100.0%** |

**Mass:**

| Co-product | Calculation | Internal Allocation |
|------------|-------------|-------------------|
| Cottonseed oil | (0.1700 ÷ 0.9013) × 100 | **18.9%** |
| Cottonseed meal | (0.4180 ÷ 0.9013) × 100 | **46.4%** |
| Cottonseed hulls | (0.2475 ÷ 0.9013) × 100 | **27.5%** |
| Cottonseed linters | (0.0658 ÷ 0.9013) × 100 | **7.3%** |
| **Total** | | **100.0%** |

> **Rounding note:** The four mass shares are 18.86%, 46.38%, 27.46% and 7.30% before rounding. Rounded independently to one decimal they sum to 100.1%. All figures in Section 6.3 are computed from unrounded values and rounded once, so the tables there sum to 100.0%.

---

## 7. Mass Balance Verification

### 7.1 Stage 1: Cotton Ginning

| Check | Value | Status |
|-------|-------|--------|
| Input: Seed cotton at 90% DM | 1.000 t | — |
| Input DM | 0.9000 t | — |
| Output: Cotton lint (as-is) | 0.380 t | 38.0% of input |
| Output: Whole cottonseed (as-is) | 0.480 t | 48.0% of input |
| Total co-product output (as-is) | 0.860 t | 86.0% of input |
| Gin trash (as-is) | 0.140 t | 14.0% of input |
| Output DM: Lint | 0.3420 t | 0.380 × 0.90 |
| Output DM: Seed | 0.4368 t | 0.480 × 0.91 |
| Total co-product DM | 0.7788 t | 86.5% of input DM |
| DM in gin trash | 0.1212 t | 13.5% of input DM |

**Stage 1 DM Balance Detail:**

| Item | Value | Notes |
|------|-------|-------|
| Input DM (1 t seed cotton at 90% DM) | 0.9000 t | 1.000 × 0.90 |
| **Output DM — co-products:** | | |
| Cotton lint | 0.3420 t | 0.380 t × 90% DM |
| Whole cottonseed | 0.4368 t | 0.480 t × 91% DM |
| Total co-product DM | **0.7788 t** | |
| DM not in a co-product | 0.1212 t | 13.5% of input DM |

> **Balance assessment:** The 0.1212 t of dry matter that does not leave as a co-product is gin trash — burrs, sticks, leaves, motes, sand and fines removed during cleaning and lint cleaning. It is a quantified stream, not an unexplained residual: 0.140 t as-is at an implied 86.6% DM (0.1212 ÷ 0.140), which is consistent with the moisture of ginning waste. The 14.0% as-is trash fraction sits within the measured range for the US crop mix — EPA AP-42 reports about 150 lb of trash per 500-lb bale for spindle-picked cotton and about 1,000 lb per bale for stripper-harvested cotton [^14^], and ICAC puts foreign matter in seed cotton at 5–10% for spindle-harvested and 10–30% for stripper-harvested material [^17^]. Gin trash is not a co-product of this system and carries no allocation.

### 7.2 Stage 2: Cottonseed Crushing

| Check | Value | Status |
|-------|-------|--------|
| Input: Whole cottonseed at 91% DM | 1.000 t | — |
| Input DM | 0.910 t | — |
| Output: Cottonseed oil (as-is) | 0.170 t | ✓ |
| Output: Cottonseed meal (as-is) | 0.475 t | ✓ |
| Output: Cottonseed hulls (as-is) | 0.275 t | ✓ |
| Output: Cottonseed linters (as-is) | 0.070 t | ✓ |
| Total as-is output | 0.990 t | 99.0% of input |
| Processing losses (as-is) | 0.010 t | 1.0% of input ✓ |
| Output DM: Oil | 0.1700 t | ✓ |
| Output DM: Meal | 0.4180 t | ✓ |
| Output DM: Hulls | 0.2475 t | ✓ |
| Output DM: Linters | 0.0658 t | ✓ |
| Total DM output | 0.9013 t | 99.0% of input DM ✓ |

**Stage 2 DM Balance Detail:**

| Item | Value | Notes |
|------|-------|-------|
| Input DM (1 t cottonseed at 91% DM) | 0.9100 t | 1.000 × 0.91 |
| **Output DM — co-products:** | | |
| Cottonseed oil | 0.1700 t | 0.17 t × 100% DM |
| Cottonseed meal | 0.4180 t | 0.475 t × 88% DM |
| Cottonseed hulls | 0.2475 t | 0.275 t × 90% DM |
| Cottonseed linters | 0.0658 t | 0.07 t × 94% DM |
| Total co-product DM | **0.9013 t** | |
| DM balance gap | −0.0087 t | −0.96% of input DM |

> **Balance assessment:** The DM output is 0.0087 t (0.96%) below the DM input. This small deficit represents processing losses (handling, residual solvent, moisture adjustment, fines) and is well within the acceptable range. 

### 7.3 As-Is Mass Balance

**Stage 1:**

| Item | Value | Notes |
|------|-------|-------|
| Input (seed cotton) | 1.000 t | — |
| **Output:** | | |
| Cotton lint | 0.380 t | — |
| Whole cottonseed | 0.480 t | — |
| **Total co-product output** | **0.860 t** | |
| **Gin trash** | **0.140 t** | 14.0%: burrs, sticks, leaves, motes, sand, fines |
| **Balance** | **1.000 t** | ✓ Exact |

**Stage 2:**

| Item | Value | Notes |
|------|-------|-------|
| Input (whole cottonseed) | 1.000 t | — |
| **Output:** | | |
| Cottonseed oil | 0.170 t | — |
| Cottonseed meal | 0.475 t | — |
| Cottonseed hulls | 0.275 t | — |
| Cottonseed linters | 0.070 t | — |
| **Total output** | **0.990 t** | |
| **Processing losses** | **0.010 t** | 1.0%: handling, moisture loss, fines |
| **Balance** | **1.000 t** | ✓ Exact |

### 7.4 Pathway B DM Balance (per tonne of seed cotton)

All five final products on a common seed cotton basis.

| Item | Value | Notes |
|------|-------|-------|
| Input DM (1 t seed cotton at 90% DM) | 0.9000 t | |
| **Output DM — final co-products:** | | |
| Cotton lint | 0.3420 t | 0.38 × 0.90 |
| Cottonseed oil | 0.0816 t | 0.48 × 0.17 × 1.00 |
| Cottonseed meal | 0.2006 t | 0.48 × 0.475 × 0.88 |
| Cottonseed hulls | 0.1188 t | 0.48 × 0.275 × 0.90 |
| Cottonseed linters | 0.0316 t | 0.48 × 0.07 × 0.94 |
| **Total co-product DM** | **0.7746 t** | |
| DM not in a co-product | 0.1254 t | 13.9% of input DM |

> **Balance assessment:** The 0.1254 t of dry matter outside the co-products decomposes into gin trash (0.1212 t, 13.5% of the DM input) and Stage 2 processing losses (0.0087 t per t cottonseed × 0.48 = 0.0042 t, 0.5% of the DM input). Gin trash accounts for 97% of the gap and is quantified in Section 7.1.

**As-is cross-check (per tonne of seed cotton):**

| Item | Value |
|------|-------|
| Cotton lint | 0.3800 t |
| Cottonseed oil, meal, hulls, linters (0.48 × 0.990) | 0.4752 t |
| Gin trash | 0.1400 t |
| Stage 2 processing losses (0.48 × 0.010) | 0.0048 t |
| **Total** | **1.0000 t** ✓ |

---

## 8. Complete Data Table

**Pathway A: Cottonseed used directly (Stage 1 only)**

| Parent Crop | Crop System | Stage | USDA Standard | Standard Moisture | Parent Input Basis | Co-product Stream | Yield (t/t seed cotton) | Yield Range | Price (USD/t) | Price Range | DM (%) | DM Output (t/t seed cotton) | Revenue (USD/t seed cotton) | Econ Alloc (%) | Mass Alloc (%) |
|-------------|-------------|-------|---------------|-------------------|-------------------|-------------------|-------------|-------------|---------------|-------------|--------|-----------------|-----------------|----------------|----------------|
| Cotton | Cotton ginning | Stage 1 | USDA AMS HVI classing | ~10% (seed cotton) | 1 t seed cotton at 90% DM | Cotton lint | 0.380 | 0.36–0.40 | 1,600 | 1,200–2,000 | 90.0 | 0.3420 | 608.00 | 81.4 | 43.9 |
| Cotton | Cotton ginning | Stage 1 | USDA AMS HVI classing | ~10% (seed cotton) | 1 t seed cotton at 90% DM | Whole cottonseed | 0.480 | 0.45–0.51 | 290 | 200–380 | 91.0 | 0.4368 | 139.20 | 18.6 | 56.1 |
| | | | | | | **Total** | | | | | | **0.7788** | **747.20** | **100.0** | **100.0** |

**Pathway B: Cottonseed crushed (five final products)**

All values are on a **per-tonne-of-seed-cotton basis**. Stage 2 yields, DM outputs and revenues are converted from the per-cottonseed basis (Section 4.2) by multiplying by the cottonseed yield (0.48 t seed/t seed cotton). Every row shares one denominator, so the allocation columns sum across all five rows — this is the direct end-of-chain treatment set out in Section 6.1.

| Parent Crop | Crop System | Stage | USDA Standard | Standard Moisture | Parent Input Basis | Co-product Stream | Yield (t/t seed cotton) | Yield Range | Price (USD/t) | Price Range | DM (%) | DM Output (t/t seed cotton) | Revenue (USD/t seed cotton) | Econ Alloc (%) | Mass Alloc (%) |
|-------------|-------------|-------|---------------|-------------------|-------------------|-------------------|-------------|-------------|---------------|-------------|--------|-----------------|-----------------|----------------|----------------|
| Cotton | Cotton ginning | Stage 1 | USDA AMS HVI classing | ~10% (seed cotton) | 1 t seed cotton | Cotton lint | 0.3800 | 0.360–0.400 | 1,600 | 1,200–2,000 | 90.0 | 0.3420 | 608.00 | 77.2 | 44.2 |
| Cotton | Cottonseed crushing | Stage 2 | NCPA specifications | ~9% (whole cottonseed) | 1 t seed cotton | Cottonseed oil | 0.0816 | 0.0768–0.0864 | 1,000 | 800–1,200 | 100.0 | 0.0816 | 81.60 | 10.4 | 10.5 |
| Cotton | Cottonseed crushing | Stage 2 | NCPA specifications | ~9% (whole cottonseed) | 1 t seed cotton | Cottonseed meal | 0.2280 | 0.2160–0.2400 | 325 | 250–400 | 88.0 | 0.2006 | 74.10 | 9.4 | 25.9 |
| Cotton | Cottonseed crushing | Stage 2 | NCPA specifications | ~9% (whole cottonseed) | 1 t seed cotton | Cottonseed hulls | 0.1320 | 0.1200–0.1440 | 90 | 60–120 | 90.0 | 0.1188 | 11.88 | 1.5 | 15.3 |
| Cotton | Cottonseed crushing | Stage 2 | NCPA specifications | ~9% (whole cottonseed) | 1 t seed cotton | Cottonseed linters | 0.0336 | 0.0240–0.0432 | 350 | 200–500 | 94.0 | 0.0316 | 11.76 | 1.5 | 4.1 |
| | | | | | | **Seed-derived subtotal** | 0.4752 | | | | | 0.4326 | 179.34 | **22.8** | **55.8** |
| | | | | | | **Total** | | | | | | **0.7746** | **787.34** | **100.0** | **100.0** |

> **Basis conversion note:** Stage 2 yields above are on a seed cotton basis (for example, oil 0.0816 = 0.48 × 0.17). On the per-cottonseed basis the yields are oil 0.17, meal 0.475, hulls 0.275 and linters 0.07 t/t cottonseed (Section 4.2). Yield ranges are converted the same way (oil 0.0768–0.0864 = 0.48 × 0.16–0.18). Stage 2 figures are carried at four decimals so that the seed cotton basis reproduces the per-cottonseed yields exactly. DM outputs and revenues are all on the seed cotton basis and can be summed down the column without a basis inconsistency.

> **Stage 2 internal allocations (for reference):** Within Stage 2 the cottonseed's own burden divides as oil 45.5%/18.9%, meal 41.3%/46.4%, hulls 6.6%/27.5%, linters 6.6%/7.3% (economic/mass), on the per-cottonseed basis. These are not the final allocations; Section 6.4 explains their role.

> **Gin trash:** 0.140 t as-is (0.1212 t DM) per tonne of seed cotton leaves the gin as trash. It is not a co-product, receives no allocation, and is excluded from both denominators. It is quantified in Section 7.1.

---

## 9. Data Quality and Limitations

### 9.1 High-Confidence Data

| Data Point | Confidence | Source |
|------------|-----------|--------|
| Lint yield (0.38 t/t) | **High** | Gin turnout is directly measured and consistently reported [^1^][^6^][^12^] |
| Oil yield (0.17 t/t) | **High** | Well-documented for solvent extraction [^7^][^10^] |
| Oil DM% (100%) | **High** | Pure lipid with negligible moisture |
| Meal DM% (88%) | **High** | Industry trading specification (max 12% moisture) [^10^] |
| Lint price ($1,600/t) | **High** | Well-documented commodity with transparent pricing [^3^] |
| Seed-to-lint ratio (1.26) | **High** | Three consecutive years of national production data agree to within 0.03, and independently measured gin turnouts agree to within 0.03 [^11^][^12^] |

### 9.2 Medium-Confidence Data

| Data Point | Confidence | Source |
|------------|-----------|--------|
| Linters yield (0.07 t/t) | **Medium** | Varies with delinting method and number of cuts; range is 0.05–0.09 |
| Linters price ($350/t) | **Medium** | Wide range ($200–500) reflecting different linter grades and end uses |
| Seed price ($290/t) | **Medium** | Varies with region, season, and dairy demand |
| Hulls yield (0.275 t/t) | **Medium** | Depends on degree of dehulling (partial vs. complete) |
| Hulls price ($90/t) | **Medium** | Low-value product with limited price transparency |
| Meal yield (0.475 t/t) | **Medium** | Depends on protein specification and hull blend |
| Seed yield (0.48 t/t) | **Medium-High** | The ratio it derives from is well constrained, but published sources still carry the older 1.62 figure, so the literature is split. Section 4.1 gives both. |
| Gin trash (0.14 t/t) | **Medium** | Set as the residual and cross-checked against measured gin waste; varies widely with harvest system, from roughly 0.08 for spindle-picked to over 0.20 for stripper-harvested cotton [^14^][^17^] |

### 9.3 Known Limitations

1. **Cottonseed linters recovery varies:** Not all cottonseed crushing facilities recover linters as a separate co-product. Some facilities leave linters on the seed (or partially on the hulls), in which case: (a) linters mass is captured in the meal/hulls, (b) there is no separate linters co-product, and (c) meal yield is higher (~0.53–0.55 t/t) and meal protein is lower (~36–38%). This table models the standard commercial practice of linters removal. Studies using data from facilities that do not remove linters should adjust the allocation model accordingly.

2. **Partial dehulling configuration:** This table represents partial dehulling, where ~70–80% of hulls are separated and the remainder stays with the meal. This produces 41% protein meal (the most common grade). Alternative configurations include:
   - **No dehulling:** Meal yield ~0.55–0.60 t/t, ~30–36% protein, lower price; hulls yield ~0.25 t/t
   - **Complete dehulling:** Meal yield ~0.40–0.43 t/t, ~48–50% protein, higher price; hulls yield ~0.35–0.40 t/t
   
   The degree of dehulling significantly affects meal and hulls yields, meal protein content, and prices. Studies should match the dehulling configuration to their specific processing facility.

3. **Gossypol toxicity limits feed use:** Cottonseed products contain gossypol, a naturally occurring polyphenolic compound that is toxic to monogastric animals (poultry, swine) at high concentrations. This limits the use of cottonseed meal primarily to ruminant feed (cattle, sheep). Gossypol also limits the use of whole cottonseed as feed. The gossypol content affects market prices and demand patterns, particularly for meal. Solvent extraction and meal toasting reduce free gossypol levels, but the residual levels still restrict end markets.

4. **Lint quality affects price:** Cotton lint prices vary dramatically with quality (staple length, micronaire, strength, color grade, leaf grade). The $1,600/t midpoint reflects average-quality upland cotton. Premium cotton (long staple, high micronaire, clean) can exceed $2,000/t, while discounted cotton (short staple, low micronaire, high trash) can fall below $1,200/t. The economic allocation is sensitive to lint price: under Pathway A, if the lint price drops to $1,200/t, lint's economic allocation falls from 81.4% to ~76.6%; under Pathway B the same drop takes it from 77.2% to ~71.8%.

5. **Cottonseed as cattle feed (dual pathway):** Whole cottonseed is a significant cattle feed product, especially for dairy rations (high energy from oil, high protein, effective fiber). In practice, a substantial fraction of cottonseed is fed directly rather than crushed — the split varies by region (more crushing near oil mills, more direct feeding near dairy operations) and season. This document presents both pathways explicitly (Sections 6.1–6.3 and 8). A given tonne of seed follows one pathway or the other, so the two factor sets are alternatives, not a double count. Practitioners should select the pathway matching their system boundary, or weight the two by the share of seed crushed in the region modelled.

6. **Regional variation:** Cotton ginning and crushing are concentrated in the US South and West (Texas, Georgia, Arkansas, Mississippi, California). Prices, yields and gin trash vary by region with variety, growing conditions, harvest system and proximity to end markets. The harvest system matters most for the mass balance: stripper-harvested cotton, which dominates the Texas High Plains, delivers far more foreign matter to the gin than spindle-picked cotton, so gin trash can range from under 0.10 to over 0.20 t/t seed cotton around the 0.14 adopted here [^12^][^14^][^17^]. The seed-to-lint ratio is far more stable across regions than the trash fraction, which is why the seed yield is derived from that ratio rather than from a turnout figure directly.

7. **Organic and non-GMO cotton:** Organic and non-GMO cotton lint commands a significant premium (~$300–800/t above conventional), and organic cottonseed products may also have higher prices. This table uses conventional cotton prices. Studies focused on organic cotton should use organic-specific pricing.

8. **Cottonseed oil as a byproduct vs. co-product:** In some economic frameworks, cottonseed oil is treated as a byproduct (with meal as the primary product) because the crushing decision is driven by meal demand rather than oil demand. This distinction affects the interpretation of economic allocation but does not change the calculation method. Under the co-product framework used in this review, all products with market value are treated equally.

9. **Seed-to-lint ratio is still moving:** Lint percent has been rising steadily and cottonseed per bale falling with it [^13^][^16^]. The 1.26 ratio adopted here reflects the 2023–2025 crops. Studies covering earlier crop years should use a ratio contemporaneous with their data; the sensitivity in Section 4.1 gives the result at the long-standing 1.62 figure.


---
## 10. System Boundary Assumption and the Alternative Sequential Treatment

### 10.1 Assumption: Single Integrated Processing Block

This methodology models the cotton processing chain — ginning and cottonseed crushing — as a **single integrated processing block**. The system boundary opens where seed cotton enters the gin and closes where the marketable co-products leave: lint and whole cottonseed under Pathway A, and lint, oil, meal, hulls and linters under Pathway B.

Within one block, all final products compete for one denominator. That is the direct end-of-chain treatment set out in Section 6.1, and it gives lint **77.2%** of the economic burden and **44.2%** of the mass burden under Pathway B.

### 10.2 Alternative: Sequential Unit Process Boundary

A study that models the gin and the crusher as **two separate unit processes** would instead cascade at the market price of the intermediate, exactly as this review does for barley, rice and peanut:

- **Process 1 (Ginning):** the ginning burden is divided between lint and whole cottonseed using the seed's market price of $290/t. Lint receives **81.4%** and the seed **18.6%** (economic); on a mass basis, 43.9% and 56.1%. These are the Pathway A figures of Section 6.2 — Pathway A and the first stage of a market-price cascade are the same calculation.
- **Process 2 (Crushing):** the seed's 18.6% is then subdivided among oil, meal, hulls and linters in proportion to their Stage 2 revenues (Section 6.4), giving oil 8.5%, meal 7.7%, hulls 1.2% and linters 1.2% of the total chain burden.

The difference from the integrated-block result is not a rounding artefact. Under the sequential treatment the seed side carries 18.6% of the economic burden however the seed is used; under the integrated-block treatment it carries 22.8% when it is crushed, because the products it becomes are worth $179.34 against the seed's own $139.20. Both are defensible; they answer different questions.

### 10.3 Why the Integrated Block Is Used Here

1. **Whole cottonseed is a final product of this study.** It is a major dairy feed and carries its own allocation factor (Pathway A). Its $290/t is the price in a competing end use, not a transfer price into the crush — the point developed in Section 6.1. This is what distinguishes cotton from the other two-stage crops in this review, where the intermediate is consumed entirely by the next stage.

2. **Much cottonseed never transacts at a market price.** A substantial share moves from gin to crusher as an internal transfer, so the spot price would be doing work the physical system does not support.

3. **The practitioner's question is about final products.** Attributing burden to what leaves the system boundary is the usual goal, and one denominator across all five products is the direct way to get there.

> **Guidance for LCA practitioners:** If your model requires separate process modules for the gin and the crusher — because you hold distinct emission factors, energy sources or waste streams for each, such as gin trash against hexane emissions — use the sequential cascade of Section 10.2. For the primary data table in this document, the integrated block applies and lint carries 77.2% (economic) and 44.2% (mass) under Pathway B.
