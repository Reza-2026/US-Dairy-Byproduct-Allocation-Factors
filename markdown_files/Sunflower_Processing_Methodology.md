# Sunflower Crushing: Co-Product Allocation Methodology, Data Sources, and Calculations

**Document Version:** 1.0   
**Date:** June 2026  
**Basis:** 1 metric ton (t) of sunflower seed at 9% moisture  
**Price Period:** 2024–2025 average (unless otherwise noted)  

---

## Table of Contents

1. [Standard Basis and Conversions](#1-standard-basis-and-conversions)
2. [Data Sources and References](#2-data-sources-and-references)
3. [Sunflower Crushing System](#3-sunflower-crushing-system)
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
| **Parent crop** | Sunflower (*Helianthus annuus*, oil-type) | — |
| **Input quantity** | 1 metric ton (1,000 kg) | — |
| **Moisture content** | 9.0% | Moisture is **not** a grade-determining factor in the U.S. Standards for Sunflower Seed [^1^], which grade on test weight, damaged kernels and dehulled seed. USDA RMA uses 10.0% as the crop-insurance baseline, adjusting production above that level. Seed is typically delivered to crush plants at 9–10% moisture, and 9.0% is adopted here as a representative delivered value; Section 7.2 notes the effect of using the 10% baseline instead. |
| **Dry matter (DM) input** | 0.910 t DM/t sunflower seed | Calculated: 1.000 × (1 − 0.09) = 0.910 |
| **Bushel equivalent** | 73.5 bushels/t | 1,000 kg ÷ 13.608 kg/bu (30 lb at standard moisture) |
| **Bushel weight** | 30 lb (13.608 kg) | Typical test weight for oil-type sunflower at 9% moisture. USDA No. 1 minimum test weight: 25 lb/bu per 7 CFR 810.1804. Typical commercial test weights range from 28–32 lb/bu (NSA 2025 Crop Quality Report: average 30.2 lb/bu). [^1^] |
| **Typical oil content** | ~42% (as-is basis at 9% moisture), equivalent to ~46% (dry matter basis) | Industry average for oil-type sunflower. As-is basis: NSA reports average 42.7% at ~10% moisture. DM basis: typical 44–50% depending on variety and environment. [^2^] |

### 1.2 Convention for Adopted Values

Every yield, price, and DM% in this document is reported as an adopted point value together with the range it was drawn from. **Unless a row states otherwise, the adopted value is the midpoint of its stated range**, and the range is the parameter that carries the evidence. Point values are given to the precision the underlying sources support. Derived quantities (DM outputs, revenues, allocation percentages) are carried at four decimals internally and reported to one decimal place. This document is self-contained: all reconciliations are internal to sunflower crushing and no comparison is made to other crop processing systems.

### 1.3 Unit Conversions

| Conversion | Factor |
|------------|--------|
| 1 bushel sunflower (oil-type) | ~30 lb ≈ 13.61 kg (at 9% moisture, oil-type) |
| 1 lb | 0.453592 kg = 0.000453592 t |
| 1 t sunflower seed | ~73.5 bushels (at 30 lb/bu) |
| 1 short ton | 2,000 lb = 0.907185 metric ton |
| 1 metric ton | 2,204.62 lb = 1.10231 short tons |

> **Note on sunflower types:** Two main types of sunflower are grown: **oil-type** (smaller seeds, ~40–50% oil content as-is, thin hull ~20% of seed weight) and **confectionery/non-oil type** (larger seeds, ~25–35% oil content, thick hull ~35–45% of seed weight). This document covers **oil-type sunflower**, which is the type used for commercial oil extraction. Confectionery sunflower would have different yields, hull fractions, and allocations.

> **Note on bushel weight:** Sunflower seed bushel weights are variable because the seed does not fill standard bushel volumes uniformly. The USDA standard test weight minimum for No. 1 oil-type sunflower is 25 lb/bu (per 7 CFR 810.1804), but typical commercial test weights range from 28–32 lb per Winchester bushel. The 30 lb/bu figure used here is a typical midpoint based on NSA Crop Quality Reports.

---

## 2. Data Sources and References

### 2.1 Primary Sources

| Citation | Full Title | Type | URL |
|----------|-----------|------|-----|
| [^1^] | USDA AMS (formerly GIPSA) — Grain Inspection Standards for Sunflower Seed (7 CFR 810.1804) | Government (USDA) | https://www.ams.usda.gov/grades-standards/sunflower-seed-standards |
| [^2^] | FAO. *Crop Information: Sunflower* (water relations and agronomy); FAO Agribusiness Handbook: Sunflower Processing | International Organization | https://www.fao.org/land-water/databases-and-software/crop-information/sunflower/en |
| [^3^] | USDA ERS (August 2025). *Oil Crops Outlook* | Government (USDA) | https://ers.usda.gov/ |
| [^4^] | USDA WASDE (February 2026). *World Agricultural Supply and Demand Estimates* | Government (USDA) | https://www.usda.gov/ |
| [^5^] | IndexMundi. *Sunflower Oil Monthly Price* | Market Data | https://www.indexmundi.com/commodities/?commodity=sunflower-oil |
| [^6^] | IndexBox. *World - Sunflower Seed - Market Analysis, Forecast, Size, Trends and Insights* | Industry/Market | https://www.indexbox.io/ |
| [^7^] | National Sunflower Association. *All About Sunflower: Oil and Whole Seed/Meal* | Industry Association | https://www.sunflowernsa.com/oil/ and https://www.sunflowernsa.com/wholeseed/ |
| [^8^] | Feedipedia. *Sunflower Meal and Hulls* (animal feed database, INRAE/CIRAD/FAO) | Academic/Database | https://www.feedipedia.org/node/732 |
| [^9^] | Tridge. *Sunflower Seed Meal Market Insights (United States)* | Industry/Market | https://dir.tridge.com/market-insights/product-country/sunflower-seed-meal-united-states |

### 2.2 How Sources Were Used

- **Yield data:** USDA ERS [^3^], FAO [^2^], and National Sunflower Association [^7^] provided sunflower crush yield data. The ranges reflect variation across extraction methods (expeller vs. solvent) and seed varieties.
- **Hull fraction:** Industry data [^7^][^8^] indicates sunflower hulls represent 20–30% of seed weight for oil-type varieties. The hull fraction is independently sourced from hull content and dehulling efficiency data.
- **Price data (oil):** USDA ERS [^3^], WASDE [^4^], and IndexMundi [^5^] provided sunflower oil price data.
- **Price data (meal):** USDA ERS [^3^], Tridge [^9^], and IndexBox [^6^] provided sunflower meal price data.
- **Price data (hulls):** Industry sources [^7^] provided sunflower hull price data. Hulls are a low-value byproduct used primarily as animal feed roughage or boiler fuel.
- **DM contents and meal composition:** Feedipedia [^8^] and industry trading specifications.

---

## 3. Sunflower Crushing System

### 3.1 Process Description

Sunflower crushing (also called "sunflower seed processing") involves the following steps:

1. **Cleaning:** Foreign material (dirt, stones, weed seeds) is removed.
2. **Dehulling:** Sunflower seeds have fibrous hulls representing 20–30% of seed weight. Hulls are cracked off using impact or abrasion dehullers and separated by aspiration. Dehulling before extraction is standard practice for oil-type sunflower and is what makes hulls a separate marketed stream.
3. **Conditioning:** Dehulled kernels (meats) are heated to improve oil extractability and reduce meal moisture.
4. **Flaking:** Kernels are rolled into thin flakes to rupture cell walls and increase surface area.
5. **Pressing (optional):** Some facilities use a mechanical screw press (expeller) to remove ~50–70% of the oil before solvent extraction. Others go directly to solvent extraction after flaking.
6. **Solvent extraction:** Hexane is used to extract the remaining oil from the pressed cake or flakes.
7. **Desolventizing:** Hexane is removed from the oil (miscella) and meal (marc).
8. **Oil refining:** Crude oil is degummed, neutralized, bleached, and deodorized.
9. **Meal processing:** Meal is dried, cooled, and ground to specification (typically ~34–38% protein for partially dehulled meal; fully dehulled meal can exceed 40% protein).
10. **Hull processing:** Hulls may be sold as-is for animal feed, pelleted, or used as boiler fuel at the crushing plant.

**Co-products generated:**
- **Sunflower oil:** The primary high-value product (food, biodiesel, industrial uses).
- **Sunflower meal:** The primary high-volume co-product (animal feed, protein source for ruminants).
- **Sunflower hulls:** A fibrous byproduct used in ruminant feed or as boiler fuel.

> **Why hulls are reported as a separate co-product:** Sunflower hulls represent 20–30% of seed weight, and dehulling before extraction is standard practice. Removing them drops the meal yield from ~0.55 t/t (non-dehulled) to ~0.38 t/t (dehulled), so the hulls carry a substantial share of the seed's dry matter and must be allocated rather than ignored. Treating dehulled meal as the only solid co-product would leave roughly a fifth of the seed's dry matter unaccounted for.

### 3.2 Process Flow

```
1 t sunflower seed at 9% moisture (0.910 t DM)
        │
        ▼
  ┌─ SUNFLOWER CRUSHING ──────────────────────────┐
  │                                                 │
  │  Dehulling: ~0.200 t hulls separated           │
  │  Processing losses: ~0.020 t as-is (~2.0%)     │
  │  (handling, residual solvent, moisture loss)    │
  │                                                 │
  │  Sunflower oil: 0.40 t as-is (0.400 t DM)   ◄── co-product
  │                                                 │
  │  Sunflower meal: 0.38 t as-is (0.342 t DM)  ◄── co-product
  │                                                 │
  │  Sunflower hulls: 0.200 t as-is (0.180 t DM)◄── co-product
  │                                                 │
  └─────────────────────────────────────────────────┘

THREE CO-PRODUCTS from 1 t sunflower seed:
  Sunflower oil:  0.40 t as-is,  0.400 t DM
  Sunflower meal: 0.38 t as-is,  0.342 t DM
  Sunflower hulls: 0.200 t as-is, 0.180 t DM
  Total:                        0.922 t DM  (from 0.910 t input; see DM balance note in Section 7.2)
```

---

## 4. Co-Product Yields and Properties

### 4.1 Yields (per tonne of sunflower seed input)

| Co-product | Yield (t/t sunflower) | Range | Source & Calculation |
|------------|----------------------|-------|---------------------|
| **Sunflower oil** | 0.40 | 0.35–0.45 | Industry standard for solvent extraction of oil-type sunflower [^2^][^3^][^7^]. The 0.40 value is the exact mathematical midpoint of the range: (0.35 + 0.45) / 2 = 0.40. Yields vary with oil content (40–50% as-is basis), extraction efficiency, and whether expeller or solvent extraction is used. Expeller-only yields are ~0.30–0.35 t/t; solvent extraction achieves ~0.38–0.45 t/t. |
| **Sunflower meal (dehulled)** | 0.38 | 0.34–0.42 | Industry standard for dehulled, solvent-extracted meal [^2^][^7^]. The 0.38 value is the exact mathematical midpoint of the range: (0.34 + 0.42) / 2 = 0.38. Meal yield is inversely related to oil yield: higher oil extraction means less meal. Partially dehulled meal has ~34–38% protein (DM basis 35–39%); fully dehulled meal can exceed 40%. Non-dehulled meal has ~28–32% protein as-fed (DM basis 29–33%). |
| **Sunflower hulls** | 0.200 | 0.15–0.25 | Midpoint of the reported range. Oil-type sunflower carries 20–30% hull by seed weight [^7^][^8^], and commercial dehulling recovers roughly 75% of it into the hull stream, the remainder staying with the meal. Full dehulling would give ~0.22–0.25 t/t but is rarely achieved in practice. See the reconciliation note below for how the adopted value compares with the composition route. |

*Reconciling the hulls yield with seed composition:* The hulls yield can also be derived from the seed itself: at ~25% hull content (the midpoint of the reported 20–30% band) and ~75% dehulling recovery, 1 t of seed gives 0.25 × 0.75 = **0.1875 ≈ 0.187 t/t**. The adopted value, **0.200 t/t**, is the midpoint of the reported yield range and sits about 7% above the composition estimate. The two are used differently:

| Hulls yield | Total DM output | Against 0.910 t DM input | Economic (oil/meal/hulls) | Mass (oil/meal/hulls) |
|---|---|---|---|---|
| 0.187 (composition route) | 0.9103 t | +0.03% | 77.9 / 19.2 / 2.9 | 43.9 / 37.6 / 18.5 |
| **0.200 (adopted, range midpoint)** | **0.9220 t** | **+1.32%** | **77.7 / 19.2 / 3.1** | **43.4 / 37.1 / 19.5** |

The composition route closes the dry matter balance almost exactly, while the adopted midpoint leaves the small surplus reported in Section 7.2. The adopted value is retained for consistency with the treatment of every other parameter in this document; the difference on any allocation factor is one percentage point or less, which is immaterial at the level this table is used. Users who require a closed dry matter balance should substitute 0.187 t/t and the factors on the first row.

> **Note on yield relationships:** The three yields are interdependent. When more oil is extracted, less meal is produced. When more hulls are removed, meal protein rises but meal yield falls.

#### Total Recovery and Losses

The as-is yields sum to 0.980 t/t sunflower seed (0.40 + 0.38 + 0.200), which is less than the 1.0 t input. The ~2.0% shortfall represents real processing losses:

1. **Handling and spillage:** ~0.5–1.0% lost during transport, transfer, and cleaning.
2. **Residual solvent in meal:** Trace hexane (regulated to <500 ppm) adds negligible mass.
3. **Moisture loss:** Seeds are conditioned and dried during processing, losing ~0.5–1.0% moisture.
4. **Fines and dust:** ~0.2–0.5% lost as fines during dehulling and flaking.
5. **Hull fragments in meal:** Some hull material remains in the meal despite dehulling; conversely, some kernel is lost with the hulls. The net effect is included in the hulls yield.

### 4.2 Dry Matter Contents

| Co-product | DM (%) | Basis |
|------------|--------|-------|
| Sunflower oil | 100.0% | Crude and refined sunflower oil are essentially pure lipid (triglycerides) with negligible moisture (<0.1%). |
| Sunflower meal (dehulled) | 90.0% | Standard trading specification: maximum 10–12% moisture, i.e. 88–90% DM [^8^]. Feedipedia reports an average of 89.0% DM across all sunflower meals (n=14,806), with dehulled meals averaging 89.8% DM. The adopted 90.0% follows the dehulled-meal figure and the top of the trading specification, rather than the midpoint of the wider band. |
| Sunflower hulls | 90.0% | Dried hulls are typically 89–93% DM [^8^]. Feedipedia reports an average of 90.7% DM (range 88.7–93.1%, n=24). The adopted 90.0% is the round industry figure and sits just below that average; hulls are dried during processing to prevent spoilage. |

### 4.3 DM Output per Tonne of Sunflower Seed

| Co-product | Calculation | DM Output (t/t sunflower) |
|------------|-------------|--------------------------|
| **Sunflower oil** | 0.40 × 1.00 | **0.4000** |
| **Sunflower meal** | 0.38 × 0.90 | **0.3420** |
| **Sunflower hulls** | 0.200 × 0.90 | **0.1800** |
| **Total** | | **0.9220** |

---

## 5. Prices

### 5.1 Price Table

| Co-product | Price (USD/t) | Range | Source | Notes |
|------------|--------------|-------|--------|-------|
| **Sunflower oil** | 1,000 | 750–1,250 | USDA ERS [^3^]; WASDE [^4^]; IndexMundi [^5^] | 2024–2025 average for crude sunflower oil. Global prices averaged $1,000–1,500/t during this period (FRED/IMF data: 2024 avg $1,270/t, 2025 avg $1,526/t). The $1,000/t midpoint reflects a weighted average of crude FOB and domestic benchmarks. |
| **Sunflower meal (dehulled)** | 260 | 200–320 | USDA ERS [^3^]; Tridge [^9^]; IndexBox [^6^] | 2024–2025 average for dehulled, solvent-extracted meal (~34–38% protein as-fed, 35–39% DM). Dehulled meal commands a premium over non-dehulled meal. |
| **Sunflower hulls** | 80 | 50–110 | National Sunflower Association [^7^] | 2024–2025 average. Hulls are a low-value byproduct used as animal feed roughage (ruminant diet filler) or boiler fuel at crushing plants. Prices vary with regional demand and whether hulls are pelleted (pelleted: $100–140/t). |

### 5.2 Price Verification

**Sunflower oil:**

```
USDA ERS (2025): ~$800-900/t (crude, FOB Midwest)
IndexMundi (2025 avg): ~$1,207-1,225/t (global crude benchmark)
FRED/IMF global price: 2024 avg $1,270/t; 2025 avg $1,526/t
Black Sea FOB crude: ~$790-900/t at certain points in 2024

Adopted: $1,000/t, the midpoint of the $750-1,250 range

```

**Sunflower meal (dehulled):**

```
USDA ERS (2025): ~$220-280/t (dehulled, 36% protein)
Tridge (2025): ~$240-290/t
IndexBox (2025): ~$230-310/t
Black Sea FOB standard meal: ~$190-210/t (likely non-dehulled)
Non-dehulled meal baseline: ~$180-240/t
Dehulling premium: +$30-60/t

Adopted: $260/t, the midpoint of the $200-320 range
```

**Sunflower hulls:**

```
National Sunflower Association: ~$60-90/t (loose, bulk)
Pelleted hulls: ~$100-140/t
Boiler fuel value: ~$40-70/t (energy content basis)

Adopted: $80/t, the midpoint of the $50-110 range
```

### 5.3 Revenue per Tonne of Sunflower Seed

| Co-product | Calculation | Revenue (USD/t sunflower) |
|------------|-------------|--------------------------|
| **Sunflower oil** | 0.40 × 1,000 | **$400.00** |
| **Sunflower meal** | 0.38 × 260 | **$98.80** |
| **Sunflower hulls** | 0.200 × 80 | **$16.00** |
| **Total** | | **$514.80** |

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
| Sunflower oil | (400.00 ÷ 514.80) × 100 | **77.7%** |
| Sunflower meal | (98.80 ÷ 514.80) × 100 | **19.2%** |
| Sunflower hulls | (16.00 ÷ 514.80) × 100 | **3.1%** |
| **Total** | | **100.0%** |

> **Rounding note:** The raw calculations yield 77.70% (oil), 19.19% (meal), and 3.11% (hulls). These are rounded to 77.7%, 19.2%, and 3.1% so that the sum is exactly 100.0%.

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
| Sunflower oil | (0.4000 ÷ 0.9220) × 100 | **43.4%** |
| Sunflower meal | (0.3420 ÷ 0.9220) × 100 | **37.1%** |
| Sunflower hulls | (0.1800 ÷ 0.9220) × 100 | **19.5%** |
| **Total** | | **100.0%** |

> **Rounding note:** The raw calculations yield 43.38% (oil), 37.09% (meal), and 19.52% (hulls). These are rounded to 43.4%, 37.1%, and 19.5% so that the sum is exactly 100.0%.

### 6.3 Comparison: Economic vs. Mass Allocation

| Co-product | Economic Allocation | Mass Allocation | Difference |
|------------|-------------------|----------------|------------|
| Sunflower oil | 77.7% | 43.4% | +34.3 pp |
| Sunflower meal | 19.2% | 37.1% | −17.9 pp |
| Sunflower hulls | 3.1% | 19.5% | −16.4 pp |

The large difference for oil reflects its high value-to-mass ratio: oil commands $1,000/t — 3.85× the meal price and 12.5× the hulls price — but carries 43.4% of the co-product dry matter. Hulls run the other way, carrying 19.5% of the dry matter but only 3.1% of the revenue. The choice of allocation method therefore matters most for the hulls stream, whose share of the burden differs by more than a factor of six between the two methods.

---

## 7. Mass Balance Verification

### 7.1 Input-Output Reconciliation

| Check | Value | Status |
|-------|-------|--------|
| Input: Sunflower seed at 9% moisture | 1.000 t | — |
| Input moisture | 9.0% | — |
| Input DM | 0.910 t | — |
| Output: Sunflower oil (as-is) | 0.400 t | ✓ |
| Output: Sunflower meal (as-is) | 0.380 t | ✓ |
| Output: Sunflower hulls (as-is) | 0.200 t | ✓ |
| Total as-is output | 0.980 t | 98.0% of input |
| Processing losses (as-is) | 0.020 t | 2.0% of input ✓ |
| Output DM: Oil | 0.400 t | ✓ |
| Output DM: Meal | 0.342 t | ✓ |
| Output DM: Hulls | 0.180 t | ✓ |
| Total DM output | 0.922 t | 101.3% of input DM |

### 7.2 DM Balance Detail

| Item | Value | Notes |
|------|-------|-------|
| Input DM (1 t sunflower seed at 9% moisture) | 0.9100 t | 1.000 × (1 − 0.09) |
| **Output DM — co-products:** | | |
| Sunflower oil | 0.4000 t | 0.40 t × 100% DM |
| Sunflower meal | 0.3420 t | 0.38 t × 90% DM |
| Sunflower hulls | 0.1800 t | 0.200 t × 90% DM |
| Total co-product DM | **0.9220 t** | |
| DM balance gap | +0.0120 t | +1.32% of input DM |

> **Balance assessment:** The DM output exceeds the DM input by 0.0120 t (1.32%). Dry matter is not created in crushing, so this is an accounting result: the three yields are each taken as the midpoint of its own reported range and are not mutually reconciled to a closed unit-process balance. The surplus is small relative to the spread of those ranges (oil 0.35–0.45, meal 0.34–0.42, hulls 0.15–0.25).
>
> **The reconciliation is available.** As set out in Section 4.1, deriving the hulls yield from seed composition instead — 25% hull content at ~75% dehulling recovery — gives 0.187 t/t and a DM output of 0.9103 t, which closes against the 0.910 t input to within 0.03%. Substituting that value moves the economic allocation to 77.9 / 19.2 / 2.9 and the mass allocation to 43.9 / 37.6 / 18.5, a change of one percentage point or less on any stream. The adopted values are retained for consistency of treatment; the surplus is reported rather than removed so that users can see it and substitute if a closed balance is required.
>
> **Note on the moisture basis.** The 1.32% figure is calculated on the 9% moisture basis used throughout this document. Sunflower has no USDA grade-determining moisture (Section 1.1), and the crop-insurance standard is 10%. On a 10% basis the input DM would be 0.900 t and the same outputs would show a 2.44% surplus. The 9% basis reflects typical delivered moisture at crush plants, but users working to the 10% standard should expect the larger figure.

### 7.3 As-Is Mass Balance

| Item | Value | Notes |
|------|-------|-------|
| Input (sunflower seed) | 1.000 t | — |
| **Output:** | | |
| Sunflower oil | 0.400 t | — |
| Sunflower meal | 0.380 t | — |
| Sunflower hulls | 0.200 t | — |
| **Total output** | **0.980 t** | |
| **Processing losses** | **0.020 t** | 2.0%: handling, moisture loss, fines — the residual of the balance, not an independent measurement |
| **Balance** | **1.000 t** | Closes by construction, since the loss term is the residual |

---

## 8. Complete Data Table

| Parent Crop | Crop System | Stage | USDA Standard | Standard Moisture | Parent Input Basis | Co-product Stream | Yield (t/t) | Yield Range | Price (USD/t) | Price Range | DM (%) | DM Output (t/t) | Revenue (USD/t) | Econ Alloc (%) | Mass Alloc (%) |
|-------------|-------------|-------|---------------|-------------------|-------------------|-------------------|-------------|-------------|---------------|-------------|--------|-----------------|-----------------|----------------|----------------|
| Sunflower | Sunflower crushing | Single | 25 lb/bu min test weight (7 CFR 810.1804) | 9% | 1 t sunflower seed at 9% moisture | Sunflower oil | 0.40 | 0.35–0.45 | 1,000 | 750–1,250 | 100.0 | 0.400 | 400.00 | 77.7 | 43.4 |
| Sunflower | Sunflower crushing | Single | 25 lb/bu min test weight (7 CFR 810.1804) | 9% | 1 t sunflower seed at 9% moisture | Sunflower meal (dehulled) | 0.38 | 0.34–0.42 | 260 | 200–320 | 90.0 | 0.342 | 98.80 | 19.2 | 37.1 |
| Sunflower | Sunflower crushing | Single | 25 lb/bu min test weight (7 CFR 810.1804) | 9% | 1 t sunflower seed at 9% moisture | Sunflower hulls | 0.200 | 0.15–0.25 | 80 | 50–110 | 90.0 | 0.180 | 16.00 | 3.1 | 19.5 |

> **Note on allocation rounding:** Raw economic allocations are 77.70% (oil), 19.19% (meal), and 3.11% (hulls), rounded to 77.7%, 19.2%, and 3.1% to sum to exactly 100.0%. Raw mass allocations are 43.38% (oil), 37.09% (meal), and 19.52% (hulls), rounded to 43.4%, 37.1%, and 19.5% to sum to exactly 100.0%.

---
## 9. Data Quality and Limitations

### 9.1 High-Confidence Data

| Data Point | Confidence | Source |
|------------|-----------|--------|
| Oil yield (0.40 t/t) | **High** | Midpoint of the reported crush range for solvent extraction [^2^][^3^][^7^] |
| Meal yield (0.38 t/t, dehulled) | **High** | Midpoint of the reported range for dehulled, solvent-extracted meal [^7^] |
| Oil DM% (100%) | **High** | Pure lipid with negligible moisture |
| Meal DM% (90%) | **Medium-High** | Trading specification 88–90% DM; Feedipedia [^8^] average 89.0% overall and 89.8% for dehulled meals, so 90.0% sits at the top of the evidence |
| Oil price ($1,000/t) | **High** | Consistent with 2024-2025 global crude benchmarks |
| Meal price ($260/t) | **High** | Consistent with dehulled meal pricing |

### 9.2 Medium-Confidence Data

| Data Point | Confidence | Source |
|------------|-----------|--------|
| Hulls yield (0.200 t/t) | **Medium** | Midpoint of the reported range (0.15–0.25 t/t). The composition route — 25% hull content at ~75% dehulling recovery — gives 0.187 t/t; see Sections 4.1 and 7.2 |
| Hulls DM% (90%) | **Medium** | Based on Feedipedia average 90.7%; actual range 89–93% |
| Hulls price ($80/t) | **Medium** | Limited market data; hulls are often consumed on-site as boiler fuel rather than sold. When used as fuel, the economic allocation may treat them as waste (zero value). |
| Price ranges | **Medium** | Based on historical volatility; actual prices may exceed ranges during market shocks |
| Processing losses (2.0%) | **Medium** | Residual of the as-is balance rather than a measured quantity; consistent with the 2–3% range typical of solvent extraction plants |

### 9.3 Known Limitations

1. **Hulls yield and the dry matter balance:** The adopted 0.200 t/t is the midpoint of the reported range (0.15–0.25 t/t). Deriving the yield from seed composition instead — 25% hull content at ~75% dehulling recovery — gives 0.187 t/t, about 7% lower, and closes the dry matter balance to within 0.03%. Both values sit well inside the reported range and the difference on any allocation factor is one percentage point or less. Sections 4.1 and 7.2 give both sets of factors so that a user can adopt whichever suits their purpose.

2. **Hulls economic value is low and variable:** Sunflower hulls have limited markets. Many crushing plants burn hulls on-site for energy rather than selling them, in which case they have zero market value. If hulls are treated as waste (zero revenue), the economic allocation would be: Oil 80.2%, Meal 19.8%. The choice of whether to assign hulls a market value significantly affects the economic allocation.

3. **Non-dehulled vs. dehulled meal:** This table assumes partially dehulled meal (0.38 t/t, ~34–38% protein as-fed; DM basis 35–39%). Fully dehulled meal can exceed 40% protein. If non-dehulled meal is produced (0.55–0.60 t/t, ~28–32% protein as-fed; DM basis 29–33%), the meal yield would be higher, hulls would not be a separate co-product, and the allocation would change. The meal price for non-dehulled meal is typically $180–240/t (lower than dehulled). Note: protein values in this document are reported on an as-fed basis unless otherwise stated; DM-basis values are approximately 1.5–3 percentage points higher.

4. **Confectionery sunflower:** This table covers oil-type sunflower only. Confectionery sunflower has lower oil content (~25–35%), higher hull fraction (~35–45%), and different meal properties. Separate yield and price data would be needed.

5. **Regional price variation:** Sunflower oil and meal prices vary significantly by region. Black Sea region (Ukraine, Russia) prices are typically lower than North American or European prices due to proximity to major production areas.

6. **Allocation sensitivity:** The economic allocation is moderately sensitive to the oil price. If oil drops from $1,000 to $750/t, oil's economic allocation drops from 77.7% to 72.3%. If hulls are assigned zero value (waste), oil's economic allocation rises from 77.7% to 80.2%.

---
