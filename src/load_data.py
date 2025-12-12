import pandas as pd
import json

def load_heart_rate(path):
    return pd.read_csv(path, parse_dates=["timestamp"])

def load_steps(path):
    with open(path) as f:
        raw = json.load(f)
    df = pd.DataFrame(raw)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df

def load_sleep(path):
    return pd.read_csv(path, parse_dates=["timestamp"])
