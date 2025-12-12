import streamlit as st
import pandas as pd
import os

from src.generate_data import (
    generate_heart_rate_csv,
    generate_steps_csv,
    generate_sleep_json
)

from src.preprocess import run_preprocessing


st.set_page_config(page_title="FitPulse – Task 1", layout="wide")

st.title("🔥 FitPulse:  – Data Collection & Cleaning Dashboard")

# ------------------------------------------------------------------
# SESSION STATE INITIALIZATION
# ------------------------------------------------------------------

if "hr_df" not in st.session_state:
    st.session_state.hr_df = None

if "steps_df" not in st.session_state:
    st.session_state.steps_df = None

if "sleep_df" not in st.session_state:
    st.session_state.sleep_df = None

if "clean_df" not in st.session_state:
    st.session_state.clean_df = None


# ------------------------------------------------------------------
# DATA GENERATION SECTION
# ------------------------------------------------------------------

st.header("📌 Step 1: Generate Raw Datasets")

col1, col2, col3 = st.columns(3)

# ----------------- HEART RATE -----------------
with col1:
    if st.button("Generate Heart Rate Data"):
        df = generate_heart_rate_csv()
        st.session_state.hr_df = df
        st.success("Heart Rate data generated!")

if st.session_state.hr_df is not None:
    st.subheader("📍 Heart Rate Data")
    st.dataframe(st.session_state.hr_df.head())

# ----------------- STEPS DATA -----------------
with col2:
    if st.button("Generate Steps Data"):
        df = generate_steps_csv()
        st.session_state.steps_df = df
        st.success("Steps data generated!")

if st.session_state.steps_df is not None:
    st.subheader("📍 Steps Data")
    st.dataframe(st.session_state.steps_df.head())

# ----------------- SLEEP DATA -----------------
with col3:
    if st.button("Generate Sleep Data"):
        sleep_json = generate_sleep_json()
        df_sleep = pd.DataFrame(sleep_json["cycles"])
        st.session_state.sleep_df = df_sleep
        st.success("Sleep data generated!")

if st.session_state.sleep_df is not None:
    st.subheader("📍 Sleep Data ")
    st.dataframe(st.session_state.sleep_df.head())


# ------------------------------------------------------------------
# PREPROCESSING SECTION
# ------------------------------------------------------------------

st.header("📌 Step 2: Clean & Merge All Data")

if st.button("Run Preprocessing Pipeline"):
    run_preprocessing()

    cleaned_path = "data_clean/cleaned_fitness_data.csv"
    if os.path.exists(cleaned_path):
        df_clean = pd.read_csv(cleaned_path)
        st.session_state.clean_df = df_clean
        st.success("🎉 Cleaning & Merging Completed")

# SHOW CLEANED DATA
if st.session_state.clean_df is not None:
    st.subheader("🧹 Cleaned Fitness Data")
    st.dataframe(st.session_state.clean_df.head(30))

    st.download_button(
        label="⬇ Download Cleaned CSV",
        data=st.session_state.clean_df.to_csv(index=False),
        file_name="cleaned_fitness_data.csv"
    )

    # Visualization
    st.subheader("📊 Heart Rate Trend")
    st.line_chart(st.session_state.clean_df.set_index("timestamp")["heart_rate"])

    st.subheader("📈 Summary Insights")
    colA, colB, colC, colD = st.columns(4)
    colA.metric("Min HR", st.session_state.clean_df["heart_rate"].min())
    colB.metric("Max HR", st.session_state.clean_df["heart_rate"].max())
    colC.metric("Avg Steps", int(st.session_state.clean_df["steps"].mean()))
    colD.metric("Avg Sleep (hrs)", round(st.session_state.clean_df["sleep_hours"].mean(), 2))
