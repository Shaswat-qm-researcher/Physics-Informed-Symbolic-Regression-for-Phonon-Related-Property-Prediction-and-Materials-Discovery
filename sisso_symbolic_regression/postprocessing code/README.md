# SISSO Equation Post-Processing Tool

A Python-based Jupyter notebook tool for evaluating and visualizing SISSO (Sure Independence Screening and Sparsifying Operator) prediction equations on material property datasets.

## Overview

This tool provides a systematic workflow to:
- Load material property data from Excel files
- Input SISSO-derived equations with coefficients
- Calculate predictions based on selected parameters
- Evaluate model performance with statistical metrics
- Generate publication-quality parity plots
- Export comprehensive results to Excel

## Requirements

### Python Version
- Python 3.12 or higher

### Dependencies

```bash
pip install pandas==2.2.3 matplotlib==3.9.2 numpy==1.26.4 scikit-learn==1.5.2 colorama==0.4.6 openpyxl
```

**Package versions:**
- pandas: 2.2.3
- matplotlib: 3.9.2
- numpy: 1.26.4
- scikit-learn: 1.5.2
- colorama: 0.4.6
- openpyxl: (latest)

## Input File Format

**Required file:** `SISSO_post_processing_input.xlsx`

The Excel file should contain sheets for different material properties with the following structure:
- **Chemical formula column**: Material identifiers
- **Actual property values**: Experimental or DFT-calculated values
- **PLSR-selected parameter columns**: Descriptors/features for SISSO prediction

### Available Property Sheets

1. `Debye_temperature`
2. `Acoustic_Debye_temperature`
3. `Cp (300 K)` - Specific heat capacity at 300 K
4. `thermal_expansion (300 K)` - Thermal expansion coefficient at 300 K
5. `thermal_conductivity (300 K)` - Thermal conductivity at 300 K

## Usage

### Running the Tool

Open and run the Jupyter notebook:

```bash
jupyter notebook SISSO_equation_postprocessing.ipynb
```

### Interactive Workflow

The notebook provides an interactive, step-by-step workflow:

#### 1. Data Loading
- Specify the directory containing your Excel file
- Select the Excel file from available options
- Choose the target property sheet

#### 2. Column Selection
- Select the **chemical formula** column
- Select the **actual property values** column
- Select **parameter columns** for SISSO prediction (comma-separated indices)

#### 3. Property Configuration
- Enter a descriptive name for the property (used in plot labels and output files)

#### 4. SISSO Equation Input

Enter your SISSO equation in the general form: `c0 + c1*(formula)`

**Input process:**
1. Enter coefficient values sequentially: `c0`, `c1`, `c2`, etc.
2. Construct the equation using these coefficients and parameter names

**Supported mathematical operators:**
- **Arithmetic**: `+`, `-`, `*`, `/`
- **Exponentiation**: `**` (note: `^` is **NOT** supported)
- **Functions**: `exp()`, `sqrt()`, `cbrt()`, `log()`, `log10()`, `abs()`
- **Trigonometric**: `sin()`, `cos()`, `tan()`
- **Grouping**: `()`

**Example equations:**
```python
c0 + c1*Parameter1
c0 + c1*Parameter1**2 + c2*Parameter2
c0 + c1*exp(Parameter1) + c2*sqrt(Parameter3)
c0 + c1*(Parameter1/Parameter2)**2
c0 + c1*log(Parameter1) + c2*Parameter2**3
```

#### 5. Equation Validation
- Automated testing on 3 representative sample rows
- Review calculated values before full computation
- Option to re-enter equation if validation fails

#### 6. Output Configuration
- Specify output directory (default: current working directory)
- Optional: create property-specific subfolders
- Customize output filenames or use auto-generated defaults

## Output Files

