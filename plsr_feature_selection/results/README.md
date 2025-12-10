# Results - PLSR Feature Selection Output

This folder contains all output files from PLSR feature selection analyses, including Excel reports and figures.

---

## Folder Structure

```
results/
│
├── excel_data_files/             # Performance metrics & selected features
│   ├── acoustic_debye_temperature_results.xlsx
│   ├── Cp_300K_results.xlsx
│   ├── Debye_temperature_MP_results.xlsx
│   ├── thermal_conductivity_300K_results.xlsx
│   ├── thermal_conductivity_with_gamma_results.xlsx
│   ├── thermal_expansion_300K_results.xlsx
│   └── thermal_expansion_with_gamma_results.xlsx
│
└── figures/                     # Plots 
# (1.pls component analysis, 2.loading heatmaps, and 3.feature contributions)
    ├── Debye_temperature/
    ├── Debye_temperature_acoustic/
    ├── Specific_heat_at_constant_pressure/
    ├── Thermal_conductivity/
    └── Thermal_expansion/
```

---

## Excel Files Structure

Each Excel file contains **4 sheets** with comprehensive analysis results:

### Sheet 1: PLS_Summary

Component-wise performance metrics.

| Column | Description |
|--------|-------------|
| `PLS_Component` | Component identifier (PLS1, PLS2, ...) |
| `Incremental_R2` | ΔR² contribution of each component |
| `Normalized_Covariance` | Normalized covariance with target property |

**Example:**
```
PLS_Component | Incremental_R2 | Normalized_Covariance
PLS1          | 0.7392         | 1.0000
PLS2          | 0.0711         | 0.1889
PLS3          | 0.0584         | 0.1465
```

---

### Sheet 2: Selected_Features

Ranked features with cumulative performance.

| Column | Description |
|--------|-------------|
| `Rank` | Feature importance ranking (1 = most important) |
| `Feature_Name` | Descriptor name (e.g., SM, YM, VPA, D) |
| `Cumulative_R2` | R² with features 1 through current rank |
| `Delta_R2` | Incremental R² contribution of this feature |

**Example:**
```
Rank | Feature_Name | Cumulative_R2 | Delta_R2
1    | SM           | 0.6500        | 0.6500
2    | YM           | 0.6944        | 0.0444
3    | VPA          | 0.7584        | 0.0640
4    | D            | 0.9000        | 0.1416
```

---

### Sheet 3: PLS_Loadings

Complete loading matrix showing feature contributions to each component.

**Format:**
- Rows: Input features
- Columns: PLS components (PLS1, PLS2, ...)
- Values: Loading weights (-1 to +1)

---

### Sheet 4: Metadata

Analysis configuration and performance metrics.

| Parameter | Description |
|-----------|-------------|
| `Output_Variable` | Target property (DT, Cp_300, etc.) |
| `Num_Components` | Number of PLS components used |
| `Loading_Threshold` | Min \|L\| for feature selection |
| `ΔR²_Threshold` | Min ΔR² for component significance |
| `Num_Selected_Features` | Count of selected features |
| `Best_CV_R²_Score` | Cross-validated R² |
| `Best_CV_RMSE` | Cross-validated RMSE (original scale) |
| `GridSearch_max_iter` | Optimized max iterations |
| `GridSearch_tol` | Optimized tolerance |

---

## Figure Files

Each property folder contains **3 high-resolution PDF plots** (800 DPI):

### Plot 1: Component Analysis
`*_pls_component_analysis.pdf`

**Shows:**
- Bar chart of incremental R² per component (left y-axis, red)
- Bar chart of normalized covariance with target (right y-axis, blue)

**Interpretation:**
- High incremental R²: Component captures significant variance
- High covariance: Strong linear relationship with target

---

### Plot 2: Loading Heatmap
`*_loading_heatmap.pdf`

**Shows:**
- Heatmap of PLS loading matrix
- Features (rows) × Components (columns)
- Color scale: Red (negative) → White (zero) → Blue (positive)
- Numerical values overlaid on each cell

**Interpretation:**
- |Loading| > 0.10: Feature significantly contributes to component
- Sign indicates direction of relationship

---

### Plot 3: Feature Contribution
`*_feature_contributions.pdf`

**Shows:**
- Line plot: Cumulative R² vs. number of features
- Scatter points: Color-coded by R² value
- Bar chart: ΔR² for each feature addition (right y-axis, gray)
- Legend: Sequential feature addition order

**Interpretation:**
- Steep initial rise: First few features capture most variance
- Plateau: Additional features contribute marginally
- Large ΔR² bars: Features add new information

---
## Reproducing Results

### Step 1: Verify Input Data
```bash
# Check data files exist
ls ../data/PLRS_training_data_*.xlsx
```

### Step 2: Run Analysis
```bash
# Open Jupyter notebook
jupyter notebook ../code_and_config/PLSR_analysis.ipynb

# Follow prompts:
# - Load data file
# - Select features and target
# - Set parameters (use defaults)
# - Run all cells
```

### Step 3: Compare Outputs
```bash
# Excel files should match:
# - Same R² values (within 0.001)
# - Same selected features
# - Same feature rankings

# Figures should be visually identical
```

---



## Important Notes

1. **Reproducibility**: Minor variations (<0.001 in R²) may occur due to random state in cross-validation
2. **Units**: All values in Excel are in original physical units (see data/README.md)
3. **LaTeX Symbols**: Feature names in figures use LaTeX formatting for scientific notations

---