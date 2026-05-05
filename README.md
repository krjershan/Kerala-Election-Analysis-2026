# 📊 2026 Kerala Legislative Election: Exploratory Data Analysis & Predictive Modeling

**Author:** KR Jershan  
**Tech Stack:** Python, Pandas, Matplotlib, Seaborn, Scikit-Learn (Machine Learning)  
**Methodology:** CRISP-DM Framework

---

## 📝 Executive Summary
This project analyzes the official results of the 2026 Kerala Legislative Assembly elections. The election marked a significant political shift: a massive sweep by the UDF (102 seats), severe anti-incumbency against the LDF (35 seats), and a historic breakthrough for the NDA (3 seats). 

The goal of this analysis was to move beyond basic seat counts and utilize data science techniques to uncover actionable insights regarding voter volatility, regional dominance, and constituency clustering.

## 🎯 Project Objectives
1. **Data Engineering:** Ingest, clean, and standardize raw election data for consistency.
2. **Exploratory Data Analysis (EDA):** Quantify victory margins and regional power dynamics.
3. **Vulnerability Mapping:** Identify "Swing Seats" critical for future campaign strategy.
4. **Machine Learning:** Deploy K-Means Clustering to mathematically profile constituencies based on voter behavior and margin volatility.

---

## 🛠️ Methodology & Technical Execution

### 1. Data Cleaning & Feature Engineering
* Handled missing values and standardized political alliance acronyms.
* Engineered a new categorical feature, `Win_Intensity`, to classify victories into 'Close Contest', 'Comfortable', and 'Landslide'.

### 2. Statistical Visualization
* Created a professional **Donut Chart** to visualize the power distribution and alliance seat share.
* Utilized **Boxplots** to map the statistical distribution of victory margins, successfully identifying outliers (e.g., Puthuppally).
* Generated **Grouped Bar Charts** to analyze alliance dominance segmented by geographic region (North, Central, South Kerala).

### 3. Predictive Analytics (K-Means Clustering)
Instead of relying on arbitrary margin thresholds, an unsupervised Machine Learning algorithm (K-Means) was utilized to segment the constituencies. 
* **Inputs:** `Turnout_Percentage` and `Margin`.
* **Output:** The model automatically identified three distinct electoral battlegrounds:
  * *Battlegrounds* (High volatility, low margins)
  * *Safe Seats* (Predictable, comfortable margins)
  * *Extreme Outliers* (Unusually high margin anomalies)

---

## 💡 Key Business/Political Insights
* **The "Zero-Margin" Threat:** Visual sorting revealed highly vulnerable constituencies (like Kazhakuttam) won by razor-thin margins. These are high-priority targets for subsequent election cycles.
* **Regional Discrepancies:** Visual geographic segmentation proved that while the UDF dominated the overall state, certain regions displayed vastly different voting behaviors, highlighting the need for hyper-localized campaign strategies.
* **Mathematical Profiling:** The clustering model successfully proved that voter turnout percentage is a crucial secondary dimension to margin analysis, creating a more accurate map of electoral safety versus vulnerability.

---

## 💻 How to Run This Project
1. Clone this repository to your local machine.
2. Ensure you have Python installed, along with `pandas`, `matplotlib`, `seaborn`, and `scikit-learn`.
3. Run the Jupyter Notebook / Google Colab file (`Kerala_Election_2026_Analysis.ipynb`) to view the interactive visualizations and machine learning outputs.
