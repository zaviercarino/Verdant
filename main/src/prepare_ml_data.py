import pandas as pd
from pathlib import Path
from data_analysis import prepare_ml_data

current_dir = Path(__file__).resolve().parent

trial_data_files = {
    "TrialDataOne" : pd.read_csv(current_dir.parent / "data" / "raw" / f"trial1data.csv"),
    "TrialDataTwo" : pd.read_csv(current_dir.parent / "data" / "raw" / f"trial2data.csv"),
    "TrialDataThree" : pd.read_csv(current_dir.parent / "data" / "raw" / f"trial3data.csv")
}

class MLDataset():
    
    feature_columns = [
        "Temperature",
        "Humidity",
        "Moisture"
    ]

    def __init__(self, trial_data):
        self.trial_data = trial_data
        self.x = trial_data[self.feature_columns]
        self.y = trial_data["Next_Moisture"]

    def __str__(self):
        return f"X Shape: {self.x.shape} \nY Shape: {self.y.shape}"

def create_new_ml_dataset(trial_name): 
    return MLDataset(prepare_ml_data(trial_data_files[f"{trial_name}"]))
