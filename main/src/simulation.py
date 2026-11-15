import random
import csv
import math # Used later for temperature and humidity equation
from pathlib import Path

class PlantSimulation:

    def __init__(self, initial_moisture, trial_hours, temperature, humidity, watering_hours, watering_amount, trial_seed):
        self.initial_moisture = initial_moisture
        self.trial_hours = trial_hours
        self.temperature = temperature
        self.humidity = humidity
        self.watering_hours = watering_hours
        self.watering_amount = watering_amount
        self.trial_seed = trial_seed
        self.rng = random.Random(trial_seed)

    def simulate_trial(self):
        temperature = self.temperature
        humidity = self.humidity
        moisture = self.initial_moisture
        data_set = {}

        for i in range(self.trial_hours):
                temperature += self.rng.uniform(-0.5, 0.5)
                humidity += self.rng.uniform(-2, 2)
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
         with open(f"{filename}", "w", newline="") as file:
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

plant1 = PlantSimulation(75, 168, 22, 60, [24, 72, 120], 12, 67)