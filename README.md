# 🗳️ Kerala Legislative Assembly Election 2026: Advanced Data Analytics & Predictive Profiling

## 📌 Executive Summary
This project is an end-to-end data analytics pipeline and interactive web dashboard built to analyze the official results of the 2026 Kerala Legislative Assembly Election. 

The analysis processes raw, unstructured government data (ECI Form 20) for all 140 constituencies to map regional political dominance, identify critical battlegrounds, and deploy unsupervised machine learning to mathematically cluster constituencies based on voter behavior.

## 🛠️ Tech Stack & Architecture
* **Data Extraction & Cleaning:** Python, Pandas, NumPy
* **Machine Learning:** Scikit-Learn (K-Means Clustering, StandardScaler)
* **Interactive Visualizations:** Plotly Express, Seaborn, Matplotlib
* **Web Deployment:** Streamlit Community Cloud

## 🚀 Core Features & Methodology

### 1. Automated Data Pipeline
* Ingested unstructured `.xlsx` files from the Election Commission of India (ECI).
* Engineered a dynamic extraction script to bypass misaligned headers, handle missing values (`NaN`), and aggregate candidate-level data into a clean 140-row constituency-level dataset.
* Mapped granular regional parties and independent candidates (e.g., RMPOI, RJD, KEC) into their respective major alliances (UDF, LDF, NDA).

### 2. Feature Engineering & Exploratory Data Analysis (EDA)
* Calculated precise **Victory Margins** and **Turnout Percentages** dynamically from total valid votes and total electors.
* Approximated geospatial regions (North, Central, South Kerala) to analyze localized political dominance.
* Designed interactive Plotly distributions to highlight the Top 10 most vulnerable "Swing Seats" for future campaign strategists.

### 3. Machine Learning: Constituency Profiling
* Implemented a **K-Means Clustering** algorithm to segment the 140 constituencies into three distinct mathematical profiles:
  * 🟢 **Battlegrounds:** High turnout, razor-thin margins.
  * 🔵 **Safe Seats:** Average turnout, comfortable margins.
  * 🔴 **Extreme Outliers:** Wave-election strongholds.

## 💻 How to View the Project

### Part 1: The Codebase (Jupyter / Colab)
The core logic, data cleaning pipeline, and static visualizations can be found in the `Kerala_Election_2026_Analysis.ipynb` notebook.

### Part 2: Interactive Web Dashboard (Coming Soon!)
*Note: The interactive Plotly & Streamlit web application is currently under progress and will be made live soon.* ---
*Developed by KR Jershan*
