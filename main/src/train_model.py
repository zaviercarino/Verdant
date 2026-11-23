import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from prepare_ml_data import create_new_ml_dataset

def train_and_evaluate(trial_name):
    dataset = create_new_ml_dataset(trial_name)

    # Split the dataset into training and testing samples
    split_index = int(len(dataset.x) * 0.8)
    x_train = dataset.x.iloc[:split_index]
    x_test = dataset.x.iloc[split_index:]
    y_train = dataset.y.iloc[:split_index]
    y_test = dataset.y.iloc[split_index:]

    # Create a linear regression model based off the samples
    model = LinearRegression()
    model.fit(x_train, y_train)

    # Make predictions about what the next value is using previous data
    predictions = model.predict(x_test)
    mae = mean_absolute_error(y_test, predictions)
    print("MAE:", mae)

    # Calculate result accuracy
    results = x_test.copy()
    results["Actual"] = y_test
    results["Predicted"] = predictions
    results["Absolute_Error"] = (results["Actual"] - results["Predicted"]).abs()

    baseline_predictions = x_test["Moisture"]
    baseline_mae = mean_absolute_error(y_test, baseline_predictions)
    print("Baseline MAE:", baseline_mae)

    xtrain_water_event_count = x_train["Watered_Next_Hour"].sum()
    xtest_water_event_count = x_test["Watered_Next_Hour"].sum()

    model_coefficients = dict(zip(dataset.x.columns, model.coef_))
    
    print("Coefficients:", model_coefficients) 
    print("Intercept:", model.intercept_)

    return model, mae

train_and_evaluate("TrialDataOne")
train_and_evaluate("TrialDataTwo")
train_and_evaluate("TrialDataThree")
train_and_evaluate("TrialDataFour")