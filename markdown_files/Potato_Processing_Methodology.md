# Potato Processing: Co-Product Allocation Methodology, Data Sources, and Calculations

**Document Version:** 1.0
**Date:** June 2026  
**Basis:** 1 metric ton (t) of fresh potatoes at ~21% DM (~79% moisture)  
**Price Period:** 2024–2025 average (unless otherwise noted)

---

## Table of Contents

1. [Standard Basis and Conversions](#1-standard-basis-and-conversions)
2. [Data Sources and References](#2-data-sources-and-references)
3. [Potato Processing System](#3-potato-processing-system)
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
| **Parent crop** | Potato (*Solanum tuberosum*) | — |
| **Input quantity** | 1 metric ton (1,000 kg) | — |
| **Moisture content** | ~79% (21% DM) | USDA nutritional data; typical for processing-grade Russet Burbank potatoes [^1^] |
| **Dry matter (DM) input** | 0.210 t DM/t fresh potatoes | Calculated: 1.000 × 0.21 = 0.210 |
| **Cwt equivalent** | 22.05 cwt/t | 1,000 kg ÷ 45.359 kg/cwt (100 lb) |
| **Typical starch content** | ~13–18% (fresh weight basis) | USDA nutritional data [^1^]; Wiley (Bertoft & Blennow, 2016); Springer reviews. Typical for processing-grade Russet Burbank: ~15–17%. |

### 1.2 Convention for Adopted Values

Every yield, price, and DM% in this document is reported as an adopted point value together with the range it was drawn from. **Unless a row states otherwise, the adopted value is the midpoint of its stated range**, and the range is the parameter that carries the evidence. Point values are given to the precision the underlying sources support and are not intended to imply plant-level accuracy. Derived quantities (DM outputs, revenues, allocation percentages) are carried at four decimals internally and reported to one decimal place.

### 1.3 Unit Conversions

| Conversion | Factor |
|------------|--------|
| 1 cwt potatoes | 100 lb = 45.359 kg |
| 1 lb | 0.453592 kg = 0.000453592 t |
| 1 t fresh potatoes | 22.05 cwt |
| 1 short ton | 2,000 lb = 0.907185 metric ton |
| 1 metric ton | 2,204.62 lb = 1.10231 short tons |

> **Note on potato moisture:** Unlike grains, potatoes have no USDA-defined standard moisture for trading. Fresh potatoes are sold by weight at their natural moisture content. The moisture varies by variety (18–25% DM), growing conditions, and storage duration. Processing-grade potatoes (typically Russet Burbank) have ~20–23% DM. This document uses 21% DM as the standard basis, consistent with industry averages for processing potatoes and USDA nutritional composition data.

> **Note on potato types:** Potatoes are broadly classified into: (1) **Russet** (high starch, ~20–23% DM, ideal for fries and baking), (2) **Red/White** (low starch, ~16–19% DM, ideal for boiling and salads), and (3) **Yellow** (medium starch, ~18–21% DM, all-purpose). This document assumes Russet-type processing potatoes at 21% DM, which is the dominant variety used in commercial potato processing in the United States.

---

## 2. Data Sources and References

### 2.1 Primary Sources

| Citation | Full Title | Type | URL |
|----------|-----------|------|-----|
| [^1^] | USDA FoodData Central — Potatoes, raw, flesh and skin | Government (USDA) | https://fdc.nal.usda.gov/ |
| [^2^] | FAO (2001). *POTATO: Post-harvest Operations* (D. Mejía & B. Lewis, eds.) | International Organization | https://www.fao.org/fileadmin/user_upload/inpho/docs/Post_Harvest_Compendium_-_Potato.pdf |
| [^3^] | USDA ERS (2025). *Vegetables and Pulses Outlook* | Government (USDA) | https://ers.usda.gov/ |
| [^4^] | USDA NASS (2025). *Potato Statistics* | Government (USDA) | https://www.nass.usda.gov/ |
| [^5^] | IndexBox (2024). *World - Potato - Market Analysis, Forecast, Size, Trends and Insights* | Industry/Market | https://www.indexbox.io/ |
| [^6^] | Lisińska & Leszczyński (1989). *Potato Science and Technology* | Academic | — |
| [^7^] | Feedipedia. *Potato by-products* (INRAE-CIRAD-AFZ feed encyclopedia) | Academic/Reference | https://www.feedipedia.org/ |
| [^8^] | OECD-FAO (2025). *OECD-FAO Agricultural Outlook 2025-2034*, Chapter 10 ("Other products"), Section 10.1 ("Roots and tubers") | International Organization | https://www.oecd.org/ |

### 2.2 How Sources Were Used

- **Yield data:** FAO [^2^] and Lisińska & Leszczyński [^6^] provided potato processing yield data. The ranges reflect variation across peeling methods (steam, abrasive, lye), potato quality, and product specifications. USDA ERS [^3^] and USDA NASS [^4^] provided production and farm-level price statistics.
- **Price data (products):** IndexBox [^5^] provided processed potato product prices. USDA ERS [^3^] provided raw potato farm-gate prices. Prices reflect peeled/cut potatoes for foodservice and further processing.
- **Price data (waste):** Feedipedia [^7^] and industry estimates provided potato waste prices for animal feed markets. Waste price data is inherently uncertain due to the non-commodity nature of potato processing waste.
- **DM contents:** USDA FoodData Central [^1^] provided nutritional composition data. Feedipedia [^7^] provided potato by-product composition data including peel DM%. FAO [^2^] provided processing waste composition data.
- **Market context:** OECD-FAO [^8^] provided global production and consumption projections for roots and tubers, used to check that the price levels adopted here are consistent with the direction of the wider potato market.

---

## 3. Potato Processing System

### 3.1 Process Description

Potato processing for the fresh-cut market involves the following steps:

1. **Receiving and storage:** Potatoes are received at the processing facility and stored under controlled temperature and humidity conditions to maintain quality.
2. **Washing:** Soil, debris, and surface contaminants are removed using water flumes and brush washers.
3. **Peeling:** Steam, abrasive, or lye peeling removes the skin. Steam peeling is the most common industrial method, generating 5–12% of input weight as peel waste. Lye peeling produces additional chemical waste.
4. **Trimming and sorting:** Defects, bruises, green spots, and off-size potatoes are removed by manual or automated inspection. Defective potatoes are redirected to waste.
5. **Cutting:** Peeled potatoes are cut into desired shapes (fries, wedges, cubes, slices) using water-guided cutting blades.
6. **Blanching (optional):** Cut potatoes may be briefly heated in hot water or steam to inactivate enzymes, reduce browning, and improve texture.
7. **Packaging:** Products are packaged in bags, cartons, or bulk containers for shipment to foodservice or retail customers.

**Co-products generated:**
- **Processed potato products:** Peeled, cut, and sorted potatoes ready for further processing or foodservice use. This category includes fresh-cut potatoes, peeled whole potatoes, and lightly processed potato items.
- **Potato-processing waste:** Peels, trimmings, reject potatoes, and other solid by-products. This stream is typically used for animal feed (primarily cattle), anaerobic digestion, or composting.

> **Note on processing scope:** This document models basic potato processing (washing, peeling, cutting, sorting) that does NOT involve significant dehydration or frying. Products are fresh or lightly processed potatoes with moisture content essentially unchanged from the raw input. Processes involving deep frying (chips, french fries) or dehydration (flakes, granules) would have dramatically different yields, DM%, and prices, and would require separate allocation models.

### 3.2 Process Flow

```
1 t fresh potatoes at ~21% DM (0.210 t DM)
        │
        ▼
  ┌─ POTATO PROCESSING ───────────────────────────┐
  │                                                 │
  │  Processing losses: ~0.0016 t DM (~0.76%)      │
  │  (dissolved solids in wash water, starch loss)  │
  │                                                 │
  │  Processed potato products:                    ◄── co-product
  │    0.84 t as-is at 21% DM (0.1764 t DM)        │
  │                                                 │
  │  Potato processing waste:                      ◄── co-product
  │    0.16 t as-is at 20% DM (0.0320 t DM)        │
  │                                                 │
  └─────────────────────────────────────────────────┘

TWO CO-PRODUCTS from 1 t fresh potatoes:
  Processed potato products:  0.84 t as-is,  0.1764 t DM
  Potato processing waste:    0.16 t as-is,  0.0320 t DM
  Total:                                   0.2084 t DM  (from 0.210 t input; 0.0016 t deficit)
```

---

## 4. Co-Product Yields and Properties

### 4.1 Yields (per tonne of potatoes input)

| Co-product | Yield (t/t potatoes) | Range | Source & Calculation |
|------------|---------------------|-------|---------------------|
| **Processed potato products** | 0.84 | 0.80–0.88 | Industry average for peeling, trimming, and sorting operations [^2^][^6^]. Yields vary with peeling method (steam peeling recovers ~85–88% vs. abrasive peeling at ~80–83%), potato size and quality, and product specifications. |
| **Potato processing waste** | 0.16 | 0.12–0.20 | Set as the complement of the product yield (1.00 − 0.84). Comprises peels (~5–12% of input), trimmings and defects (~2–5%), and other solid rejects, which together bracket the adopted value. The range is the inverse of the product yield range: higher product recovery means less waste. |

> **Note on yield relationship:** Product and waste yields are inversely related: when more product is recovered, less waste is generated. The waste yield in this table is set as the complement of the product yield (0.16 = 1.00 − 0.84), so the two sum to 1.00 t/t **by construction rather than by measurement**. Real plants also discharge a wash and process water stream carrying dissolved solids, which this two-stream model does not track; its dry matter appears as the 0.76% deficit in Section 7.2.

### 4.2 Dry Matter Contents

| Co-product | DM (%) | Basis |
|------------|--------|-------|
| Processed potato products | 21.0% | Same as fresh potato input. Basic processing (peeling, cutting, sorting) does not significantly change moisture content. Peeled potato flesh has similar DM% to whole potatoes (~20–22%) [^1^]. Washing may add trace surface water, but this is negligible in the overall mass balance. |
| Potato processing waste | 20.0% | Peels dominate the waste stream, and Feedipedia [^7^] reports potato peel at 20.1% DM on average (range 14.3–24.7%). Trimmings are close to flesh DM (~20–22%). The adopted 20% follows the Feedipedia peel average and sits just below whole-potato DM% [^6^][^7^]. |

### 4.3 DM Output per Tonne of Potatoes

| Co-product | Calculation | DM Output (t/t potatoes) |
|------------|-------------|-------------------------|
| **Processed potato products** | 0.84 × 0.21 | **0.1764** |
| **Potato processing waste** | 0.16 × 0.20 | **0.0320** |
| **Total** | | **0.2084** |

---

## 5. Prices

### 5.1 Price Table

| Co-product | Price (USD/t) | Range | Source | Notes |
|------------|--------------|-------|--------|-------|
| **Processed potato products** | 1,000 | 700–1,300 | IndexBox [^5^]; USDA ERS [^3^] | 2024–2025 average for peeled/cut potatoes for foodservice and further processing. Price reflects value added through peeling, cutting, and packaging. Raw potatoes typically sell for $200–350/t at farm level [^3^][^4^]; processing adds significant value through labor, equipment, and quality assurance. |
| **Potato processing waste** | 35 | 20–50 | Feedipedia [^7^]; industry estimates | 2024–2025 average for potato waste used as animal feed (primarily cattle). Price varies with waste composition, moisture content, starch content, and proximity to livestock operations. Peel/trim waste typically fetches $15–40/t; cull whole potatoes (higher DM, more feed value) command $30–75/t. The $20–50/t range reflects the mixed composition of the waste stream (predominantly peels and trimmings). Some facilities pay for disposal rather than sell waste, effectively giving it a negative value. |

### 5.2 Price Verification

**Processed potato products:**

```
USDA ERS (2025): raw potato farm prices ~$250-350/t (season average)
IndexBox (2024): peeled/cut potatoes for foodservice ~$700-1,300/t
Processing adds ~$400-800/t in value

Adopted: $1,000/t, the midpoint of the $700–1,300 range
```

**Potato processing waste:**

```
Feedipedia: potato by-products for animal feed; peel/trim ~$15-40/t
Cull whole potatoes (if present in waste stream): ~$30-75/t
Industry estimates for mixed waste: ~$20-50/t
Disposal cost (if not sold): ~$20-50/t (negative revenue)

Adopted: $35/t, the midpoint of the $20–50 range
```

### 5.3 Revenue per Tonne of Potatoes

| Co-product | Calculation | Revenue (USD/t potatoes) |
|------------|-------------|-------------------------|
| **Processed potato products** | 0.84 × 1,000 | **$840.00** |
| **Potato processing waste** | 0.16 × 35 | **$5.60** |
| **Total** | | **$845.60** |

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
| Processed potato products | (840.00 ÷ 845.60) × 100 | **99.3%** |
| Potato processing waste | (5.60 ÷ 845.60) × 100 | **0.7%** |
| **Total** | | **100.0%** |

> **Rounding note:** The raw calculations yield 99.34% (products) and 0.66% (waste). These are rounded to 99.3% and 0.7% so that the sum is exactly 100.0%.

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
| Processed potato products | (0.1764 ÷ 0.2084) × 100 | **84.6%** |
| Potato processing waste | (0.0320 ÷ 0.2084) × 100 | **15.4%** |
| **Total** | | **100.0%** |

> **Rounding note:** The raw calculations yield 84.65% (products) and 15.35% (waste). These are rounded to 84.6% and 15.4% so that the sum is exactly 100.0%.

### 6.3 Comparison: Economic vs. Mass Allocation

| Co-product | Economic Allocation | Mass Allocation | Difference |
|------------|-------------------|----------------|------------|
| Processed potato products | 99.3% | 84.6% | +14.7 pp |
| Potato processing waste | 0.7% | 15.4% | −14.7 pp |

The difference reflects the value disparity between processed potato products ($1,000/t) and waste ($35/t), a ratio of about 29:1. Processed products command 99.3% of revenue but carry 84.6% of the dry matter. It is worth separating the two figures: the **price ratio** is one of the widest in this work, but the resulting **allocation divergence**, 14.7 pp, is one of the narrower ones — smaller than almond, sweet corn, citrus, safflower, peanut, sunflower, wheat, flaxseed, sugarbeet, canola, corn or oat milling. The reason is that the waste stream is small in dry matter terms, so even assigning it nothing on an economic basis moves the product share by only about 15 points. A wide price ratio does not by itself produce a wide divergence between methods.

---

## 7. Mass Balance Verification

### 7.1 Input-Output Reconciliation

| Check | Value | Status |
|-------|-------|--------|
| Input: Fresh potatoes | 1.000 t | — |
| Input DM% | 21% | — |
| Input DM | 0.210 t | — |
| Output: Products (as-is) | 0.840 t | ✓ |
| Output: Waste (as-is) | 0.160 t | ✓ |
| Total as-is output | 1.000 t | 100.0% of input, by construction |
| Untracked as-is loss | 0.000 t | Zero by definition, not by measurement |
| Output DM: Products | 0.1764 t | ✓ |
| Output DM: Waste | 0.0320 t | ✓ |
| Total DM output | 0.2084 t | 99.2% of input DM — the informative check |

### 7.2 DM Balance Detail

| Item | Value | Notes |
|------|-------|-------|
| Input DM (1 t potatoes at 21% DM) | 0.2100 t | 1.000 × 0.21 |
| **Output DM — co-products:** | | |
| Processed potato products | 0.1764 t | 0.84 t × 21% DM |
| Potato processing waste | 0.0320 t | 0.16 t × 20% DM |
| Total co-product DM | **0.2084 t** | |
| DM balance gap | −0.0016 t | −0.76% of input DM |

> **Balance assessment:** The DM output is 0.0016 t (0.76%) below the DM input. This small deficit represents dissolved solids in wash water and starch losses during processing that are not captured in the solid waste stream. During potato washing, peeling, and blanching, a small fraction of starch and other soluble solids dissolves in the process water and is discharged as wastewater rather than being captured as a co-product. The balance is well within the acceptable range and consistent with literature reporting ~0.5–2% DM losses to wastewater [^6^].

### 7.3 As-Is Mass Balance

| Item | Value | Notes |
|------|-------|-------|
| Input (fresh potatoes) | 1.000 t | — |
| **Output:** | | |
| Processed potato products | 0.840 t | — |
| Potato processing waste | 0.160 t | — |
| **Total output** | **1.000 t** | |
| **Untracked as-is loss** | **0.000 t** | Not measured — the waste yield is set as 1.00 − 0.84, so this term is zero by definition |
| **Balance** | **1.000 t** | Closes by construction (see note below) |

> **Note on as-is vs. DM balance:** The as-is balance closes at exactly 1.000 t because the waste yield is defined as the complement of the product yield, not because the two streams were measured independently. The check that carries information is the dry matter balance, which does not close: 0.2084 t out against 0.2100 t in, a deficit of 0.0016 t (0.76%).
>
> Read as a water balance, the model implies 0.840 × 79% + 0.160 × 80% = 0.7916 t of water leaving against 0.790 t entering — a 0.0016 t gain, exactly offsetting the dry matter deficit. In a real plant these are two separate physical facts: potatoes pick up some wash water, and some starch and soluble solids leave in the process water. Because the wastewater stream is not modelled as a third output, the two effects are compressed into a single residual. The magnitude, under 1% of input DM, is consistent with reported losses of ~0.5–2% to wastewater [^6^], but it should be read as a residual rather than as a measured loss.

---

## 8. Complete Data Table

| Parent Crop | Crop System | Stage | USDA Standard | Typical Moisture | Parent Input Basis | Co-product Stream | Yield (t/t) | Yield Range | Price (USD/t) | Price Range | DM (%) | DM Output (t/t) | Revenue (USD/t) | Econ Alloc (%) | Mass Alloc (%) |
|-------------|-------------|-------|---------------|-------------------|-------------------|-------------------|-------------|-------------|---------------|-------------|--------|-----------------|-----------------|----------------|----------------|
| Potato | Potato processing | Single | U.S. No. 1 grade | ~79% (21% DM) | 1 t fresh potatoes at 21% DM | Processed potato products | 0.84 | 0.80–0.88 | 1,000 | 700–1,300 | 21.0 | 0.1764 | 840.00 | 99.3 | 84.6 |
| Potato | Potato processing | Single | U.S. No. 1 grade | ~79% (21% DM) | 1 t fresh potatoes at 21% DM | Potato processing waste | 0.16 | 0.12–0.20 | 35 | 20–50 | 20.0 | 0.0320 | 5.60 | 0.7 | 15.4 |

> **Note on allocation rounding:** Raw economic allocations are 99.34% (products) and 0.66% (waste), rounded to 99.3% and 0.7% to sum to exactly 100.0%. Raw mass allocations are 84.65% (products) and 15.35% (waste), rounded to 84.6% and 15.4% to sum to exactly 100.0%.

> **Note on "Typical Moisture":** Unlike grains, potatoes have no USDA-defined standard moisture for trading. The column header uses "Typical Moisture" rather than "Standard Moisture" to reflect this distinction. The 21% DM value represents an industry average for processing-grade Russet Burbank potatoes.

---

## 9. Data Quality and Limitations

### 9.1 High-Confidence Data

| Data Point | Confidence | Source |
|------------|-----------|--------|
| Product yield (0.84 t/t) | **High** | Peeling and trimming recoveries are well documented [^2^][^6^] |
| Product DM% (21%) | **High** | Same as raw potato DM%; consistent with no-dehydration processing [^1^] |
| Waste yield (0.16 t/t) | **Medium-High** | Defined as the complement of the product yield rather than measured; consistent with the reported peel and trim fractions |
| Product price ($1,000/t) | **Medium-High** | Reasonable for peeled/cut potatoes; wide range reflects product mix and contract terms |

### 9.2 Medium-Confidence Data

| Data Point | Confidence | Source |
|------------|-----------|--------|
| Waste DM% (20%) | **Medium** | Weighted average of peels and trimmings; Feedipedia reports avg peel DM of 20.1%; actual composition varies by facility [^7^] |
| Waste price ($35/t) | **Medium** | Limited market data; varies with region, waste composition, and end use. Prices above ~$40/t are reached only where the stream carries cull whole potatoes, not for peel and trim waste alone |
| Product yield range (0.80–0.88) | **Medium** | Varies significantly with peeling method and potato quality |
| Waste yield range (0.12–0.20) | **Medium** | Inverse of product yield range; actual waste composition varies |
| Price ranges | **Medium** | Potato product prices are less standardized than grain prices |
| Input DM% (21%) | **Medium** | Varies by variety (18–25%), growing conditions, and storage duration |

### 9.3 Known Limitations

1. **Generic "processed potato products" category:** This table treats all processed potato products as a single category. In practice, potato processing produces multiple distinct products (frozen fries, chips, dehydrated flakes, fresh-cut) with different yields, DM%, and prices. The single-category approach averages these differences. Studies focused on a specific product type should use product-specific data rather than this generic model.

2. **No standard moisture for potatoes:** Unlike grains, potatoes have no USDA-defined standard moisture for trading. The 21% DM basis used here is an industry average for processing-grade Russet potatoes. Actual DM% can range from 18% (low-starch varieties) to 25% (high-starch varieties under ideal growing conditions). This 7-percentage-point range in input DM% creates significant uncertainty in mass allocation calculations. If input DM% were 18% instead of 21%, the mass allocation to products would decrease (less product DM relative to waste DM).

3. **Waste composition varies:** Potato processing waste is a heterogeneous stream that can include peels, trimmings, reject potatoes, and (in some configurations) wastewater sludge. The DM% and price of waste depend heavily on its composition. If a facility generates wastewater sludge as a separate stream, the waste DM% would be much lower (~5–15%) and the yield would be different. Facilities that separate peel waste from trim waste may have two distinct co-product streams with different DM% and prices.

4. **Economic-vs-mass allocation divergence:** The ~29:1 price ratio between products ($1,000/t) and waste ($35/t) means economic allocation assigns almost the whole burden to products (99.3%), while mass allocation assigns a meaningful share to waste (15.4%). The gap of 14.7 pp is moderate by comparison with the other crops in this work (see Section 6.3), because the waste stream carries only about a sixth of the dry matter. Practitioners should nonetheless state which method they use, since the waste stream's burden differs by more than a factor of twenty between them.

5. **Waste price uncertainty:** Potato waste may have a negative value (disposal cost) at some facilities or a positive value (animal feed) at others, depending on proximity to livestock operations and local regulations. The $35/t average hides this bimodal distribution. At some facilities, waste is given away or the facility pays for disposal, which would make the economic allocation to products even more extreme (approaching 100%). The upper bound of the $20–50/t range reflects mixed waste that includes some cull whole potatoes; pure peel/trim waste typically does not exceed $40/t.

6. **Scope limited to basic processing:** This table does not cover processes involving significant dehydration or frying. Note when reading the figures below that fried products **gain dry matter from absorbed frying oil**, which is a purchased non-potato input: at ~0.60 t/t and ~37% DM, frozen fries carry roughly 0.225 t DM against 0.210 t of potato DM input, and potato chips more still. Any allocation model for those systems must treat the frying oil as an input rather than as recovered potato mass. Frozen french fry production would have:
   - Product yield: ~0.55–0.65 t/t
   - Product DM%: ~35–40%
   - Additional co-product: used frying oil
   - Product price: ~$800–1,200/t
   
   Potato chip manufacturing would have:
   - Product yield: ~0.30–0.35 t/t
   - Product DM%: ~95–97%
   - Additional co-product: used frying oil, potato scraps
   - Product price: ~$2,000–4,000/t
   
   Dehydrated potato flake production would have:
   - Product yield: ~0.20–0.25 t/t
   - Product DM%: ~88–92%
   - Additional co-product: potato peel waste, process water
   - Product price: ~$1,200–2,000/t
   
   Each of these processes would require a separate allocation model with different yields, DM%, and prices.

7. **Seasonal and storage effects:** Potato DM% increases during storage (moisture loss). Potatoes processed shortly after harvest may have 20–21% DM, while those stored for 6–8 months may reach 23–25% DM. This affects the DM balance and mass allocation. The 21% DM basis used here represents a typical average across the processing season, but studies focused on early-season or late-season processing should adjust accordingly.

8. **Water use not modeled:** Potato processing uses significant volumes of water for washing, peeling, and blanching. While this water does not change the mass balance of products and waste (the water is discharged as wastewater), it represents an environmental burden that should be allocated along with other processing inputs. The water balance is outside the scope of this allocation methodology.

---