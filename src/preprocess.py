import pandas as pd
import json
import os

def run_preprocessing():
    # Ensure folder exists
    os.makedirs("data_clean", exist_ok=True)

    # Load heart rate
    hr = pd.read_csv("data_raw/heart_rate.csv")
    hr["timestamp"] = pd.to_datetime(hr["timestamp"])

    # Load steps
    steps = pd.read_csv("data_raw/steps.csv")
    steps["timestamp"] = pd.to_datetime(steps["timestamp"])

    # Load sleep
    with open("data_raw/sleep.json", "r") as f:
        sleep_json = json.load(f)

    sleep_df = pd.DataFrame(sleep_json["cycles"])
    sleep_df["timestamp"] = pd.to_datetime(sleep_df["timestamp"])
    sleep_df.rename(columns={"duration_min": "sleep_minutes"}, inplace=True)

    # Merge all
    df = hr.merge(steps, on="timestamp", how="left")
    df = df.merge(sleep_df[["timestamp", "sleep_minutes"]], on="timestamp", how="left")

    # Fill missing values
    df["steps"] = df["steps"].fillna(0)
    df["calories_burned"] = df["calories_burned"].fillna(0)
    df["sleep_minutes"] = df["sleep_minutes"].fillna(0)

    # Add enriched features
    df["sleep_hours"] = df["sleep_minutes"] / 60

    # Save final cleaned dataset
    df.to_csv("data_clean/cleaned_fitness_data.csv", index=False)

    print("✔ Preprocessing complete — cleaned_fitness_data.csv generated")
