# Gross Energy Reference for Agricultural Co-Products: Data and Methodology Guide

**Document Version:** 1.0  
**Date:** May 2026
**Scope:** Gross Energy (GE/HHV) reference values and uncertainty ranges for all co-products in the LCA co-product allocation methodology series
---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Why Gross Energy: Comparison of Energy Metrics](#2-why-gross-energy-comparison-of-energy-metrics)
3. [Methodology](#3-methodology)
4. [Wet vs. Dry Products: Why Energy Allocation Is Unaffected](#4-wet-vs-dry-products-why-energy-allocation-is-unaffected)
5. [Data Sources and Quality](#5-data-sources-and-quality)
6. [GE Midpoints — Literature Sources](#6-ge-midpoints--literature-sources)
7. [GE Uncertainty Range — Compositional Propagation Method](#7-ge-uncertainty-range--compositional-propagation-method)
8. [Special Cases](#8-special-cases)
9. [Gross Energy Values by Co-Product Category](#9-gross-energy-values-by-co-product-category)
10. [Master GE Reference Table](#10-master-ge-reference-table)
11. [Complete GE Range Results Table](#11-complete-ge-range-results-table)
12. [Implementation in Monte Carlo Simulation](#12-implementation-in-monte-carlo-simulation)

---

## 1. Purpose and Scope

This document provides **Gross Energy (GE) reference values and their uncertainty ranges** for all co-products in the agricultural co-product LCA allocation methodology series. These GE values are the input needed to calculate energy allocation factors alongside the existing economic and mass allocation factors. The document covers:

1. **GE midpoints** — sourced from literature review (bomb calorimetry, feed databases, and published reference values)
2. **GE uncertainty ranges** — derived from compositional uncertainty propagation with PERT-validity corrections

**This document provides GE values only.** The DM outputs and the energy allocation calculations themselves are performed in each crop's individual methodology document, using:
- **DM outputs** from the crop-specific methodology documents (authoritative source)
- **GE values** from this reference document

**Why add energy allocation?**

Economic and mass allocation represent two endpoints on a spectrum. Economic allocation reflects market value (which can be volatile and influenced by policy), while mass allocation reflects physical mass (which ignores the qualitative differences between co-products). Energy allocation occupies an intermediate position: it accounts for the physical energy content of each co-product, which is a stable, measurable property that reflects the thermodynamic investment in producing each stream. ISO 14044 recommends that when allocation significantly affects study conclusions, multiple allocation methods should be applied and results compared. Adding energy allocation provides this third perspective.

The scope includes all co-products from the following crops and processing systems:

| Crop | Processing System | Co-Products |
|------|-------------------|-------------|
| Barley | Malting (Stage 1) | Malt (intermediate), Malt sprouts |
| Barley | Brewing (Stage 2) | Beer, Brewers spent grain (dried) |
| Corn | Wet Milling | Corn starch, Corn gluten meal, Corn gluten feed (dry), Corn germ, Corn steep liquor |
| Corn | Dry Milling | Corn meal & grits, Hominy feed, Corn germ |
| Corn | Dry-Grind Ethanol | Fuel ethanol, Distillers grains (total), Corn oil |
| Sweet Corn | Canning | Edible kernels, Cannery waste silage |
| Soybean | Crushing | Soybean oil, Soybean meal (48% protein), Soybean hulls (whole) |
| Wheat | Flour Milling | Wheat flour (all-purpose), Wheat bran, Wheat middlings |
| Wheat | Dry-Grind Ethanol | Fuel ethanol, Wheat DGS |
| Canola | Crushing | Canola oil (crude), Canola meal |
| Flaxseed | Crushing | Linseed oil, Linseed meal |
| Sunflower | Crushing | Sunflower oil, Sunflower meal (dehulled), Sunflower hulls |
| Safflower | Crushing | Safflower oil, Safflower meal (non-dehulled) |
| Oat | Milling | Food oats, Oat hulls, Oat mill feed |
| Rice | Hulling (Stage 1) | Brown rice (intermediate), Rice hulls |
| Rice | Milling (Stage 2) | White rice (head rice), Rice bran, Rice mill feed |
| Peanut | Shelling (Stage 1) | Shelled kernels (intermediate), Peanut hulls |
| Peanut | Crushing (Stage 2) | Peanut oil, Peanut meal |
| Cotton | Ginning — seed sold (Pathway A) | Cotton lint, Whole cottonseed |
| Cotton | Ginning → Crushing (Pathway B) | Cotton lint, Cottonseed oil, Cottonseed meal, Cottonseed hulls, Cottonseed linters |
| Potato | Processing | Processed potato products, Potato processing waste |
| Citrus | Processing | Citrus juice, Citrus pulp (wet) |
| Sugar Beet | Processing | Refined sugar, Beet pulp (wet), Beet molasses |
| Sugarcane | Milling | Raw sugar, Cane molasses |
| Almond | Hulling | Almond kernels, Almond hulls, Almond shells |

---

## 2. Why Gross Energy: Comparison of Energy Metrics

### 2.1 Available Energy Metrics

Several energy metrics are used in nutrition science and energy engineering. The choice of metric has a direct impact on the resulting allocation factors. The following table compares the four main options:

| Metric | Definition | Measurement Method | Scope of Applicability |
|--------|-----------|-------------------|----------------------|
| **Gross Energy (GE)** / Higher Heating Value (HHV) | Total heat released by complete combustion of a material to CO₂ and liquid H₂O at constant volume | Bomb calorimetry (adiabatic or isoperibol) | Universal: applies to all combustible materials regardless of end use |
| Digestible Energy (DE) | GE minus energy lost in feces | Animal feeding trial or in vitro digestibility | Animal feed only; species-specific (ruminant DE ≠ pig DE ≠ poultry DE) |
| Metabolizable Energy (ME) | DE minus energy lost in urine and combustible gases (methane) | Animal feeding trial with urine/gas collection | Animal feed only; species-specific |
| Net Energy (NE) | ME minus the heat increment — the energy cost of digestion and metabolism | Calculation from ME | Animal feed only; species- and purpose-specific (NE for lactation ≠ NE for growth) |
| Lower Heating Value (LHV) | GE minus the latent heat of vaporisation of the water formed on combustion | Calculation from GE or from elemental analysis | Universal, but an engineering/combustion metric rather than a thermodynamic total |

### 2.2 Why Gross Energy Is the Correct Choice

Gross Energy (GE) — also called Higher Heating Value (HHV) or Gross Calorific Value (GCV) — is the appropriate energy metric for co-product allocation for three fundamental reasons:

**Reason 1: Universal applicability across all end uses.** The co-products in this review serve fundamentally different purposes: human food (almond kernels, wheat flour, beer), animal feed (soybean meal, almond hulls, beet pulp), industrial materials (cotton lint, corn starch), and energy carriers (fuel ethanol, almond shells as boiler fuel). Digestible, metabolizable, and net energy metrics are only meaningful for animal feed — they are undefined or meaningless for industrial products like cotton lint, and they are species-specific (soybean meal has different DE for cattle vs. swine vs. poultry). Gross Energy, by contrast, is a universal physical property that can be measured for any combustible material using the same method (bomb calorimetry), regardless of its end use.

**Reason 2: Stability and reproducibility.** Gross Energy is an intrinsic thermodynamic property of a material that does not change with market conditions, policy interventions, or animal species. It is measured by a standardized physical method (bomb calorimetry, ISO 9831:1998 / EN 14918:2009) with high precision (typically ±0.5%).

**Reason 3: Alignment with LCA principles.** ISO 14044 Section 4.3.4.2 states that allocation should reflect the physical relationships between the products and their respective shares of the total environmental burden. Gross Energy reflects the thermodynamic energy content embedded in each co-product — a fundamental physical property that relates to the solar energy captured during photosynthesis and the processing energy invested in producing each stream.

### 2.3 Why Not the Alternatives?

| Alternative | Why Not |
|-------------|---------|
| **Digestible Energy (DE)** | Only applicable to animal feed co-products. Cannot be calculated for cotton lint, sugar, corn starch, or fuel ethanol. Even for feed co-products, DE values differ by species. |
| **Metabolizable Energy (ME)** | Same limitations as DE, plus additional losses that are species-specific and diet-context-dependent. |
| **Net Energy (NE)** | Most context-dependent of all energy metrics. Additionally, LHV systematically underestimates the energy content of hydrogen-rich materials (oils, proteins) relative to carbon-rich materials. |
| **Lower Heating Value (LHV)** | LHV assumes water vapor in combustion products is not condensed. This is appropriate for engine/combustion applications but not for LCA allocation. LHV of vegetable oils ≈ 37.0–37.5 MJ/kg vs. GE/HHV ≈ 39.3 MJ/kg. For allocation purposes, GE (HHV) captures the total energy that was physically embedded in the co-product. |

---

## 3. Methodology

### 3.1 Calculation Formula

Energy allocation is calculated analogously to economic and mass allocation, using Gross Energy on a DM basis:

```
Energy output_i  = DM_output_i (t DM/t parent input) × GE_i (MJ/kg DM) × 1,000 (kg/t)
Energy alloc_i   = Energy_output_i / Σ(Energy_outputs) × 100%
```

This formula requires two inputs per co-product:
1. **DM output** (t DM/t parent input) — from the crop-specific methodology documents (authoritative source for DM)
2. **Gross Energy on a DM basis** (MJ/kg DM) — provided in this document

> **Important:** The DM outputs used in energy allocation calculations must be taken directly from the crop-specific economic/mass allocation methodology documents. These are the authoritative source for DM data.

### 3.2 Worked Example: Barley Malting/Brewing (2-stage cascade)

Barley is modelled as a 2-stage cascade, consistent with the economic and mass allocation methodology. **Stage 1 (Malting)** allocates between malt (intermediate) and malt sprouts. **Stage 2 (Brewing)** allocates malt's share between beer and brewers spent grain. DM outputs are taken from the Barley Processing Methodology document; GE values are from Section 10 of this document.

#### Stage 1: Malting (1 t barley at 12% moisture, DM input = 0.880 t)

| Co-product | DM Output (t/t barley)¹ | GE (MJ/kg DM)² | Energy Output (MJ/t barley) | Energy Alloc (Stage 1) |
|------------|------------------------|-----------------|------------------------------|------------------------|
| Malt (intermediate) | 0.7980 | 19.5 | 15,561 | **95.8%** |
| Malt sprouts | 0.0372 | 18.4 | 684 | **4.2%** |
| **Stage 1 total** | **0.8352** | — | **16,245** | **100.0%** |

The 0.045 t of DM not appearing as a Stage 1 output is respiration loss during germination and kilning (5.1% of the DM input); it carries no allocation.

#### Stage 2: Brewing (subdividing malt's 95.8% energy share)

| Co-product | DM Output (t/t barley)¹ | GE (MJ/kg DM)² | Energy Output (MJ/t barley) | Energy Sub-Share (Stage 2) |
|------------|------------------------|-----------------|------------------------------|----------------------------|
| Beer | 0.3910 | 22.7 | 8,876 | **75.3%** |
| Brewers spent grain (dried) | 0.1456 | 20.0 | 2,912 | **24.7%** |
| **Stage 2 total** | **0.5366** | — | **11,788** | **100.0%** |

#### Final cascade energy allocation (per t barley)

| Co-product | Calculation | Energy Alloc |
|------------|-------------|--------------|
| Malt sprouts | Stage 1 direct | **4.2%** |
| Beer | 95.8% × 75.3% | **72.1%** |
| Brewers spent grain | 95.8% × 24.7% | **23.7%** |
| **Total** | | **100.0%** |

¹ DM output from the Barley Processing Methodology document
² GE from Section 10 of this document

> **Note on beer DM:** Beer is entered at **8.5% DM** (≈3.9% ethanol by weight at 5% ABV, ≈4% residual extract, ≈0.5% protein and ash). This is not the same quantity as original gravity — a 12°P wort has 12% dissolved solids *before* fermentation, and roughly two-thirds of that extract is converted to ethanol and CO₂, with the CO₂ leaving the system. Using original gravity in place of beer DM would overstate beer's dry matter by about 40%.

### 3.3 Three-Way Comparison (cascade)

| Co-product | Economic | Mass | Energy |
|------------|----------|------|--------|
| Malt sprouts | 2.5% | 4.5% | 4.2% |
| Beer | 96.0% | 69.6% | 72.1% |
| Brewers spent grain | 1.5% | 25.9% | 23.7% |

**Interpretation:** Energy allocation sits close to mass allocation for barley and far from economic. It tracks mass because the three co-products differ only moderately in GE per kg DM (18.4–22.7 MJ/kg DM, a ratio of 1.23), so the result is driven mainly by how the dry matter divides. It departs from mass by about 2.5 pp on beer and spent grain, in beer's favour, because beer's dry matter is largely ethanol and so is more energy-dense than the fibre and protein of spent grain. Economic allocation is in a different place entirely — beer takes 96.0% of the revenue against 72.1% of the energy — because beer sells for many times the price per tonne of spent grain or sprouts. The cascade structure also preserves malt sprouts' Stage 1 share (4.2% energy) rather than letting beer's revenue swamp it in a single combined pool.

## 4. Wet vs. Dry Products: Why Energy Allocation Is Unaffected

**Gross Energy is a property of the dry matter, not the as-is product.** Water has zero calorific value — it does not burn and contributes no energy to the combustion. Therefore:

- A wet product (e.g., beet pulp at 25% DM) and its dry equivalent (dried beet pulp at 90% DM) have **the same GE per kg of DM** (~17.1 MJ/kg DM for beet pulp DM)
- The **DM output** is also the same regardless of form
- Therefore, **energy allocation is completely unaffected by whether a wet or dry form is modeled**

This is a crucial difference from economic allocation, where the wet/dry choice changes the price and thus the allocation. Energy allocation, like mass allocation, is robust to this choice.

---

## 5. Data Sources and Quality

### 5.1 Primary Data Sources for GE Midpoints

The Gross Energy midpoint values in this document are sourced from three categories of references, listed in order of priority:

**Tier 1: INRAE-CIRAD-AFZ Feed Tables (Sauvant et al., 2004)**

The INRAE-CIRAD-AFZ feed tables (available at https://feedtables.com/) are the primary source for GE values of feed ingredients. These tables report Gross Energy on both an as-fed and DM basis, with standard deviations, minimum and maximum values, and sample counts. The GE values are measured by adiabatic bomb calorimetry according to standardized methods. This is the same database used by Feedipedia (https://www.feedipedia.org/). Online edition continuously updated at https://feedtables.com/; original publication Sauvant et al. 2004.

**Tier 2: NRC/NAS Feed Tables**

The National Research Council (NRC) publications provide GE, DE, ME and NE values for common feed ingredients used in the United States. The edition used here is *Nutrient Requirements of Swine*, 11th rev. ed. (2012); its feed ingredient composition tables cover 122 feedstuffs. Because that volume is a monogastric reference, it is used only for ingredients it actually lists — ruminant-oriented and food-grade co-products (citrus pulp, beet pulp and molasses, potato products, almond hulls and shells) are sourced from INRAE-CIRAD-AFZ, Feedipedia or composition calculation instead.

**Tier 3: Composition-Based Calculation**

For co-products not directly listed in the INRAE-CIRAD-AFZ or NRC tables (e.g., beer, corn steep liquor), GE is calculated from proximate composition. The left-hand column below gives heats of combustion (the GE coefficients used in this document); the right-hand column gives the Atwater general factors, which are metabolizable energy and are **not** used for allocation:

| Component | Gross Energy (MJ/kg) | Metabolizable Energy (MJ/kg) |
|-----------|----------------------|-----------------------------|
| Fat (lipid) | 39.3 | 37.7 |
| Protein (crude) | 23.6 | 16.7 |
| Carbohydrate (available) | 17.5 | 16.7 |
| Fiber (NDF) | 17.5 | — |
| Ash | 0.0 | 0.0 |
| Organic acids | 14.0 | — |
| Ethanol | 29.7 | — |

**Organic acids coefficient:** INRAE-CIRAD-AFZ standard coefficient for organic acids; weighted average of lactic acid (~14.9 MJ/kg), acetic acid (~14.6 MJ/kg), and citric acid (~10.2 MJ/kg).

**Atwater general factor derivation:** Fat 9.0 kcal/g × 4.184 = 37.66 ≈ 37.7 MJ/kg; Protein 4.0 kcal/g × 4.184 = 16.74 ≈ 16.7 MJ/kg; CHO 4.0 kcal/g × 4.184 = 16.74 ≈ 16.7 MJ/kg.

**Important distinction between GE and ME factors:** The GE values in the left column represent the total heat of combustion measured by bomb calorimetry. The ME values in the right column represent the Atwater general factors, which account for digestive and metabolic losses. The most commonly confused pair is fat: GE = 39.3 MJ/kg (total energy upon combustion) vs. ME = 37.7 MJ/kg (Atwater general factor, 9.0 kcal/g × 4.184 kJ/kcal). For energy allocation, the GE column is the correct one — we are measuring the total physical energy content, not the biologically available energy.

### 5.2 Composition Data Sources for GE Ranges

For the compositional uncertainty propagation used to derive GE ranges (Section 7), composition data are sourced from standard references:

- **NRC (2012)** *Nutrient Requirements of Swine*, 11th rev. ed. — feed ingredient composition tables
- **FAO Feedipedia** (www.feedipedia.org)
- **USDA National Nutrient Database** (SR28 / FoodData Central)
- **ECOINVENT v3.9** agricultural co-product datasets
- **Peer-reviewed literature** (cited per product)

Each composition fraction is assigned a **(minimum, midpoint, maximum)** range based on the observed variability across these sources.

### 5.3 Quality Classification

| Quality Level | Criteria | Typical Uncertainty |
|--------------|----------|-------------------|
| **High** | GE measured by bomb calorimetry in INRAE-CIRAD-AFZ with n ≥ 20 | ±3–5% |
| **Medium** | GE measured by bomb calorimetry with n ≥ 5, or calculated from well-characterized composition | ±5–10% |
| **Low** | GE estimated from similar products or limited composition data | ±10–15% |

---

## 6. GE Midpoints — Literature Sources

### 6.1 Reference Hierarchy

The GE midpoint (mode of the PERT distribution) for each co-product is taken from the following reference hierarchy:

| Priority | Source | Use Case |
|----------|--------|----------|
| 1 | INRAE-CIRAD-AFZ Feed Tables (Sauvant et al. 2004; feedtables.com) | Primary GE values (bomb calorimetry) |
| 2 | NRC (2012) *Nutrient Requirements of Swine*, 11th rev. ed. — feed ingredient composition tables | Feed-grade co-products |
| 3 | FAO Feedipedia (www.feedipedia.org) | Supplementary feed data |
| 4 | USDA National Nutrient Database (SR28 / FoodData Central) | Food-grade products |
| 5 | CRC Handbook of Chemistry & Physics | Pure substances (ethanol, sucrose, cellulose) |
| 6 | Peer-reviewed literature (cited per product) | Specialized products |

**Supplementary:** ECOINVENT v3.9 dataset documentation is used as a consistency check only, not as a primary GE source. ECOINVENT GE values are often derived from the same underlying databases (INRAE-CIRAD-AFZ, NRC) and should not be treated as independent measurements.

### 6.2 GE Midpoint Table

All values in MJ/kg DM (dry matter basis).

| Crop System | Co-product | GE (MJ/kg DM) | Source |
|---|---|---|---|
| **Soybean (Crushing)** | Soybean oil | 39.3 | INRAE-CIRAD-AFZ (n=9) |
|  | Soybean meal (48%) | 19.7 | INRAE-CIRAD-AFZ (n=136) |
|  | Soybean hulls | 18.1 | INRAE-CIRAD-AFZ (n=8–12) |
| **Canola (Crushing)** | Canola oil | 39.3 | INRAE-CIRAD-AFZ |
|  | Canola meal | 19.7 | INRAE-CIRAD-AFZ |
| **Flaxseed (Crushing)** | Linseed oil | 39.3 | INRAE-CIRAD-AFZ |
|  | Linseed meal | 19.5 | INRAE-CIRAD-AFZ |
| **Sunflower (Crushing)** | Sunflower oil | 39.3 | INRAE-CIRAD-AFZ |
|  | Sunflower meal | 19.4 | Feedipedia |
|  | Sunflower hulls | 20.1 | INRAE-CIRAD-AFZ |
| **Safflower (Crushing)** | Safflower oil | 39.3 | INRAE-CIRAD-AFZ |
|  | Safflower meal | 19.0 | NRC 2012; FAO Feedipedia |
| **Wheat (Flour Milling)** | Wheat flour | 18.3 | INRAE-CIRAD-AFZ |
|  | Wheat bran | 18.9 | INRAE-CIRAD-AFZ (n=65) |
|  | Wheat middlings | 19.2 | INRAE-CIRAD-AFZ |
| **Wheat (Dry-Grind Ethanol)** | Fuel ethanol | 29.7 | Physical constant |
|  | Wheat DGS | 20.3 | INRAE-CIRAD-AFZ / Cozannet et al. |
| **Corn (Wet Milling)** | Corn starch | 17.5 | INRAE-CIRAD-AFZ |
|  | Corn gluten meal | 23.9 | INRAE-CIRAD-AFZ |
|  | Corn gluten feed | 18.8 | Feedipedia (n=28) |
|  | Corn germ | 28.9 | NRC 2012; FAO Feedipedia |
|  | Corn steep liquor | 17.5 | Calculated from composition |
| **Corn (Dry Milling)** | Corn meal & grits | 18.6 | INRAE-CIRAD-AFZ |
|  | Hominy feed | 18.7 | Feedipedia (n=8) |
|  | Corn germ (dry) | 28.9 | NRC 2012; FAO Feedipedia |
| **Corn (Dry-Grind Ethanol)** | Fuel ethanol | 29.7 | Physical constant |
|  | Distillers grains (total) | 21.4 | Feedipedia / INRAE-CIRAD-AFZ |
|  | Corn oil (post-ferm) | 39.3 | INRAE-CIRAD-AFZ |
| **Sweet Corn (Canning)** | Edible kernels | 18.3 | Estimated |
|  | Cannery waste silage | 17.5 | Estimated from composition; FAO Feedipedia |
| **Oat (Milling)** | Food oats | 19.5 | Feedipedia |
|  | Oat hulls | 18.4 | Feedipedia |
|  | Oat mill feed | 17.5 | Estimated from composition |
| **Almond (Hulling)** | Almond kernels | 30.7 | Feedipedia |
|  | Almond hulls | 17.0 | Estimated from composition |
|  | Almond shells | 19.5 | Research literature |
| **Potato (Processing)** | Processed potato products | 17.5 | INRAE-CIRAD-AFZ |
|  | Potato processing waste | 16.5 | Estimated |
| **Citrus (Processing)** | Citrus juice | 16.5 | Calculated from USDA composition |
|  | Citrus pulp (wet) | 17.6 | INRAE-CIRAD-AFZ (n=21) |
| **Sugar Beet (Processing)** | Refined sugar | 16.5 | Physical constant |
|  | Beet pulp (wet) | 17.1 | INRAE-CIRAD-AFZ |
|  | Beet molasses | 14.5 | Estimated |
| **Sugarcane (Milling)** | Raw sugar | 16.0 | Calculated |
|  | Cane molasses | 14.7 | Feedipedia |
| **Cotton (Ginning → Crushing)** | Cotton lint | 17.5 | CRC Handbook (cellulose HHV) |
|  | Whole cottonseed | 23.8 | INRAE-CIRAD-AFZ |
|  | Cottonseed oil | 39.3 | INRAE-CIRAD-AFZ |
|  | Cottonseed meal | 20.0 | Feedipedia |
|  | Cottonseed hulls | 19.8 | Feedipedia |
|  | Cottonseed linters | 17.5 | NBS bomb calorimetry (pure cellulose); CRC Handbook |
| **Rice (Hulling → Milling)** | Brown rice | 18.1 | Derived from milled product composition |
|  | Rice hulls | 16.3 | Feedipedia |
|  | White rice | 18.0 | Feedipedia |
|  | Rice bran | 20.5 | Feedipedia (n=2) |
|  | Rice mill feed | 16.5 | Estimated from composition; FAO Feedipedia |
| **Barley (Malting → Brewing)** | Malt | 19.5 | Estimated from barley grain proxy |
|  | Malt sprouts | 18.4 | INRAE-CIRAD-AFZ / Feedipedia |
|  | Beer | 22.7 | Calculated from composition |
|  | Brewers spent grain | 20.0 | INRAE-CIRAD-AFZ / Feedipedia |
| **Peanut (Shelling → Crushing)** | Shelled kernels | 29.3 | Feedipedia |
|  | Peanut hulls | 19.8 | Feedipedia (n=4) |
|  | Peanut oil | 39.3 | INRAE-CIRAD-AFZ |
|  | Peanut meal | 20.0 | Feedipedia (n=6) |

---

## 7. GE Uncertainty Range — Compositional Propagation Method

### 7.1 Rationale

GE is not an arbitrary parameter — it is a calculable property of a product's composition. The standard proximate composition formula relates GE to four energy-containing fractions:

**GE = (CP × 23.6) + (CF × 39.3) + (CHO × 17.5) + (CFiber × 17.5)** MJ/kg DM

Where:
- **CP** = Crude Protein fraction (DM basis), energy coefficient 23.6 MJ/kg
- **CF** = Crude Fat / Oil fraction (DM basis), energy coefficient 39.3 MJ/kg
- **CHO** = Nitrogen-Free Extract / Carbohydrate fraction (DM basis), energy coefficient 17.5 MJ/kg
- **CFiber** = Crude Fiber fraction (DM basis), energy coefficient 17.5 MJ/kg

The energy coefficients are heats of combustion for the four proximate fractions, as used in NRC (2012) and in ECOINVENT v3 dataset documentation. (ISO 9831:1998 and EN 14918:2009, cited in Section 2, specify how GE is *measured* by bomb calorimetry; they are not the source of these coefficients.)

Since GE is determined by composition, GE uncertainty is entirely driven by **variability in composition fractions**. This variability is well-documented in feed composition databases and reflects cultivar differences, growing conditions, and processing methods.

### 7.2 Baseline Range Calculation

The baseline GE range is calculated as:

- **GE_lo** = (CP_min × 23.6) + (CF_min × 39.3) + (CHO_min × 17.5) + (CFiber_min × 17.5)
- **GE_hi** = (CP_max × 23.6) + (CF_max × 39.3) + (CHO_max × 17.5) + (CFiber_max × 17.5)

This is a **conservative independent-bounds approach**: each fraction is independently set to its lower bound for GE_lo and upper bound for GE_hi. This gives the widest plausible GE range consistent with documented compositional variability.

### 7.3 Key Principle: Midpoint from Literature, Range from Composition

The GE midpoint (PERT mode) comes from **literature review** — bomb calorimetry measurements, database-reported GE values, and published reference values (Section 6).

The GE range (PERT min/max) comes from **compositional uncertainty propagation** as described above.

The compositionally-calculated GE midpoint will generally **not exactly match** the literature GE midpoint, because:
1. The proximate composition formula is an approximation that does not capture all energy-containing components (e.g., organic acids, lignin, ethanol)
2. Composition data may not perfectly represent the specific product variant described in the literature
3. Bomb calorimetry measures total heat release directly, including contributions from minor components not captured in the CP/CF/CHO/CFiber framework

The delta between the compositionally-calculated midpoint and the literature midpoint (`comp_mid − GE_lit`) serves as a diagnostic of formula approximation error. For most products, this delta is between −2 and +1 MJ/kg. Products with larger deltas indicate systematic formula limitations that require correction (Section 7.5).

Therefore, the literature midpoint should be used as the PERT mode, and only the **range bounds** should be taken from the compositional analysis.

### 7.4 PERT-Validity Requirement

The PERT distribution requires **GE_lo ≤ GE_lit ≤ GE_hi** (min ≤ mode ≤ max). When the baseline composition-derived range violates this condition, a range correction is applied. These corrections address known systematic limitations of the 4-coefficient Atwater formula. Seven correction types are defined below.

### 7.5 PERT-Validity Corrections

#### 7.5.1a Half-Mirror Correction (Lignin Effect)

**Applies to**: Sunflower hulls, Cottonseed hulls, Peanut hulls, Almond shells

**Problem**: The 4-coefficient formula uses CFiber × 17.5 MJ/kg, but hulls and shells contain significant lignin (~15–30% of DM) with a gross energy of approximately 25–27 MJ/kg (Van Soest 1967; NRC 2001 p.12). The formula systematically underestimates GE for lignin-rich materials, causing the composition-derived GE_hi to fall below the literature midpoint.

**Correction**: GE_hi = GE_lit + 0.5 × (GE_lit − GE_lo_comp)

This half-mirror extension preserves the compositionally-derived uncertainty on the valid (lower) side while acknowledging the formula's systematic upper-bound bias. The factor of 0.5 (rather than 1.0 for a full mirror) is chosen because it acknowledges the formula underestimates these materials without overclaiming how high GE can go — a full mirror would produce physically implausibly wide ranges that would dominate the Monte Carlo uncertainty unrealistically.

**Physical cap**: For products where the half-mirror produces GE_hi values exceeding the published upper bound for lignocellulosic materials in Feedipedia (~21.5 MJ/kg DM), a cap is applied. Currently, peanut hulls is the only product requiring this cap.

**Note**: Sunflower hulls (GE_hi = 22.9), cottonseed hulls (GE_hi = 22.5), and almond shells (GE_hi = 22.4) also exceed 21.5 MJ/kg. These products retain their half-mirror values because Feedipedia reports individual GE values for these specific hulls above 21.5 MJ/kg (unlike peanut hulls, where the Feedipedia maximum is 21.5). The cap is applied per-product based on available literature bounds, not as a universal ceiling.

**Citation basis**: Van Soest PJ (1967) Development of a comprehensive system of feed analyses and its application to forages. J Anim Sci 26:119–128; NRC (2001) Nutrient Requirements of Dairy Cattle, 7th rev ed, p.12.

#### 7.5.1b Half-Mirror Correction (Zero Upper Tail)

**Applies to**: Peanut meal, Malt

**Problem**: For these products, the composition-derived GE_hi equals GE_lit exactly, producing a zero upper tail that crashes the PERT sampler (mode = max). The composition-derived midpoint matches the literature value, but the lack of an upper tail prevents valid PERT sampling.

**Correction**: GE_hi = GE_lit + 0.5 × (GE_lit − GE_lo_comp)

The same half-mirror formula is applied, but for a different reason: not lignin underestimation, but the mathematical artifact of composition-derived GE_hi coinciding exactly with GE_lit. The factor of 0.5 provides a conservative upper extension that reflects the uncertainty in the compositional data without overclaiming.

#### 7.5.2 Literature-Anchored Correction (Corn Gluten Meal)

**Applies to**: Corn gluten meal

**Problem**: CGM has ~60%+ crude protein content, and bomb calorimetry consistently returns 23–25 MJ/kg for such concentrated protein fractions. The Atwater formula substantially underestimates CGM's GE (comp_mid = 20.1 vs. GE_lit = 23.9, delta = −3.8 MJ/kg) because it does not capture residual lipids associated with the zein protein fraction. The composition-derived range does not bracket the literature midpoint at all.

**Correction**: The range is fully literature-anchored from Feedipedia bomb calorimetry data (n=12 studies, range 22.4–25.1 MJ/kg DM). No formula dependence.

PERT(22.4, 23.9, 25.1) — fully literature-based, no compositional approximation.

**Citation basis**: FAO Feedipedia, Corn gluten meal, bomb calorimetry values.

#### 7.5.3 Minimal Buffer Correction

**Applies to**: Corn gluten feed

**Problem**: The composition-derived GE_hi is within rounding error of the literature midpoint, falling only 0.2 MJ/kg below it. This is not a systematic formula limitation but rather a minor rounding/aggregation discrepancy.

**Correction**: GE_hi = GE_lit + 0.3 MJ/kg (minimal buffer above the literature midpoint). This ensures a nonzero upper tail for the PERT distribution while staying within the range of documented variability.

PERT(14.8, 18.8, 19.1)

#### 7.5.4 Impurity Correction (Raw Sugar)

**Applies to**: Raw sugar

**Problem**: Raw/centrifugal sugar (~97–99% sucrose) has lower GE than the formula predicts for pure carbohydrate because of moisture content (0.3–0.8%) and ash (0.1–0.5%). The formula treats all CHO at 17.5 MJ/kg, but the effective energy density is reduced by these non-energy components. This results in a composition-derived GE_lo that exceeds the literature midpoint, violating PERT validity.

**Correction**: GE_lo = GE_lit − 0.5 MJ/kg; GE_hi = composition-derived upper bound. The 0.5 MJ/kg buffer below the literature midpoint accounts for measurement uncertainty in bomb calorimetry of impure materials.

PERT(15.5, 16.0, 17.1)

**Citation basis**: NRC (2012); FAO Feedipedia; ICUMSA standards for raw/centrifugal sugar.

#### 7.5.5 Formula Overestimate Correction (Corn Steep Liquor)

**Applies to**: Corn steep liquor

**Problem**: CSL contains significant lactic acid (produced during steeping), organic acids, and mineral salts that are not captured by the Atwater 4-coefficient framework. The formula overestimates CSL's GE by +1.5 MJ/kg (comp_mid = 19.0 vs. GE_lit = 17.5). The composition-derived range (17.1–20.9) places GE_lit near the very bottom, producing a heavily right-skewed PERT distribution with most of its mass above the literature midpoint — which is not physically realistic.

**Correction**: Cap GE_hi at the composition midpoint (19.0) rather than the composition upper bound. This acknowledges that the formula itself overestimates, so the upper bound from the formula is not trustworthy. Keep GE_lo from composition (17.1), which is a valid lower bound.

PERT(17.1, 17.5, 19.0)

**Citation basis**: Calculated from composition; NRC (2012); FAO Feedipedia.

#### 7.5.6 Literature Cap Correction (Beet Molasses)

**Applies to**: Beet molasses

**Problem**: Beet molasses has significant ash content (8–12% DM) and organic salts (betaine, etc.) that lower GE well below what the CHO coefficient predicts. The composition-derived GE_hi exceeds the GE of pure sucrose (16.5 MJ/kg), which is physically impossible for a material that is ~70% sugar plus 10% ash.

**Correction**: Cap GE_hi at the published Feedipedia maximum for beet molasses (15.5 MJ/kg DM, n=8 studies, reported range 13.5–15.5). Keep GE_lo from composition (13.9).

PERT(13.9, 14.5, 15.5)

**Citation basis**: FAO Feedipedia, Beet molasses, n=8 bomb calorimetry studies.

#### 7.5.7 Minimal Extension Correction (Citrus Pulp)

**Applies to**: Citrus pulp (wet)

**Problem**: The composition-derived GE_hi equals the literature midpoint exactly, producing a zero upper tail that crashes the PERT sampler (mode = max).

**Correction**: GE_hi = GE_lit + 0.4 MJ/kg, reflecting batch-to-batch variation in peel:pulp ratio which affects fiber content and hence GE. The 0.4 MJ/kg extension is conservative and consistent with the variability observed in FAO Feedipedia citrus pulp data.

PERT(13.6, 17.6, 18.0)

### 7.6 Correction Summary Table

| Product | Correction Type | PERT(min, mode, max) | Rationale |
|---|---|---|---|
| Sunflower hulls | Half-mirror (lignin) | (14.5, 20.1, 22.9) | Lignin effect; Section 7.5.1a |
| Cottonseed hulls | Half-mirror (lignin) | (14.5, 19.8, 22.5) | Lignin effect; Section 7.5.1a |
| Peanut hulls | Half-mirror (lignin) + cap | (13.6, 19.8, 21.5) | Lignin effect; capped at Feedipedia lignocellulosic ceiling; Section 7.5.1a |
| Almond shells | Half-mirror (lignin) | (13.8, 19.5, 22.4) | Lignin effect; Section 7.5.1a |
| Peanut meal | Half-mirror (zero upper tail) | (17.2, 20.0, 21.4) | Composition-derived GE_hi = GE_lit; zero upper tail (Section 7.5.1b) |
| Malt | Half-mirror (zero upper tail) | (17.6, 19.5, 20.4) | Composition-derived GE_hi = GE_lit; zero upper tail (Section 7.5.1b) |
| Corn gluten meal | Literature-anchored | (22.4, 23.9, 25.1) | Feedipedia bomb calorimetry n=12 |
| Corn gluten feed | Minimal buffer | (14.8, 18.8, 19.1) | GE_hi within rounding error; +0.3 buffer |
| Raw sugar | Impurity | (15.5, 16.0, 17.1) | Moisture/ash lower effective GE |
| Corn steep liquor | Formula overestimate | (17.1, 17.5, 19.0) | Lactic acid/minerals; cap at comp_mid |
| Beet molasses | Literature cap | (13.9, 14.5, 15.5) | Feedipedia n=8 range 13.5–15.5 |
| Citrus pulp (wet) | Minimal extension | (13.6, 17.6, 18.0) | Zero upper tail; +0.4 for peel:pulp variation |

### 7.7 Composition Data and Reproducibility

The GE_lo and GE_hi values produced by this method, after all Section 7.5 corrections, are listed in full in **Section 11**. Every product satisfies the PERT validity condition GE_lo ≤ GE_lit ≤ GE_hi, and the six half-mirror corrections reproduce exactly from the formula in Section 7.5.1.

The Section 11 triples are carried verbatim into the companion Monte Carlo script `monte_carlo_uncertainty_v11.py`, which is the executable reference implementation for the uncertainty propagation.

---

## 8. Special Cases

### 8.1 Vegetable Oils

All refined vegetable oils (soybean, canola, linseed, sunflower, safflower, cottonseed, peanut, corn oil) are >99% triglyceride. Compositional variation is negligible. GE range is set to **(38.5, 40.0) MJ/kg** to account for measurement uncertainty, minor FFA content variation, and unsaturation degree differences, rather than being derived from composition.

The INRAE-CIRAD-AFZ tables report GE = 39.3 MJ/kg DM for soybean oil (n = 9).

> **Note on GE vs. LHV vs. ME for vegetable oils:** Three different energy values are commonly reported for vegetable oils, and these are frequently confused. **GE/HHV = 39.3 MJ/kg** (total heat from complete combustion, including latent heat of water condensation; confirmed by INRAE-CIRAD-AFZ and bomb calorimetry). **LHV ≈ 37.0–37.5 MJ/kg** (HHV minus latent heat of water vaporization; engineering/combustion metric). **ME ≈ 37.7 MJ/kg** (Atwater general factor for fat, 9.0 kcal/g × 4.184 kJ/kcal; nutrition labeling metric). The value 37.0–37.7 MJ/kg is sometimes erroneously cited as "gross energy" but is actually LHV or ME. For LCA co-product allocation, GE/HHV (39.3 MJ/kg) is the correct metric.

### 8.2 Fuel Ethanol

GE = **29.7 MJ/kg** (HHV of pure ethanol, C2H5OH). This is a physical constant with no compositional variation. PERT distribution is degenerate: (29.7, 29.7, 29.7).

**Important**: The proximate composition formula does NOT apply to ethanol. Using the CHO coefficient (17.5 MJ/kg) for ethanol would underestimate its energy content by approximately 41%.

### 8.3 Refined Sugar

GE ≈ **16.5 MJ/kg** (HHV of sucrose, C12H22O11). Essentially pure (>99.5% CHO) with negligible variation. PERT distribution: (16.4, 16.5, 16.6).

### 8.4 Beer

GE = **22.7 MJ/kg DM**, range (22.0, 23.9).

Beer is the only co-product in this review whose dry matter is largely ethanol, and the proximate composition formula cannot be applied to it: that formula would treat the ethanol as carbohydrate at 17.5 MJ/kg and understate the energy content by about a third. Beer's GE is instead built from its components, using ethanol's heat of combustion directly:

```
GE_DM = [(ethanol_wt% × 29.7) + (extract_wt% × 17.5) + (protein_wt% × 23.6)] ÷ DM_wt%
```

At the 8.5% DM used in the barley methodology document and in the Monte Carlo model — roughly 3.9% ethanol by weight at 5% ABV, 4.0% residual extract and 0.5% protein and ash:

```
GE_DM = [(0.039 × 29.7) + (0.040 × 17.5) + (0.003 × 23.6)] ÷ 0.085 = 22.7 MJ/kg DM
```

Ethanol makes up about 46% of beer's dry matter on this basis, which is why beer DM has a higher GE (22.7) than the barley it came from (19.5 MJ/kg DM).

**Range.** The bounds come from the span of normal beer strengths, 4–6% ABV, with residual extract moving in the opposite direction as more of it ferments:

| Case | ABV | Ethanol (w/w) | Residual extract | DM | GE (MJ/kg DM) |
|------|-----|---------------|------------------|-----|---------------|
| Low  | 4% | 3.1% | 4.5% | 8.1% | **22.0** |
| Adopted | 5% | 3.9% | 4.0% | 8.5% | **22.7** |
| High | 6% | 4.7% | 3.5% | 8.7% | **23.9** |

> **Note on beer DM and original gravity:** These are not the same quantity and are easily confused. A 12°P wort carries 12% dissolved solids *before* fermentation; roughly two-thirds of that extract is converted to ethanol and CO₂, and the CO₂ leaves the system. Finished beer is about 8.5% DM, not 12%. Substituting original gravity for beer DM overstates beer's dry matter by about 40% and dilutes the ethanol fraction of the DM from ~46% to ~26%, which depresses the calculated GE to about 20.5 MJ/kg DM. That substitution is the reason a value of 20.5 appears in some sources; it is not used here.

---

## 9. Gross Energy Values by Co-Product Category

### 9.1 Vegetable Oils

All vegetable oils are triglycerides with nearly identical GE values. The INRAE-CIRAD-AFZ tables report GE = 39.3 MJ/kg DM for soybean oil (n = 9).

| Co-product | GE Midpoint (MJ/kg DM) | Range (GE_lo–GE_hi) | Source | Quality |
|------------|----------------------|-------|--------|---------|
| Soybean oil | 39.3 | 38.5–40.0 | INRAE-CIRAD-AFZ (n=9) | High |
| Canola/rapeseed oil | 39.3 | 38.5–40.0 | INRAE-CIRAD-AFZ | High |
| Sunflower oil | 39.3 | 38.5–40.0 | INRAE-CIRAD-AFZ | High |
| Safflower oil | 39.3 | 38.5–40.0 | INRAE-CIRAD-AFZ | High |
| Linseed/flaxseed oil | 39.3 | 38.5–40.0 | INRAE-CIRAD-AFZ | High |
| Cottonseed oil | 39.3 | 38.5–40.0 | INRAE-CIRAD-AFZ | High |
| Peanut oil | 39.3 | 38.5–40.0 | INRAE-CIRAD-AFZ | High |
| Corn oil | 39.3 | 38.5–40.0 | INRAE-CIRAD-AFZ | High |

### 9.2 Oilseed Meals (Solvent-Extracted)

| Co-product | GE Midpoint (MJ/kg DM) | Range (GE_lo–GE_hi) | Source | Quality |
|------------|----------------------|-------|--------|---------|
| Soybean meal (48% CP, solvent) | 19.7 | 16.3–20.2 | INRAE-CIRAD-AFZ (n=136) | High |
| Canola/rapeseed meal | 19.7 | 16.1–21.2 | INRAE-CIRAD-AFZ | High |
| Cottonseed meal (low fibre, solvent) | 20.0 | 15.8–20.2 | Feedipedia | High |
| Sunflower meal (dehulled, solvent) | 19.4 | 14.3–21.8 | Feedipedia | High |
| Safflower meal (non-dehulled, solvent) | 19.0 | 14.7–20.9 | NRC 2012; FAO Feedipedia | High |
| Linseed/flaxseed meal | 19.5 | 15.9–22.8 | INRAE-CIRAD-AFZ | High |
| Peanut meal (solvent) | 20.0 | 17.2–21.4 | Feedipedia (n=6) | High |

> **Note on soybean meal GE by protein grade:** INRAE-CIRAD-AFZ differentiates soybean meal by protein content: 48% CP (dehulled) = 19.7 MJ/kg DM (n=136); 46% CP (non-dehulled) = 19.5 MJ/kg DM (n=16); 50% CP = 19.7 MJ/kg DM (n=20). This document uses 19.7 MJ/kg DM, specifying 48% CP solvent-extracted meal as the reference type.

> **Note on peanut meal range:** The composition-derived GE_hi equals GE_lit exactly, producing a zero upper tail. The half-mirror correction extends GE_hi to 21.4 MJ/kg (Section 7.5.1b).

### 9.3 Hulls and Fibrous By-Products

| Co-product | GE Midpoint (MJ/kg DM) | Range (GE_lo–GE_hi) | Source | Quality |
|------------|----------------------|-------|--------|---------|
| Soybean hulls | 18.1 | 15.4–19.9 | INRAE-CIRAD-AFZ (n=8–12) | High |
| Sunflower hulls | 20.1 | 14.5–22.9 | INRAE-CIRAD-AFZ | High |
| Peanut hulls | 19.8 | 13.6–21.5 | Feedipedia (n=4) | Medium |
| Cottonseed hulls | 19.8 | 14.5–22.5 | Feedipedia | High |
| Cottonseed linters | 17.5 | 15.9–18.2 | NBS bomb calorimetry (pure cellulose); CRC Handbook | Medium |
| Oat hulls | 18.4 | 14.5–19.2 | Feedipedia | High |
| Rice hulls | 16.3 | 13.8–18.2 | Feedipedia | High |
| Almond hulls | 17.0 | 14.5–18.8 | Estimated from composition | Medium |
| Almond shells | 19.5 | 13.8–22.4 | Research literature | Medium |

> **Note on sunflower hulls:** Sunflower hulls have a surprisingly high GE (20.1 MJ/kg DM) for a fibrous by-product, due to residual oil (~3–5%) and high lignin content (GE ~25 MJ/kg DM). The half-mirror correction (Section 7.5.1a) extends GE_hi from the composition-derived value to 22.9 MJ/kg to account for the lignin effect.

> **Note on rice hulls:** Rice hulls have the lowest GE of any co-product in this review (16.3 MJ/kg DM) because they contain ~17–20% silica (SiO₂), which is completely non-combustible.

> **Note on peanut hulls:** The half-mirror correction produces GE_hi = 22.9, which exceeds the published upper bound for lignocellulosic materials in Feedipedia (~21.5 MJ/kg DM). GE_hi is capped at 21.5 per the Feedipedia lignocellulosic ceiling (Section 7.5.1a).

### 9.4 Cereal Grains and Flours

| Co-product | GE Midpoint (MJ/kg DM) | Range (GE_lo–GE_hi) | Source | Quality |
|------------|----------------------|-------|--------|---------|
| Wheat flour (all-purpose) | 18.3 | 17.0–18.7 | INRAE-CIRAD-AFZ | High |
| Wheat bran | 18.9 | 15.9–20.1 | INRAE-CIRAD-AFZ (n=65) | High |
| Wheat middlings | 19.2 | 15.8–19.6 | INRAE-CIRAD-AFZ | High |
| White rice (head rice) | 18.0 | 17.0–18.4 | Feedipedia | High |
| Rice bran | 20.5 | 17.3–23.4 | Feedipedia (n=2) | Medium |
| Rice mill feed | 16.5 | 14.4–19.8 | Estimated from composition; FAO Feedipedia | Medium |
| Brown rice (intermediate) | 18.1 | 17.0–18.8 | Derived from milled product composition | Medium |
| Malt (brewers, intermediate) | 19.5 | 17.6–20.4 | Estimated from barley grain proxy | Medium |
| Food oats (oat groats) | 19.5 | 16.6–20.6 | Feedipedia | High |
| Oat mill feed | 17.5 | 14.4–18.9 | Estimated from composition | Medium |
| Corn meal & grits | 18.6 | 16.9–18.7 | INRAE-CIRAD-AFZ | High |
| Hominy feed | 18.7 | 14.1–19.0 | Feedipedia (n=8) | High |
| Edible sweet corn kernels | 18.3 | 16.9–18.6 | Estimated | Medium |

> **Note on brown rice (intermediate):** Brown rice is the intermediate product of the rice hulling stage, comprising the inner white rice, bran, and germ layers with the hull removed. It is not a traded commodity with published GE data. Its GE (18.1 MJ/kg DM) is derived as the DM-weighted average of its constituent milled products. At the rice methodology document's Stage 2 DM outputs (white rice 0.5720, bran 0.0712, mill feed 0.0445 t/t rough rice, totalling 0.6877), the shares are white rice **83.2%**, bran **10.4%** and mill feed **6.5%**, giving 0.832 × 18.0 + 0.104 × 20.5 + 0.065 × 16.5 = **18.2 MJ/kg DM**. The adopted 18.1 sits within rounding of that, so the total energy of brown rice is consistent with the sum of the energies of its milled products. This GE value is used only for Stage 1 energy allocation in the rice cascade.

> **Note on malt (intermediate):** Malt is the intermediate product of the barley malting stage, produced by steeping, germinating, and kilning barley grain. It is not typically listed in feed GE tables as a standalone ingredient. Its GE (19.5 MJ/kg DM) is estimated from the parent barley grain GE (~19.5 MJ/kg DM from INRAE-CIRAD-AFZ), as malting does not significantly alter the total energy content: the germination process converts some starch to sugars and produces CO₂ and water vapor, but the remaining DM retains essentially the same caloric value per unit mass. The 5.1% DM loss during malting (0.045 t on a 0.880 t DM input, to respiration) reduces total DM output but not the GE per kg of remaining DM. This GE value is used only for Stage 1 energy allocation in the barley cascade. The half-mirror correction extends GE_hi to 20.4 (Section 7.5.1b).

> **Note on rice mill feed:** Rice mill feed is a mixture of rice bran, hulls, and broken rice that is lower in quality than pure rice bran. Its GE (16.5 MJ/kg DM) is closer to rice hulls (16.3) than to rice bran (20.5) because the hull fraction dominates in typical mill feed.

### 9.5 Corn Wet-Milling By-Products

| Co-product | GE Midpoint (MJ/kg DM) | Range (GE_lo–GE_hi) | Source | Quality |
|------------|----------------------|-------|--------|---------|
| Corn starch | 17.5 | 17.3–17.7 | INRAE-CIRAD-AFZ | High |
| Corn gluten meal (60% CP) | 23.9 | 22.4–25.1 | INRAE-CIRAD-AFZ | High |
| Corn gluten feed (dry) | 18.8 | 14.8–19.1 | Feedipedia (n=28) | High |
| Corn germ (whole, wet milling) | 28.9 | 22.9–29.5 | NRC 2012; FAO Feedipedia | High |
| Corn steep liquor | 17.5 | 17.1–19.0 | Calculated from composition | Medium |

> **Note on corn germ (whole vs. meal):** The corn germ in wet milling is the whole germ before oil extraction, containing ~45–50% fat. Its GE (28.9 MJ/kg DM) is much higher than corn germ meal (~19.4 MJ/kg DM), which is the defatted residue after oil extraction. The economic and mass allocation methodology documents list "Corn germ" (whole) as the co-product, so the whole-germ GE is used.

> **Note on corn steep liquor:** Corn steep liquor is a concentrated liquid by-product of the corn steeping process. Its composition (~46% CP, ~25% lactic acid, ~10% ash on DM) gives it a relatively low GE of ~17.5 MJ/kg DM. The high lactic acid content (GE ~14.9 MJ/kg, against 17.5 for carbohydrate) and high ash content depress the GE relative to other corn co-products. The formula overestimate correction caps GE_hi at 19.0 (Section 7.5.5).

> **Note on corn gluten meal:** CGM's range is fully literature-anchored from Feedipedia bomb calorimetry (n=12, range 22.4–25.1 MJ/kg DM), as the Atwater formula cannot capture residual lipid energy in the zein protein fraction (Section 7.5.2).

> **Note on corn gluten feed:** The composition-derived GE_hi is within rounding error of GE_lit. A minimal buffer of +0.3 extends GE_hi to 19.1 (Section 7.5.3).

### 9.6 Fermentation and Ethanol Products

| Co-product | GE Midpoint (MJ/kg DM) | Range (GE_lo–GE_hi) | Source | Quality |
|------------|----------------------|-------|--------|---------|
| Fuel ethanol (pure) | 29.7 | 29.7 (fixed) | Physical constant (HHV of ethanol) | High |
| Beer (5% ABV, 8.5% DM) | 22.7 | 22.0–23.9 | Calculated from composition | Medium |
| Distillers grains (total), corn | 21.4 | 17.2–22.3 | Feedipedia (n=32) / INRAE-CIRAD-AFZ (n=42) | High |
| Wheat DGS | 20.3 | 16.1–21.2 | INRAE-CIRAD-AFZ / Cozannet et al. | High |
| Brewers spent grain (dried) | 20.0 | 16.2–21.6 | INRAE-CIRAD-AFZ / Feedipedia | High |
| Malt sprouts | 18.4 | 16.1–20.0 | INRAE-CIRAD-AFZ / Feedipedia | High |

> **Note on DDGS vs. grain GE:** Both maize DDGS (21.4 MJ/kg DM) and wheat DGS (20.3 MJ/kg DM) have significantly higher GE than their parent grains (18.6 and ~18.0 MJ/kg DM respectively). This is because fermentation removes starch (GE ~17.5 MJ/kg DM) and concentrates the remaining fat and protein by ~3-fold. Maize DDGS has higher GE than wheat DGS because maize has higher oil content (~4.5% vs. ~2%).

### 9.7 High-Fat Whole Products (Seeds)

| Co-product | GE Midpoint (MJ/kg DM) | Range (GE_lo–GE_hi) | Source | Quality |
|------------|----------------------|-------|--------|---------|
| Almond kernels | 30.7 | 26.8–32.6 | Feedipedia | High |
| Peanut seeds / shelled kernels (intermediate) | 29.3 | 25.9–31.0 | Feedipedia | High |
| Whole cottonseed | 23.8 | 19.8–25.2 | INRAE-CIRAD-AFZ | High |

> **Note on peanut seeds / shelled kernels (intermediate):** Shelled peanut kernels are the intermediate product of the peanut shelling stage (Stage 1), produced by removing the hulls from in-shell peanuts. They are also the input to the crushing stage (Stage 2), where they are processed into peanut oil and peanut meal. Their GE (29.3 MJ/kg DM) is the Feedipedia measured value for whole peanut seeds (n ≥ 6, bomb calorimetry). This high GE reflects the kernels' ~47% oil content (fat GE = 39.3 MJ/kg). A derivation from the DM-weighted average of the Stage 2 products confirms it: at the peanut methodology document's Stage 2 DM outputs of 0.420 t oil and 0.475 t meal per tonne of kernels, (0.420 × 39.3 + 0.475 × 20.0) / 0.895 = **29.1 MJ/kg DM**, within 0.8% of the adopted 29.3. This GE value is used for Stage 1 energy allocation in the peanut cascade, analogous to brown rice in the rice cascade.

> **Note on whole cottonseed:** Whole cottonseed contains the kernel, hull and linters. Its GE (23.8 MJ/kg DM) reflects its ~18–22% oil content — lower than peanut kernels (~47%) or almond kernels (~50%), but well above hulls and meals. Unlike the intermediates of the three cascade crops, whole cottonseed is itself a marketed final product (dairy feed), and this GE is used for it as a final co-product under Pathway A. It is **not** used as a cascade intermediate: Pathway B places all five final products on one denominator (Section 10). For reference, the DM-weighted GE of the four crush products is 23.4 MJ/kg DM, within 1.7% of the seed's measured 23.8.

### 9.8 Sugar Products

| Co-product | GE Midpoint (MJ/kg DM) | Range (GE_lo–GE_hi) | Source | Quality |
|------------|----------------------|-------|--------|---------|
| Refined sugar (sucrose) | 16.5 | 16.4–16.6 | Bomb calorimetry (physical constant) | High |
| Raw sugar (~97% sucrose) | 16.0 | 15.5–17.1 | Calculated | Medium |
| Beet molasses | 14.5 | 13.9–15.5 | Estimated | Medium |
| Cane molasses | 14.7 | 13.7–15.5 | Feedipedia | High |

> **Note on raw sugar:** The impurity correction applies to raw sugar (Section 7.5.4). Moisture and ash content lower the effective GE below what the CHO coefficient predicts. GE_lo = 15.5 (GE_lit − 0.5) and GE_hi = 17.1 (composition-derived upper bound).

> **Note on beet molasses:** The literature cap correction applies (Section 7.5.6). Feedipedia reports a range of 13.5–15.5 MJ/kg DM (n=8 studies) for beet molasses, and GE_hi is capped at 15.5. The composition-derived GE_hi would exceed the GE of pure sucrose, which is physically impossible for a material containing significant ash.

### 9.9 Pulp and Processing By-Products

| Co-product | GE Midpoint (MJ/kg DM) | Range (GE_lo–GE_hi) | Source | Quality |
|------------|----------------------|-------|--------|---------|
| Beet pulp (wet or dry) | 17.1 | 14.9–18.6 | INRAE-CIRAD-AFZ | High |
| Citrus pulp (wet or dry) | 17.6 | 13.6–18.0 | INRAE-CIRAD-AFZ (n=21) | High |
| Citrus juice (DM basis) | 16.5 | 15.9–17.9 | Calculated from USDA composition | Medium |
| Cannery waste silage (sweet corn) | 17.5 | 13.5–18.1 | Estimated from composition; FAO Feedipedia | Medium |
| Processed potato products | 17.5 | 16.0–18.5 | INRAE-CIRAD-AFZ | High |
| Potato processing waste | 16.5 | 14.9–18.5 | Estimated | Medium |
| Cotton lint | 17.5 | 14.9–18.6 | CRC Handbook (cellulose HHV) | Medium |

> **Note on citrus pulp:** The minimal extension correction applies (Section 7.5.7). The composition-derived GE_hi equals the literature midpoint exactly, so GE_hi is extended by +0.4 to 18.0 MJ/kg to account for batch-to-batch peel:pulp variation.

---

## 10. Master GE Reference Table

The following table provides the complete set of GE values for all co-products in the LCA methodology series, organized by crop and processing system. This table is the reference for GE inputs used in energy allocation calculations.

**To calculate energy allocation:** Use the DM outputs from the crop-specific methodology documents together with the GE values from this table. Apply the formula in Section 3.1.

| Crop | Co-product | GE (MJ/kg DM) | Range (GE_lo–GE_hi) | Source | Quality |
|------|------------|---------------|-------|--------|---------|
| **Barley – Stage 1: Malting** | Malt (intermediate) | 19.5 | 17.6–20.4 | Estimated from barley grain proxy | Medium |
| | Malt sprouts | 18.4 | 16.1–20.0 | INRAE-CIRAD-AFZ / Feedipedia | High |
| **Barley – Stage 2: Brewing** | Beer | 22.7 | 22.0–23.9 | Calculated from composition | Medium |
| | Brewers spent grain (dried) | 20.0 | 16.2–21.6 | INRAE-CIRAD-AFZ / Feedipedia | High |
| **Corn (Wet Milling)** | Corn starch | 17.5 | 17.3–17.7 | INRAE-CIRAD-AFZ | High |
| | Corn gluten meal | 23.9 | 22.4–25.1 | INRAE-CIRAD-AFZ | High |
| | Corn gluten feed (dry) | 18.8 | 14.8–19.1 | Feedipedia (n=28) | High |
| | Corn germ (whole) | 28.9 | 22.9–29.5 | NRC 2012; FAO Feedipedia | High |
| | Corn steep liquor | 17.5 | 17.1–19.0 | Calculated from composition | Medium |
| **Corn (Dry Milling)** | Corn meal & grits | 18.6 | 16.9–18.7 | INRAE-CIRAD-AFZ | High |
| | Hominy feed | 18.7 | 14.1–19.0 | Feedipedia (n=8) | High |
| | Corn germ (whole) | 28.9 | 22.9–29.5 | NRC 2012; FAO Feedipedia | High |
| **Corn (Dry-Grind Ethanol)** | Fuel ethanol | 29.7 | 29.7 (fixed) | Physical constant | High |
| | Distillers grains (total) | 21.4 | 17.2–22.3 | Feedipedia / INRAE-CIRAD-AFZ | High |
| | Corn oil | 39.3 | 38.5–40.0 | INRAE-CIRAD-AFZ | High |
| **Sweet Corn (Canning)** | Edible kernels | 18.3 | 16.9–18.6 | Estimated | Medium |
| | Cannery waste silage | 17.5 | 13.5–18.1 | Estimated from composition; FAO Feedipedia | Medium |
| **Soybean (Crushing)** | Soybean oil | 39.3 | 38.5–40.0 | INRAE-CIRAD-AFZ (n=9) | High |
| | Soybean meal (48% protein) | 19.7 | 16.3–20.2 | INRAE-CIRAD-AFZ (n=136) | High |
| | Soybean hulls (whole) | 18.1 | 15.4–19.9 | INRAE-CIRAD-AFZ (n=8–12) | High |
| **Wheat (Flour Milling)** | Wheat flour (all-purpose) | 18.3 | 17.0–18.7 | INRAE-CIRAD-AFZ | High |
| | Wheat bran | 18.9 | 15.9–20.1 | INRAE-CIRAD-AFZ (n=65) | High |
| | Wheat middlings | 19.2 | 15.8–19.6 | INRAE-CIRAD-AFZ | High |
| **Wheat (Dry-Grind Ethanol)** | Fuel ethanol | 29.7 | 29.7 (fixed) | Physical constant | High |
| | Wheat DGS | 20.3 | 16.1–21.2 | INRAE-CIRAD-AFZ / Cozannet et al. | High |
| **Canola (Crushing)** | Canola oil (crude) | 39.3 | 38.5–40.0 | INRAE-CIRAD-AFZ | High |
| | Canola meal | 19.7 | 16.1–21.2 | INRAE-CIRAD-AFZ | High |
| **Flaxseed (Crushing)** | Linseed oil | 39.3 | 38.5–40.0 | INRAE-CIRAD-AFZ | High |
| | Linseed meal | 19.5 | 15.9–22.8 | INRAE-CIRAD-AFZ | High |
| **Sunflower (Crushing)** | Sunflower oil | 39.3 | 38.5–40.0 | INRAE-CIRAD-AFZ | High |
| | Sunflower meal (dehulled) | 19.4 | 14.3–21.8 | Feedipedia | High |
| | Sunflower hulls | 20.1 | 14.5–22.9 | INRAE-CIRAD-AFZ | High |
| **Safflower (Crushing)** | Safflower oil | 39.3 | 38.5–40.0 | INRAE-CIRAD-AFZ | High |
| | Safflower meal (non-dehulled) | 19.0 | 14.7–20.9 | NRC 2012; FAO Feedipedia | High |
| **Oat (Milling)** | Food oats | 19.5 | 16.6–20.6 | Feedipedia | High |
| | Oat hulls | 18.4 | 14.5–19.2 | Feedipedia | High |
| | Oat mill feed | 17.5 | 14.4–18.9 | Estimated from composition | Medium |
| **Rice – Stage 1: Hulling** | Brown rice (intermediate) | 18.1 | 17.0–18.8 | Derived from milled product composition | Medium |
| | Rice hulls | 16.3 | 13.8–18.2 | Feedipedia | High |
| **Rice – Stage 2: Milling** | White rice (head rice) | 18.0 | 17.0–18.4 | Feedipedia | High |
| | Rice bran | 20.5 | 17.3–23.4 | Feedipedia (n=2) | Medium |
| | Rice mill feed | 16.5 | 14.4–19.8 | Estimated from composition; FAO Feedipedia | Medium |
| **Peanut – Stage 1: Shelling** | Shelled kernels (intermediate) | 29.3 | 25.9–31.0 | Feedipedia | High |
| | Peanut hulls | 19.8 | 13.6–21.5 | Feedipedia (n=4) | Medium |
| **Peanut – Stage 2: Crushing** | Peanut oil | 39.3 | 38.5–40.0 | INRAE-CIRAD-AFZ | High |
| | Peanut meal | 20.0 | 17.2–21.4 | Feedipedia (n=6) | High |
| **Cotton – Stage 1: Ginning** | Cotton lint | 17.5 | 14.9–18.6 | CRC Handbook (cellulose HHV) | Medium |
| | Whole cottonseed | 23.8 | 19.8–25.2 | INRAE-CIRAD-AFZ | High |
| **Cotton – Stage 2: Cottonseed Crushing** | Cottonseed oil | 39.3 | 38.5–40.0 | INRAE-CIRAD-AFZ | High |
| | Cottonseed meal | 20.0 | 15.8–20.2 | Feedipedia | High |
| | Cottonseed hulls | 19.8 | 14.5–22.5 | Feedipedia | High |
| | Cottonseed linters | 17.5 | 15.9–18.2 | NBS bomb calorimetry (pure cellulose); CRC Handbook | Medium |
| **Potato (Processing)** | Processed potato products | 17.5 | 16.0–18.5 | INRAE-CIRAD-AFZ | High |
| | Potato processing waste | 16.5 | 14.9–18.5 | Estimated | Medium |
| **Citrus (Processing)** | Citrus juice | 16.5 | 15.9–17.9 | Calculated from USDA composition | Medium |
| | Citrus pulp (wet) | 17.6 | 13.6–18.0 | INRAE-CIRAD-AFZ (n=21) | High |
| **Sugar Beet (Processing)** | Refined sugar | 16.5 | 16.4–16.6 | Physical constant | High |
| | Beet pulp (wet) | 17.1 | 14.9–18.6 | INRAE-CIRAD-AFZ | High |
| | Beet molasses | 14.5 | 13.9–15.5 | Estimated | Medium |
| **Sugarcane (Milling)** | Raw sugar | 16.0 | 15.5–17.1 | Calculated | Medium |
| | Cane molasses | 14.7 | 13.7–15.5 | Feedipedia | High |
| **Almond (Hulling)** | Almond kernels | 30.7 | 26.8–32.6 | Feedipedia | High |
| | Almond hulls | 17.0 | 14.5–18.8 | Estimated from composition | Medium |
| | Almond shells | 19.5 | 13.8–22.4 | Research literature | Medium |

> **Note on cotton (two pathways, no cascade):** Cotton is **not** modelled as a cascade. Whole cottonseed is itself a marketed final product — a dairy feed with its own allocation factor — so its quoted price is the price in a competing end use, not a transfer price into crushing. The cotton methodology document therefore models two separate systems, and the Monte Carlo model implements both as single-stage blocks:
>
> - **Pathway A — "Cotton (Ginning — seed sold)":** two final products, cotton lint and whole cottonseed. Energy allocation **lint 36.5% / whole cottonseed 63.5%**.
> - **Pathway B — "Cotton (Ginning → Crushing)":** five final products on one seed cotton basis. Energy allocation **lint 37.1%, cottonseed oil 20.0%, meal 24.9%, hulls 14.6%, linters 3.5%**.
>
> A given tonne of seed follows one pathway or the other, so the two sets of factors are alternatives rather than a double count. For the economic method the direct end-of-chain calculation used here is algebraically identical to a cascade in which the seed is valued at its derived value; for the mass and energy methods the two differ slightly, because Stage 2 processing losses are attributed differently. The cotton methodology document gives the derivation.

> **Note on rice cascade:** Rice is modeled as a 2-stage cascade, consistent with the economic and mass allocation methodology. **Stage 1 (Hulling):** Rough rice is separated into brown rice (intermediate, GE = 18.1 MJ/kg DM) and rice hulls. **Stage 2 (Milling):** Brown rice is processed into white rice, rice bran, and rice mill feed. The energy allocation for each final milled product is calculated as: Stage 1 energy allocation (brown rice) × Stage 2 energy sub-share (individual product). The brown rice GE is derived from the DM-weighted average of its milled products to ensure mass-energy consistency.

> **Note on barley cascade:** Barley is modeled as a 2-stage cascade, consistent with the economic and mass allocation methodology. **Stage 1 (Malting):** Barley is processed into malt (intermediate, GE = 19.5 MJ/kg DM) and malt sprouts. **Stage 2 (Brewing):** Malt is fermented into beer and brewers spent grain. The energy allocation for each final product is calculated as: Stage 1 energy allocation (malt) × Stage 2 energy sub-share (individual product). The malt GE is estimated from the parent barley grain GE, as malting does not significantly alter the caloric value per unit of remaining DM.

> **Note on peanut cascade:** Peanut is modeled as a 2-stage cascade, consistent with the economic and mass allocation methodology. **Stage 1 (Shelling):** In-shell peanuts are separated into shelled kernels (intermediate, GE = 29.3 MJ/kg DM from Feedipedia) and peanut hulls. **Stage 2 (Crushing):** Shelled kernels are processed into peanut oil and peanut meal. The energy allocation for each final product is calculated as: Stage 1 energy allocation (shelled kernels) × Stage 2 energy sub-share (individual product). The shelled kernels GE (29.3 MJ/kg DM) is the Feedipedia measured value for whole peanut seeds; a derivation from the DM-weighted average of the Stage 2 products (oil 0.420 t DM at 39.3 MJ/kg, meal 0.475 t DM at 20.0 MJ/kg, per tonne of kernels) gives 29.1 MJ/kg DM, confirming consistency within 0.8%. The DM outputs for both stages come from the peanut methodology document.

> **General cascade principle:** Where a crop is modelled in two stages, the cascade structure reflects the physical processing chain. Energy allocation must use the same structure as economic and mass allocation, so that the three methods describe the same system: Final_Alloc_i = Stage1_Alloc_intermediate × Stage2_SubShare_i. **Three crops use 2-stage cascade allocation:** rice (hulling → milling), barley (malting → brewing) and peanut (shelling → crushing). In each, the intermediate — brown rice, malt, shelled kernels — is consumed entirely by the next stage and leaves no allocation factor of its own. Cotton is the exception and is treated directly, for the reason given above.

---

## 11. Complete GE Range Results Table

All values in MJ/kg DM. This table presents the final PERT distribution parameters for every co-product after applying all corrections described in Section 7.5.

| # | Product | GE_lo | GE_lit (mode) | GE_hi | Width | Correction | Source |
|---|---------|-------|---------------|-------|-------|------------|--------|
| **Vegetable Oils (Override)** | | | | | | | |
| 1 | Soybean oil | 38.5 | 39.3 | 40.0 | 1.5 | Override | INRAE-CIRAD-AFZ (n=9) |
| 2 | Canola oil | 38.5 | 39.3 | 40.0 | 1.5 | Override | INRAE-CIRAD-AFZ |
| 3 | Linseed oil | 38.5 | 39.3 | 40.0 | 1.5 | Override | INRAE-CIRAD-AFZ |
| 4 | Sunflower oil | 38.5 | 39.3 | 40.0 | 1.5 | Override | INRAE-CIRAD-AFZ |
| 5 | Safflower oil | 38.5 | 39.3 | 40.0 | 1.5 | Override | INRAE-CIRAD-AFZ |
| 6 | Cottonseed oil | 38.5 | 39.3 | 40.0 | 1.5 | Override | INRAE-CIRAD-AFZ |
| 7 | Peanut oil | 38.5 | 39.3 | 40.0 | 1.5 | Override | INRAE-CIRAD-AFZ |
| 8 | Corn oil (post-ferm) | 38.5 | 39.3 | 40.0 | 1.5 | Override | INRAE-CIRAD-AFZ |
| **Pure Substances (Override)** | | | | | | | |
| 9 | Fuel ethanol | 29.7 | 29.7 | 29.7 | 0.0 | Override (constant) | Physical constant |
| 10 | Refined sugar | 16.4 | 16.5 | 16.6 | 0.2 | Override | Physical constant |
| **Protein Meals** | | | | | | | |
| 11 | Soybean meal (48%) | 16.3 | 19.7 | 20.2 | 3.9 | Comp-derived | INRAE-CIRAD-AFZ (n=136) |
| 12 | Canola meal | 16.1 | 19.7 | 21.2 | 5.1 | Comp-derived | INRAE-CIRAD-AFZ |
| 13 | Linseed meal | 15.9 | 19.5 | 22.8 | 6.9 | Comp-derived | INRAE-CIRAD-AFZ |
| 14 | Sunflower meal | 14.3 | 19.4 | 21.8 | 7.5 | Comp-derived | Feedipedia |
| 15 | Safflower meal | 14.7 | 19.0 | 20.9 | 6.2 | Comp-derived | NRC 2012; FAO Feedipedia |
| 16 | Cottonseed meal | 15.8 | 20.0 | 20.2 | 4.4 | Comp-derived | Feedipedia |
| 17 | Peanut meal | 17.2 | 20.0 | 21.4 | 4.2 | **Half-mirror (7.5.1b)** | Feedipedia (n=6) |
| 18 | Distillers grains (total), corn | 17.2 | 21.4 | 22.3 | 5.1 | Comp-derived | Feedipedia / INRAE-CIRAD-AFZ |
| 19 | Wheat DGS | 16.1 | 20.3 | 21.2 | 5.1 | Comp-derived | INRAE-CIRAD-AFZ / Cozannet et al. |
| 20 | Brewers spent grain (dried) | 16.2 | 20.0 | 21.6 | 5.4 | Comp-derived | INRAE-CIRAD-AFZ / Feedipedia |
| **Bran / Germ Products** | | | | | | | |
| 21 | Wheat bran | 15.9 | 18.9 | 20.1 | 4.2 | Comp-derived | INRAE-CIRAD-AFZ (n=65) |
| 22 | Rice bran | 17.3 | 20.5 | 23.4 | 6.1 | Comp-derived | Feedipedia (n=2) |
| 23 | Corn germ | 22.9 | 28.9 | 29.5 | 6.6 | Comp-derived | NRC 2012; FAO Feedipedia |
| **High-Fat Products** | | | | | | | |
| 24 | Whole cottonseed | 19.8 | 23.8 | 25.2 | 5.4 | Comp-derived | INRAE-CIRAD-AFZ |
| 25 | Peanut kernels | 25.9 | 29.3 | 31.0 | 5.1 | Comp-derived | Feedipedia |
| 26 | Almond kernels | 26.8 | 30.7 | 32.6 | 5.8 | Comp-derived | Feedipedia |
| **Starch / Carbohydrate Products** | | | | | | | |
| 27 | Corn starch | 17.3 | 17.5 | 17.7 | 0.4 | Comp-derived | INRAE-CIRAD-AFZ |
| 28 | Wheat flour | 17.0 | 18.3 | 18.7 | 1.7 | Comp-derived | INRAE-CIRAD-AFZ |
| 29 | White rice | 17.0 | 18.0 | 18.4 | 1.4 | Comp-derived | Feedipedia |
| 30 | Brown rice | 17.0 | 18.1 | 18.8 | 1.8 | Comp-derived | Derived from milled product composition |
| 31 | Corn meal & grits | 16.9 | 18.6 | 18.7 | 1.8 | Comp-derived | INRAE-CIRAD-AFZ |
| 32 | Raw sugar | 15.5 | 16.0 | 17.1 | 1.6 | **Impurity** | Calculated |
| 33 | Malt | 17.6 | 19.5 | 20.4 | 2.8 | **Half-mirror (7.5.1b)** | Estimated from barley grain proxy |
| 34 | Food oats | 16.6 | 19.5 | 20.6 | 4.0 | Comp-derived | Feedipedia |
| 35 | Sweet corn kernels | 16.9 | 18.3 | 18.6 | 1.7 | Comp-derived | Estimated |
| **Fibrous Byproducts** | | | | | | | |
| 36 | Soybean hulls | 15.4 | 18.1 | 19.9 | 4.5 | Comp-derived | INRAE-CIRAD-AFZ (n=8–12) |
| 37 | Sunflower hulls | 14.5 | 20.1 | 22.9 | 8.4 | **Half-mirror (7.5.1a)** | INRAE-CIRAD-AFZ |
| 38 | Cottonseed hulls | 14.5 | 19.8 | 22.5 | 8.0 | **Half-mirror (7.5.1a)** | Feedipedia |
| 39 | Cottonseed linters | 15.9 | 17.5 | 18.2 | 2.3 | Comp-derived | NBS bomb calorimetry (pure cellulose); CRC Handbook |
| 40 | Cotton lint | 14.9 | 17.5 | 18.6 | 3.7 | Comp-derived | CRC Handbook (cellulose HHV) |
| 41 | Rice hulls | 13.8 | 16.3 | 18.2 | 4.4 | Comp-derived | Feedipedia |
| 42 | Peanut hulls | 13.6 | 19.8 | 21.5 | 7.9 | **Half-mirror (7.5.1a) + cap** | Feedipedia (n=4) |
| 43 | Oat hulls | 14.5 | 18.4 | 19.2 | 4.7 | Comp-derived | Feedipedia |
| 44 | Almond hulls | 14.5 | 17.0 | 18.8 | 4.3 | Comp-derived | Estimated from composition |
| 45 | Almond shells | 13.8 | 19.5 | 22.4 | 8.6 | **Half-mirror (7.5.1a)** | Research literature |
| **Mixed Byproducts** | | | | | | | |
| 46 | Corn gluten feed | 14.8 | 18.8 | 19.1 | 4.3 | **Minimal buffer** | Feedipedia (n=28) |
| 47 | Corn gluten meal | 22.4 | 23.9 | 25.1 | 2.7 | **Literature-anchored** | INRAE-CIRAD-AFZ |
| 48 | Corn steep liquor | 17.1 | 17.5 | 19.0 | 1.9 | **Formula overestimate** | Calculated from composition |
| 49 | Hominy feed | 14.1 | 18.7 | 19.0 | 4.9 | Comp-derived | Feedipedia (n=8) |
| 50 | Wheat middlings | 15.8 | 19.2 | 19.6 | 3.8 | Comp-derived | INRAE-CIRAD-AFZ |
| 51 | Oat mill feed | 14.4 | 17.5 | 18.9 | 4.5 | Comp-derived | Estimated from composition |
| 52 | Malt sprouts | 16.1 | 18.4 | 20.0 | 3.9 | Comp-derived | INRAE-CIRAD-AFZ / Feedipedia |
| 53 | Rice mill feed | 14.4 | 16.5 | 19.8 | 5.4 | Comp-derived | Estimated from composition; FAO Feedipedia |
| **Wet / Low-DM Products** | | | | | | | |
| 54 | Beet pulp (wet) | 14.9 | 17.1 | 18.6 | 3.7 | Comp-derived | INRAE-CIRAD-AFZ |
| 55 | Beet molasses | 13.9 | 14.5 | 15.5 | 1.6 | **Literature cap** | Estimated |
| 56 | Cane molasses | 13.7 | 14.7 | 15.5 | 1.8 | Comp-derived | Feedipedia |
| 57 | Citrus juice | 15.9 | 16.5 | 17.9 | 2.0 | Comp-derived | Calculated from USDA composition |
| 58 | Citrus pulp (wet) | 13.6 | 17.6 | 18.0 | 4.4 | **Minimal extension** | INRAE-CIRAD-AFZ (n=21) |
| 59 | Cannery waste silage | 13.5 | 17.5 | 18.1 | 4.6 | Comp-derived | Estimated from composition; FAO Feedipedia |
| 60 | Potato products | 16.0 | 17.5 | 18.5 | 2.5 | Comp-derived | INRAE-CIRAD-AFZ |
| 61 | Potato waste | 14.9 | 16.5 | 18.5 | 3.6 | Comp-derived | Estimated |
| 62 | Beer | 22.0 | 22.7 | 23.9 | 1.9 | Override | Calculated from composition |

**Notes on high-uncertainty products**: Sunflower hulls (width 8.4), almond shells (8.6), and cottonseed hulls (8.0) have the widest ranges in the dataset. These products genuinely have high compositional variability and are subject to the lignin effect described in Section 7.5.1a. They should be flagged in the manuscript as high-uncertainty products where the energy allocation results are most sensitive to the GE parameter.

---

## 12. Implementation in Monte Carlo Simulation

The GE values and ranges are used in the Monte Carlo uncertainty propagation as follows:

| Parameter | PERT Distribution | Source |
|-----------|-------------------|--------|
| GE mode (midpoint) | Literature value (Section 6) | Bomb calorimetry / database |
| GE min | GE_lo from compositional propagation (Section 7) | Section 7 |
| GE max | GE_hi from compositional propagation with corrections (Section 7.5) | Section 7.5 |

The simulation runs **10,000 iterations** with a fixed seed. In each iteration one value is drawn from each parameter's PERT distribution, and the allocation factors are recomputed from that draw. GE is one of three uncertain parameters — yield and price are the others — and all three are varied simultaneously. Dry matter contents are held at their point values.

Reported outputs are the deterministic factors (computed once from the midpoints) alongside the MC P5, P50 and P95. The two differ only slightly: across all products the median MC result departs from the deterministic value by at most 0.05 pp for economic and mass allocation and 1.12 pp for energy allocation.

The implementation is the companion script `monte_carlo_uncertainty_v11.py`, which carries the GE midpoints and ranges of Section 11 verbatim.

---
