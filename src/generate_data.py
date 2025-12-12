import pandas as pd
import numpy as np
import json
from datetime import datetime, timedelta
import os

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

ensure_dir("data_raw")

# ------------------------ HEART RATE DATA ------------------------
def generate_heart_rate_csv():
    start = datetime.now().replace(hour=6, minute=0, second=0, microsecond=0)
    timestamps, hr_values, stress_score = [], [], []

    for i in range(240):   # 4 hours of data
        ts = start + timedelta(minutes=i)
        base = 72 + 8*np.sin(i/15) + np.random.normal(0, 3)
        stress = round(np.interp(base, [55, 120], [10, 90]))  

        timestamps.append(ts)
        hr_values.append(round(max(45, min(base, 160))))
        stress_score.append(stress)

    df = pd.DataFrame({
        "timestamp": timestamps,
        "heart_rate": hr_values,
        "stress_level": stress_score
    })
    df.to_csv("data_raw/heart_rate.csv", index=False)
    return df

# ------------------------ STEPS DATA ------------------------
def generate_steps_csv():
    start = datetime.now().replace(hour=6, minute=0)
    timestamps, steps, calories = [], [], []

    for i in range(240):
        ts = start + timedelta(minutes=i)
        step_count = np.random.poisson(20)
        calories_burn = round(step_count * 0.04, 2)

        timestamps.append(ts)
        steps.append(step_count)
        calories.append(calories_burn)

    df = pd.DataFrame({
        "timestamp": timestamps,
        "steps": steps,
        "calories_burned": calories
    })
    df.to_csv("data_raw/steps.csv", index=False)
    return df

# ------------------------ SLEEP DATA ------------------------
def generate_sleep_json():
    sleep_data = {
        "user": "fit_user_001",
        "sleep_start": "2025-01-12 23:45:00",
        "sleep_end": "2025-01-13 07:10:00",
        "cycles": []
    }

    stages = ["light", "deep", "rem"]
    start = datetime.strptime(sleep_data["sleep_start"], "%Y-%m-%d %H:%M:%S")

    for i in range(15):
        stage_time = start + timedelta(minutes=i * 30)

        sleep_data["cycles"].append({
            "timestamp": stage_time.isoformat(),
            "stage": np.random.choice(stages),
            "duration_min": np.random.randint(15, 40)
        })

    with open("data_raw/sleep.json", "w") as f:
        json.dump(sleep_data, f, indent=2)

    return sleep_data
