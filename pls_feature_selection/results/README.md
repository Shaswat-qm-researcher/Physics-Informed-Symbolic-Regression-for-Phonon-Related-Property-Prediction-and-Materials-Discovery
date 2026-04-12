# Results - PLS Feature Selection Output

This folder contains all output files from PLS regression feature selection analyses, including Excel reports and figures.

---

## Folder Structure

```
results/
│
├── excel_data_files/             # Performance metrics & selected features
│   ├── Cp_300K_AFLOW_results.xlsx
│   ├── Debye_temperature_AFLOW_results.xlsx
│   ├── Debye_temperature_MP_results.xlsx
│   ├── thermal_conductivity_300K_AFLOW_results.xlsx
|
└── figures/      # Plots # (1.pls component analysis, 2.loading heatmaps, and 3.feature contributions)
    ├── Debye_temperature/
    ├── Specific_heat_at_constant_pressure/
    ├── Thermal_conductivity/
```

---

## Excel File Structure

Each Excel file contains **5 sheets** with comprehensive analysis results:

---

### Sheet 1: Metadata_and_Grid_Search

Two sections in one sheet: analysis configuration at the top, followed by the full grid search cross-validation results table below.

**Metadata section:**

| Parameter | Description |
|-----------|-------------|
| `Output Variable` | Target property name |
| `Num Components` | Number of PLS components used |
| `Loading Threshold` | Min \|loading\| for feature selection |
| `Delta R2 Threshold` | Min ΔR² for component significance |
| `Num Selected Features` | Count of selected features |
| `Best CV R2 Score` | Cross-validated R² (scaled) |
| `Best CV RMSE (orig units)` | Cross-validated RMSE in original units |
| `GridSearch max_iter` | Optimized max iterations |
| `GridSearch tol` | Optimized tolerance |

**Grid Search CV Results table** (appended below metadata):

Includes all parameter combinations tested, with columns for `rank_test_RMSE`, `mean_test_RMSE`, `std_test_RMSE`, `mean_test_R2`, `std_test_R2`, `mean_train_RMSE`, `mean_train_R2`, overfitting gap metrics (`overfit_gap_R2`, `overfit_gap_RMSE`), and fit/score timing. The best-performing row is highlighted in green.

---

### Sheet 2: PLS Component Summary

Component-wise performance and selection status.

| Column | Description |
|--------|-------------|
| `PLS Component` | Component identifier (PLS1, PLS2, ...) |
| `Incremental R2` | ΔR² contribution of each component |
| `Normalized Covariance` | Normalized \|covariance\| with target property |
| `Selected Component` | Whether this component passed the ΔR² threshold (Yes/No) |

**Example:**
```
PLS Component | Incremental R2 | Normalized Covariance | Selected Component
PLS1          | 0.7392         | 1.0000                | Yes
PLS2          | 0.0711         | 0.1889                | Yes
PLS3          | 0.0584         | 0.1465                | No
```

---

### Sheet 3: PLS Loadings (All)

Complete loading matrix for **all** PLS components.

**Format:**
- Rows: Input features
- Columns: `Feature` + all PLS components (PLS1, PLS2, ...)
- Values: Loading weights (approximately −1 to +1)

---

### Sheet 4: PLS Loadings (Selected)

Loading matrix restricted to **selected components only** (those passing the ΔR² threshold). This matches exactly what is shown in Plot 2.

**Format:**
- Rows: Input features
- Columns: `Feature` + selected PLS components only
- Values: Loading weights (approximately −1 to +1)

---

### Sheet 5: NLR Feature Selection

Ranked features with cumulative performance from the nested linear regression (NLR) step.

| Column | Description |
|--------|-------------|
| `PLS Rank` | Feature importance ranking (1 = most important) |
| `Feature Name` | Descriptor name (e.g., SM, YM, VPA, D) |
| `NLR Cumulative R2` | R² with features 1 through current rank |
| `NLR Delta R2` | Incremental R² contribution of this feature |

**Example:**
```
PLS Rank | Feature Name | NLR Cumulative R2 | NLR Delta R2
1        | SM           | 0.6500            | 0.6500
2        | YM           | 0.6944            | 0.0444
3        | VPA          | 0.7584            | 0.0640
4        | D            | 0.9000            | 0.1416
```

---

## Figure Files

Each property folder contains **3 high-resolution PDF plots** (600 DPI), * = user defined name:

### Plot 1: Component Analysis
`*_1_pls_component_analysis.pdf`

**Shows:**
- Bar chart of incremental R² per component (left y-axis, red)
- Bar chart of normalized \|covariance\| with target (right y-axis, blue)
- Components selected by the ΔR² threshold are marked with ★ and bolded on the x-axis

**Interpretation:**
- High incremental R²: Component captures significant variance
- High covariance: Strong linear relationship with target
- ★ markers indicate which components were used for feature selection

---

### Plot 2: Loading Heatmap
`*_2_loading_heatmap.pdf`

**Shows:**
- Heatmap of PLS loadings for **selected components only** (not all components)
- Features (rows) × selected components (columns)
- Color scale: Red (negative) → White (zero) → Blue (positive), seismic colormap
- Numerical values overlaid on each cell
- Subtitle states how many components are shown vs. total

**Interpretation:**
- \|Loading\| > threshold: Feature significantly contributes to that component
- Sign indicates direction of relationship with the target
- Full loadings for all components are available in Sheet 3 of the Excel file

---

### Plot 3: Feature Contribution
`*_3_feature_contributions.pdf`

**Shows:**
- Line plot: Cumulative R² vs. number of features (left y-axis)
- Scatter points: Color-coded by cumulative R² value using the jet colormap
- Bar chart: ΔR² for each feature addition (right y-axis, gray)
- Color bar: Maps point colors to R² values
- Legend (left of plot): Sequential feature addition order with symbols if provided

**Interpretation:**
- Steep initial rise: First few features capture most variance
- Plateau: Additional features contribute marginally
- Large ΔR² bars: Features add new information

---

## Reproducing Results

### Step 1: Verify Input Data
```bash
# Check data files exist
ls ../data/*_cleaned_dataset.csv
* = MP/AFLOW
```

### Step 2: Run Analysis
```bash
# Open Jupyter notebook
jupyter notebook ../code_and_config/setup_environment.ipynb
jupyter notebook ../code_and_config/PLS_analysis.ipynb

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
```

---



## Notes

1. **Reproducibility**: Minor variations (<0.001 in R²) may occur due to random state in cross-validation
2. **Units**: All values in INPUT CSV file are in original physical units (see data/README.md)
3. **LaTeX Symbols**: Feature names in figures use LaTeX formatting for scientific notations

---