import random
import pandas as pd
import math

from data_analysis import generate_csv

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

if __name__ == "__main__":
    plant1 = PlantSimulation(75, 168, 22, 60, [24, 72, 120,], 12, 67)
    trial1 = pd.DataFrame(plant1.simulate_trial()).T
    generate_csv(trial1, "Trial_One_Data", "raw")

    plant2 = PlantSimulation(75, 168, 20, 63, [24, 72, 120], 11, 69)
    trial2 = pd.DataFrame(plant2.simulate_trial()).T
    generate_csv(trial2, "Trial_Two_Data", "raw")

    plant3 = PlantSimulation(75, 168, 25, 57, [24, 72, 120], 13, 65)
    trial3 = pd.DataFrame(plant3.simulate_trial()).T
    generate_csv(trial3, "Trial_Three_Data", "raw")

    plant4 = PlantSimulation(75, 168, 25, 57, [30, 60, 90, 120, 150], 13, 63)
    trial4 = pd.DataFrame(plant4.simulate_trial()).T
    generate_csv(trial4, "Trial_Four_Data", "raw")
