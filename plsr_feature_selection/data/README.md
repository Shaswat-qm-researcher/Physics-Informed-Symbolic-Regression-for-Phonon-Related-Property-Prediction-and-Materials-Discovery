# PLSR Feature Selection - Data Directory

## 📋 Overview

This directory contains input data for **Partial Least Squares Regression (PLSR)** analysis to identify the most influential physical descriptors for predicting **Debye temperature ($Θ_D$)** and related thermodynamic and transport properties.

---

## 📂 Files Description

### **1. Training Data Files**

#### **PLRS_training_data_MP.xlsx**
- **Source**: Materials Project Database
- **Materials Count**: 6,433 crystalline compounds
- **ID Column**: `MP_ID` (e.g., `mp-24390`)
- **Target Property**: `DT` (Debye Temperature in K)
- **Features**: 22 columns including:
  - **Identifiers**: `MP_ID`, `formula` (⚠️ MUST DROP)
  - **Structural**: `NE`, `NA`, `V`, `VPA`, `D`
  - **Electronic**: `BGAP`, `EPA`, `FEPA`, `EFMR`
  - **Magnetic**: `TM`, `MSITE`
  - **Mechanical**: `BM`, `SM`, `YM`, `PR`, `PUGR`, `IPUGR`
  - **Vibrational**: `DT`, `vs`, `vl`, `vm`

#### **PLRS_training_data_AFLOW.xlsx**
- **Source**: AFLOW Consortium Database
- **Materials Count**: 5,154 crystalline compounds
- **ID Column**: `auid` (e.g., `aflow:001a4bbb607a30b0`)
- **Target Property**: `DT_AGL` (Debye Temperature via AGL method in K). **OTHER** - `DT_A_AGL`, `Cp_300`, `TEX_300`, `TC_300`
- **Features**: 29 columns including:
  - **Identifiers**: `auid`, `formula` (⚠️ MUST DROP)
  - **Structural**: `NE`, `NA`, `VPA`, `D`
  - **Electronic**: `BGAP`, `EPA`, `ASPIN`, `ENPA`
  - **Mechanical**: `BM`, `SM`, `YM`, `ANI`, `PR`, `PUGR`, `IPUGR`
  - **Vibrational**: `DT_AGL`, `vs`, `vl`, `vm`, `DT_A_AGL`
  - **Thermodynamic** (300K): `gruneisen`, `Cv_300`, `Cp_300`, `TEX_300`, `TC_300`
  - **Advanced**: `VIB_EN_300`, `VIB_FE_300`


### **2. Metadata Files**

#### **feature_descriptions.json**
- Comprehensive documentation of all 30+ features
- Physical significance and units
- PLSR importance rankings
- Usage guidelines and warnings
- See full file above for complete details

#### **feature_metadata.json**
- Simple lookup table: `{feature_name: {unit, example, type}}`
- Used programmatically for validation and plotting

---


### **Why Drop These Columns?**
1. **MP_ID / auid**: String identifiers - no numerical meaning
2. **formula**: Chemical formula strings - not ML-compatible
3. **Keeping them causes**: TypeError in sklearn, meaningless correlations

---

## 🗂️ Database Differences

| Feature | Materials Project | AFLOW | Notes |
|---------|-------------------|-------|-------|
| **ID Column** | `MP_ID` | `auid` | Both must be dropped |
| **Formula** | `formula` | `formula` | Both must be dropped |
| **Debye Temp** | `DT` | `DT_AGL` | Target variable |
| **Fermi Energy** | `EFMR` | ❌ | MP-only |
| **Magnetization** | `TM` | `ASPIN` | Different conventions |
| **Magnetic Sites** | `MSITE` | ❌ | MP-only |
| **Cell Volume** | `V` | ❌ | MP-only (can derive from VPA×NA) |
| **Anisotropy** | ❌ | `ANI` | AFLOW-only |
| **Grüneisen γ** | ❌ | `gruneisen` | AFLOW-only (critical for α, κ) |
| **Heat Capacity** | ❌ | `Cp_300` | AFLOW-only |
| **Thermal Exp.** | ❌ | `TEX_300` | AFLOW-only |
| **Thermal Cond.** | ❌ | `TC_300` | AFLOW-only |

---
