# FHIR Allergy Documentation System

This project implements a **FHIR-compliant AllergyIntolerance documentation workflow** for converting allergy information from EHR-like tabular data into structured FHIR resources.

This is based on my academic project for Biomedical Informatics and demonstrates:

- Use of official HL7/FHIR resources  
- AllergyIntolerance modeling  
- Clinical terminology mapping (SNOMED CT)  
- Data validation and quality checks  
- Generation of FHIR JSON  
- Visualization of allergy patterns  
- Python ETL pipeline for clinical data  

---

# 🔍 What This Project Does

### ✔ Converts tabular allergy entries → FHIR AllergyIntolerance JSON  
### ✔ Ensures proper SNOMED coding  
### ✔ Adds FHIR clinical status & verification status  
### ✔ Adds reaction details (mild / moderate / severe)  
### ✔ Uses `pydantic` validation through `fhir.resources`  
### ✔ Produces export-ready FHIR bundles  

---

# 📂 Project Structure
fhir-allergy-documentation/
│
├── data/ # allergy CSV data (real course project)
├── src/ # FHIR creation + validation code
├── notebooks/ # FHIR demonstration notebook
├── figures/ # plots (optional)
├── config/ # terminology maps (optional)
├── requirements.txt
└── README.md

---

# ▶️ How To Run
pip install -r requirements.txt

---
from src.allergy_processing import build_fhir_allergy_dataset
import pandas as pd

df = pd.read_csv("data/allergy_example.csv")
fhir_json_list = build_fhir_allergy_dataset(df)

print(fhir_json_list[0])

---

# 🧠 Skills Demonstrated

- FHIR resource modeling  
- SNOMED coding  
- Clinical documentation workflows  
- ETL + data validation  
- Python, pydantic, fhir.resources  
- Healthcare interoperability  

---

# 🔒 Data Note

This uses **course project data**, not employer data.
