import random
import csv
import math

from pathlib import Path
current_dir = Path(__file__).resolve().parent

class PlantSimulation:

    def __init__(self, initial_moisture, trial_hours, temperature, humidity, watering_hours, watering_amount, trial_seed):
        self.initial_moisture = initial_moisture
        self.trial_hours = trial_hours
        self.temperature = temperature
        self.humidity = humidity
        self.watering_hours = watering_hours
        self.watering_amount = watering_amount
        self.trial_seed = trial_seed

    def simulate_trial(self):
        self.rng = random.Random(self.trial_seed)
        temperature = self.temperature
        humidity = self.humidity
        moisture = self.initial_moisture
        data_set = {}

        for i in range(self.trial_hours):
                temperature = self.temperature + 3 * math.sin((2 * math.pi * (i - 8))/24) + self.rng.uniform(-0.3, 0.3)
                humidity = self.humidity - 8 * math.sin((2 * math.pi * (i - 8))/24) + self.rng.uniform(-0.3, 0.3)
                moisture_equation = (0.15 + 0.02 * (temperature - 20) + 0.005 * (60 - humidity) + self.rng.uniform(0.1, 0.3))
                watered = False
        
                if (i + 1) in self.watering_hours:
                    moisture += self.watering_amount
                    watered = True
                moisture -= moisture_equation
        
                data_set[f"Hour{i + 1}"] = {
                    "Temperature" : round(temperature, 2),
                    "Humidity" : round(humidity, 2),
                    "Moisture" : round(moisture, 2),
                    "Watered" : watered

                }

        return data_set

    def generate_csv(self, dataset, filename):
        output_path = current_dir.parent / "data" / "raw" / f"{filename}.csv"

        with open(output_path, "w", newline="") as file:
                writer = csv.writer(file)
         
                writer.writerow(["Hour", "Temperature", "Humidity", "Moisture", "Watered"])
         
                for hour, values in dataset.items():
                    writer.writerow([
                        hour, 
                        values["Temperature"],
                        values["Humidity"],
                        values["Moisture"],
                        values["Watered"]
                    ])

if __name__ == "main":
    plant1 = PlantSimulation(75, 168, 22, 60, [24, 72, 120], 12, 67)
    trial1 = plant1.simulate_trial()
    plant1.generate_csv(trial1, "trial1data")

    plant2 = PlantSimulation(75, 165, 20, 63, [84], 11, 69)
    trial2 = plant2.simulate_trial()
    plant2.generate_csv(trial2, "trial2data")