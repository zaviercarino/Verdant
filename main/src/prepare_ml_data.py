import pandas as pd
from pathlib import Path
from data_analysis import clean_data, generate_csv

current_dir = Path(__file__).resolve().parent

trial_data_files = {
    "TrialDataOne" : pd.read_csv(current_dir.parent / "data" / "raw" / f"Trial_One_Data.csv"),
    "TrialDataTwo" : pd.read_csv(current_dir.parent / "data" / "raw" / f"Trial_Two_Data.csv"),
    "TrialDataThree" : pd.read_csv(current_dir.parent / "data" / "raw" / f"Trial_Three_Data.csv")
}

class MLDataset():
    
    feature_columns = [
        "Temperature",
        "Humidity",
        "Moisture",
        "Watered_Next_Hour"
    ]

    def __init__(self, trial_data, trial_name):
        trial_data = clean_data(trial_data, trial_name)
        trial_data["Watered_Next_Hour"] = trial_data["Watered"].shift(-1)
        trial_data["Next_Moisture"] = trial_data["Moisture"].shift(-1)
        trial_data = trial_data.dropna(subset=["Next_Moisture"])

        self.trial_data = trial_data
        self.x = trial_data[self.feature_columns]
        self.y = trial_data["Next_Moisture"]
        
        generate_csv(trial_data, trial_name, "ml")

    def __str__(self):
        return f"X Shape: {self.x.shape} \nY Shape: {self.y.shape}"

def create_new_ml_dataset(trial_name): 
    return MLDataset(trial_data_files[f"{trial_name}"], trial_name)
