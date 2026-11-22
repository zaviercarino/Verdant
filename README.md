# 🌱 VERDANT

<div align="center">

### Intelligent Soil Moisture Prediction

**A lightweight machine-learning system for environmental simulation, time-series forecasting, and predictive soil monitoring.**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data_Engineering-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Simulation-013243?style=for-the-badge&logo=numpy&logoColor=white)

![Status](https://img.shields.io/badge/STATUS-ACTIVE_DEVELOPMENT-2EA44F?style=flat-square)
![Stage](https://img.shields.io/badge/PHASE-ML_MODELING-228B22?style=flat-square)
![Data](https://img.shields.io/badge/DATA-SYNTHETIC-6B7280?style=flat-square)

*Simulate. Analyze. Predict.*

---

</div>

## 🌿 Overview

**Verdant** is an experimental machine-learning project exploring how environmental conditions and historical measurements can be used to predict soil moisture levels.

The system combines a custom-built environmental simulator, a time-series data processing pipeline, and lightweight regression models to investigate whether machine learning can outperform simpler forecasting approaches.

Rather than relying on preexisting datasets, Verdant generates controlled synthetic environmental data, allowing experiments across different temperatures, humidity levels, watering schedules, and initial soil conditions.

The long-term objective is to transition from software simulation to a physical monitoring system using a **Raspberry Pi Pico 2**.

> **Core Research Question**
>
> Can a lightweight machine-learning model accurately predict future soil moisture levels using historical measurements and environmental conditions, and can it outperform a simple statistical baseline?

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🌡️ Environmental Simulation | Generates temperature, humidity, and moisture data 
| 💧 Watering Simulation | Supports configurable watering schedules and amounts 
| 📊 Data Engineering | Processes raw time-series measurements into ML-ready datasets
| 🧠 Linear Regression | Trains a supervised model to predict future soil moisture 
| 📉 Error Evaluation | Evaluates predictions using Mean Absolute Error
| 📏 Baseline Comparison | Compares ML predictions against persistence forecasting
| 📈 Model Visualization | Visualizes predictions and forecasting errors

---

## 🏗️ System Architecture

```text
                 🌱 VERDANT
                      │
          ┌───────────▼───────────┐
          │Environmental Simulator│
          │                       │
          │  • Temperature        │
          │  • Humidity           │
          │  • Soil Moisture      │
          │  • Watering Events    │
          └───────────┬───────────┘
                      │
                      ▼
             Raw Time-Series Data
                      │
          ┌───────────▼───────────┐
          │   Data Processing     │
          │                       │
          │  • Moisture Changes   │
          │  • Rolling Averages   │
          │  • Feature Selection  │
          │  • Target Creation    │
          └───────────┬───────────┘
                      │
                      ▼
              ML-Ready Dataset
                      │
          ┌───────────▼───────────┐
          │ Chronological Split   │
          │                       │
          │    80% Training       │
          │    20% Testing        │
          └───────────┬───────────┘
                      │
                      ▼
          ┌───────────────────────┐
          │  Linear Regression    │
          │                       │
          │  Model Training       │
          │  Future Prediction    │
          └───────────┬───────────┘
                      │
                      ▼
          ┌───────────────────────┐
          │   Model Evaluation    │
          │                       │
          │  • MAE                │
          │  • Baseline Comparison│
          │  • Error Analysis     │
          └───────────────────────┘
```

The architecture is designed to support experimentation with multiple prediction algorithms without requiring significant changes to the simulation or preprocessing pipeline.

---

## 🔬 Environmental Simulation

Verdant's custom simulation engine generates hourly environmental measurements using configurable parameters.

### Simulation Inputs

| Parameter | Description |
|---|---|
| `initial_moisture` | Starting soil moisture level |
| `trial_hours` | Duration of the simulation |
| `temperature` | Baseline environmental temperature |
| `humidity` | Baseline relative humidity |
| `watering_hours` | Hours when watering occurs |
| `watering_amount` | Moisture added during watering |
| `trial_seed` | Random seed for reproducibility |

### Environmental Modeling

**Temperature**

Daily temperature fluctuations are modeled using a sinusoidal function:

\[
T(t)=T_{base}+3\sin\left(\frac{2\pi(t-8)}{24}\right)+\epsilon_T
\]

**Humidity**

Humidity varies throughout the day using an inverse sinusoidal pattern:

\[
H(t)=H_{base}-8\sin\left(\frac{2\pi(t-8)}{24}\right)+\epsilon_H
\]

**Moisture Loss**

The simulation uses an empirical moisture-loss equation:

\[
L=0.15+0.02(T-20)+0.005(60-H)+\epsilon
\]

Where:

- \(T\) represents temperature.
- \(H\) represents relative humidity.
- \(\epsilon\) introduces stochastic variation.
- \(L\) represents simulated moisture loss.

These equations are simplified assumptions for generating synthetic datasets, not validated physical models of soil evaporation.

---

## 🧠 Machine Learning Pipeline

Verdant currently uses **Scikit-learn's Linear Regression** as its first predictive model.

### 01 — Feature Engineering

Raw simulation measurements are transformed into structured machine-learning inputs.

Engineered features include:

- Hourly moisture changes
- Rolling three-hour moisture-change averages
- Historical moisture measurements
- Environmental measurements
- Watering-related observations

The prediction target, `Next_Moisture`, represents soil moisture at the following time step.

### 02 — Time-Series Splitting

Unlike randomly shuffled datasets, Verdant preserves chronological order during model evaluation.

```python
split_index = int(len(dataset.x) * 0.8)

x_train = dataset.x.iloc[:split_index]
x_test = dataset.x.iloc[split_index:]

y_train = dataset.y.iloc[:split_index]
y_test = dataset.y.iloc[split_index:]
```

The first 80% of observations are used for training, while the final 20% are reserved for testing.

This better reflects the forecasting objective: predicting later observations using patterns learned from earlier data.

### 03 — Model Training

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(x_train, y_train)

predictions = model.predict(x_test)
```

Linear Regression provides an interpretable starting point for investigating relationships between environmental variables and future soil moisture.

### 04 — Performance Evaluation

Verdant currently evaluates prediction accuracy using **Mean Absolute Error (MAE)**.

\[
MAE=\frac{1}{n}\sum_{i=1}^{n}|y_i-\hat{y}_i|
\]

```python
from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(y_test, predictions)

print("MAE:", mae)
```

MAE measures the average absolute prediction error in the target's units.

Lower values indicate more accurate predictions.

### 05 — Baseline Comparison

**Next development milestone**

A persistence baseline will predict that the next soil moisture measurement equals the current measurement:

\[
\hat{M}_{t+1}=M_t
\]

The Linear Regression model will be evaluated against this baseline on the same held-out observations.

This comparison is essential because low prediction error alone does not demonstrate that machine learning offers a meaningful improvement.

---

## 📊 Experimental Evaluation

The following questions guide Verdant's development:

1. How accurately can Linear Regression predict future soil moisture?
2. Does it outperform a persistence-based forecast?
3. How does performance change under different environmental conditions?
4. Can a model trained on one simulation generalize to independently generated trials?
5. Can the prediction pipeline eventually operate efficiently on resource-constrained hardware?

### Current Results

The initial Linear Regression training and MAE evaluation pipeline has been implemented.

Quantitative performance results are not yet documented here. Baseline comparisons and cross-trial validation are upcoming experiments.

Future results will include model error tables, prediction visualizations, and comparisons across independent trials.

---

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Numerical Computing | NumPy |
| Data Processing | Pandas |
| Machine Learning | Scikit-learn |
| Automated Testing | Pytest |
| Development | Visual Studio Code |
| Version Control | Git / GitHub |

---

## ⚠️ Limitations

Verdant is currently a **synthetic-data research prototype**.

Its environmental simulation intentionally simplifies real-world soil dynamics. Physical processes such as drainage, soil composition, plant uptake, and sensor behavior are not yet fully represented.

Additionally, evaluating a model on synthetic data generated from known mathematical relationships does not establish its accuracy on real-world measurements.

Future experiments will prioritize:

- Testing on independently generated trials.
- Comparing performance against simple baselines.
- Preventing data leakage in time-series features.
- Evaluating performance under changing conditions.
- Validating predictions against physical sensor measurements.

---

## 🌍 Long-Term Vision

Verdant's long-term goal is to bridge software-based predictive modeling and practical embedded environmental monitoring.

Potential future applications include intelligent irrigation assistance, low-cost plant monitoring, environmental forecasting, and resource-efficient edge machine learning.

The project is developed with an emphasis on **reproducible experimentation, transparent evaluation, and engineering fundamentals** rather than unsupported performance claims.

---

<div align="center">

### 🌱 VERDANT

**From environmental data to intelligent prediction.**

*Python • Machine Learning • Environmental Simulation • Embedded Systems*

**Status: Active Development | November 2026**
*README.md built with assistance of my best bud, GPT*

</div>
