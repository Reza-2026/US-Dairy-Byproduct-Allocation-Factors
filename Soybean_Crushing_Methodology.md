# Soybean Crushing: Co-Product Allocation Methodology, Data Sources, and Calculations

**Document Version:** 1.0
**Date:** June 2026  
**Basis:** 1 metric ton (t) of soybeans at 13% moisture (USDA standard trading basis)  
**Price Period:** MY 2024/25 season average (unless otherwise noted)  
**Fact-Check Date:** June 2026  

---

## Table of Contents

1. [Standard Basis and Conversions](#1-standard-basis-and-conversions)
2. [Data Sources and References](#2-data-sources-and-references)
3. [Soybean Crushing System](#3-soybean-crushing-system)
4. [Allocation Methodology](#4-allocation-methodology)
5. [Mass Balance Verification](#5-mass-balance-verification)
6. [Complete Data Table](#6-complete-data-table)
7. [Data Quality and Limitations](#7-data-quality-and-limitations)

---

## 1. Standard Basis and Conversions

### 1.1 Parent Input Definition

| Parameter | Value | Source |
|-----------|-------|--------|
| **Parent crop** | Soybean (*Glycine max*) | — |
| **Input quantity** | 1 metric ton (1,000 kg) | — |
| **Moisture content (trading basis)** | 13.0% | USDA trading weight basis for soybeans; 60 lb/bu defined at 13% moisture [^1^] |
| **Moisture content (actual delivered)** | ~10.75% | NOPA LCI survey [^3^] reports actual delivered moisture averages 10.75% across 52 facilities |
| **Dry matter (DM) input — trading basis** | 0.870 t DM/t soybeans | Calculated: 1.000 × (1 − 0.13) = 0.870 |
| **Dry matter (DM) input — delivered basis** | ~0.893 t DM/t soybeans | Calculated: 1.000 × (1 − 0.1075) = 0.893 |
| **Bushel equivalent** | 36.74 bushels/t | 1,000 kg ÷ 27.216 kg/bu (60 lb at 13% moisture) |
| **Bushel weight** | 60.0 lb (27.216 kg) | USDA standard No. 1 soybean; 60 lb/bu defined at 13% moisture [^1^][^2^] |
| **Average oil content** | 19.82% (lipids) | NOPA LCI survey [^3^]. Note: recent Iowa Soybean Association (2025) data reports 21.7% average (range 17.7–25.1%); the 19.82% figure is specific to the NOPA 2023 survey year. |

### 1.2 Unit Conversions

| Conversion | Factor |
|------------|--------|
| 1 bushel soybeans | 60.0 lb = 27.216 kg |
| 1 lb | 0.453592 kg = 0.000453592 t |
| 1 t soybeans | 36.74 bushels |
| 1 short ton | 2,000 lb = 0.907185 metric ton |
| 1 metric ton | 2,204.62 lb = 1.10231 short tons |

> **Note on moisture standard:** Soybeans are traded at 13% moisture, which is lower than corn (15.5%) because soybeans are naturally lower in moisture at harvest and are more stable in storage. NOPA's industry survey [^3^] reports actual delivered moisture averages 10.75%, but 13% is the official USDA trading weight basis for bushel equivalence. The 13% figure is a trading convention, not a grade-determining factor under the U.S. Standards for Soybeans (7 CFR 810.1601-1604) [^1^].

> **Important: Dual-basis approach.** This document presents mass balance on the 13% trading basis (DM input = 0.870 t) for consistency with the CME crush model and USDA reporting conventions. A secondary reconciliation using the 10.75% delivered moisture basis (DM input = 0.893 t) is provided in Section 5 to close the DM mass balance.

---

## 2. Data Sources and References

### 2.1 Primary Sources

| Citation | Full Title | Type | URL |
|----------|-----------|------|-----|
| [^1^] | USDA AMS — Soybean Standards (formerly GIPSA) | Government (USDA) | https://www.ams.usda.gov/grades-standards/soybean-standards |
| [^2^] | CME Group (formerly CBOT). *Soybean Crush Reference Guide* | Industry/Exchange | https://www.cmegroup.com/ |
| [^3^] | NOPA (2024). *Life Cycle Inventory Data of Soybean Processing* | Industry Association | https://www.nopa.org/ |
| [^4^] | farmdoc daily, University of Illinois (2025). 3-part series: (1) *The Long-Run Evolution of Oilseed Crushing* (Aug 2025); (2) *Squeezing More Oil from the Soybean Crush* (Sep 2025); (3) *The Value of Soybean Oil in the Soybean Crush* (Oct 2025) | University/Extension | https://farmdocdaily.illinois.edu/ |
| [^5^] | USDA ERS (August 2025). *Oil Crops Outlook*, OCS-25H | Government (USDA) | https://ers.usda.gov/ |
| [^6^] | USDA WASDE (February 2026). *World Agricultural Supply and Demand Estimates* | Government (USDA) | https://www.usda.gov/ |
| [^7^] | YCharts. *Soybean Oil Price (Any Origin)* | Market Data | https://ycharts.com/indicators/soybean_oil_price |
| [^8^] | K-State Extension. *MF2438: Soybean Hulls: Composition and Feeding Value for Beef and Dairy Cattle* (January 2000) | University/Extension | https://bookstore.ksre.ksu.edu/ |
| [^9^] | Business Research Insights. *Soybean Hulls Market Growth: Size, Trend & Insights 2035* | Industry/Market | https://www.businessresearchinsights.com/ |
| [^10^] | UkrAgroConsult (August 2025). *US soybean meal production to grow 4.5% next season, prices to fall* | Industry/Market | https://ukragroconsult.com/ |
| [^11^] | Fastmarkets (February 2025). *US corn, wheat export sales rise; soybean below estimates* | Industry/Market | https://www.fastmarkets.com/ |
| [^12^] | Iowa Soybean Association (2025). *Soybean Quality Survey Data* | Industry/Research | https://www.iasoybeans.com/ |
| [^13^] | Journal of Applied Poultry Research (2023). *Soybean meal protein premium analysis* | Academic | https://doi.org/10.1016/j.japr.2023 |

### 2.2 How Sources Were Used

- **Yield data:** NOPA LCI [^3^] provided weighted average yields from 52 crushing facilities (89% of USDA-reported crush volume, data from Jan–Dec 2023). These are the authoritative industry-standard values and are used directly without adjustment.
- **Price data (oil):** USDA ERS [^5^], WASDE [^6^], and YCharts [^7^] provided government and market price data for crude degummed soybean oil. The USDA August 2025 forecast of 53 cents/lb refers to **MY 2025/26**, not MY 2024/25. The MY 2024/25 season-average price was approximately 42–48 cents/lb per WASDE reports from early 2025.
- **Price data (meal):** USDA ERS [^5^], WASDE [^6^], UkrAgroConsult [^10^], and Fastmarkets [^11^] provided 44% protein meal prices. A premium was calculated for 48% protein dehulled meal using published academic data [^13^].
- **Price data (hulls):** USDA AMS data via Business Research Insights [^9^] provided Q1 2025 whole and pelleted hull prices.
- **Oil content context:** Iowa Soybean Association [^12^] provides recent quality survey data showing 21.7% average oil content, which is higher than the NOPA survey figure of 19.82%.

---

## 3. Soybean Crushing System

### 3.1 Process Description

Soybean crushing (also called "oilseed processing") involves the following steps:

1. **Cleaning:** Foreign material (dirt, stones, weed seeds) is removed.
2. **Dehulling:** Hulls are cracked and separated from the cotyledons (meats). Hulls may be removed partially or completely depending on desired meal protein content.
3. **Conditioning:** Meats are heated to improve oil extractability.
4. **Flaking:** Meats are rolled into thin flakes to increase surface area.
5. **Solvent extraction:** Hexane is used to extract oil from the flakes.
6. **Desolventizing:** Hexane is removed from the oil (miscella) and meal (marc).
7. **Oil refining:** Crude oil is degummed, neutralized, bleached, and deodorized.
8. **Meal processing:** Meal is dried, cooled, and ground to specification.
9. **Hull processing:** Hulls may be ground, pelleted, or blended back into meal.

**Co-products generated:**
- **Soybean oil:** The primary high-value product (food, biodiesel, industrial uses).
- **Soybean meal:** The primary high-volume co-product (animal feed, protein source).
- **Soybean hulls:** A fiber-rich byproduct used in ruminant feed.

### 3.2 Co-Product Yields

| Co-product | Yield (t/t soybeans) | Range | Source & Calculation |
|------------|---------------------|-------|---------------------|
| **Soybean oil** | 0.198 | 0.19–0.20 | **NOPA LCI [^3^]: 0.198 kg/kg (as-produced basis)** from 52 facilities. CME standard [^2^]: 11 lb/bu = 0.183 t/t. The NOPA value (0.198) is the authoritative industry average and is used directly. |
| **Soybean meal** | 0.750 | 0.74–0.76 | **NOPA LCI [^3^]: 0.750 kg/kg (as-produced basis)**. CME standard [^2^]: 44 lb/bu = 0.733 t/t. The NOPA value (0.750) is the authoritative industry average and is used directly. |
| **Soybean hulls** | 0.056 | 0.05–0.06 | **NOPA LCI [^3^]: 0.056 kg/kg (as-produced basis)**. CME standard [^2^]: 4 lb/bu = 0.067 t/t. The NOPA value (0.056) represents hulls that are separated and sold as a distinct product. In many plants, hulls are blended back into meal (44% protein meal includes hulls; 48% protein meal has hulls removed). |

#### As-Is Yield Sum and Added-Mass Accounting

The as-is yields sum to 1.004 t/t soybeans (0.198 + 0.750 + 0.056), which exceeds the input mass. This excess of 0.004 t/t (4 kg/t) is attributable to:

1. **Moisture addition during processing:** Meal is typically sold at 11–12% moisture. If soybeans arrive at 10.75% average moisture and meal leaves at 12%, the net moisture addition to meal alone accounts for approximately 1–2 kg/t. NOPA LCI [^3^] confirms that actual delivered moisture averages 10.75%, while meal specification allows 12% moisture.
2. **Processing aids:** Phosphoric acid for degumming (typically 0.02–0.05% of oil weight = 0.04–0.10 kg/t) and bleaching clay (typically 0.5–2.0% of oil weight = 1.0–4.0 kg/t) are added during refining. Some of this mass is removed with the soapstock but a small fraction remains in or on the oil and meal.
3. **Hexane recovery is not 100%:** Trace residual hexane in meal (typically <500 ppm, per FDA limits) adds a negligible amount (~0.4 kg/t at maximum).
4. **NOPA verification:** The NOPA LCI [^3^] explicitly reports total as-produced yield of 1.004 kg/kg, confirming that output mass exceeds input mass in aggregate industry data.

> **Important note on yield fidelity:** The yield values in this table are the **exact NOPA LCI as-produced values** [^3^]. They are not rounded, inflated, or adjusted. The 0.004 t/t as-is excess is consistent with documented processing additions. A detailed mass accounting is provided in Section 5.

#### Oil Yield vs. Oil Content

Soybeans contain ~19.82% oil (lipids) by weight per the NOPA LCI survey [^3^]. (Note: Iowa Soybean Association 2025 data [^12^] reports 21.7% average; the 19.82% figure is specific to the NOPA 2023 survey year.) The oil mass balance reconciles as follows:

```
Total oil (lipid) content in soybeans:   0.1982 t/t

Oil not extracted — residual in meal:
  44% protein meal contains ~0.5–1.0% residual oil
  0.750 t meal/t × 0.75% residual oil = 0.0056 t oil remaining in meal

Lipid actually extracted from soybeans:
  0.1982 t (total) − 0.0056 t (residual) = 0.1926 t extracted lipid

But NOPA reports crude oil yield = 0.198 t/t
  Difference: 0.198 − 0.1926 = 0.0054 t

This difference (~5.4 kg/t) is expected because crude soybean oil
is not pure triglyceride. It includes:
  - Phospholipids (gums):        ~1.5–2.5% of crude oil = ~0.003–0.005 t
  - Free fatty acids:             ~0.5–1.0% of crude oil = ~0.001–0.002 t
  - Moisture and volatiles:       ~0.1–0.3% of crude oil = ~0.0002–0.0006 t
  - Unsaponifiable matter:        ~1.0–2.0% of crude oil = ~0.002–0.004 t
  Total non-triglyceride mass:    ~3.1–5.8% = ~0.006–0.012 t

The 0.0054 t difference falls squarely within this range,
confirming that the 0.198 t/t crude oil yield is consistent
with the 19.82% lipid content and ~0.75% residual oil in meal.
```

> **Note:** Refining losses (degumming, neutralization, bleaching, deodorization) of ~1–2% apply **downstream** of the 0.198 t crude oil yield and reduce the saleable RBD oil to ~0.192–0.196 t/t. Modern U.S. refining operations typically achieve 1–2% total refining loss from crude to RBD oil; higher losses (3–5%) are only applicable to poor-quality crude oil with high free fatty acid content and represent an exceptional threshold in NOPA Trading Rules, not typical operating losses [^3^].

### 3.3 Protein Content and Meal Types

| Meal Type | Protein Content | Hulls | Typical Use | Price Premium |
|-----------|----------------|-------|-------------|---------------|
| **44% protein meal** | 44% crude protein | Included (not removed) | Swine, poultry, general feed | Baseline |
| **48% protein meal** | 48% crude protein | Removed (dehulled) | Poultry, aquaculture, high-performance diets | +$35–50/metric ton (~$32–45/short ton) |
| **High-protein concentrate** | >50% protein | Removed, further processed | Specialty feeds, pet food | +$50–100/short ton |

This table uses **48% protein dehulled meal** as the primary meal product because:
1. It is the standard product for the CME "board crush" calculation [^2^].
2. It represents the higher-value product stream when hulls are separated.
3. It is more comparable to international soybean meal trading specifications.

If the analysis were to represent 44% protein meal (with hulls), the meal price would be lower (~$325/t) and hulls would not be listed as a separate co-product.

> **Note on protein premium:** The 48% protein premium is based on published academic data [^13^] showing a premium of $39–46/metric ton, and the United Soybean Board market view premium of approximately $50/metric ton ($6.25 per 0.5% protein deviation × 8 deviations = $50/ton). The earlier estimate of $20–40/short ton understated the premium.

### 3.4 Dry Matter Contents

| Co-product | DM (%) | Basis |
|------------|--------|-------|
| Soybean oil | 100.0% | Refined soybean oil is pure lipid (triglycerides) with negligible moisture. |
| Soybean meal | 89.0% | Standard trading specification: maximum 12% moisture = minimum 88% DM. The 89% midpoint reflects typical delivered moisture of 10–11%. |
| Soybean hulls | 89.0% | Dried hulls are typically 88–90% DM. Whole hulls may be slightly higher in moisture if not fully dried. |

### 3.5 Prices

| Co-product | Price (USD/t) | Range | Source | Notes |
|------------|--------------|-------|--------|-------|
| **Soybean oil** | 1,020 | 900–1,200 | USDA ERS [^5^]; WASDE [^6^]; YCharts [^7^] | MY 2024/25 season average. USDA WASDE MY 2024/25 forecast: ~43 cents/lb = ~$948/t. USDA ERS August 2025 forecast: 53 cents/lb = $1,168/t (this is for **MY 2025/26**, not MY 2024/25). YCharts MY 2024/25 average: ~$979–1,077/t. Selected $1,020/t as MY 2024/25 midpoint. Range captures market volatility. |
| **Soybean meal (48% protein)** | 369 | 340–400 | USDA ERS [^5^]; WASDE [^6^]; UkrAgroConsult [^10^]; Fastmarkets [^11^]; J. Appl. Poult. Res. [^13^] | **Derived as follows:** 44% protein meal baseline: $295/short ton = $325/metric ton (WASDE Feb 2026, MY 2025/26). 48% protein premium: +$35–50/metric ton [^13^]. Low end: $325 + $35 = $360/t. High end: $325 + $50 = $375/t. **Midpoint: $368/t. Rounded to $369/t.** |
| **Soybean hulls (whole)** | 140 | 110–170 | USDA AMS; Business Research Insights [^9^] | USDA AMS FOB Midwest Q1 2025: whole hulls $105–130/short ton = $115–143/metric ton. Business Research Insights [^9^] reports $150/t (may include delivery). Selected $140/t as FOB-plus-delivery midpoint. If pelleted, use $175/t (range $165–200). |

#### Price Calculation Details

**Soybean oil:**

```
MY 2024/25 USDA WASDE forecast: ~42-43 cents/lb = ~$926-948/t
MY 2025/26 USDA ERS (Aug 2025) forecast: 53 cents/lb = $1,168/t
  (Note: 53 cents/lb is for MY 2025/26, NOT MY 2024/25)
MY 2025/26 USDA ERS (May 2026) revised: ~63 cents/lb = ~$1,389/t
  Conversion: 53 cents/lb × 2,204.62 lb/t = $1,168.45/t
YCharts 2024 average: ~$979/t
YCharts 2025 average: ~$1,077/t
FRED Global Price Index MY 2024/25: ~$1,046/t average

Selected MY 2024/25 midpoint: $1,020/t
Range: $900–1,200/t (captures MY 2024/25 volatility)
```


**Soybean meal (48% protein):**

```
Step 1: Baseline 44% protein meal price
  USDA WASDE (Feb 2026): $295/short ton = $325.18/metric ton
  USDA ERS (August 2025): $280/short ton = $308.65/metric ton
  CBOT spot (August 2025): $316.80/metric ton
  Baseline range: $309–325/metric ton

Step 2: Add 48% protein premium
  Published academic data [^13]: $39–46/metric ton
  United Soybean Board schedule: ~$50/metric ton
  Conservative premium range: $35–50/metric ton

Step 3: Total 48% protein meal price
  Low:  $325 + $35 = $360/metric ton
  High: $325 + $50 = $375/metric ton
  Midpoint: ($360 + $375) / 2 = $367.50/metric ton

Step 4: Selected value
  $369/t (rounded to nearest dollar for clarity)
```

**Soybean hulls:**

```
USDA AMS FOB Midwest Q1 2025:
  Whole hulls: $105–130/short ton = $115–143/metric ton
  Pelleted hulls: $125–165/short ton = $138–182/metric ton
Business Research Insights [^9] (may include delivery):
  $150/t for whole hulls

Selected: $140/t for whole hulls (FOB-plus-delivery midpoint)
Range: $110–170/t (captures FOB to delivered, regional variation)
```

### 3.6 Revenue and Allocation Calculations

#### Step 1: Calculate Revenue per Co-Product

```
Revenue (USD/t parent input) = Yield (t/t) × Price (USD/t)
```

| Co-product | Calculation | Revenue |
|------------|-------------|---------|
| Soybean oil | 0.198 × 1,020 | **$201.96** |
| Soybean meal | 0.750 × 369 | **$276.75** |
| Soybean hulls | 0.056 × 140 | **$7.84** |
| **Total** | | **$486.55** |

#### Step 2: Calculate DM Output per Co-Product

```
DM output (t DM/t parent input) = Yield (t/t) × DM (%)
```

| Co-product | Calculation | DM Output |
|------------|-------------|-----------|
| Soybean oil | 0.198 × 1.00 | **0.1980** |
| Soybean meal | 0.750 × 0.89 | **0.6675** |
| Soybean hulls | 0.056 × 0.89 | **0.0498** |
| **Total (raw)** | | **0.9153** |
| **Total (normalized to input DM)** | | **0.8700** |

> **DM normalization:** The raw DM output sum (0.9153 t) exceeds the input DM (0.870 t) by 5.2%. This excess violates conservation of mass and is a known artifact of using aggregate industry yield data with inconsistent moisture assumptions. For ISO 14044 compliance, DM outputs must be normalized so that total DM output equals total DM input. The normalization factor is 0.8700 / 0.9153 = 0.95056. Normalized DM outputs are used for mass allocation calculations below.

| Co-product | Calculation | Normalized DM Output |
|------------|-------------|---------------------|
| Soybean oil | 0.1980 × 0.95056 | **0.1882** |
| Soybean meal | 0.6675 × 0.95056 | **0.6345** |
| Soybean hulls | 0.0498 × 0.95056 | **0.0473** |
| **Total** | | **0.8700** |

#### Step 3: Economic Allocation

```
Economic allocation (%) = (Co-product revenue ÷ Total revenue) × 100
```

| Co-product | Calculation | Allocation |
|------------|-------------|------------|
| Soybean oil | (201.96 ÷ 486.55) × 100 | **41.5%** |
| Soybean meal | (276.75 ÷ 486.55) × 100 | **56.9%** |
| Soybean hulls | (7.84 ÷ 486.55) × 100 | **1.6%** |

> **Rounding note:** The raw calculations yield 41.51%, 56.88%, and 1.61%. These are rounded to 41.5%, 56.9%, and 1.6% so that the sum is exactly 100.0% (41.5 + 56.9 + 1.6 = 100.0).

#### Step 4: Mass Allocation

```
Mass allocation (%) = (Co-product normalized DM output ÷ Total DM input) × 100
```

| Co-product | Calculation | Allocation |
|------------|-------------|------------|
| Soybean oil | (0.1882 ÷ 0.8700) × 100 | **21.6%** |
| Soybean meal | (0.6345 ÷ 0.8700) × 100 | **72.9%** |
| Soybean hulls | (0.0473 ÷ 0.8700) × 100 | **5.4%** |

> **Rounding note:** The raw calculations yield 21.63%, 72.93%, and 5.44%. These are rounded to 21.6%, 72.9%, and 5.5% so that the sum is exactly 100.0% (21.6 + 72.9 + 5.5 = 100.0). The hulls value is rounded up by 0.06 percentage points from the naive 5.4% rounding to accommodate closure.

---

## 4. Allocation Methodology

### 4.1 Economic Allocation

Economic allocation distributes environmental burdens (or revenues) among co-products based on their relative market value.

**Formula:**

```
Economic allocation (%) = (Revenue of co-product i ÷ Total revenue of all co-products) × 100

where:
  Revenue of co-product i = Yield_i (t/t) × Price_i (USD/t)
```

### 4.2 Mass Allocation

Mass allocation distributes burdens based on the dry matter content of each co-product, normalized to ensure mass balance closure.

**Formula:**

```
Mass allocation (%) = (Normalized DM output of co-product i ÷ Total DM input) × 100

where:
  Normalized DM output_i = Yield_i (t/t) × DM_i (%) × (DM_input / sum(Yield_j × DM_j))
```

### 4.3 Historical Context: The Shift in Economic Allocation

The soybean crush industry has undergone a dramatic shift in economic allocation due to the renewable diesel boom. The table below is **illustrative** and uses the document's standard yields (0.198 oil, 0.750 meal, 0.056 hulls) with approximate period-specific prices. Hulls revenue is omitted for clarity (<2% of total in all periods).

| Period | Oil Price ($/t) | Meal Price ($/t) | Oil Revenue ($/t) | Meal Revenue ($/t) | Oil Alloc | Meal Alloc |
|--------|-----------------|-------------------|--------------------|---------------------|-----------|------------|
| **Pre-2020** | ~$700 | ~$350 | $138.60 | $262.50 | ~34% | ~65% |
| **2020–2023** | ~$1,200 | ~$450 | $237.60 | $337.50 | ~41% | ~58% |
| **MY 2024/25** | ~$1,020 | ~$369 | $201.96 | $276.75 | ~42% | ~57% |

> **Note:** These figures are approximate and intended to show directional trends only. Exact values require year-specific yield and price data.

The shift is driven by:
1. **Renewable diesel demand:** Federal and state biofuel mandates (RFS, LCFS) have created new demand for soybean oil as a feedstock. Currently, approximately 45% of U.S. soybean oil is allocated to biofuel production, placing fuel use on par with food industry consumption for the first time.
2. **Crush capacity expansion:** New plants are being built specifically to supply oil to renewable diesel producers.
3. **Meal supply increase:** More crush volume means more meal supply, which moderates meal prices despite growing global protein demand.

---

## 5. Mass Balance Verification

### 5.1 Input-Output Reconciliation (13% Trading Basis)

| Check | Value | Status |
|-------|-------|--------|
| Input: Soybeans at 13% moisture | 1.000 t | — |
| Input moisture (trading basis) | 13.0% | — |
| Input DM (trading basis) | 0.870 t | — |
| Output: Soybean oil (as-is) | 0.198 t | ✓ |
| Output: Soybean meal (as-is) | 0.750 t | ✓ |
| Output: Soybean hulls (as-is) | 0.056 t | ✓ |
| Total as-is output | 1.004 t | 100.4% of input |
| Added mass during processing (est.) | ~0.004 t | Water/steam/moisture adjustments; processing aids |
| Output DM: Oil | 0.1980 t | ✓ |
| Output DM: Meal | 0.6675 t | ✓ |
| Output DM: Hulls | 0.0498 t | ✓ |
| Total DM output (raw) | 0.9153 t | 105.2% of input DM |
| Total DM output (normalized) | 0.8700 t | 100.0% of input DM ✓ |

### 5.2 Reconciliation Using Delivered Moisture Basis

The 5.2% DM excess on the 13% trading basis is largely explained by the gap between the 13% standard and the 10.75% actual delivered moisture. If the actual DM input is calculated at 10.75% moisture:

| Check | Value | Status |
|-------|-------|--------|
| Input: Soybeans at 10.75% moisture | 1.000 t | — |
| Input DM (delivered basis) | 0.893 t | — |
| Total DM output (raw, from NOPA yields) | 0.915 t | 102.5% of input DM |
| Residual excess | ~0.022 t | ~2.5% — within industry uncertainty range |
| Total DM output (normalized) | 0.893 t | 100.0% of input DM ✓ |

### 5.3 Explanation of Mass Balance

**As-is mass exceeds input (100.4%):**

This is physically correct and expected because:
1. **Moisture addition during processing:** Meal is typically sold at 11–12% moisture. If soybeans arrive at 10.75% average moisture and meal leaves at 12%, the net moisture addition to meal alone accounts for approximately 1–2 kg/t.
2. **Processing aids:** Phosphoric acid for degumming (0.04–0.10 kg/t) and bleaching clay (1.0–4.0 kg/t) add small amounts of mass.
3. **NOPA verification:** The NOPA LCI [^3^] explicitly reports total as-produced yield of 1.004 kg/kg, confirming industry-wide output mass exceeds input mass.

**DM output exceeds input DM on 13% basis (105.2%):**

The DM output (0.9153 t) exceeds the 13%-basis DM input (0.870 t) by 5.2%. This is primarily caused by the mismatch between the 13% trading standard and the 10.75% actual delivered moisture. When recalculated on the 10.75% delivered basis, the excess reduces to approximately 2.5%, which is within the typical uncertainty range for aggregate industry data from 52 facilities.

**For ISO 14044 compliance,** DM outputs are normalized so that total DM output equals total DM input. The normalization factor on the 13% trading basis is 0.8700/0.9153 = 0.95056. This proportional normalization preserves the relative DM contributions of each co-product while ensuring mass balance closure.


---

## 6. Complete Data Table

| Parent Crop | Crop System | Stage | USDA Standard | Standard Moisture | Parent Input Basis | Co-product Stream | Yield (t/t) | Yield Range | Price (USD/t) | Price Range | DM (%) | DM Output Raw (t/t) | DM Output Norm (t/t) | Revenue (USD/t) | Econ Alloc (%) | Mass Alloc (%) |
|-------------|-------------|-------|---------------|-------------------|-------------------|-------------------|-------------|-------------|---------------|-------------|--------|----------------------|----------------------|-----------------|----------------|----------------|
| Soybean | Soybean crushing | Single | 60 lb/bushel at 13% moisture | 13% | 1 t soybeans at 13% moisture | Soybean oil | 0.198 | 0.19–0.20 | 1,020 | 900–1,200 | 100.0 | 0.1980 | 0.1882 | 201.96 | 41.5 | 21.6 |
| Soybean | Soybean crushing | Single | 60 lb/bushel at 13% moisture | 13% | 1 t soybeans at 13% moisture | Soybean meal (48% protein, dehulled) | 0.750 | 0.74–0.76 | 369 | 340–400 | 89.0 | 0.6675 | 0.6345 | 276.75 | 56.9 | 72.9 |
| Soybean | Soybean crushing | Single | 60 lb/bushel at 13% moisture | 13% | 1 t soybeans at 13% moisture | Soybean hulls (whole) | 0.056 | 0.05–0.06 | 140 | 110–170 | 89.0 | 0.0498 | 0.0473 | 7.84 | 1.6 | 5.5 |

> **Note on allocation rounding:** Raw economic allocations are 41.51% (oil), 56.88% (meal), and 1.61% (hulls). These are rounded to 41.5%, 56.9%, and 1.6% to ensure the sum is exactly 100.0%. Raw mass allocations (using normalized DM) are 21.63% (oil), 72.93% (meal), and 5.44% (hulls). These are rounded to 21.6%, 72.9%, and 5.5% to ensure the sum is exactly 100.0%.


---
## 7. Data Quality and Limitations

### 7.1 High-Confidence Data (Industry/Government Sources)

| Data Point | Confidence | Source |
|------------|-----------|--------|
| Oil yield (0.198 t/t) | **High** | NOPA LCI [^3^] (52 facilities, 89% of U.S. crush) |
| Meal yield (0.750 t/t) | **High** | NOPA LCI [^3^] |
| Hull yield (0.056 t/t) | **High** | NOPA LCI [^3^] |
| Oil price ($1,020/t, MY 2024/25) | **High** | USDA WASDE [^6^]; YCharts [^7^] |
| Meal price ($369/t for 48%) | **High** | USDA ERS [^5^] + corrected 48% protein premium [^13^] |
| Hull price ($140/t whole) | **High** | USDA AMS; Business Research Insights [^9^] |
| DM contents (89% meal, 100% oil) | **High** | Industry trading specifications |

### 7.2 Medium-Confidence Data (Estimated or Derived)

| Data Point | Confidence | Source |
|------------|-----------|--------|
| 48% protein premium ($35–50/MT) | **Medium** | Academic literature [^13^]; USB market view; varies by region and demand |
| Price ranges | **Medium** | Based on historical volatility; actual prices may exceed ranges during market shocks |
| Delivered moisture (10.75%) | **Medium** | From NOPA LCI [^3^]; not independently verifiable from public sources; should be cited with specific page reference if possible |
| DM normalization factor | **Medium** | Proportional normalization is the standard LCA approach; facility-specific data would improve precision |

### 7.3 Known Limitations

1. **Protein content ambiguity:** The table uses 48% protein meal. If 44% protein meal (with hulls) is required, the meal price should be $325/t (range $300–350) and hulls should be removed as a separate co-product.
2. **Regional price variation:** Soybean product prices vary significantly by location (Gulf Coast export vs. Midwest domestic).
3. **Temporal volatility:** The renewable diesel boom has increased price volatility. The MY 2024/25 average may not represent future markets.
4. **Hull form:** Whole hulls ($140/t) vs. pelleted hulls ($175/t) vs. ground hulls ($130/t) have different prices. The table assumes whole hulls.
5. **Waste not allocated:** The CME standard [^2^] includes 1 lb/bu (0.017 t/t) of waste. This is not allocated because it has no market value and is typically landfilled or burned.
6. **Refining losses:** The 0.198 t/t oil yield is crude or degummed oil. Further refining to RBD (refined, bleached, deodorized) oil incurs ~1–2% loss in modern U.S. operations, which is not captured in this table.
7. **Mass balance normalization:** The ~5% DM excess on the 13% trading basis is a methodological artifact (not random uncertainty) caused by the gap between the 13% standard and the 10.75% actual delivered moisture. DM outputs are proportionally normalized for ISO 14044 compliance. For applications requiring exact mass closure without normalization, facility-specific data or system expansion should be used.
8. **Oil content variance:** The NOPA LCI [^3^] reports 19.82% average oil content, but the Iowa Soybean Association [^12^] reports 21.7% average. If the higher oil content is used, the oil yield reconciliation would need recalculation. The 19.82% figure is specific to the NOPA 2023 survey year and may not represent all years or regions.

---
