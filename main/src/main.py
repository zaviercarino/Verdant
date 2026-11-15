# Moisture Simulation
import random
import csv
from pathlib import Path

hour_count = 24
moisture_level = 75
watering_moisture_increase = 12

def simulate_moisture(moisture, hours, watering_hour):
    data_set = {}
    for i in range(hours):
        watered = False

        if i == watering_hour - 1:
            moisture = apply_watering(moisture, watering_moisture_increase)
            watered = True
        moisture -= random.uniform(0.1, 0.5)

        data_set[f"Hour{i + 1}"] = {
            "moisture" : round(moisture, 2),
            "watered" : watered
        }
    return data_set

def apply_watering(current_moisture, amount):
    return current_moisture + amount

def display_data(dataset):
    print(dataset)

def save_to_csv(dataset, filename):
    with open(f"{filename}", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Hour", "Moisture", "Watered"])

        for hour, values in dataset.items():
            writer.writerow([
                hour, 
                values["moisture"],
                values["watered"]
            ])

trial_data = simulate_moisture(moisture_level, hour_count, 12)

current_dir = Path(__file__).resolve().parent
trial_data_file = current_dir.parent / "data" / "raw" / "trialdata1.csv"

save_to_csv(trial_data, trial_data_file)