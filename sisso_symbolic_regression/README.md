# SISSO Symbolic Regression
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![SISSO](https://img.shields.io/badge/SISSO-symbolic_regression-green.svg)](https://github.com/rouyang2017/SISSO)

A comprehensive workflow repository for material property prediction using SISSO (Sure Independence Screening and Sparsifying Operator) with post-processing tools for analysis and visualization.

> **Note:** This is a sub-repository of the main project:  
> **[Physics-Informed-Symbolic-Regression-for-Phonon-Related-Property-Prediction-and-Materials-Discovery](https://github.com/Shaswat-qm-researcher/Physics-Informed-Symbolic-Regression-for-Phonon-Related-Property-Prediction-and-Materials-Discovery/)**

## Overview

This repository contains:
- **SISSO input files** for various material properties
- **SISSO output** files with model predictions and performance metrics
- **Post-processing tools** for evaluating and visualizing SISSO results
- **Prediction results** with publication-quality plots

## Repository Structure

```
sisso_symbolic_regression/
├── config and data - SISSO INPUT/
│   ├── Debye_temperature/
│   │   ├── SISSO.in
│   │   └── train.dat
│   ├── Debye_temperature_acoustic/
│   │   ├── SISSO.in
│   │   └── train.dat
│   ├── Specific_heat_at_constant_pressure/
│   │   ├── SISSO.in
│   │   └── train.dat
│   ├── Thermal_conductivity/
│   │   ├── SISSO.in
│   │   └── train.dat
│   └── Thermal_expansion/
│       ├── SISSO.in
│       └── train.dat
│
├── model and equation - SISSO OUTPUT/
│   ├── Debye_temperature/
│   │   ├── SIS_subspaces/
│   │   │   ├── Uspace.dat
│   │   │   └── Uspace.expressions
│   │   └── Models/
│   │       └── data_top1/
│   │           ├── top0100_D001
│   │           └── top0100_D001_coeff
│   ├── Debye_temperature_acoustic/
│   │   ├── SIS_subspaces/
│   │   └── Models/
│   ├── Specific_heat_at_constant_pressure/
│   │   ├── SIS_subspaces/
│   │   └── Models/
│   ├── Thermal_conductivity/
│   │   ├── SIS_subspaces/
│   │   └── Models/
│   └── Thermal_expansion/
│       ├── SIS_subspaces/
│       └── Models/
│
├── postprocessing code/
│   ├── README.md
│   ├── SISSO_postprocessing.ipynb
│   └── SISSO_post_processing_input.xlsx
│
└── postprocessing results/
    ├── debye_temperature/
    │   ├── DT_prediction_plot.pdf
    │   └── DT_SISSO_results.xlsx
    ├── debye_temperature_acoustic/
    │   ├── DT_A_prediction_plot.pdf
    │   └── DT_A_SISSO_results.xlsx
    ├── specific_heat/
    │   ├── Cp_prediction_plot.pdf
    │   └── Cp_SISSO_results.xlsx
    ├── thermal_conductivity/
    │   ├── TC_prediction_plot.pdf
    │   └── TC_SISSO_results.xlsx
    └── thermal_expansion/
        ├── TEX_prediction_plot.pdf
        └── TEX_SISSO_results.xlsx
```

## Material Properties Analyzed

1. **Debye Temperature ($\Theta_D$, DT)** - Characterizes phonon frequency distribution
2. **Acoustic Debye Temperature ($\Theta_{D,a}$, DT_A)** - Based on acoustic phonon branches
3. **Specific Heat at Constant Pressure ($C_p\ (300\ K)$, Cp)** - Heat capacity at 300 K
4. **Thermal Expansion ($\alpha\ (300\ K)$, TEX)** - Thermal expansion coefficient at 300 K
5. **Thermal Conductivity ($\kappa\ (300\ K)$, TC)** - Lattice thermal conductivity at 300 K

## Getting Started

### Prerequisites

**For SISSO execution:**
- Fortran compiler (gfortran or ifort)
- LAPACK library
- OpenMP (optional, for parallel execution)

**For post-processing:**
- Python 3.12 or higher
- See `requirements.txt` for Python dependencies

### Installation

1. **Clone this repository:**
```bash
git clone https://github.com/yourusername/sisso_symbolic_regression.git
cd sisso_symbolic_regression
```

2. **Install SISSO:**

For detailed SISSO installation and execution instructions, visit:
**[rouyang2017/SISSO](https://github.com/rouyang2017/SISSO)** - Official SISSO repository

Quick installation:
```bash
git clone https://github.com/rouyang2017/SISSO.git
cd SISSO/src
make
```

3. **Install Python dependencies for post-processing:**
```bash
pip install -r requirements.txt
```

## Usage

## Running SISSO

1. Navigate to the input directory for your target property:
```bash
cd "config and data - SISSO INPUT/Debye_temperature"
```

2. Copy or link the SISSO executable:
```bash
cp /path/to/SISSO/SISSO .
```

3. Run SISSO:
```bash
./SISSO > SISSO.in
```

4. Check the output files in the current directory for results.

**For detailed SISSO usage, parameters, and methodology, refer to:**
- Official repository: https://github.com/rouyang2017/SISSO
- Original paper: Ouyang, R. et al. (2018). *Physical Review Materials*, 2(8), 083802.

### INPUT FILE FORMAT

### train.dat
The training data file containing your dataset with the following structure:

**Format:**
```
sample_id  material_name  target_property  feature1  feature2  feature3  ...
```

**Example:**
```
1  Al2O3      523.45    2.99   400.5   8.21   3.96
2  SiO2       645.12    2.65   450.2   7.85   2.20
3  MgO        946.85    3.58   510.8   9.45   3.58
...
```

**Structure:**
- **Column 1**: Sample index (integer)
- **Column 2**: Material identifier (chemical formula or name)
- **Column 3**: Target property value (e.g., Debye temperature in K)
- **Columns 4+**: Input features/descriptors (e.g., shear modulus, Young's modulus, density, volume per atom)

**Requirements:**
- Space-separated values
- No header row
- All numerical features must be properly scaled
- Missing values not allowed
- Each row represents one material sample

### SISSO.in
Configuration file controlling SISSO execution parameters:

**Key Parameters:**

```fortran
!>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
! SISSO input file
!>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

! Property type (1:regression, 2:classification)
ptype=1

! Number of tasks (typically 1 for single property prediction)
ntask=1

! Descriptor dimension (1:scalar, 2:vector, 3:matrix)
desc_dim=1

! Number of samples in training data
nsample=6200

! Number of input features (columns in train.dat minus first 2)
nfeat=4

! Feature space construction depth (complexity of symbolic expressions)
! Higher values allow more complex features but increase computation
rung=3

! Maximum feature complexity (number of operators per feature)
maxcomplexity=7

! Size of SIS-selected subspace (features passed to sparse regression)
subs_sis=200

! Operators for feature construction at each rung
! Available: (+)(-)(*)(/)(^-1)(^2)(^3)(^6)(sqrt)(cbrt)(exp)(exp-)(log)(sin)(cos)
opset='(+)(-)(*)(/)(^-1)(^2)(^3)(sqrt)(cbrt)(^6)(exp)(exp-)(log)(sin)(cos)'

! Method for sparse regression (L0 for LASSO)
method='L0'

! Fitting intercept (T:yes, F:no)
fit_intercept=.true.

! Model selection metric (RMSE, MaxAE, or combinations)
metric='RMSE'

! Number of top models to output
nm_output=100
```

**Important Parameters Explained:**

- **`ptype`**: Task type - use 1 for continuous property prediction
- **`desc_dim`**: Descriptor dimensionality - usually 1 for scalar properties
- **`nsample`**: Must match number of rows in train.dat
- **`nfeat`**: Must match number of feature columns in train.dat
- **`rung`**: Feature space depth (1-3 typical; higher = more complex features)
- **`maxcomplexity`**: Max operators per feature (prevents overly complex expressions)
- **`subs_sis`**: Number of features to retain after SIS screening (100-200 typical)
- **`opset`**: Mathematical operators used to construct features
- **`method`**: Sparse regression method (L0 recommended for interpretability)
- **`nm_output`**: Number of best models to save

### OUTPUT FILES

### Understanding SISSO Output

After running SISSO, several output files are generated in the working directory:

#### 1. **SISSO.out** (Main Output File)
The primary output file containing:

**Header Information:**
- SISSO version and execution date
- Input data summary (number of samples, features)
- Configuration parameters read from SISSO.in
- Target property statistics (mean, standard deviation)

**Feature Construction Progress:**
```
Feature Construction (FC) starts ...
Total number of features in Phi00:              4      (Primary features)
Total number of features in Phi01:             67      (After 1st rung)
Total number of features in Phi02:           4945     (After 2nd rung)
Total number of features in Phi03:       37147062     (After 3rd rung)
Size of SIS-selected subspace:        200
Time used for FC:          103.08 seconds
```

**Best Model Information:**
```
1D descriptor/model (y = c0 + c1*d1):
================================================================================
    d001 = (((SM+YM)/cbrt(VPA))/sqrt((YM*D)))    feature_ID:000001
    
    Coefficients:
        c1:     0.1500823088E+03
        c0:    -0.7572654431E+00
    
    Performance Metrics:
        RMSE:   0.1715290516E+01    (Root Mean Square Error)
        MaxAE:  0.2320009950E+02    (Maximum Absolute Error)
================================================================================
```

**How to Read the Descriptor:**
- The descriptor is a symbolic expression combining input features
- Example: `(((SM+YM)/cbrt(VPA))/sqrt((YM*D)))`
  - `SM` = Shear Modulus (Feature 1)
  - `YM` = Young's Modulus (Feature 2)
  - `VPA` = Volume Per Atom (Feature 3)
  - `D` = Density (Feature 4)
- Operators: `cbrt` = cube root, `sqrt` = square root
- The predicted value = `c0 + c1 × descriptor_value`

#### 2. **SIS_subspaces/** Folder

**Uspace.expressions:**
- Contains all SIS-selected feature expressions (200 features)
- Human-readable symbolic form of each feature
- Feature rankings based on correlation with target property

**Example content:**
```
Feature_ID  Expression                                    Correlation
000001      (((SM+YM)/cbrt(VPA))/sqrt((YM*D)))           1.0000
000002      ((SM+YM)/sqrt(D))                            0.9823
000003      (YM/sqrt((VPA*D)))                           0.9801
...
```

**Uspace.dat:**
- Numerical values of the SIS-selected features
- Matrix format: [n_samples × n_features]
- Used internally for sparse regression
- Each column corresponds to a feature in Uspace.expressions

**Format:**
```
sample1_feat1  sample1_feat2  sample1_feat3  ...
sample2_feat1  sample2_feat2  sample2_feat3  ...
...
```

#### 3. **Models/** Folder

**data_top1/** subdirectory contains the best model files:

**top0100_D001:**
- Predictions for all training samples using the best 1D model
- Format: `sample_id  material_name  actual_value  predicted_value`

**Example:**
```
1  Al2O3      523.45    524.12
2  SiO2       645.12    643.87
3  MgO        946.85    948.21
...
```

**top0100_D001_coeff:**
- Coefficients for the top 100 models (ranked by RMSE)
- Format: `model_rank  RMSE  MaxAE  feature_ID  c0  c1  [c2...]`

**Example:**
```
1   1.7153   23.20   000001   -0.7573   150.0823
2   1.8234   24.15   000002   -1.2341   145.3421
3   1.9102   25.33   000003    0.4523   152.1234
...
```

**Reading the coefficient file:**
- **Column 1**: Model rank (1 = best)
- **Column 2**: RMSE of the model
- **Column 3**: Maximum absolute error
- **Column 4**: Feature ID (links to Uspace.expressions)
- **Column 5+**: Intercept (c0) and coefficients (c1, c2, ...)

#### 4. **Additional Output Files**

**feat_XX.dat:**
- Contains all generated features at each rung (XX = rung number)
- Large files, typically not needed for analysis
- Can be deleted after successful run to save space

**residual.dat:**
- Prediction residuals (actual - predicted) for each sample
- Useful for error analysis and identifying outliers

### Key SISSO Outputs Summary

Each property folder contains:

- **SISSO.out**: Main results with best descriptor equation and performance
- **SIS_subspaces/Uspace.expressions**: Top 200 symbolic features (human-readable)
- **SIS_subspaces/Uspace.dat**: Numerical values of selected features
- **Models/data_top1/top0100_D001**: Predictions for all samples
- **Models/data_top1/top0100_D001_coeff**: Coefficients for top 100 models

## Post-Processing SISSO Results

The post-processing tool allows you to:
- Load SISSO equations and coefficients
- Evaluate predictions on your dataset
- Calculate performance metrics (R², RMSE, MAE)
- Generate publication-quality parity plots
- Export comprehensive results to Excel

### POST-PROCESSING SCRIPT

#### Quick Start

1. Navigate to the post-processing directory:
```bash
cd "postprocessing code"
```

2. Prepare your input Excel file (`SISSO_post_processing_input.xlsx`) with:
   - Chemical formulas
   - Actual property values
   - PLSR-selected parameter values

3. Launch Jupyter notebook:
```bash
jupyter notebook SISSO_postprocessing.ipynb
```

4. Follow the interactive workflow:
   - Load your data file
   - Select the property sheet
   - Choose columns (formula, actual values, parameters)
   - Input SISSO equation with coefficients
   - Validate on sample data
   - Generate plots and results

#### Detailed Post-Processing Documentation

For comprehensive documentation on the post-processing tool, including:
- Input file format requirements
- Step-by-step usage instructions
- Equation syntax and supported operators
- Troubleshooting guide

See: [`postprocessing code/README.md`](postprocessing%20code/README.md)


### POST-PROCESSING OUTPUTS

For each property (e.g., `debye_temperature/`, `thermal_conductivity/`):

1. **Prediction Plot (PDF)**
   - Parity plot (Actual vs Predicted)
   - Performance metrics annotation
   - Maximum error point highlighted

2. **Results Excel File**
   - **Sheet 1 - Predictions**: Full dataset with predictions and errors
   - **Sheet 2 - Summary**: Statistical metrics and equation details

### Performance Metrics

All models are evaluated using:
- **R² (Coefficient of Determination)**: Model fit quality
- **RMSE (Root Mean Square Error)**: Overall prediction accuracy
- **MAE (Mean Absolute Error)**: Average prediction deviation
- **Max Error**: Largest absolute prediction error with material identification

## Features

### SISSO Capabilities
- Automatic feature construction from primary features
- Multi-level feature space exploration
- Built-in cross-validation
- Support for multi-dimensional descriptors
- Handles large feature spaces efficiently

### Post-Processing Tool Features
- Interactive command-line interface
- Flexible equation input (supports complex mathematical expressions)
- Automatic equation validation
- Color-coded terminal output
- Comprehensive error handling
- Batch processing capability

## Mathematical Operations Supported

The post-processing tool supports:

**Basic operators:** `+`, `-`, `*`, `/`, `**` (exponentiation)

**Functions:**
- `exp()`, `sqrt()`, `cbrt()`, `log()`, `log10()`, `abs()`
- `sin()`, `cos()`, `tan()`

**Example equations:**
```python
c0 + c1*Parameter1**2
c0 + c1*exp(Parameter1) + c2*sqrt(Parameter2)
c0 + c1*(Parameter1/Parameter2)**2
c0 + c1*log(Parameter1) + c2*Parameter2**3
```

## Example Workflow

1. **Prepare training data** with material properties and descriptors
2. **Configure SISSO.in** with desired complexity and validation settings
3. **Run SISSO** to identify optimal symbolic equations
4. **Extract coefficients** from SISSO output
5. **Use post-processing tool** to:
   - Validate equations on test data
   - Generate publication plots
   - Export comprehensive results

## Citation

If you use this repository, SISSO methodology, or the post-processing tools in your research, please cite:

**This Work:**
```bibtex
@article{
}
```

**SISSO Method:**
```bibtex
@article{ouyang2018sisso,
  title={SISSO: a compressed-sensing method for identifying the best low-dimensional descriptor in an immensity of offered candidates},
  author={Ouyang, Runhai and Curtarolo, Stefano and Ahmetcik, Emre and Scheffler, Matthias and Ghiringhelli, Luca M},
  journal={Physical Review Materials},
  volume={2},
  number={8},
  pages={083802},
  year={2018},
  publisher={APS}
}
```

## Authors

- **Shaswat Pathak**
- **Vardhman Dwivedi**
- **Albert Linda**
- **Somnath Bhowmick**

## Contact

For questions, issues, or collaboration:
- **Email**: shaswatpathak.qm.researcher@gmail.com, bsomnath@iitk.ac.in
- **Institution:** Indian Institute of Technology Kanpur, Uttar Pradesh, 208016, India
## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- SISSO methodology developed by Ouyang et al. (2018)
- Python scientific computing stack (NumPy, pandas, matplotlib, scikit-learn)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Troubleshooting

### SISSO Execution Issues
- Ensure LAPACK is properly linked
- Check input file format (no extra spaces, correct data types)
- Verify feature count matches between SISSO.in and train.dat

### Post-Processing Issues
- Verify Python package versions match requirements
- Check Excel file format and column names
- Use `**` for exponentiation (not `^`)
- Ensure parameter names match exactly between equation and Excel columns

For more detailed troubleshooting, see the post-processing README or open an issue on GitHub.

---

**Keywords:** Materials informatics, Machine learning, Symbolic regression, SISSO, Compressed sensing, Feature engineering, Debye temperature, Specific Heat, Thermal Conductivity, Thermal properties, Materials prediction
