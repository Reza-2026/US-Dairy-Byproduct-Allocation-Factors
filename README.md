# US-Dairy-Byproduct-Allocation-Factors
# Crop Byproduct Allocation Factors for U.S. Dairy Rations: Methodology & Data

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

This repository contains the comprehensive, line-by-line methodology documentation for calculating co-product allocation factors for **22 U.S. crop-processing systems**, yielding factors for **65 dairy-relevant co-products**. 

It serves as the open-access supplementary data and methodological foundation for the manuscript: *"Transparent and Harmonized Allocation Factors for Crop-Processing Byproducts in U.S. Dairy Rations."*

## 📊 Repository Contents

- **`/methodologies/`**: Contains 22 detailed, "bulletproof" Markdown files. Each file documents the process flow, yield derivations, dry matter (DM) balances, price verifications, and allocation calculations for a specific crop-processing system.
- **`/data/`**: Contains the master summary tables (`.csv`) of the final economic, mass, and gross energy allocation factors, as well as the Monte Carlo uncertainty bounds.
- **`/scripts/`**: Contains the Python scripts used for the Monte Carlo simulations (10,000 iterations per system) and the cross-method divergence index calculations.

## 🔬 Methodological Standards

Every methodology file in this repository was subjected to rigorous forensic fact-checking and adheres to strict LCA standards:
- **ISO 14044 Compliance**: Prioritizes physical relationships (mass/energy) and economic valuation. Multi-stage processes (e.g., Cotton ginning $\rightarrow$ crushing, Rice hulling $\rightarrow$ milling) utilize **cascade allocation** to prevent double-counting and properly handle intermediate products.
- **Strict Mass Balance Verification**: Every system includes a step-by-step Dry Matter (DM) input-output reconciliation. Unallocated losses (e.g., dust, moisture evaporation, wastewater organics) are explicitly quantified.
- **The Midpoint Rule**: All chosen yield and price parameters are verified to be the exact mathematical midpoints of their stated, evidence-backed ranges.
- **No "Residual Plugs"**: Co-product yields are independently sourced from industry/USDA data rather than back-calculated as algebraic residuals to force mass balance closure.
- **Fact-Checked References**: All citations (USDA ERS, NASS, AMS, FAO, Feedipedia, industry associations) have been verified for existence, correct titles, and accurate data attribution. Ghost databases and hallucinated references have been systematically eliminated.

## 🌾 Index of Crop-Processing Systems

| Crop | Processing System | Primary Co-Products Allocated |
| :--- | :--- | :--- |
| **Almond** | Hulling & Shelling | Kernels, Hulls, Shells |
| **Barley** | Malting & Brewing | Malt, Beer, Spent Grains, Sprouts |
| **Canola** | Crushing | Oil, Meal |
| **Citrus** | Juice Processing | Juice, Wet Pulp |
| **Corn** | Wet Milling | Starch, Gluten Meal, Gluten Feed, Germ, Steep Liquor |
| **Corn** | Dry Milling | Grits/Meal, Hominy Feed, Germ |
| **Corn** | Dry-Grind Ethanol | Ethanol, DDGS, Corn Oil |
| **Cotton** | Ginning & Seed Crushing | Lint, Seed, Oil, Meal, Hulls, Linters |
| **Flaxseed** | Crushing | Linseed Oil, Linseed Meal |
| **Oat** | Milling | Food Oats, Hulls, Mill Feed |
| **Peanut** | Shelling & Crushing | Oil, Meal, Hulls |
| **Potato** | Fresh-Cut Processing | Processed Products, Waste/Peels |
| **Rice** | Hulling & Milling | White Rice, Bran, Hulls, Mill Feed |
| **Safflower** | Crushing | Safflower Oil, Meal |
| **Soybean** | Crushing | Soybean Oil, Meal (48%), Hulls |
| **Sugar Beet** | Processing | Refined Sugar, Wet Pulp, Molasses |
| **Sugarcane** | Milling | Raw Sugar, Molasses, Bagasse |
| **Sunflower** | Crushing | Sunflower Oil, Meal, Hulls |
| **Sweet Corn** | Canning | Edible Kernels, Cannery Waste |
| **Wheat** | Flour Milling | Flour, Bran, Middlings |

*(Note: Navigate to the `/methodologies/` folder and click on any `.md` file to view the full mass-balance and allocation math for that specific system.)*

## 📈 Allocation Methods Documented

For each co-product, we provide three dimensionless allocation factors:
1. **Economic Allocation**: Partitions burden based on relative market value (revenue). Highly sensitive to market volatility and US policy (e.g., the US Sugar Program).
2. **Dry-Matter Mass Allocation**: Partitions burden based on the physical dry matter content of the co-products.
3. **Gross Energy Allocation**: Partitions burden based on the gross energy content (MJ/kg DM) of the co-products.

Additionally, a **Cross-Method Divergence Index** is calculated for each co-product to identify which ingredients are highly sensitive to the choice of allocation method versus those that are methodologically stable.

## 📥 How to Use This Data

These allocation factors are **impact-category neutral** and designed to interface with any upstream crop life-cycle inventory (LCI) expressed per unit of parent input (e.g., per kg of rough rice, per kg of seed cotton, per kg of soybeans). 

To apply these factors:
1. Identify the crop-processing system that matches your LCA system boundary.
2. Select the appropriate allocation method (Economic, Mass, or Energy) based on your study's goal and scope (ISO 14044).
3. Multiply the upstream environmental burden of the parent crop by the chosen allocation factor to assign the burden to the specific byproduct.

*For systems with dual pathways (e.g., Cottonseed used directly as feed vs. crushed for oil/meal), ensure you select the pathway that matches the physical reality of the supply chain you are modeling.*

## 📝 Citation

If you use this methodology database or the resulting allocation factors in your research, please cite both the repository and the main manuscript:

**For the Dataset & Methodology (This Repository):**
> [Author Last Name], [First Initial]., et al. (2026). *Crop Byproduct Allocation Factors for U.S. Dairy Rations: Methodology & Data* [Data set]. Zenodo. https://doi.org/10.5281/zenodo.[XXXXXXX]

**For the Main Manuscript:**
> [Author Last Name], [First Initial]., et al. (2026). "Transparent and Harmonized Allocation Factors for Crop-Processing Byproducts in U.S. Dairy Rations." *[Journal Name]*, [Volume](Issue), [Page range]. https://doi.org/[XXXXXX]

## 📄 License

This repository and its contents are licensed under the **Creative Commons Attribution 4.0 International License (CC-BY 4.0)**. You are free to share and adapt the material for any purpose, even commercially, as long as appropriate credit is given.

## 📬 Contact & Contributions

For questions regarding specific yield assumptions, mass balance closures, or to report updates based on new crop-year data (e.g., USDA WASDE updates), please open an Issue on this repository or contact the corresponding author:

**[Corresponding Author Name]**  
[Institution / Organization]  
[Email Address]  
[ORCID ID]
