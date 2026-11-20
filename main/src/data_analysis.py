import pandas as pd
import csv
from pathlib import Path
current_dir = Path(__file__).resolve().parent

def clean_data(df, trial_name):
    df = df.copy()

    df["Moisture_Change"] = df["Moisture"].diff().fillna(0)
    df["Hour"] = df["Hour"].str.replace("Hour", "").astype(int)
    df["Three_Hour_Avg"] = round((df["Moisture"].rolling(window=3).mean()), 2)
    
    df.set_index("Hour", inplace=True)
    
    generate_csv(df, trial_name, "processed")

    return df

def generate_csv(dataset, filename, folder_name):
    try:
        output_path = current_dir.parent / "data" / f"{folder_name}" / f"{filename}.csv"
        with open(output_path, "w", newline="") as file:
                writer = csv.writer(file)
        
                writer.writerow([dataset.index.name or "Hour", *dataset.columns.tolist()])
        
                for hour, values in dataset.iterrows():
                    writer.writerow([hour, *values.tolist()])

    except ValueError:
        return ValueError

def calculate_statistics(df):
    stats = {
        "Mean" : round(df["Moisture"].mean(), 2),
        "Max" : df["Moisture"].max(),
        "Min" : df["Moisture"].min(),
    }
    return stats

def get_watering_hours(df):
    return df.loc[df["Watered"]].index.tolist()