### 1. Parity Plot (PDF)
A publication-ready scatter plot with the following features:
- **Format**: Vector graphics (PDF, 800 DPI)
- **Type**: Actual vs. Predicted values (parity plot)
- **Elements**: 
  - Data points (crimson circles with black edges)
  - Perfect prediction line (black dashed)
  - Performance metrics annotation box
  - Maximum error point (blue X marker)
- **Styling**: Nature-compatible formatting with scientific notation
- **Default name**: `{property_name}_prediction_plot.pdf`

### 2. Results Excel File
Contains two comprehensive sheets:

**Sheet 1: Predictions**
- All original data columns preserved
- `SISSO_Prediction`: Model-predicted values
- `Absolute_Error`: |Actual - Predicted|
- `Relative_Error_%`: Percentage relative errors

**Sheet 2: Summary**
- Property name and SISSO equation
- Dataset size (number of data points)
- Statistical metrics: R², RMSE, MAE
- Maximum error value and corresponding chemical formula
- Error distribution statistics (mean, standard deviation)

**Default name**: `{property_name}_SISSO_results.xlsx`

## Performance Metrics

The tool calculates standard regression metrics:
- **R² (Coefficient of Determination)**: Model fit quality (0 to 1)
- **RMSE (Root Mean Square Error)**: Overall prediction accuracy
- **MAE (Mean Absolute Error)**: Average prediction deviation
- **Max Error**: Largest absolute prediction error with material identification

## Key Features

- **Interactive CLI**: Color-coded terminal output for enhanced user experience
- **Robust Error Handling**: Comprehensive input validation with informative error messages
- **Mathematical Flexibility**: Supports complex nested expressions
- **Automatic Data Cleaning**: Handles missing values automatically
- **Reproducible**: Complete equation and parameter documentation in output files

## Example Workflow

```
1. Load Excel file: ./SISSO_post-processing_input.xlsx
2. Select sheet: "Debye_temperature"
3. Choose columns:
   - Formula: "Chemical_Formula"
   - Actual: "DT_Actual"
   - Parameters: "Param1, Param2, Param3"
4. Property name: "Debye Temperature"
5. Input equation:
   - c0 = 125.5
   - c1 = 0.0034
   - Equation: c0 + c1*Param1**2
6. Validate on sample data → Proceed
7. Generate outputs → Complete
```

## Best Practices

**Data Preparation:**
- Ensure consistent units across all data
- Remove duplicate entries before processing
- Verify parameter column names match exactly

**Equation Input:**
- Always use `**` for exponentiation (not `^`)
- Include explicit multiplication operators (`*`)
- Verify parentheses are properly balanced
- Test complex equations on sample data first

**File Organization:**
- Create separate subfolders for each property
- Use descriptive property names for easy identification
- Maintain consistent naming conventions

## Troubleshooting

**Common Issues:**

| Issue | Solution |
|-------|----------|
| Equation validation fails | Check parameter names match Excel columns exactly; use `**` not `^` |
| File not found error | Verify file path and extension (.xlsx or .xls) |
| Column not recognized | Ensure column names are case-sensitive and match exactly |
| Division by zero | Check for zero values in denominator parameters |
| Unexpected NaN results | Review equation for log/sqrt of negative values |

**Getting Help:**
- Review sample equations in the notebook
- Check error messages for specific guidance
- Verify all dependencies are correctly installed

---

## Authors

- **Shaswat Pathak**, **Vardhman Dwivedi**, **Albert Linda**, and **Somnath Bhowmick**

---

## Contact & Support

For questions, issues, or collaboration:
- **Email**: shaswatpathak.qm.researcher@gmail.com and bsomnath@iitk.ac.in
- **Institution**: Indian Institute of Technology Kanpur, Kanpur, Uttar Pradesh, 208016, India

---

## License

MIT License - See LICENSE file for details

---

## Acknowledgments

**SISSO Method**: Ouyang, R. et al. (2018). SISSO: a compressed-sensing method for identifying the best low-dimensional descriptor in an immensity of offered candidates. Physical Review Materials, 2(8), 083802.