def detect_anomalies(df):
    df = df.copy()

    hr_mean = df["heart_rate"].mean()
    hr_std = df["heart_rate"].std()

    df["anomaly"] = (
        (df["heart_rate"] > hr_mean + 2 * hr_std) |
        (df["heart_rate"] < hr_mean - 2 * hr_std)
    )

    return df
