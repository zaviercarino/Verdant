import pandas as pd
from pathlib import Path

current_dir = Path(__file__).resolve().parent
trial_data = current_dir.parent / "tests" / "trialdata1.csv"

df = pd.read_csv(trial_data)
print(df.head())