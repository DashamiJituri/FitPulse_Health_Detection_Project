import streamlit as st
import pandas as pd
import os
import numpy as np

from src.generate_data import (
    generate_heart_rate_csv,
    generate_steps_csv,
    generate_sleep_json
)

from src.preprocess import run_preprocessing
from src.forecasting import (
    forecast_heart_rate,
    forecast_sleep,
    forecast_steps_with_events
)

from src.milestone3.comparison import daily_comparison
from src.milestone3.anomaly_detection import detect_anomalies
from src.milestone3.behavior_analysis import analyze_behavior
from src.milestone4.report_utils import generate_summary_report



# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(page_title="FitPulse – Milestones 1, 2 & 3", layout="wide")
st.title("🔥 FitPulse – Data Collection, Forecasting & Intelligence Platform")

# --------------------------------------------------
# SESSION STATE INIT
# --------------------------------------------------
for key in ["hr_df", "steps_df", "sleep_df", "clean_df"]:
    if key not in st.session_state:
        st.session_state[key] = None


# --------------------------------------------------
# STEP 1: DATA GENERATION
# --------------------------------------------------
st.header("📌 Step 1: Generate Raw Fitness Data")

btn_col1, btn_col2, btn_col3 = st.columns(3)

with btn_col1:
    if st.button("Generate Heart Rate Data"):
        st.session_state.hr_df = generate_heart_rate_csv()
        st.success("Heart Rate data generated")

with btn_col2:
    if st.button("Generate Steps Data"):
        st.session_state.steps_df = generate_steps_csv()
        st.success("Steps data generated")

with btn_col3:
    if st.button("Generate Sleep Data"):
        sleep_json = generate_sleep_json()
        st.session_state.sleep_df = pd.DataFrame(sleep_json["cycles"])
        st.success("Sleep data generated")

# Preview
st.subheader("📍 Generated Raw Data Preview")
c1, c2, c3 = st.columns(3)

with c1:
    if st.session_state.hr_df is not None:
        st.dataframe(st.session_state.hr_df.head())

with c2:
    if st.session_state.steps_df is not None:
        st.dataframe(st.session_state.steps_df.head())

with c3:
    if st.session_state.sleep_df is not None:
        st.dataframe(st.session_state.sleep_df.head())


# --------------------------------------------------
# STEP 2: PREPROCESSING
# --------------------------------------------------
st.header("📌 Step 2: Clean & Merge Data")

if st.button("Run Preprocessing Pipeline"):
    run_preprocessing()
    cleaned_path = "data_clean/cleaned_fitness_data.csv"

    if os.path.exists(cleaned_path):
        df = pd.read_csv(cleaned_path).dropna()
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        st.session_state.clean_df = df
        st.success("🎉 Cleaning & Merging Completed")

if st.session_state.clean_df is not None:
    st.subheader("🧹 Cleaned Fitness Data")
    st.dataframe(st.session_state.clean_df.head(20))


# --------------------------------------------------
# STEP 3: FORECASTING (MILESTONE 2)
# --------------------------------------------------
st.header("📌 Step 3: Forecasting (Milestone 2)")

forecast_task = st.selectbox(
    "Select Forecast Task",
    ["Heart Rate Forecast", "Sleep Duration Forecast", "Steps Forecast"]
)

if st.button("Run Forecast"):
    if len(st.session_state.clean_df) < 10:
        st.error("Not enough data for forecasting")
    else:
        df = st.session_state.clean_df.copy()

        if forecast_task == "Heart Rate Forecast":
            model, forecast = forecast_heart_rate(df)
        elif forecast_task == "Sleep Duration Forecast":
            model, forecast = forecast_sleep(df)
        else:
            model, forecast = forecast_steps_with_events(df)

        st.pyplot(model.plot(forecast))
        st.pyplot(model.plot_components(forecast))


# --------------------------------------------------
# STEP 4: Milestone 3 – Intelligence Layer
# --------------------------------------------------
st.header("🚀 Milestone 3 – Intelligence Layer")

if st.session_state.clean_df is not None:
    df = st.session_state.clean_df.copy()

    # --------- Fix unrealistic values (for demo clarity) ----------
    df["sleep_hours"] = df["sleep_hours"].clip(lower=5.5, upper=8.5)
    df["steps"] = df["steps"].clip(lower=800, upper=12000)

    # ----------------- Daily Comparative Analytics -----------------
    st.subheader("📊 Daily Comparative Analytics")
    daily_df = daily_comparison(df)
    st.dataframe(daily_df)

    st.line_chart(
    df.set_index("timestamp")["heart_rate"],
    height=300
)

    # ----------------- Anomaly Detection -----------------
    st.subheader("⚠ Heart Rate Anomaly Detection")
    anomaly_df = detect_anomalies(df)
    anomaly_count = int(anomaly_df["anomaly"].sum())

    st.metric(
        label="Total Heart Rate Anomalies Detected",
        value=anomaly_count
    )

    # ----------------- Behaviour Analysis -----------------
    st.subheader("🧠 Behaviour Analysis Summary")
    behavior = analyze_behavior(df)

    b1, b2, b3 = st.columns(3)
    b1.metric("Avg Daily Steps", int(behavior["average_steps"]))
    b2.metric("Avg Sleep (hrs)", round(behavior["average_sleep_hours"], 1))
    b3.metric("Lifestyle", behavior["behavior_label"])

    # ----------------- NEW FEATURE: Wellness Score -----------------
    st.subheader("🌿 Overall Wellness Score")

    avg_hr = daily_df["avg_heart_rate"].mean()
    avg_steps = behavior["average_steps"]
    avg_sleep = behavior["average_sleep_hours"]

    score = (
        (100 - abs(avg_hr - 70)) * 0.4 +
        min(avg_steps / 100, 100) * 0.3 +
        (avg_sleep / 8 * 100) * 0.3
    )

    score = int(min(max(score, 0), 100))

    if score >= 75:
        status = "Good 😊"
    elif score >= 50:
        status = "Moderate 🙂"
    else:
        status = "Needs Improvement ⚠"

    s1, s2 = st.columns(2)
    s1.metric("Wellness Score", score)
    s2.metric("Health Status", status)


# --------------------------------------------------
# STEP 5: Milestone 4 – Unified Dashboard & Export
# --------------------------------------------------
st.header("🧩 Milestone 4 – Unified Dashboard & Productivity")

if st.session_state.clean_df is not None:

    st.subheader("📋 Auto-Generated Health Summary")
    summary_df = generate_summary_report(st.session_state.clean_df)
    st.dataframe(summary_df)

    st.download_button(
        label="⬇ Download Summary Report",
        data=summary_df.to_csv(index=False),
        file_name="fitpulse_summary_report.csv"
    )

    st.download_button(
        label="⬇ Download Cleaned Dataset",
        data=st.session_state.clean_df.to_csv(index=False),
        file_name="cleaned_fitness_data.csv"
    )
else:
    st.info("Please run preprocessing to enable report export.")
