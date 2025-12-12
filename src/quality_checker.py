import pandas as pd

def quality_report(df):
    report = {
        "total_rows": len(df),
        "missing_values": df.isnull().sum().to_dict(),
        "timestamp_range": (
            df.index.min(),
            df.index.max()
        ),
        "duplicate_timestamps": df.index.duplicated().sum()
    }

    print("\n📊 DATA QUALITY REPORT")
    for k, v in report.items():
        print(f"{k}: {v}")

    return report
