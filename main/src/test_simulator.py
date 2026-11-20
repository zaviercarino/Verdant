from simulation import PlantSimulation

def test_random_seed():
    plant = PlantSimulation(
        75, 168, 22, 60,
        [24, 72, 120], 12, 67
    )

    first = plant.simulate_trial()
    second = plant.simulate_trial()

    assert first == second

def test_simulation_length():
    plant = PlantSimulation(
        75, 168, 22, 60,
        [24, 72, 120], 12, 67
    )

    dataset = plant.simulate_trial()

    assert len(dataset) == 168

def test_watering_hours():
    plant = PlantSimulation(
        75, 168, 22, 60,
        [24, 72, 120], 12, 67
    )

    dataset = plant.simulate_trial()
    actual_watering_hours = []

    for hour, values in dataset.items():
        if values["Watered"]:
            hour_number = int(hour.replace("Hour", ""))
            actual_watering_hours.append(hour_number)

    assert actual_watering_hours == [24, 72, 120]
