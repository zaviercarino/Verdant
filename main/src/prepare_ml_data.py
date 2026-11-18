# Load one of your simulated CSV files using pandas.
# Convert the hour labels into integers.
# Create a Next_Moisture column using shift(-1).
# Remove rows where Next_Moisture is missing.
# Separate your input features (X) from your prediction target (y).
# Print the shapes of X and y.

import pandas as pd
from pathlib import Path
current_dir = Path(__file__).resolve().parent

trial_data_files = {
    "TrialDataOne" : pd.read_csv(current_dir.parent / "data" / "raw" / f"trial1data.csv"),
    "TrialDataTwo" : pd.read_csv(current_dir.parent / "data" / "raw" / f"trial2data.csv")
}

def string_to_int_hour_column(df):
    new_df = df.copy()
    new_df["Hour"] = new_df["Hour"].str.replace("Hour", "").astype(int)
    
    return new_df

new_df_one = string_to_int_hour_column(trial_data_files["TrialDataOne"])
print(new_df_one)