# Crop Co-Product Allocation Factors for U.S. Dairy Rations: Methodology and Data

This repository contains the system-specific methodology documentation supporting allocation-factor calculations for crop-processing co-products used in U.S. dairy rations.

The repository accompanies the manuscript:

Keshavarz Afshar et al. (2026). *Transparent and Harmonized Allocation Factors for Crop-Processing Co-products in U.S. Dairy Rations* (under review)

## Overview

The materials in this repository document allocation-factor calculations for **22 U.S. crop-processing systems** supplying **62 dairy-relevant co-products**.

For each system, the repository provides the information used to calculate three allocation factors:

- Economic allocation
- Dry-matter mass allocation
- Gross energy allocation

Where applicable, the repository also documents multi-stage allocation for systems in which an intermediate product from one processing stage becomes the input to a second stage.

These materials are intended to support transparency and reproducibility for the methodology described in the manuscript. They are designed to be used with an upstream crop life-cycle inventory (LCI) expressed per unit of parent input material.

## Repository contents

### `markdown_files/`

System-specific methodology files. Each file documents the processing structure, key assumptions, source-based parameter values, and allocation calculations for one crop-processing system.

Depending on the system, files may include:

- Process-flow description
- Co-product yield assumptions
- Dry matter content
- Gross energy values
- Price inputs
- Dry-matter balance checks
- Allocation equations
- Notes on multi-stage allocation where relevant

`Gross_Energy-Reference.md` documents the gross energy values and uncertainty bounds used across all systems, including the derivation of composition-based ranges.

### `monte_carlo_uncertainty_v11.py`

This script implements the uncertainty analysis reported in the manuscript: PERT-distributed sampling of co-product yields, market prices and gross energy contents (10,000 iterations per processing system), the deterministic and percentile allocation factors, the cross-method spread, and the block divergence index. Running it reproduces the allocation factors and 90% confidence intervals reported in the manuscript's tables. It requires Python 3.11 with NumPy, pandas, SciPy and Matplotlib.

## Allocation methods

The repository documents three allocation approaches for co-products within each processing system:

**Economic allocation** — allocates burden according to each co-product's share of total system revenue.

**Dry-matter mass allocation** — allocates burden according to each co-product's share of total dry-matter output.

**Gross energy allocation** — allocates burden according to each co-product's share of total gross-energy output on a dry-matter basis.

All reported allocation factors are dimensionless and are intended to partition the upstream burden of the parent crop among co-products within the defined processing system. Factors are reported on all three bases without a recommended default; the appropriate choice follows from the goal and scope of the study applying them.

## Processing systems covered

The repository covers the 22 processing systems evaluated in the manuscript:

| Parent crop | Processing system |
|---|---|
| Almond | Hulling and shelling |
| Barley | Malting → brewing (two-stage) |
| Canola | Crushing |
| Citrus | Juice processing |
| Corn | Wet milling |
| Corn | Dry milling |
| Corn | Dry-grind ethanol |
| Cotton | Ginning, seed sold (Pathway A) |
| Cotton | Ginning followed by seed crushing (Pathway B) |
| Flaxseed | Crushing |
| Oat | Milling |
| Peanut | Shelling → crushing (two-stage) |
| Potato | Processing |
| Rice | Hulling → milling (two-stage) |
| Safflower | Crushing |
| Soybean | Crushing |
| Sugar beet | Processing |
| Sugarcane | Milling |
| Sunflower | Crushing |
| Sweet corn | Canning |
| Wheat | Flour milling |
| Wheat | Dry-grind ethanol |

Cotton is represented as two alternative pathways rather than a single cascade, because whole cottonseed is itself a marketed dairy feed as well as an input to crushing. A given tonne of seed follows one pathway or the other, so the two factor sets are alternatives and should not be combined.

Please refer to the individual methodology files for the exact system boundaries, co-products included, and assumptions used in each case.

## How to use the allocation factors

These allocation factors are impact-category neutral. They can be combined with any upstream crop LCI expressed per unit of parent input material, provided the system boundary is compatible with the one documented in the corresponding methodology file.

General use steps:

1. Identify the processing system that matches the ingredient or co-product being modeled.
2. Confirm that the system boundary and product form are consistent with your LCI and study goal.
3. Select the allocation method appropriate for your analysis.
4. Multiply the upstream burden of the parent crop by the selected allocation factor to estimate the burden assigned to the co-product.

Apply the factors to an **unallocated** upstream inventory expressed per tonne of parent input at the plant gate. Applying them to a database record in which co-product allocation has already been performed would partition the same burden twice.

For multi-stage systems, use the pathway and cascade structure documented in the corresponding file.

## Notes on interpretation

- These materials provide allocation factors, not complete environmental footprints.
- The factors are intended for use in attributional modeling contexts consistent with the manuscript.
- Values should be interpreted as representative of the assumptions, data sources, and time frame documented in the methodology files (2024–2025 price and yield period).
- Users should review the manuscript and the system-specific files before applying the factors in new studies.

## Citation

If you use these materials, please cite the associated manuscript:

Keshavarz Afshar, R., Tricarico, J., Medel-Jiménez, F., Kukal, M.S., Gulati, D., Fishman, R., and Purdy, A.J. (2026). *Transparent and Harmonized Allocation Factors for Crop-Processing Co-products in U.S. Dairy Rations.* [full citation will be added when available]

## License

This repository and its contents are licensed under the Creative Commons Attribution 4.0 International License (CC-BY 4.0). You are free to share and adapt the material for any purpose, even commercially, as long as appropriate credit is given.
