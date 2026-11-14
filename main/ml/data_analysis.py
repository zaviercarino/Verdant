import pandas as pd
from pathlib import Path

current_dir = Path(__file__).resolve().parent
trial_data = current_dir.parent / "tests" / "trialdata1.csv"

df = pd.read_csv(trial_data)

def clean_data(df):
    df["Hour"] = range(len(df))
    df.set_index("Hour", inplace=True)
    
    df["Moisture_Change"] = df["Moisture"].diff().fillna(0)
    
    return df


def calculate_statistics(df):
    stats = {
        "Mean" : round(df["Moisture"].mean(), 2),
        "Max" : df["Moisture"].max(),
        "Min" : df["Moisture"].min(),
    }
    return stats

clean_data(df)
print(calculate_statistics(df))
print(df)