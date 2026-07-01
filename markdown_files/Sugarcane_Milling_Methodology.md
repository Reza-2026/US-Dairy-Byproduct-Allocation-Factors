# Sugarcane Milling: Co-Product Allocation Methodology, Data Sources, and Calculations

**Document Version:** 1
**Date:** June 2026  
**Basis:** 1 metric ton (t) of sugarcane at ~70% moisture (30% DM)  
**Price Period:** 2024–2025 average (unless otherwise noted)  
---

## Table of Contents

1. [Standard Basis and Conversions](#1-standard-basis-and-conversions)
2. [Data Sources and References](#2-data-sources-and-references)
3. [Sugarcane Milling Processing System](#3-sugarcane-milling-processing-system)
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
| **Parent crop** | Sugarcane (*Saccharum* spp. hybrids) | — |
| **Input quantity** | 1 metric ton (1,000 kg) | — |
| **Moisture content** | ~70% (30% DM) | Industry average for whole sugarcane stalks at the mill [^1^][^2^]; moisture varies 65–75% depending on variety, growing conditions, irrigation, and harvest timing |
| **Dry matter (DM) input** | 0.300 t DM/t sugarcane | Calculated: 1.000 × 0.30 = 0.300 |
| **Typical sugar content** | ~12–15% sucrose (on a cane weight basis) | Industry average for US sugarcane [^1^]; expressed as "pol %" (polarimetric sucrose) of cane. The extractable sugar yield depends on fiber content, juice purity, and mill extraction efficiency |
| **Typical fiber content** | ~11–14% (on a cane weight basis) | Industry average [^5^]; fiber content affects bagasse yield and mill extraction efficiency |
| **Growing regions** | Primarily Florida (Lake Okeechobee area), Louisiana (southern), and Texas (Rio Grande Valley) | US sugarcane production is concentrated in these three states [^3^]. Hawaii was historically a major producer but its last sugar mill closed in 2016. |

### 1.2 Unit Conversions

| Conversion | Factor |
|------------|--------|
| 1 short ton | 2,000 lb = 0.907185 metric ton |
| 1 metric ton | 2,204.62 lb = 1.10231 short tons |
| 1 lb sucrose | 0.453592 kg |
| Sugar content conversion | 1% pol in cane = 10 kg sucrose per tonne of cane |
| Raw sugar (96° pol) | ~96% sucrose, ~0.5–1.0% moisture, remainder invert sugar + ash |

> **Note on sugarcane definition:** "Sugarcane" refers to the whole sugarcane stalk (cane) as delivered to the sugar mill. The stalks are typically cut into 20–30 cm billets during mechanical harvesting. Leaf material (trash) is mostly removed in the field by the harvester, though some trash (typically 5–15% of delivered cane weight) remains in the billeted cane. Mills may include a cleaning station to remove field trash before milling. The clean cane is the input to the processing system modeled here.

> **Note on raw sugar vs. refined sugar:** This document models the production of **raw cane sugar** (typically 96–99° pol, ~97–99% sucrose), which is the primary product of sugarcane milling. Raw sugar may be further refined at a separate refinery to produce white refined sugar, but the refining stage is not included in this system boundary. The $600/t price is for raw sugar under the US Sugar Program, which is lower than refined sugar (~$900/t) because it retains a thin molasses film and requires further processing for use in most food applications.

---

## 2. Data Sources and References

### 2.1 Primary Sources

| Citation | Full Title | Type | URL |
|----------|-----------|------|-----|
| [^1^] | USDA ERS (2025). *Sugar and Sweeteners Yearbook Tables* | Government (USDA) | https://ers.usda.gov/ |
| [^2^] | Feedipedia / INRA / CIRAD / FAO (2015). *Sugarcane molasses* | Academic/Database | https://www.feedipedia.org/node/562 |
| [^3^] | USDA NASS (2025). *Crop Production Annual Summary* | Government (USDA) | https://www.nass.usda.gov/ |
| [^4^] | CRS Report R43998. *U.S. Sugar Program Fundamentals* | Government | https://crsreports.congress.gov/ |
| [^5^] | Chen, J.C.P. & Chou, C.C. (1993). *Cane Sugar Handbook: A Manual for Cane Sugar Manufacturers and Their Chemists* | Academic | — |
| [^6^] | Hugot, E. (1986). *Handbook of Cane Sugar Engineering* | Academic | — |
| [^7^] | Rein, P.W. (2007). *Cane Sugar Engineering* | Academic | — |
| [^8^] | USDA FSA. *Sugar Program (Farm Service Agency)* | Government (USDA) | https://www.fsa.usda.gov/programs-and-services/sugar-program/ |

### 2.2 How Sources Were Used

- **Yield data:** USDA ERS [^1^], Feedipedia [^2^], Chen & Chou [^5^], and Hugot [^6^] provided sugarcane milling yield data. Yield ranges reflect variation across cane sugar content, fiber content, mill extraction efficiency, and crystallization recovery.
- **Price data (raw sugar):** USDA ERS [^1^], USDA FSA [^8^], and CRS [^4^] provided raw cane sugar price data from US domestic markets and the US Sugar Program framework.
- **Price data (molasses):** USDA ERS [^1^] and industry estimates provided cane molasses price data.
- **DM contents:** Chen & Chou [^5^], Feedipedia [^2^], and Rein [^7^] provided sugarcane and co-product DM specifications.

---

## 3. Sugarcane Milling Processing System

### 3.1 Process Description

Sugarcane milling is an integrated, single-stage system that converts whole sugarcane stalks into raw sugar and cane molasses, with bagasse (fibrous residue) produced as a non-marketed by-product that is burned for process energy. Although the physical process involves many sequential steps (preparation, juice extraction, clarification, evaporation, crystallization, and centrifugation), the process is modeled as a single stage because all marketed co-products are produced from a single integrated operation — there is no intermediate product that can be sold or diverted to a separate pathway.

**Processing steps:**

1. **Cane preparation:** Billeted cane is shredded by rotating knives and/or heavy-duty shredders (hammer mills) to break the cane into a fibrous mat that maximizes juice extraction efficiency.
2. **Juice extraction (milling or diffusion):** The prepared cane passes through a series of three-roller mills (typically 4–6 mills in tandem) that crush the cane and extract the juice. Alternatively, some factories use a diffuser (similar to sugar beet processing) for extraction. The extraction efficiency of a modern milling tandem is typically 94–97%. The fibrous residue after juice extraction is **bagasse**.
3. **Bagasse handling:** Bagasse (~45–55% moisture) is conveyed to the boiler house where it is burned to generate steam and electricity for the mill. Most sugarcane mills are energy self-sufficient, using only bagasse as fuel. Surplus electricity (if any) may be sold to the grid. Bagasse is not modeled as a marketed co-product in this document because it is consumed internally for process energy and does not leave the system boundary as a tradable product.
4. **Juice clarification:** The extracted juice (mixed juice) is heated, treated with lime (CaO) and flocculant, and settled to remove impurities (soil, fiber, proteins, waxes). The clear juice is decanted from the settled mud. The mud is filtered to recover additional juice (filter press), and the filter cake (press mud) is returned to the fields as a soil amendment.
5. **Evaporation:** The clarified juice is concentrated in multiple-effect evaporators from ~12–15° Brix to ~55–65° Brix syrup.
6. **Crystallization:** The syrup is further concentrated under vacuum in crystallizers (pans), forming sucrose crystals in a mother liquor. Multiple crystallization stages (typically 3, called A, B, and C strikes) progressively extract sugar from the syrup.
7. **Centrifugation:** Crystal-syrup mixtures are centrifuged to separate raw sugar crystals from the mother liquor. A-massecuite produces A-sugar (raw sugar) and A-molasses. B-massecuite produces B-sugar (re-melted and returned to the process) and B-molasses. C-massecuite produces C-sugar (also re-melted) and final molasses.
8. **Drying and storage:** Raw sugar crystals are dried in rotary or fluidized-bed driers, cooled, and stored for shipment to a refinery.

**Marketed co-products:**

- **Raw sugar:** The primary product — raw cane sugar crystals (~96–99° pol, typically ~98% sucrose). Raw sugar has a light brown color due to a thin film of residual molasses. It is shipped to a refinery for further purification into white sugar, or sold directly for certain food applications (e.g., rum production, some baking applications).
- **Cane molasses:** The residual syrup after the final crystallization stage — contains non-crystallizable sugars (sucrose, invert sugar), organic acids, minerals, and color bodies. Used as animal feed supplement, fermentation substrate (rum, ethanol, yeast, citric acid), or further sugar recovery.

**Non-marketed by-products:**

- **Bagasse:** The fibrous residue after juice extraction (~0.25–0.30 t/t cane at ~48–52% DM). Burned for process energy. Not modeled as a marketed co-product in this system.
- **Filter cake (press mud):** The insoluble residue from juice clarification (~0.03–0.05 t/t cane at ~45–55% DM). Returned to fields as soil amendment.
- **Boiler ash:** From bagasse combustion. Also returned to fields.

> **Note on process integration:** Sugarcane milling is modeled as a single stage because there is no discrete intermediate product that can be physically separated and directed to an alternative processing pathway. The entire process — from cane to raw sugar and molasses — is integrated within a single factory. Raw sugar and molasses are parallel outputs of a single integrated process, not sequential stages with separate inputs.

> **Note on bagasse:** Bagasse is excluded from the co-product allocation in this document because it is consumed internally for process energy and does not leave the system boundary as a tradable product. This is consistent with the system boundary definition for many LCA studies of sugar production, where bagasse is treated as an internal energy recovery stream. However, some LCAs include bagasse as a co-product, especially in contexts where surplus electricity from bagasse combustion is sold to the grid. See Section 9.1 for a discussion of how bagasse inclusion affects allocation.

### 3.2 Process Flow

```
1 t sugarcane at ~30% DM (0.300 t DM)
        │
        ▼
  ┌─ SUGARCANE MILLING ──────────────────────────┐
  │                                                │
  │  Preparation: shredding                        │
  │  Extraction: 4-6 roller mills in tandem        │
  │  Clarification: lime treatment, settling       │
  │  Evaporation: multiple-effect evaporators      │
  │  Crystallization: A/B/C strikes                │
  │  Centrifugation: separate crystals             │
  │                                                │
  │  Water removed: ~0.537 t                       │
  │  (evaporation, wastewater, juice heating)       │
  │                                                │
  │  Bagasse (non-marketed): ~0.27 t at ~50% DM   │
  │  (0.135 t DM; burned for process energy)        │
  │                                                │
  │  Filter cake (non-marketed): ~0.035 t          │
  │  at ~50% DM (~0.0175 t DM)                     │
  │  DM losses: ~0.006 t DM (1.9%)                │
  │                                                │
  │  Raw sugar: 0.11 t at 100% DM              ◄── co-product
  │    (0.1100 t DM)                                │
  │                                                │
  │  Cane molasses: 0.0425 t at 75% DM        ◄── co-product
  │    (0.0319 t DM)                                │
  │                                                │
  └────────────────────────────────────────────────┘

ALLOCATION (single stage, marketed co-products only, US Domestic):
  Economic:   Raw sugar 89.6%, Cane molasses 10.4%
  Mass:       Raw sugar 77.5%, Cane molasses 22.5%
```

---

## 4. Co-Product Yields and Properties

### 4.1 Processing Yields

| Co-product | Yield (t/t sugarcane) | Range | Source & Calculation |
|------------|----------------------|-------|---------------------|
| **Raw sugar** | 0.11 | 0.10–0.12 | Midpoint of range. Industry average for US sugarcane mills with modern extraction technology [^1^][^5^]. The 0.11 value is the mathematical midpoint of the stated range. Sugar yield depends on cane sugar content (typically 12–15% sucrose on a cane weight basis), mill extraction efficiency (94–97%), and crystallization recovery. Florida mills, which process higher-sugar cane, tend to achieve yields at the upper end of the range. Louisiana mills, processing cane with lower sugar content and higher fiber, tend to achieve yields at the lower end. |
| **Cane molasses** | 0.0425 | 0.035–0.05 | Midpoint of range. Represents the final (blackstrap) molasses from the C-strike crystallization stage [^5^][^7^]. The 0.0425 value is the mathematical midpoint of the stated range: (0.035 + 0.05) / 2 = 0.0425. Molasses yield depends on the non-sugar content of the cane juice (higher impurities → more molasses), the number of crystallization stages, and whether additional sugar recovery from molasses is practiced. |

> **Note on yield relationships:** Sugar and molasses yields are inversely related — more efficient sugar extraction (more crystallization stages, or additional recovery from molasses) reduces molasses yield and increases sugar yield. The two marketed co-products (raw sugar + cane molasses) sum to 0.1525 t/t (as-is), meaning only ~15% of the cane mass leaves as marketed products. The majority of the cane mass becomes bagasse (~0.27 t), water removed during processing (~0.537 t), and minor by-products (filter cake, boiler ash).

### 4.2 Dry Matter Contents

| Co-product | DM (%) | Basis |
|------------|--------|-------|
| Raw sugar | 100.0% | Raw cane sugar is essentially pure dry solid with negligible moisture (~0.5–1.0% moisture). The 100% DM value is standard for LCA allocation purposes; the <1% moisture content is negligible for mass balance calculations. |
| Cane molasses | 75.0% | Cane molasses (blackstrap) typically contains 73–80% total solids (20–27% moisture). The 75% DM value represents standard-density blackstrap molasses as produced at the crystallization stage [^5^][^7^]. Cane molasses has lower sugar content than beet molasses (~55% total sugars vs. ~60%) but higher mineral content. |

### 4.3 DM Output per Tonne

| Co-product | Calculation | DM Output (t/t sugarcane) |
|------------|-------------|---------------------------|
| **Raw sugar** | 0.11 × 1.00 | **0.1100** |
| **Cane molasses** | 0.0425 × 0.75 | **0.0319** |
| **Total (marketed co-products)** | | **0.1419** |

> **Note on total DM output:** The marketed co-products carry only 0.1419 t DM of the 0.300 t DM input (47.3%). The remaining DM (0.1581 t, or 52.7% of input DM) is in non-marketed by-products: bagasse (~0.135 t DM) and filter cake (~0.0175 t DM), with minor losses (~0.0056 t DM). This large non-marketed DM fraction is characteristic of sugarcane milling, where the fiber (bagasse) constitutes a major fraction of the cane's dry matter but is consumed internally for energy rather than sold as a co-product.

---

## 5. Prices

### 5.1 Co-Product Prices

| Co-product | Price (USD/t) | Range | Source | Notes |
|------------|--------------|-------|--------|-------|
| **Raw sugar** | 600 | 450–750 | USDA ERS [^1^]; USDA FSA [^8^]; CRS [^4^] | 2024–2025 average for US domestic raw cane sugar (bulk, FOB mill). Equivalent to ~$0.27/lb. US sugar prices are supported by the US sugar program (tariff-rate quotas, price support loans, marketing allotments), which keeps domestic prices well above world market levels [^4^]. Midpoint of range: ($450 + $750) / 2 = $600. |
| **Cane molasses** | 180 | 130–230 | USDA ERS [^1^]; USDA FSA [^8^]; industry estimates | 2024–2025 average for blackstrap cane molasses (75–78% DM). Prices vary with sugar content, regional demand from feedlots and fermentation industries, and competing molasses sources. Cane molasses used for rum or ethanol fermentation typically commands a premium over feed-grade molasses. Midpoint of range: ($130 + $230) / 2 = $180. |

### 5.2 Price Verification

**Raw sugar:**

```
USDA ERS (2025): US raw cane sugar ~$0.24-0.35/lb = $530-772/t
USDA FSA (2025): loan rate ~$0.1975/lb; effective market ~$0.25-0.38/lb = $551-838/t
World raw sugar price (2025): ~$0.18-0.28/lb = $400-617/t
Historical range (2020-2025): $0.18-0.38/lb = $400-838/t

Selected midpoint: $600/t
Mathematical midpoint of range ($450-750): $600/t ✓
The price midpoint IS the true mathematical midpoint of the stated range.

Note: The US domestic raw sugar price (~$600/t) is substantially above the
world market price (~$400-500/t) due to the US Sugar Program, which provides
price support through tariff-rate quotas and non-recourse loans (CRS Report
R43998 [^4^]). LCA studies for non-US contexts should use the World Market
price scenario in Section 6.4.
```

**Cane molasses:**

```
USDA ERS (2025): cane molasses ~$140-220/t
Feed-grade molasses: ~$130-180/t
Fermentation-grade molasses: ~$160-240/t
Blended estimate across end uses: ~$130-230/t

Selected midpoint: $180/t
Mathematical midpoint of range ($130-230): $180/t ✓
The price midpoint IS the true mathematical midpoint of the stated range.
```

### 5.3 Revenue per Tonne

| Co-product | Calculation | Revenue (USD/t sugarcane) |
|------------|-------------|--------------------------|
| **Raw sugar** | 0.11 × 600 | **$66.00** |
| **Cane molasses** | 0.0425 × 180 | **$7.65** |
| **Total** | | **$73.65** |

> **Note on revenue distribution:** Raw sugar accounts for 89.6% of total revenue, making it the dominant product economically. Cane molasses contributes only 10.4% of revenue. This extreme economic concentration in the primary product is characteristic of sugar production from both sugarcane and sugar beet, and is similar to other high-value/low-volume primary products (e.g., oil from oilseeds, juice from citrus). The total revenue per tonne of sugarcane ($73.65) is lower than for sugar beet, reflecting sugarcane's lower sugar yield (0.11 vs. 0.150 t/t) and the difference between raw sugar ($600/t) and refined beet sugar ($900/t) prices.

---

## 6. Allocation Methodology

### 6.1 Economic Allocation (US Domestic)

| Co-product | Calculation | Allocation |
|------------|-------------|------------|
| Raw sugar | (66.00 ÷ 73.65) × 100 | **89.6%** |
| Cane molasses | (7.65 ÷ 73.65) × 100 | **10.4%** |
| **Total** | | **100.0%** |

> **Rounding note:** The exact economic allocation percentages are Raw sugar 89.61% and Cane molasses 10.39%. When rounded to one decimal place, Molasses is adjusted by +0.1 pp to ensure the sum equals exactly 100.0%.

### 6.2 Mass Allocation

| Co-product | Calculation | Allocation |
|------------|-------------|------------|
| Raw sugar | (0.1100 ÷ 0.1419) × 100 | **77.5%** |
| Cane molasses | (0.0319 ÷ 0.1419) × 100 | **22.5%** |
| **Total** | | **100.0%** |

> **Rounding note:** The exact mass allocation percentages are Raw sugar 77.52% and Cane molasses 22.48%. When rounded to one decimal place, these become 77.5% and 22.5%, summing to 100.0%.

> **Note on mass allocation basis:** Mass allocation is calculated among the marketed co-products only (raw sugar and cane molasses). Bagasse, which carries ~0.135 t DM/t sugarcane (45.0% of total DM output), is excluded because it is not a marketed co-product. If bagasse were included as a co-product, the mass allocation would shift dramatically: raw sugar would drop to ~39.7%, bagasse would receive ~48.8%, and molasses would drop to ~11.5%. See Section 9.1 for a discussion of this issue.

### 6.3 Comparison (US Domestic)

| Co-product | Economic | Mass | Difference |
|------------|----------|------|------------|
| Raw sugar | 89.6% | 77.5% | +12.1 pp |
| Cane molasses | 10.4% | 22.5% | −12.1 pp |

The 12.1 pp difference for raw sugar reflects its high value-to-mass ratio. Raw sugar commands $600/t (3.3× the molasses price) and carries 100% DM, but it represents only 77.5% of the marketed co-product DM. Under economic allocation, sugar's high price per tonne amplifies its share of the environmental burden relative to its mass share. Conversely, molasses carries 22.5% of the marketed DM but only 10.4% of the economic value, because molasses is a lower-value product ($180/t) with significant water content (25% moisture).

The allocation divergence for sugarcane (12.1 pp) is moderate compared to other crops in this review. It is lower than the divergences for safflower oil (43.2 pp), citrus juice (43.1 pp), and cotton lint (34.6 pp in cascade), but slightly higher than for soybean meal (7.5 pp). This reflects raw sugar's position as a high-value product that also carries a large share of the marketed DM — unlike cotton lint, which is high-value but low-DM, or soybean meal, which is moderate-value and moderate-DM.

### 6.4 World Market Scenario

The US Domestic allocation in Sections 6.1–6.3 uses the US domestic sugar price (~$600/t), which is supported by the US Sugar Program (tariff-rate quotas, price support loans, and marketing allotments) [^4^]. For LCA studies conducted in international contexts — or for studies that wish to avoid the distortion of domestic price support programs — a World Market price scenario is provided below using a representative world raw sugar price of $400/t.

**World Market Price Assumptions:**

| Co-product | Price (USD/t) | Source | Notes |
|------------|--------------|--------|-------|
| Refined sugar | 400 | World market (ICE No. 11 futures, 2024–2025 average) | Representative world raw sugar price. The world raw sugar price is substantially below the US domestic price due to the absence of price support mechanisms. |
| Cane molasses | 180 | Unchanged | Molasses price is driven by feed/fermentation demand, not directly by the sugar program. |

**World Market Revenue per Tonne:**

| Co-product | Calculation | Revenue (USD/t sugarcane) |
|------------|-------------|--------------------------|
| **Raw sugar** | 0.11 × 400 | **$44.00** |
| **Cane molasses** | 0.0425 × 180 | **$7.65** |
| **Total** | | **$51.65** |

**World Market Economic Allocation:**

| Co-product | Calculation | Allocation |
|------------|-------------|------------|
| Raw sugar | (44.00 ÷ 51.65) × 100 | **85.2%** |
| Cane molasses | (7.65 ÷ 51.65) × 100 | **14.8%** |
| **Total** | | **100.0%** |

> **Rounding note:** The exact World Market economic allocation percentages are Raw sugar 85.19% and Cane molasses 14.81%. When rounded to one decimal place, these become 85.2% and 14.8%, summing to 100.0%.

**Comparison: US Domestic vs. World Market Economic Allocation:**

| Co-product | US Domestic | World Market | Difference |
|------------|-------------|-------------|------------|
| Raw sugar | 89.6% | 85.2% | −4.4 pp |
| Cane molasses | 10.4% | 14.8% | +4.4 pp |

Under the World Market scenario, raw sugar's economic allocation decreases by 4.4 pp (from 89.6% to 85.2%), while molasses gains proportionally. This shift reflects the fact that the US Sugar Program inflates sugar's price — and therefore its revenue share — by approximately 50% above the world market level. LCA practitioners should select the price scenario that matches their study's geographic and policy context. Mass allocation is unaffected by the price scenario because it depends only on DM outputs.

---

## 7. Mass Balance Verification

### 7.1 DM Balance

| Check | Value | Status |
|-------|-------|--------|
| Input: Sugarcane at ~30% DM | 1.000 t | — |
| Input DM | 0.300 t | — |
| Output: Raw sugar (as-is) | 0.110 t | ✓ |
| Output: Cane molasses (as-is) | 0.0425 t | ✓ |
| Total marketed co-product output (as-is) | 0.1525 t | 15.3% of input |
| Output DM: Raw sugar | 0.1100 t | ✓ |
| Output DM: Cane molasses | 0.0319 t | ✓ |
| Total marketed co-product DM | 0.1419 t | 47.3% of input DM |
| Non-marketed: Bagasse DM | ~0.1350 t | 45.0% of input DM |
| Non-marketed: Filter cake DM | ~0.0175 t | 5.8% of input DM |
| DM losses | ~0.0056 t | 1.9% of input DM |
| Total DM output (all streams) | ~0.3000 t | 100.0% of input DM ✓ |

**DM Balance Detail:**

| Item | Value | Notes |
|------|-------|-------|
| Input DM (1 t sugarcane at ~30% DM) | 0.3000 t | 1.000 × 0.30 |
| **Output DM — marketed co-products:** | | |
| Raw sugar | 0.1100 t | 0.11 t × 100% DM |
| Cane molasses | 0.0319 t | 0.0425 t × 75% DM |
| Total marketed co-product DM | **0.1419 t** | |
| **Output DM — non-marketed by-products:** | | |
| Bagasse (~0.27 t at ~50% DM) | ~0.1350 t | Primary non-marketed stream; burned for process energy |
| Filter cake (~0.035 t at ~50% DM) | ~0.0175 t | Soil amendment; returned to fields |
| **DM losses (wastewater organics, evaporation of volatiles)** | ~0.0056 t | ~1.9% of input DM |
| **Total output DM** | **~0.3000 t** | |

> **Balance assessment:** The DM balance closes when bagasse and filter cake are included. The marketed co-products carry only 47.3% of the input DM, with the remaining 45.0% in bagasse, 5.8% in filter cake, and 1.9% in minor losses. This is fundamentally different from sugar beet processing (where the marketed co-products carry ~93% of the input DM) because sugarcane has a much higher fiber content (~11–14% of cane weight) that becomes bagasse. The 1.9% DM loss is within the acceptable range and represents non-recovered organics in wastewater, volatile losses during heating, and minor measurement uncertainty.
>
> **Note on bagasse yield:** The bagasse yield of ~0.27 t/t cane at ~50% DM (~0.135 t DM) is at the lower end of the typical range (0.25–0.35 t/t cane) and reflects modern high-extraction mills. Older mills with lower extraction efficiency produce more bagasse (up to ~0.30–0.35 t/t) because more juice remains in the fiber. The bagasse yield is inversely related to extraction efficiency: higher extraction → less residual juice in bagasse → lower bagasse yield.

### 7.2 As-Is Mass Balance

| Item | Value | Notes |
|------|-------|-------|
| Input (sugarcane) | 1.000 t | — |
| **Output — marketed co-products:** | | |
| Raw sugar | 0.110 t | — |
| Cane molasses | 0.0425 t | — |
| **Total marketed co-product output** | **0.1525 t** | |
| **Output — non-marketed streams:** | | |
| Bagasse | ~0.270 t | Burned for process energy |
| Filter cake | ~0.035 t | Returned to fields |
| Water removed (evaporation, wastewater) | ~0.537 t | Total cane water (0.700 t) minus water in products (0.163 t) |
| DM losses (wastewater organics, volatiles) | ~0.006 t | See DM balance above |
| **Balance** | **~1.000 t** | ✓ |

> **Note on water balance:** Sugarcane is ~70% water (0.700 t per tonne of cane). Of this, only ~0.011 t remains in the marketed co-products (all in molasses at 25% moisture), ~0.135 t remains in bagasse (at ~50% moisture), and ~0.0175 t remains in filter cake (at ~50% moisture). The remaining ~0.537 t is removed during processing — primarily by evaporation during juice concentration and crystallization, and as wastewater from clarification and cooling operations. This large water removal, combined with the large bagasse stream, explains why marketed product yields sum to only 15.3% of the input mass.

---

## 8. Complete Data Table

| Parent Crop | Crop System | Stage | USDA Standard | Standard Moisture | Parent Input Basis | Co-product Stream | Yield (t/t sugarcane) | Yield Range | Price (USD/t) | Price Range | DM (%) | DM Output (t/t sugarcane) | Revenue (USD/t sugarcane) | Econ Alloc (%) | Mass Alloc (%) |
|-------------|-------------|-------|---------------|-------------------|-------------------|-------------------|-------------|-------------|---------------|-------------|--------|-----------------|-----------------|----------------|----------------|
| Sugarcane | Sugarcane milling | Single | ICUMSA raw sugar standards; cane sugar content by polarimetry (pol %) | ~70% moisture (~30% DM) | 1 t sugarcane at ~30% DM | Raw sugar | 0.11 | 0.10–0.12 | 600 | 450–750 | 100.0 | 0.1100 | 66.00 | 89.6 | 77.5 |
| Sugarcane | Sugarcane milling | Single | ICUMSA raw sugar standards; cane sugar content by polarimetry (pol %) | ~70% moisture (~30% DM) | 1 t sugarcane at ~30% DM | Cane molasses | 0.0425 | 0.035–0.05 | 180 | 130–230 | 75.0 | 0.0319 | 7.65 | 10.4 | 22.5 |

---

## 9. Data Quality and Limitations

### 9.1 Key Methodological Issue: Bagasse Exclusion

The most significant methodological decision in this allocation is the **exclusion of bagasse** from the co-product allocation. Bagasse (~0.25–0.30 t/t cane at ~50% DM) carries approximately 45% of the input DM but is not modeled as a marketed co-product because it is consumed internally for process energy. This decision has a major impact on the mass allocation:

**Current allocation (bagasse excluded):**

| Co-product | Economic | Mass |
|------------|----------|------|
| Raw sugar | 89.6% | 77.5% |
| Cane molasses | 10.4% | 22.5% |

**Hypothetical allocation (bagasse included at ~0.27 t/t, ~50% DM, ~$30/t as boiler fuel):**

| Co-product | Economic | Mass |
|------------|----------|------|
| Raw sugar | 80.7% | 39.7% |
| Cane molasses | 9.4% | 11.5% |
| Bagasse | 9.9% | 48.8% |

Including bagasse as a co-product dramatically shifts the mass allocation — raw sugar drops from 77.5% to 39.7% because bagasse carries ~49% of the total DM (including bagasse). The economic impact is smaller because bagasse has a low value ($30/t for energy use) relative to raw sugar ($600/t), but it still reduces sugar's economic share by ~8.9 pp. LCA practitioners must carefully consider whether bagasse should be included as a co-product based on their system boundary and study goals. If surplus electricity from bagasse combustion is sold to the grid, the bagasse-derived electricity may be modeled as a co-product with a revenue-based allocation.

### 9.2 High-Confidence Data

| Data Point | Confidence | Source |
|------------|-----------|--------|
| Raw sugar yield (0.11 t/t) | **High** | Well-documented; midpoint of narrow range [^1^][^5^] |
| Raw sugar DM% (100%) | **High** | Pure crystalline sucrose with negligible moisture |
| Sugarcane DM% (~30%) | **High** | Well-documented industry average [^2^][^5^] |
| Raw sugar price ($600/t, US domestic) | **High** | Well-documented commodity with transparent pricing [^1^][^4^] |
| Bagasse yield (~0.27 t/t) | **High** | Well-documented [^5^][^6^] |
| Bagasse DM% (~50%) | **High** | Well-documented [^5^][^6^] |
| DM balance (1.9% gap, fully accounted) | **High** | Well within acceptable range; gap explained by wastewater organics and volatiles |

### 9.3 Medium-Confidence Data

| Data Point | Confidence | Source |
|------------|-----------|--------|
| Cane molasses yield (0.0425 t/t) | **Medium** | Depends on non-sugar content of juice and number of crystallization stages |
| Cane molasses DM% (75%) | **Medium** | Standard trading specifications cite 73–80% DM; some factories concentrate further |
| Cane molasses price ($180/t) | **Medium** | Varies with sugar content, end use (feed vs. fermentation), and competing sources |
| Sugarcane moisture (~70%) | **Medium** | Varies with variety, growing conditions, and harvest timing (65–75% range) |
| Filter cake yield (~0.035 t at ~50% DM) | **Medium** | Varies with soil content of cane and clarification process; limited published data |
| Filter cake composition | Medium | Varies with soil content of delivered cane and clarification process; limited published data available

### 9.4 Known Limitations

1. **Bagasse as internal energy vs. co-product:** This document treats bagasse as an internal energy source, not a co-product. This is appropriate when the mill consumes all bagasse for process energy and no surplus energy is sold. However, many modern sugarcane mills — especially in Brazil — generate surplus electricity from bagasse and sell it to the grid. In such cases, bagasse (or the surplus electricity derived from it) should be included as a co-product. The allocation impact of including bagasse is discussed in Section 9.1 above.

2. **Raw sugar vs. refined sugar system boundary:** This document models sugarcane milling only, producing raw sugar at $600/t (US domestic). Many LCA studies include the subsequent refining step, which produces refined white sugar at ~$900/t. If the system boundary is extended to include refining, the co-product structure changes: refined sugar and refinery molasses become the co-products, and the raw sugar becomes an intermediate product. This would require a two-stage (cascade) allocation model similar to cotton processing.

3. **Molasses end use:** Cane molasses has multiple end uses with different economic values: (a) animal feed supplement (lowest value, ~$130–160/t), (b) fermentation substrate for rum, ethanol, or citric acid (medium value, ~$160–200/t), and (c) raw material for additional sugar recovery (reduces molasses yield, increases sugar yield). This table uses a blended price ($180/t) that averages across these end uses. Studies with specific molasses end uses should use the corresponding price.

4. **Sugarcane DM% variability:** The ~30% DM assumption is an industry average, but sugarcane DM% varies significantly with variety, growing conditions (rainfall, irrigation, soil type), and harvest timing. Early-season cane (October in Louisiana) typically has lower DM% (~27–28%), while late-season cane (December–January) can reach 32–34% DM. Harvest method also matters: green cane harvesting (without pre-harvest burning) includes more trash (leaf material), which increases the as-is weight but reduces the effective DM% of the delivered cane. The 30% DM value is appropriate for an annual average but may not reflect specific harvest periods.

5. **Non-marketed by-products:** Sugarcane milling produces several by-products that are not captured as marketed co-products: (a) bagasse (burned for energy, ~0.27 t/t cane), (b) filter cake/press mud (~0.03–0.05 t/t, returned to fields), and (c) boiler ash (from bagasse combustion, returned to fields). The filter cake carries ~0.015–0.020 t DM/t cane, which is the second largest non-marketed DM stream after bagasse. These non-marketed materials do not receive an allocation of environmental burdens under the co-product allocation framework.

6. **US sugar program and dual price scenario:** US domestic sugar prices are supported by the US sugar program (tariff-rate quotas, price support loans, and marketing allotments), which keeps domestic prices above world market levels [^4^]. The $600/t price reflects the US domestic market. The World Market scenario in Section 6.4 uses a $400/t sugar price, which reduces sugar's economic allocation from 89.6% to 85.2%. LCA practitioners must select the price scenario appropriate for their study's geographic and policy context. For studies conducted outside the US, or for studies that wish to avoid the distortion of domestic price support programs, the World Market scenario should be used.

7. **Regional variation:** Sugarcane growing conditions and mill configurations vary significantly across US regions. Florida cane (high sugar content, ~14–15% sucrose, lower fiber ~10–12%) tends to achieve higher sugar yields. Louisiana cane (lower sugar content, ~12–13% sucrose, higher fiber ~13–15%) tends to achieve lower sugar yields. Mill extraction efficiency also varies: newer mills with 6-roller tandems achieve 95–97% extraction, while older mills may achieve 92–94%. These regional differences affect both yields and allocation results.

8. **Molasses desugarization:** Some sugarcane mills operate ion-exclusion chromatography or other processes that recover additional sugar from molasses, reducing the final molasses yield to ~0.02–0.03 t/t and increasing sugar yield to ~0.12–0.13 t/t. This table models standard molasses production without additional sugar recovery. Studies of mills with molasses desugarization should adjust yields accordingly.

9. **Hawaii historical production:** Hawaii was historically a significant US sugarcane producer, but its last sugar mill (Hawaiian Commercial & Sugar Company on Maui) closed in December 2016. Hawaii is therefore excluded from the current growing regions. LCA studies using historical data that includes Hawaii should note this change.

---
