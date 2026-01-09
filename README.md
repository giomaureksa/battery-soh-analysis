State-of-Health (SOH) Analysis and Degradation Modeling of Lithium-Ion Battery Cells Using Discharge Cycle Data

PROJECT OVERVIEW
===============================================================================
This project analyzes the degradation behavior and State-of-Health (SOH) 
evolution of lithium-ion battery cells. The analysis is conducted using 
discharge cycle data obtained from periodic cell checkups within the 
SiCWell Dataset, which includes cells subjected to various aging scenarios.

The study focuses on SOH estimation, degradation trend analysis, and 
predictive modeling, using machine learning techniques for comparison and 
evaluation purposes.

This project is designed for academic research and experimental analysis, 
not for direct deployment in real-time Battery Management Systems (BMS).

DATASET INFORMATION
===============================================================================
Dataset Source:
- Dataset Name: SiCWell Dataset
- Primary File: cell_checkup.zip (155.21 MB)
- Provider: IEEE DataPort
- Official URL: https://ieee-dataport.org/open-access/sicwell-dataset

Dataset Description:
The SiCWell Dataset contains data of battery electric vehicle lithium-ion 
batteries for modeling and diagnosis purposes. Automotive-grade lithium-ion 
pouch cells are cycled with current profiles representative of electric 
vehicle operation.

The dataset includes various aging scenarios:
- Calendar aging
- DC cycling
- Sinusoidal ripple current cycling
- Artificial ripple cycling
- Realistic ripple cycling

Files Used in This Project:
IMPORTANT NOTE: Although the SiCWell Dataset contains multiple aging 
scenarios, this project focuses specifically on analyzing discharge 
cycle data from periodic checkups, regardless of the specific aging 
scenario applied to the cells.

This project uses checkup-level discharge capacity data to:
1. Calculate State of Health (SOH)
2. Analyze degradation trends
3. Build predictive models for capacity fade

CELL SPECIFICATIONS
===============================================================================
Selected Cells for Analysis:
- AC01
- AC02

Note on Aging Conditions:
While AC01 and AC02 are from the sinusoidal ripple current aging group 
in the original dataset, this analysis focuses on the discharge capacity 
measurements from their periodic checkups. The analysis method applies 
equally to cells from any aging scenario, as it relies solely on 
capacity measurements from checkup tests.

PROJECT STRUCTURE
===============================================================================
This project follows a notebook-based workflow with the following structure:

Notebook Sequence:
1. Notebook 1: Data Understanding & Preprocessing
2. Notebook 2: Feature Engineering & SOH Quantification
3. Notebook 3: Degradation Modeling & Evaluation

Data Flow:
- Raw CSV files → Notebook 1 → Cleaned data
- Cleaned data → Notebook 2 → SOH features
- SOH features → Notebook 3 → Predictive models

DETAILED NOTEBOOK DESCRIPTIONS
===============================================================================
Notebook 1: Data Understanding & Preprocessing
-------------------------------------------------------------------------------
Objectives:
- Raw CSV ingestion and validation
- Selection of relevant checkup records
- Data cleaning and consistency checks
- Preparation of cycle-indexed datasets

Key Processes:
1. File discovery and loading
2. Metadata extraction from filenames
3. Data quality assessment
4. Invalid record filtering
5. Dataset standardization

Output:
- Cleaned discharge capacity dataset
- Quality validation report

Notebook 2: Feature Engineering & SOH Quantification
-------------------------------------------------------------------------------
Objectives:
- Beginning-of-Life (BOL) capacity estimation
- SOH computation using capacity ratio definition
- SOH delta calculation between consecutive checkups
- End-of-Life (EOL) threshold labeling (80% SOH)

Key Processes:
1. Baseline capacity determination
2. SOH calculation for each checkup
3. Degradation rate computation
4. Feature engineering for predictive modeling

Output:
- Feature-level dataset containing SOH indicators
- Degradation rate statistics

Notebook 3: Degradation Modeling & Evaluation
-------------------------------------------------------------------------------
Objectives:
- Degradation trend visualization
- SOH delta interpretation
- Predictive modeling using multiple algorithms
- Model performance evaluation

Models Implemented:
- Linear Regression
- Random Forest
- XGBoost

Evaluation Metrics:
- Mean Absolute Error (MAE)
- Root Mean Square Error (RMSE)
- R² Score

Output:
- Model performance comparison
- Degradation prediction visualizations
- Predictive analytics insights

KEY FINDINGS
===============================================================================
Degradation Patterns:
- Both AC01 and AC02 exhibit clear monotonic SOH degradation
- Ripple current aging accelerates capacity fade compared to DC aging
- Non-linear degradation patterns observed in later checkups

Model Performance:
- XGBoost achieves the highest prediction accuracy (R² ≈ 0.999)
- Linear Regression provides interpretable degradation rates
- Random Forest offers robust performance across different conditions

SOH Metrics:
- SOH delta provides interpretable insight into degradation rate changes
- Capacity fade correlates with checkup frequency and operating conditions
- EOL prediction accuracy improves with more checkup data

ANALYSIS METHODOLOGY
===============================================================================
SOH Definition:
State of Health (SOH) is defined as the ratio between current discharge 
capacity and Beginning-of-Life capacity:
SOH = (Current Capacity / Initial Capacity) × 100%

SOH Delta:
SOH delta represents incremental degradation between consecutive checkups:
ΔSOH = SOH_current - SOH_previous

End-of-Life Criteria:
EOL threshold is defined at 80% SOH retention, following industry standards 
for automotive applications.

LIMITATIONS AND SCOPE
===============================================================================
Scope Boundaries:
- Analysis limited to two battery cells (AC01, AC02)
- Focus on discharge capacity as primary degradation indicator
- Specific to sinusoidal ripple current aging conditions
- Academic research focus, not production deployment

Technical Limitations:
- SOH estimation relies solely on discharge capacity
- No impedance or resistance-based SOH metrics are used
- Limited to periodic checkup data, not real-time monitoring
- Cell-to-cell variation analysis constrained by sample size

REPRODUCIBILITY
===============================================================================
Requirements:
- Python 3.8 or higher
- Required packages: pandas, numpy, matplotlib, scikit-learn, xgboost
- SiCWell Dataset access (cell_checkup.zip)

Execution Instructions:
1. Download the SiCWell Dataset from IEEE DataPort
2. Extract cell_checkup.zip to the data directory
3. Execute notebooks in sequential order (1 → 2 → 3)
4. All intermediate data is saved for verification

Documentation:
All preprocessing steps, parameters, and models are fully documented within 
the notebooks. Running the notebooks sequentially reproduces all results 
and visualizations.

AUTHOR AND ACKNOWLEDGMENTS
===============================================================================
Primary Author:
Gio Maureksa Nugraha

Dataset Acknowledgement:
This research utilizes the SiCWell Dataset provided by IEEE DataPort. 
Please refer to the original dataset license for usage terms and conditions.

License Information:
This project is intended for academic and research use only. Please refer 
to the original SiCWell Dataset license provided by IEEE DataPort for any 
redistribution or commercial use considerations.

CONTACT INFORMATION
===============================================================================
Author: Gio Maureksa Nugraha
Email: giomaureksa026@gmail.com
GitHub: https://github.com/gmreksan

Project Repository:
https://github.com/gmreksan/battery-soh-analysis
