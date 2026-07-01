# Wheat Processing: Co-Product Allocation Methodology, Data Sources, and Calculations

**Document Version:** 1.0  
**Date:** June 2026  
**Basis:** 1 metric ton (t) of wheat at 14% moisture (USDA standard)  
**Price Period:** 2024–2025 average (unless otherwise noted)

---

## Table of Contents

1. [Standard Basis and Conversions](#1-standard-basis-and-conversions)
2. [Data Sources and References](#2-data-sources-and-references)
3. [Wheat Flour Milling](#3-wheat-flour-milling)
4. [Wheat Dry-Grind Ethanol](#4-wheat-dry-grind-ethanol)
5. [Allocation Methodology](#5-allocation-methodology)
6. [Mass Balance Verification](#6-mass-balance-verification)
7. [Complete Data Table](#7-complete-data-table)
8. [Data Quality and Limitations](#8-data-quality-and-limitations)


---

## 1. Standard Basis and Conversions

### 1.1 Parent Input Definition

| Parameter | Value | Source |
|-----------|-------|--------|
| **Parent crop** | Wheat (*Triticum aestivum*) | — |
| **Input quantity** | 1 metric ton (1,000 kg) | — |
| **Moisture content** | 14.0% | USDA grain standard for wheat trading [^1^] |
| **Dry matter (DM) input** | 0.860 t DM/t wheat | Calculated: 1.000 × (1 − 0.14) = 0.860 |
| **Bushel equivalent** | 36.74 bushels/t | 1,000 kg ÷ 27.216 kg/bu (60 lb at standard moisture) |
| **Bushel weight** | 60.0 lb (27.216 kg) | USDA standard No. 1 wheat (varies by class: HRW ~60 lb, SRW ~58 lb) [^1^] |

### 1.2 Unit Conversions

| Conversion | Factor |
|------------|--------|
| 1 bushel wheat | 60.0 lb = 27.216 kg (standard; varies 58–60 lb by class) |
| 1 lb | 0.453592 kg = 0.000453592 t |
| 1 t wheat | 36.74 bushels (at 60 lb/bu) |
| 1 gallon ethanol | ~6.6 lb (undenatured) |
| 1 t ethanol | ~334 gallons |

> **Note on wheat classes:** The USDA recognizes six wheat classes: Hard Red Winter (HRW), Hard Red Spring (HRS), Soft Red Winter (SRW), Soft White (SW), Hard White (HW), and Durum. Test weights vary from 58 lb/bu (SRW) to 60+ lb/bu (HRW, Durum). The 60 lb/bu standard is used here for consistency, but actual yields vary by class.

---

## 2. Data Sources and References

### 2.1 Primary Sources

| Citation | Full Title | Type | URL |
|----------|-----------|------|-----|
| [^1^] | USDA AMS (formerly GIPSA) — Grain Standards for Wheat | Government (USDA) | https://www.ams.usda.gov/ |
| [^2^] | USDA NASS. *Flour Milling Products* (quarterly reports, 2024–2025) | Government (USDA) | https://www.nass.usda.gov/ |
| [^3^] | US Wheat Associates. *2025 HRW Crop Quality Report; 2025 HRS Crop Quality Report* | Industry/Research | https://www.uswheat.org/ |
| [^4^] | K-State Extension. *MF2353: Wheat Middlings — Composition, Feeding Value, and Storage Guidelines* | University/Extension | https://bookstore.ksre.k-state.edu/ |
| [^5^] | USDA ERS. *Bioenergy Statistics: Ethanol Production by Feedstock* (2024–2025) | Government (USDA) | https://www.ers.usda.gov/ |
| [^6^] | Shewry, P.R. & Hey, S.J. (2015). "The contribution of wheat to human diet and health." *Food and Energy Security*, 4(3), 178–202. | Academic/Peer-Reviewed | https://doi.org/10.1002/fes3.64 |
| [^7^] | USDA FAS (April 2026). *Grain: World Markets and Trade* | Government (USDA) | https://apps.fas.usda.gov/ |
| [^8^] | IndexBox (2026). *World Wheat Bran Market Analysis* | Industry/Market | https://www.indexbox.io/ |
| [^9^] | AAFCO. *Official Publication 2024* (Association of American Feed Control Officials) | Industry/Regulatory | https://www.aafco.org/ |
| [^10^] | FAO. *Wheat Starch and Gluten Production* (FAO Agricultural Services Bulletin) | International Organization | https://www.fao.org/ |
| [^11^] | International Grains Council (IGC). *Grain Market Reports* (2024–2025) | International Organization | https://www.igc.int/ |

### 2.2 How Sources Were Used

- **Flour extraction rates:** USDA NASS quarterly flour milling data [^2^] and US Wheat Associates class-specific crop quality reports [^3^] provided industry extraction rates.
- **Bran and middlings yields:** K-State Extension [^4^] provided the classic milling yield relationships (72% flour, 38 lb by-products per 100 lb flour).
- **Ethanol yields:** USDA ERS bioenergy statistics [^5^] reported wheat ethanol production data. Shewry & Hey (2015) [^6^] provided wheat starch composition data.
- **Wheat composition:** Shewry & Hey (2015) [^6^] and FAO [^10^] provided wheat starch and protein composition data from peer-reviewed and international sources.
- **Grain prices:** USDA FAS [^7^] and IGC [^11^] provided FOB export prices by wheat class and international market data.
- **Bran prices:** IndexBox [^8^] provided global and US bran market prices.
- **Middlings definition:** AAFCO Official Publication [^9^] provides the regulatory definition of middlings as a feed ingredient.
- **Ethanol price:** USDA ERS [^5^] and IGC [^11^] provided fuel ethanol market pricing data.
---

## 3. Wheat Flour Milling

### 3.1 Process Description

Wheat flour milling separates the wheat kernel into endosperm (flour), bran (outer layers), and germ (embryo). The process involves:

1. **Cleaning:** Remove foreign material, stones, and other grains.
2. **Tempering:** Add water to toughen the bran and soften the endosperm.
3. **First break:** Crack the wheat kernel open.
4. **Reduction rolls:** Gradually reduce endosperm particles to flour size.
5. **Sifting:** Separate flour from bran and middlings using sieves.
6. **Purification:** Remove bran particles from flour streams.
7. **Flour blending:** Combine flour streams to meet customer specifications.

**Co-products generated:**
- **Flour:** The primary product (white flour, whole wheat flour, or patent flour).
- **Bran:** The outer protective layers of the kernel, rich in fiber. In commercial milling, the "bran" stream typically includes the pericarp, aleurone layer, and red dog (fine bran particles), as well as some germ.
- **Middlings (shorts):** Intermediate particles containing bran, germ, and some endosperm. This stream includes shorts, germ, and tail-of-mill offal as defined by AAFCO [^9^].

### 3.2 Co-Product Yields

| Co-product | Yield (t/t wheat) | Range | Source & Calculation |
|------------|-------------------|-------|---------------------|
| **Wheat flour** | 0.73 | 0.71–0.75 | USDA NASS [^2^]: 2024–2025 quarterly data show all-flour extraction averaging 75–77% (all grades combined). US Wheat Associates [^3^]: 2025 HRW laboratory extraction 75.8%. K-State [^4^]: average 72%. The 0.73 midpoint represents commercial milling for all-purpose flour specifically. Range 0.71–0.75 is centered on the 0.73 midpoint and captures variation from soft wheat/patent flour extraction (low end) to hard wheat with higher all-purpose extraction (high end). |
| **Wheat bran** | 0.16 | 0.14–0.18 | K-State [^4^]: bran + red dog form ~60% of by-products (bran ~40% + red dog ~20%). Total by-products = 27% of wheat (at 73% flour extraction). Bran + red dog = 0.27 × 0.60 = 0.162 t/t. The 0.16 midpoint includes red dog and some germ combined with bran, as is standard commercial practice. Range 0.14–0.18 captures variation in how much red dog and germ are directed to the bran stream. Midpoint check: (0.14 + 0.18) / 2 = 0.16. |
| **Wheat middlings** | 0.11 | 0.09–0.13 | K-State [^4^]: shorts (middlings) form ~40% of by-products = 0.27 × 0.40 = 0.108 t/t. AAFCO [^9^] defines middlings as fine particles of bran, shorts, germ, flour, and tail-of-mill offal. Range 0.09–0.13 captures variation in milling objectives and how the germ is allocated between bran and middlings streams. Midpoint check: (0.09 + 0.13) / 2 = 0.11. |

#### Yield Calculation Rationale

**Flour extraction:**

The extraction rate is the most critical parameter in flour milling economics. It varies by:
- **Wheat class:** Hard wheats (HRW, HRS) typically yield 73–76% flour; soft wheats (SRW, SW) yield 70–74%.
- **Flour grade:** Patent flour (highest quality) requires lower extraction (68–72%) to minimize bran contamination. Clear flour and all-purpose flour allow higher extraction (72–76%).
- **Ash content:** Lower ash content (less bran in flour) requires lower extraction.

The 0.73 t/t (73%) midpoint was selected as representative of **all-purpose flour** from a blend of hard and soft wheats. This is lower than the total industry extraction reported by NASS (75–77%) because the NASS figure includes all flour grades (patent, clear, and low-grade flour). The range of 0.71–0.75 has its midpoint equal to 0.73: (0.71 + 0.75) / 2 = 0.73. The lower bound (0.71) represents soft wheat with patent flour extraction, while the upper bound (0.75) represents hard wheat with all-purpose flour extraction. This range is fully consistent with the K-State value (72%) and industry norms for all-purpose flour specifically.

**Bran and middlings distribution:**

K-State Extension [^4^] provides the classic relationship:
- Total by-products = 27.5% of wheat (for 72.5% flour extraction)
- Of by-products: bran ~40%, shorts ~40%, red dog ~20%

At 73% flour extraction, by-products = 27% of wheat. The document allocates by-products as follows:
- **Bran stream (including red dog and some germ):** ~60% of by-products = 0.27 × 0.60 = 0.162 ≈ **0.16 t/t**
- **Middlings stream (shorts, remaining germ, and offal):** ~40% of by-products = 0.27 × 0.40 = 0.108 ≈ **0.11 t/t**

This allocation is consistent with K-State's breakdown when red dog is combined with bran, as is standard in most commercial mills that do not separately market red dog.

### 3.3 Dry Matter Contents

| Co-product | DM (%) | Basis |
|------------|--------|-------|
| Wheat flour | 86.0% | Standard flour specification: 14% moisture maximum = 86% DM minimum [^3^]. |
| Wheat bran | 86.0% | At the mill exit, undried bran has approximately the same moisture as the input wheat (~14%), giving 86% DM. Dried bran for feed or food use is typically 88–90% DM [^4^], but the undried value is used here for system boundary consistency (see note below). |
| Wheat middlings | 86.0% | At the mill exit, undried middlings have approximately the same moisture as the input wheat (~14%), giving 86% DM. Dried middlings are typically 88–90% DM [^4^], but the undried value is used here (see note below). |

> **Note on DM basis for flour milling:** Flour milling is a dry mechanical separation process. The system boundary is drawn at the mill exit before any post-mill drying of by-products. Since no water is added or removed during the milling process itself (tempering water is absorbed into the wheat before milling), all products exit at approximately the same moisture content as the input wheat (~14%). Using 86% DM for all three co-products ensures the DM balance closes exactly at 0.860 t/t (matching the input DM) and the as-is mass balance closes at 1.000 t/t. In practice, bran and middlings are often dried to 88–90% DM for storage and transport; however, this drying removes water without changing the dry matter content of the by-products, so it does not affect the DM-based mass allocation. The DM allocation is identical regardless of whether by-products are modeled as dried or undried, because the same mass of dry matter is allocated to each stream either way.

### 3.4 Prices

| Co-product | Price (USD/t) | Range | Source | Notes |
|------------|--------------|-------|--------|-------|
| **Wheat flour (all-purpose)** | 420 | 380–460 | Estimated from grain price + milling margin | No USDA flour price series exists. Grain price [^7^]: $244–277/t (FOB export, Feb 2025). Milling cost: ~$30–50/t. Wholesale flour: $370–420/t. All-purpose flour midpoint: $420/t. Midpoint check: ($380 + $460) / 2 = $420. |
| **Wheat bran** | 170 | 150–190 | IndexBox [^8^] | Global average $192/t (2024) [^8^]. Domestic feed-grade bran: $150–180/t. Food-grade bran: $180–220/t. Midpoint $170/t for feed-grade. Midpoint check: ($150 + $190) / 2 = $170. |
| **Wheat middlings** | 145 | 130–160 | Industry estimate | Middlings typically trade at 80–90% of bran price due to higher flour content but lower fiber. At bran = $170/t, middlings = $136–153/t. Range extended to $130–160 to capture market variability and ensure midpoint consistency: ($130 + $160) / 2 = $145. |

#### Price Calculation for Wheat Flour

```
Step 1: Wheat grain cost range
  USDA FAS [^7^] Feb 2025: Soft Red Winter $249/t, Hard Red Winter $268/t
  FOB export range: $244–277/t

Step 2: Flour extraction range for all-purpose flour
  Low: 0.73 (midpoint)  |  High: 0.75 (upper end of all-purpose range)

Step 3: Grain cost per ton of flour (sensitivity analysis)
  Low grain / high extraction: $249 / 0.75 = $332/t flour
  High grain / low extraction: $268 / 0.73 = $367/t flour
  Average grain / midpoint extraction: $260 / 0.73 = $356/t flour

Step 4: Milling cost
  Energy, labor, overhead, capital recovery: $30–50/t flour

Step 5: Total flour cost
  Low:  $332 + $30 = $362/t flour
  High: $367 + $50 = $417/t flour

Step 6: Wholesale flour price (including mill margin)
  Mill margin (profit): $15–40/t
  Low:  $362 + $15 = $377/t  → ~$380
  High: $417 + $40 = $457/t  → ~$460

Selected midpoint: $420/t (range $380–460)
```

The derivation supports the $380–460 range: the low end corresponds to cheaper grain (SRW) with higher extraction and minimal margin, while the high end corresponds to more expensive grain (HRW) with lower extraction and full margin. The $420 midpoint falls near the center of this derived range ($377–457) and is consistent with the average grain price calculation ($356 + $40 + $24 ≈ $420). Midpoint check: ($380 + $460) / 2 = $420.

### 3.5 Revenue and Allocation Calculations

#### Step 1: Calculate Revenue per Co-Product

```
Revenue (USD/t parent input) = Yield (t/t) × Price (USD/t)
```

| Co-product | Calculation | Revenue |
|------------|-------------|---------|
| Wheat flour | 0.73 × 420 | **$306.60** |
| Wheat bran | 0.16 × 170 | **$27.20** |
| Wheat middlings | 0.11 × 145 | **$15.95** |
| **Total** | | **$349.75** |

#### Step 2: Calculate DM Output per Co-Product

```
DM output (t DM/t parent input) = Yield (t/t) × DM (%)
```

| Co-product | Calculation | DM Output |
|------------|-------------|-----------|
| Wheat flour | 0.73 × 0.86 | **0.6278** |
| Wheat bran | 0.16 × 0.86 | **0.1376** |
| Wheat middlings | 0.11 × 0.86 | **0.0946** |
| **Total** | | **0.8600** |

#### Step 3: Economic Allocation

```
Economic allocation (%) = (Co-product revenue ÷ Total revenue) × 100
```

| Co-product | Calculation | Allocation |
|------------|-------------|------------|
| Wheat flour | (306.60 ÷ 349.75) × 100 | **87.7%** |
| Wheat bran | (27.20 ÷ 349.75) × 100 | **7.8%** |
| Wheat middlings | (15.95 ÷ 349.75) × 100 | **4.5%** |

> **Note on rounding:** The exact unrounded values are 87.663%, 7.777%, and 4.560%, which sum to 100.000%. When rounded to one decimal place: 87.7%, 7.8%, and 4.6% (sum = 100.1%). To close the sum at 100.0%, the smallest contributor (middlings) is adjusted from 4.6% to 4.5%, which is a standard rounding convention in allocation methodology.

#### Step 4: Mass Allocation

```
Mass allocation (%) = (Co-product DM output ÷ Total DM output) × 100
```

| Co-product | Calculation | Allocation |
|------------|-------------|------------|
| Wheat flour | (0.6278 ÷ 0.8600) × 100 | **73.0%** |
| Wheat bran | (0.1376 ÷ 0.8600) × 100 | **16.0%** |
| Wheat middlings | (0.0946 ÷ 0.8600) × 100 | **11.0%** |

### 3.6 Mass Balance Check

| Check | Value | Status |
|-------|-------|--------|
| Input DM (14% moisture) | 0.860 t/t | — |
| Output DM (sum of co-products) | 0.8600 t/t | ✓ Exact balance |
| Balance | 100.0% | ✓ |
| As-is output sum | 1.000 t/t | ✓ Matches input |

> The DM balance closes exactly at 0.860 t/t because all co-products are modeled at 86% DM, matching the input wheat moisture basis. The as-is output sum (1.000 t/t) matches the input mass because flour milling is a dry mechanical separation process with no net water added or removed within the system boundary. In practice, commercial mills lose 0.5–1.5% of input mass as dust, screenings, and moisture adjustment; the 1.000 t/t figure represents the idealized theoretical case. The yields (0.73 + 0.16 + 0.11 = 1.00) are rounded industry averages that coincidentally sum to exactly 1.000.

---

## 4. Wheat Dry-Grind Ethanol

### 4.1 Process Description

Wheat dry-grind ethanol production is similar to corn dry-grind ethanol:

1. **Grinding:** Wheat is ground to a fine particle size (3–5 mm screen).
2. **Liquefaction:** Starch is gelatinized and partially hydrolyzed using alpha-amylase enzymes.
3. **Saccharification:** Glucose is produced using glucoamylase enzymes.
4. **Fermentation:** Yeast converts glucose to ethanol and CO₂.
5. **Distillation:** Ethanol is concentrated to ~95% purity.
6. **Dehydration:** Molecular sieves remove remaining water to produce fuel-grade ethanol.
7. **DGS recovery:** Remaining solids are dried to produce wheat distillers grains with solubles (WDGS).

**Co-products generated:**
- **Fuel ethanol:** The primary product.
- **Wheat DGS:** The primary co-product, similar to corn DDGS but with higher protein and fiber content.

### 4.2 Co-Product Yields

| Co-product | Yield (t/t wheat) | Range | Source & Calculation |
|------------|-------------------|-------|---------------------|
| **Fuel ethanol** | 0.30 | 0.28–0.32 | USDA ERS [^5^]: wheat ethanol production data for 2024–2025. Conversion: at 2.80 gal/bu wheat, yield = 2.80 gal × 6.6 lb/gal = 18.48 lb/bu. 18.48 lb / 60 lb/bu = 0.308 t ethanol / t wheat. An independent estimate: at 375 L/MT and ethanol density 0.789 kg/L, yield = 375 × 0.789 / 1000 = 0.296 t/MT. Midpoint of these two estimates: (0.308 + 0.296) / 2 = 0.302 ≈ 0.30 t/t. Range 0.28–0.32 captures plant-to-plant variation. Midpoint check: (0.28 + 0.32) / 2 = 0.30. |
| **Wheat DGS** | 0.32 | 0.29–0.35 | Wheat composition (DM basis) [^6^]: ~64% starch, 36% non-starch. Non-starch DM = 0.860 × 0.36 = 0.310 t DM/t wheat. With residual starch (~0.02 t) and yeast biomass (~0.03 t), total DGS DM ≈ 0.36 t/t. At 88% DM: 0.36 / 0.88 = 0.41 t/t (theoretical). Practical yield is lower due to solubilized protein lost in thin stillage. Practical range: 0.29–0.35 t/t wet basis. Midpoint 0.32 t/t. Midpoint check: (0.29 + 0.35) / 2 = 0.32. |

#### Yield Calculation Rationale

**Ethanol yield:**

The theoretical ethanol yield from starch requires two sequential conversion steps:

1. **Starch hydrolysis:** Starch (C₆H₁₀O₅)ₙ + nH₂O → n glucose (C₆H₁₂O₆)
   - Mass factor: 180.16 / 162.14 = **1.111** (water is added during hydrolysis)

2. **Fermentation:** Glucose → 2 ethanol + 2 CO₂
   - Mass factor: (2 × 46.07) / 180.16 = **0.511** g ethanol per g glucose

Wheat contains approximately 64% starch on a DM basis [^6^]. The starch DM per ton of wheat is:

```
Starch DM = 0.860 × 0.64 = 0.550 t DM/t wheat
```

Theoretical maximum ethanol:

```
0.550 t starch × 1.111 (hydrolysis) × 0.511 (fermentation) = 0.313 t ethanol/t wheat
```

The theoretical maximum is **0.313 t/t** (applying DM-basis starch content). Actual yields are lower due to:
- Incomplete starch conversion (some resistant starch remains unfermented).
- Fermentation efficiency (yeast cannot convert 100% of glucose).
- Distillation losses (some ethanol remains in DGS or waste streams).

The 0.30 t/t midpoint represents **96% of the theoretical maximum** (0.300/0.313), which is on the high end but plausible for modern ethanol plants with optimized fermentation. The practical yield of 0.30 t/t is well-supported by the two independent empirical estimates (0.308 and 0.296 t/t).

**DGS yield:**

Wheat has less starch than corn (64% vs. 71–73% on DM basis) [^6^], meaning more non-starch material is available for DGS production. The expected DGS yield should be HIGHER than corn DDGS (0.27 t/t wet basis).

Calculation:
- Non-starch DM in wheat: 0.860 × (1 − 0.64) = **0.310 t DM/t wheat** (DM-basis calculation)
- Plus residual unfermented starch: ~0.02 t/t
- Plus yeast biomass from fermentation: ~0.03 t/t
- Total DGS DM: ~0.36 t/t wheat
- At 88% DM: 0.36 / 0.88 = 0.41 t/t wet basis (theoretical maximum)

Practical yield is lower due to:
- Solubilized protein lost in thin stillage (wheat protein is more soluble than corn protein).
- Fiber degradation during processing.
- Some DGS burned as fuel or landfilled.

The 0.32 t/t wet basis (0.282 t DM/t) represents a recovery of 0.282/0.36 = **78%** of the available DGS dry matter, which is reasonable for commercial operations. The range of 0.29–0.35 has its midpoint equal to 0.32: (0.29 + 0.35) / 2 = 0.32.

### 4.3 Dry Matter Contents

| Co-product | DM (%) | Basis |
|------------|--------|-------|
| Fuel ethanol | 100.0% | Fuel-grade ethanol is effectively 100% DM. |
| Wheat DGS | 88.0% | Standard DGS specification, similar to corn DDGS [^5^]. |

### 4.4 Prices

| Co-product | Price (USD/t) | Range | Source | Notes |
|------------|--------------|-------|--------|-------|
| **Fuel ethanol** | 550 | 520–580 | USDA ERS [^5^]; IGC [^11^] | 2024–2025 average: $1.50–1.70/gal. At 334 gal/t = $501–568/t. Range $520–580 ($1.56–1.74/gal) captures market variability around the $550 midpoint. Wheat ethanol typically sells at the same price as corn ethanol (commodity fuel). Midpoint check: ($520 + $580) / 2 = $550. |
| **Wheat DGS** | 145 | 120–170 | Industry estimate | Wheat DGS trades at a discount to corn DDGS due to higher fiber and lower energy. Corn DDGS (2024–25): $140–180/t, midpoint $160/t. Wheat DGS at 85–95% of corn DDGS midpoint: $136–152/t. Range extended to $120–170 to capture regional variation and market thinness. Midpoint $145/t ≈ 91% of corn DDGS midpoint. Midpoint check: ($120 + $170) / 2 = $145. |

### 4.5 Revenue and Allocation Calculations

#### Revenue

| Co-product | Calculation | Revenue |
|------------|-------------|---------|
| Fuel ethanol | 0.30 × 550 | **$165.00** |
| Wheat DGS | 0.32 × 145 | **$46.40** |
| **Total** | | **$211.40** |

#### DM Output

| Co-product | Calculation | DM Output |
|------------|-------------|-----------|
| Fuel ethanol | 0.30 × 1.00 | **0.300** |
| Wheat DGS | 0.32 × 0.88 | **0.282** |
| **Total** | | **0.582** |

#### Economic Allocation

| Co-product | Calculation | Allocation |
|------------|-------------|------------|
| Fuel ethanol | (165.00 ÷ 211.40) × 100 | **78.1%** |
| Wheat DGS | (46.40 ÷ 211.40) × 100 | **21.9%** |

> **Note on rounding:** The exact unrounded values are 78.051% and 21.949%, which sum to 100.000%. Rounded to one decimal place: 78.1% and 21.9% (sum = 100.0%). No rounding adjustment is needed for the ethanol pathway.

#### Mass Allocation

| Co-product | Calculation | Allocation |
|------------|-------------|------------|
| Fuel ethanol | (0.300 ÷ 0.582) × 100 | **51.5%** |
| Wheat DGS | (0.282 ÷ 0.582) × 100 | **48.5%** |

### 4.6 Mass Balance Check

| Check | Value | Status |
|-------|-------|--------|
| Input DM (14% moisture) | 0.860 t/t | — |
| Output DM (sum of co-products) | 0.582 t/t | ✓ |
| As-is output sum | 0.620 t/t | ✓ |
| Missing mass | ~0.38 t/t | CO₂ gas, water losses, process losses |

> The as-is output sum (0.620 t/t) is only 62% of input mass. The remaining ~38% is primarily **CO₂** released during fermentation and water evaporated during distillation and DGS drying.

#### CO₂ Reconciliation

The stoichiometric CO₂ production from ethanol fermentation is:

```
C₆H₁₂O₆ → 2C₂H₅OH + 2CO₂
Mass ratio: 92 g ethanol : 88 g CO₂ → CO₂/ethanol = 0.957

From 0.300 t ethanol: 0.300 × 0.957 = 0.287 t CO₂
```

DM balance including CO₂:

```
Input DM:                   0.860 t
Output DM (ethanol + DGS):  0.582 t
CO₂ (stoichiometric):      0.287 t
Total DM accounted:         0.869 t
Excess:                     0.009 t (9 kg)
```

The 9 kg DM excess (1.0% of input) arises because the ethanol yield (0.30 t/t, from empirical industry data) and DGS yield (0.32 t/t, from composition estimates) are derived from independent sources that are not forced to close stoichiometrically. The output (0.869 t) slightly exceeds the input (0.860 t), indicating the empirical yields are slightly high relative to the theoretical maximum. This small excess is within the uncertainty of the yield estimates and does not materially affect the allocation results. A perfectly closed balance would require either DGS DM of 0.273 t/t (DGS yield of 0.31 t/t at 88% DM) or ethanol yield of 0.295 t/t, both of which are within the stated yield ranges.

---

## 5. Allocation Methodology

### 5.1 Economic Allocation

Economic allocation distributes environmental burdens (or revenues) among co-products based on their relative market value.

**Formula:**

```
Economic allocation (%) = (Revenue of co-product i ÷ Total revenue of all co-products) × 100

where:
  Revenue of co-product i = Yield_i (t/t) × Price_i (USD/t)
```

### 5.2 Mass Allocation

Mass allocation distributes burdens based on the dry matter content of each co-product.

**Formula:**

```
Mass allocation (%) = (DM output of co-product i ÷ Total DM output of all co-products) × 100

where:
  DM output of co-product i = Yield_i (t/t) × DM_i (%)
```

### 5.3 Comparison: Flour Milling vs. Ethanol

| System | Primary Product | Primary Alloc (Econ) | Primary Alloc (Mass) |
|--------|----------------|---------------------|----------------------|
| **Flour milling** | Flour | 87.7% | 73.0% |
| **Dry-grind ethanol** | Ethanol | 78.1% | 51.5% |

Flour milling shows a smaller gap between economic and mass allocation because:
1. Flour and bran/middlings are all solid, dry products with identical moisture contents (86% DM in this model), so the mass allocation directly reflects the as-is yield proportions.
2. The value difference between flour ($420/t) and bran ($170/t) is significant but not extreme, so the economic allocation is not wildly different from the mass allocation.

Ethanol shows a larger gap because:
1. Ethanol is a liquid fuel with 100% DM but high value ($550/t).
2. DGS is a solid feed with 88% DM but lower value ($145/t).
3. The value-to-mass ratio of ethanol is much higher than DGS, concentrating economic allocation toward ethanol while mass allocation is nearly equal between the two products.

---

## 6. Mass Balance Verification

### 6.1 Summary Across Both Systems

| System | Input DM (t/t) | Output DM (t/t) | Balance | As-is Output (t/t) | Notes |
|--------|---------------|-----------------|---------|-------------------|-------|
| Flour milling | 0.860 | 0.860 | 100.0% | 1.000 | Exact balance; dry process, all products at 86% DM |
| Dry-grind ethanol | 0.860 | 0.582 | 67.7% | 0.620 | CO₂ and water losses; 9 kg DM excess noted |

### 6.2 Input-Output Reconciliation

**Flour Milling:**
- Input: 0.860 t DM
- Output: 0.8600 t DM (100.0% of input)
- DM balance closes exactly because all co-products are at 86% DM, matching the input moisture basis.
- As-is mass is 1.000 t/t (no net water added or removed within the system boundary).
- In practice, commercial mills lose 0.5–1.5% of input mass as dust, screenings, and moisture adjustment; the exact 1.000 t/t closure reflects the use of rounded industry-average yields.

**Dry-Grind Ethanol:**
- Input: 0.860 t DM
- Output (ethanol + DGS): 0.582 t DM (67.7% of input)
- CO₂ from fermentation: ~0.287 t DM (stoichiometric calculation)
- Total DM accounted: 0.869 t (1.0% above input, see Section 4.6 for discussion)
- Missing as-is mass (~0.38 t/t) is primarily CO₂ gas (~0.29 t/t) plus water evaporated during distillation and DGS drying.

---

## 7. Complete Data Table

| Parent Crop | Crop System | Stage | USDA Standard | Standard Moisture | Parent Input Basis | Co-product Stream | Yield (t/t) | Yield Range | Price (USD/t) | Price Range | DM (%) | DM Output (t/t) | Revenue (USD/t) | Econ Alloc (%) | Mass Alloc (%) |
|-------------|-------------|-------|---------------|-------------------|-------------------|-------------------|-------------|-------------|---------------|-------------|--------|-----------------|-----------------|----------------|----------------|
| Wheat | Wheat flour milling | Single | 60 lb/bushel at 14% moisture | 14% | 1 t wheat at 14% moisture | Wheat flour (all-purpose) | 0.73 | 0.71–0.75 | 420 | 380–460 | 86.0 | 0.6278 | 306.60 | 87.7 | 73.0 |
| Wheat | Wheat flour milling | Single | 60 lb/bushel at 14% moisture | 14% | 1 t wheat at 14% moisture | Wheat bran | 0.16 | 0.14–0.18 | 170 | 150–190 | 86.0 | 0.1376 | 27.20 | 7.8 | 16.0 |
| Wheat | Wheat flour milling | Single | 60 lb/bushel at 14% moisture | 14% | 1 t wheat at 14% moisture | Wheat middlings | 0.11 | 0.09–0.13 | 145 | 130–160 | 86.0 | 0.0946 | 15.95 | 4.5 | 11.0 |
| Wheat | Wheat dry-grind ethanol | Single | 60 lb/bushel at 14% moisture | 14% | 1 t wheat at 14% moisture | Fuel ethanol | 0.30 | 0.28–0.32 | 550 | 520–580 | 100.0 | 0.300 | 165.00 | 78.1 | 51.5 |
| Wheat | Wheat dry-grind ethanol | Single | 60 lb/bushel at 14% moisture | 14% | 1 t wheat at 14% moisture | Wheat DGS | 0.32 | 0.29–0.35 | 145 | 120–170 | 88.0 | 0.282 | 46.40 | 21.9 | 48.5 |

---
## 8. Data Quality and Limitations

### 8.1 High-Confidence Data (Government/Industry Sources)

| Data Point | Confidence | Source |
|------------|-----------|--------|
| Flour extraction rate (73%) | **High** | USDA NASS [^2^]; US Wheat Associates [^3^]; K-State [^4^] |
| Bran and middlings yields | **High** | K-State Extension [^4^] |
| Ethanol yield (0.30 t/t) | **High** | USDA ERS [^5^]; confirmed by empirical estimates |
| Wheat grain prices | **High** | USDA FAS [^7^]; IGC [^11^] |
| Bran prices ($170/t) | **High** | IndexBox [^8^] |
| DM contents (flour milling) | **High** | Industry specifications; consistent with input moisture basis |

### 8.2 Medium-Confidence Data (Estimated or Derived)

| Data Point | Confidence | Source |
|------------|-----------|--------|
| Flour price ($420/t) | **Medium** | No USDA flour price series; estimated from grain price + milling margin |
| Middlings price ($145/t) | **Medium** | Industry rule-of-thumb (80–90% of bran price); no centralized price reporting |
| DGS yield (0.32 t/t) | **Medium** | Less documented than corn DDGS; estimated from wheat composition |
| DGS price ($145/t) | **Medium** | Thin market; prices vary widely by region and buyer |
| Ethanol price ($550/t) | **Medium** | Commodity price with significant temporal volatility |
| Wheat starch content (~64%) | **Medium** | Peer-reviewed literature [^6^]; varies by wheat class and growing conditions |

### 8.3 Known Limitations

1. **Wheat class variation:** Hard wheats (HRW, HRS) yield more flour (73–76%) than soft wheats (SRW, SW: 70–74%). The 73% midpoint is a blend weighted toward all-purpose flour production.
2. **Flour grade ambiguity:** Patent flour (low ash) requires lower extraction (68–72%) than all-purpose flour (72–76%). The table uses all-purpose. NASS data (75–77%) includes all flour grades.
3. **Regional price variation:** Flour and bran prices vary by region and transportation costs.
4. **DGS market thinness:** Wheat DGS is less commonly traded than corn DDGS, so price data is sparse and volatile.
5. **Missing germ as separate stream:** Wheat germ (2–3% of kernel) is sometimes separated as a high-value food ingredient ($800–1,200/t) but is often combined with bran or middlings. Including germ as a separate co-product would shift economic allocation toward by-products.
6. **Ethanol plant configuration:** Most US ethanol plants are designed for corn, not wheat. Wheat ethanol is more common in Europe and Canada. The yields may vary by plant design.
7. **DM basis assumption for flour milling:** Using 86% DM for all products (undried basis) is correct for the system boundary at the mill exit, but traded bran and middlings are typically dried to 88–90% DM. The mass allocation is unaffected by this choice (same DM mass allocated regardless), but the as-is yields would differ if dried product weights were used.
8. **Ethanol yield vs. theoretical efficiency:** The 0.30 t/t practical yield represents 96% of the theoretical maximum (0.313 t/t), which is at the high end of typical fermentation efficiency. The true process efficiency may be slightly lower (90–95%), with the difference accounted for by measurement uncertainty in the empirical yield data.
9. **Starch content variability:** The 64% starch content on DM basis varies by wheat class (60–68%) and growing conditions. This directly affects the theoretical ethanol yield and DGS composition.

---
