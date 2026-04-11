# SISSO Equation Post-Processing Tool

A Python-based Jupyter notebook tool for evaluating and visualizing SISSO (Sure Independence Screening and Sparsifying Operator) prediction equations on material property datasets.

## Overview

This tool provides a systematic workflow to:
- Load material property data from Excel/CSV files
- Load LaTeX symbols from `symbol_conversion.txt` files
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

**Required file:** `SISSO_post_processing_input_data.xlsx`

The Excel file should contain sheets for different material properties with the following structure:
- **Chemical formula column**: Material identifiers
- **Target property values**: Experimental or DFT-calculated values
- **PLS-selected parameter columns**: Descriptors/features for SISSO prediction

**Optional file:** `symbol_conversion.txt`
- Contains LaTeX symbol conversion for Excel file headings.
- If not provide, the code will use Excel file headings as label to plots by default.

### Available Property Sheets

1. `Debye_temperature`
2. `Cp (300 K)` - Specific heat capacity at 300 K
3. `thermal_conductivity (300 K)` - Thermal conductivity at 300 K

## Usage

### Running the Tool

Open and run the Jupyter notebook:

```bash
jupyter notebook SISSO_postprocessing.ipynb
```

### Interactive Workflow

The notebook provides an interactive, step-by-step workflow:

#### 1. Data Loading
- Specify the directory containing your Excel file
- Select the Excel file from available options
- Choose the target property sheet
- *Optional* Specify symbol_conversion.txt file location

#### 2. Column Selection
- Select the **chemical formula** column
- Select the **target property values** column
- Select **parameter columns** for SISSO prediction (comma-separated indices)


#### 3. SISSO Equation Input

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

#### 4. Equation Validation
- Automated testing on 3 representative sample rows
- Review calculated values before full computation
- Option to re-enter equation if validation fails

#### 5. Output Configuration
- Specify output location (default: current working directory)
- Enter prefix for outputs

### Output Files

#### 1. Parity Plot (PDF)

A publication-ready scatter plot showing actual vs. predicted values (parity plot), with data points marked by crimson circles with black edges,  perfect prediction line (black dashed), performance metrics annotation box, maximum error point (blue X marker).

- **Default name**: `{property_name}_prediction_plot.pdf`

#### 2. Results Excel File
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

**Default name**: `{property_name}_results.xlsx`

### Performance Metrics

The tool calculates standard regression metrics:
- **R² (Coefficient of Determination)**: Model fit quality (0 to 1)
- **RMSE (Root Mean Square Error)**: Overall prediction accuracy
- **MAE (Mean Absolute Error)**: Average prediction deviation
- **Max Error**: Largest absolute prediction error with material identification

### Key Features

- **Interactive CLI**: Color-coded terminal output for enhanced user experience
- **Robust Error Handling**: Comprehensive input validation with informative error messages
- **Mathematical Flexibility**: Supports complex nested expressions
- **Automatic Data Cleaning**: Handles missing values automatically
- **Reproducible**: Complete equation and parameter documentation in output files

## Example Workflow

```
1. Load Excel file: ./SISSO_postprocessing_input_data.xlsx
2. Select sheet: "Debye_temperature"
3. Choose columns:
   - Formula: "Chemical_Formula"
   - Target Coloumn: "DT"
   - Parameters: "Param1, Param2, Param3"
4. Load Symbol Conversion: ./symbol_conversion.txt
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
- Always use `**` for exponentiation
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
| Equation validation fails | Check parameter names match Excel columns exactly. |
| File not found error | Verify file path and extension (.xlsx or .xls or .csv) |
| Column not recognized | Ensure column names are case-sensitive and match exactly |
| Division by zero | Check for zero values in denominator parameters |
| Unexpected NaN results | Review equation for log/sqrt of negative values |
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

**[SISSO Method](https://github.com/rouyang2017/SISSO)**: Ouyang, R. et al. (2018). SISSO: a compressed-sensing method for identifying the best low-dimensional descriptor in an immensity of offered candidates. Physical Review Materials, 2(8), 083802.