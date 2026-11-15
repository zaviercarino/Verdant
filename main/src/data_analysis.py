import pandas as pd
from pathlib import Path

current_dir = Path(__file__).resolve().parent
trial_data = current_dir.parent / "data" / "raw" / "trialdata1.csv"

df = pd.read_csv(trial_data)

def clean_data(df):
    df = df.copy()

    df["Moisture_Change"] = df["Moisture"].diff().fillna(0)
    df["Hour"] = df["Hour"].str.replace("Hour", "").astype(int)
    df["Three_Hour_Avg"] = round((df["Moisture"].rolling(window=3).mean()), 2)

    df.set_index("Hour", inplace=True)
    return df

def calculate_statistics(df):
    stats = {
        "Mean" : round(df["Moisture"].mean(), 2),
        "Max" : df["Moisture"].max(),
        "Min" : df["Moisture"].min(),
    }
    return stats

def get_watering_hours(df):
    return df.loc[df["Watered"]].index.tolist()

new_df = clean_data(df)
water_hours = get_watering_hours(new_df)
