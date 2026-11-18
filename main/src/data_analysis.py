import pandas as pd

def clean_data(df):
    df = df.copy()

    df["Moisture_Change"] = df["Moisture"].diff().fillna(0)
    df["Hour"] = df["Hour"].str.replace("Hour", "").astype(int)
    df["Three_Hour_Avg"] = round((df["Moisture"].rolling(window=3).mean()), 2)

    df.set_index("Hour", inplace=True)

    return df

def prepare_ml_data(df):
    cleaned_df = clean_data(df)

    cleaned_df["Next_Moisture"] = cleaned_df["Moisture"].shift(-1)
    cleaned_df = cleaned_df.dropna(subset=["Next_Moisture"])
    
    return cleaned_df

def calculate_statistics(df):
    stats = {
        "Mean" : round(df["Moisture"].mean(), 2),
        "Max" : df["Moisture"].max(),
        "Min" : df["Moisture"].min(),
    }
    return stats

def get_watering_hours(df):
    return df.loc[df["Watered"]].index.tolist()