import pandas as pd
from prophet import Prophet

# -------------------------------------------------
# HEART RATE FORECAST
# -------------------------------------------------
def forecast_heart_rate(df):
    data = df[["timestamp", "heart_rate"]].dropna()

    if len(data) < 2:
        raise ValueError("Not enough heart rate data to forecast.")

    data = data.rename(columns={"timestamp": "ds", "heart_rate": "y"})

    model = Prophet()
    model.fit(data)

    future = model.make_future_dataframe(periods=14)
    forecast = model.predict(future)

    return model, forecast


# -------------------------------------------------
# SLEEP FORECAST
# -------------------------------------------------
def forecast_sleep(df):
    data = df[["timestamp", "sleep_hours"]].dropna()

    if len(data) < 2:
        raise ValueError("Not enough sleep data to forecast.")

    data = data.rename(columns={"timestamp": "ds", "sleep_hours": "y"})

    model = Prophet(weekly_seasonality=True)
    model.fit(data)

    future = model.make_future_dataframe(periods=14)
    forecast = model.predict(future)

    return model, forecast


# -------------------------------------------------
# STEPS FORECAST WITH EVENTS
# -------------------------------------------------
def forecast_steps_with_events(df):
    data = df[["timestamp", "steps"]].dropna()

    if len(data) < 2:
        raise ValueError("Not enough steps data to forecast.")

    data = data.rename(columns={"timestamp": "ds", "steps": "y"})

    model = Prophet()
    model.fit(data)

    future = model.make_future_dataframe(periods=14)
    forecast = model.predict(future)

    return model, forecast
