🏃‍♀️ FitPulse – Health & Fitness Analytics System

FitPulse is an end-to-end health data analytics and intelligence system that simulates wearable fitness data, processes it, generates insights, and applies basic predictive and analytical intelligence.
The project is built incrementally across three milestones, with each milestone adding real, working features.

🚩 Problem Statement

Wearable fitness devices generate large volumes of health data such as heart rate, steps, and sleep patterns.
However, raw data alone is not useful without:
• Proper cleaning and structuring
• Trend analysis and forecasting
• Intelligence to detect anomalies and behavioral patterns

FitPulse addresses this by building a complete pipeline from data generation → analytics → intelligence.

🧩 Milestone 1 – Data Collection & Preprocessing
Features Implemented
• Synthetic generation of fitness data:
        • Heart Rate (CSV)
        • Steps Count (CSV)
        • Sleep Cycles (JSON)
• Data cleaning and preprocessing:
        • Missing value handling
        • Timestamp alignment
        • Data merging into a single dataset
• Cleaned dataset export for further analysis

Output:
        • Unified cleaned dataset (cleaned_fitness_data.csv)
        • Raw and cleaned data preview using Streamlit

📈 Milestone 2 – Forecasting & Trend Analysis
Features Implemented:
• Time-series forecasting for:
        • Heart rate trends
        • Sleep duration patterns
        • Step count with event awareness
• Visualization of:
        • Forecasted trends
        • Model components and seasonality
• Interactive selection of forecast type via UI

Outcome:
        • Enables short-term prediction of fitness metrics
        • Helps understand future behavior patterns

🧠 Milestone 3 – Intelligence & Insights Layer
Features Implemented
1️⃣ Comparative Analytics:
        • Daily aggregation of fitness data
        • Comparison of average heart rate, steps, and sleep across days
        • Visual trend analysis for easier interpretation

2️⃣ Anomaly Detection
        • Automatic detection of abnormal heart rate values
        • Useful for identifying unusual health events or irregular patterns

3️⃣ Behaviour Analysis
• Computes:
        • Average steps
        • Average sleep duration
• Classifies user lifestyle as:
        • Sedentary
        • Moderately Active
        • Active

• Outcome:
        • Transforms raw metrics into meaningful health insights
        • Adds intelligence beyond basic visualization

🛠️ Technology Stack

Frontend / UI: Streamlit
Backend: Python
Data Processing: Pandas, NumPy
Visualization: Streamlit Charts, Matplotlib
Forecasting: Time-series models
Version Control: Git & GitHub

📂 Project Structure
FitPulse_Health_Detection_Project/
│
├── app.py                     # Main Streamlit application
├── src/
│   ├── generate_data/          # Synthetic data generators
│   ├── preprocess/             # Cleaning & merging logic
│   ├── forecasting/            # Forecasting models
│   └── milestone3/             # Intelligence features
│
├── data_raw/                   # Generated raw data
├── data_clean/                 # Cleaned datasets
├── notebooks/                  # Exploration notebooks
├── README.md

▶️ How to Run the Project

• Clone the repository:

git clone https://github.com/DashamiJituri/FitPulse_Health_Detection_Project.git


• Navigate to the project folder:

cd FitPulse_Health_Detection_Project


• Install dependencies:

pip install -r requirements.txt


• Run the application:

streamlit run app.py

✅ Project Status
All features are fully implemented and working.

👩‍💻 Author

Dashami Govind Jituri
📧 Email: dashamijituri02@gmail.com