# Crop Byproduct Allocation Factors for U.S. Dairy Rations: Methodology and Data


This repository contains methodology files and supporting code for calculating allocation factors for crop-processing co-products used in U.S. dairy rations.

The repository accompanies the manuscript:

*Keshavarz Afshar et al., (2026). Transparent and Harmonized Allocation Factors for Crop-Processing Byproducts in U.S. Dairy Rations (under review)*
  


## Overview

The materials in this repository document allocation-factor calculations for **22 U.S. crop-processing systems** and **65 dairy-relevant co-products**.

For each system, the repository provides information used to calculate three allocation factors:

- **Economic allocation**
- **Dry-matter mass allocation**
- **Gross energy allocation**

Where applicable, the repository also documents **multi-stage (cascade) allocation** for systems in which an intermediate product from one processing stage becomes the input to a second stage.

These materials are intended to support transparency and reproducibility for the methodology described in the manuscript. They are designed to be used with an upstream crop life-cycle inventory (LCI) expressed per unit of parent input material.

## Repository contents

### `markdown_files/`
This folder contains system-specific methodology files. Each file documents the processing structure, key assumptions, source-based parameter values, and allocation calculations for one crop-processing system.

Depending on the system, files may include:

- Process-flow description
- Co-product yield assumptions
- Dry matter content
- Gross energy values
- Price inputs
- Dry-matter balance checks
- Allocation equations
- Notes on multi-stage allocation where relevant

## Allocation methods

The repository documents three allocation approaches for co-products within each processing system:

1. **Economic allocation**  
   Allocates burden according to each co-product’s share of total system revenue.

2. **Dry-matter mass allocation**  
   Allocates burden according to each co-product’s share of total dry-matter output.

3. **Gross energy allocation**  
   Allocates burden according to each co-product’s share of total gross-energy output on a dry-matter basis.

All reported allocation factors are dimensionless and are intended to partition the upstream burden of the parent crop among co-products within the defined processing system.

## Processing systems covered

The repository includes methodology files for the crop-processing systems evaluated in the manuscript, including systems such as:

- Almond hulling and shelling
- Barley malting and brewing
- Canola crushing
- Citrus juice processing
- Corn wet milling
- Corn dry milling
- Corn dry-grind ethanol production
- Cotton ginning and cottonseed processing
- Flaxseed crushing
- Oat milling
- Peanut shelling and crushing
- Potato processing
- Rice hulling and milling
- Safflower crushing
- Soybean crushing
- Sugar beet processing
- Sugarcane milling
- Sunflower crushing
- Sweet corn canning
- Wheat flour milling

Please refer to the individual methodology files for the exact system boundaries, co-products included, and assumptions used in each case.

## How to use the allocation factors

These allocation factors are **impact-category neutral**. They can be combined with any upstream crop LCI that is expressed per unit of parent input material, provided that the system boundary is compatible with the one documented in the corresponding methodology file.

General use steps:

1. Identify the processing system that matches the ingredient or co-product being modeled.
2. Confirm that the system boundary and product form are consistent with your LCI and study goal.
3. Select the allocation method appropriate for your analysis.
4. Multiply the upstream burden of the parent crop by the selected allocation factor to estimate the burden assigned to the co-product.

For multi-stage systems, use the pathway and cascade structure documented in the corresponding file.

## Notes on interpretation

- These materials provide **allocation factors**, not complete environmental footprints.
- The factors are intended for use in attributional modeling contexts consistent with the manuscript.
- Values should be interpreted as representative of the assumptions, data sources, and time frame documented in the methodology files.
- Users should review the manuscript and system-specific files before applying the factors in new studies.

## Reproducibility

The repository is intended to provide transparent documentation of the calculations and assumptions used in the associated study. Source-based parameter values, equations, and analysis scripts are included to support review and reuse.

## Citation

If you use these materials, please cite the Zenodo record for this repository and, where relevant, the associated manuscript.

* Keshavarz Afshar, et al. (2026). Transparent and Harmonized Allocation Factors for Crop-Processing Byproducts in U.S. Dairy Rations*  
[full citation will be added when available]

## License

This repository and its contents are licensed under the **Creative Commons Attribution 4.0 International License (CC-BY 4.0)**. You are free to share and adapt the material for any purpose, even commercially, as long as appropriate credit is given.

