from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from prepare_ml_data import create_new_ml_dataset

def train_and_evaluate(trial_name):
    dataset = create_new_ml_dataset(trial_name)
    
    split_index = int(len(dataset.x) * 0.8)
    x_train = dataset.x.iloc[:split_index]
    x_test = dataset.x.iloc[split_index:]
    y_train = dataset.y.iloc[:split_index]
    y_test = dataset.y.iloc[split_index:]

    model = LinearRegression()
    model.fit(x_train, y_train)

    predictions = model.predict(x_test)
    mae = mean_absolute_error(y_test, predictions)
    print("MAE:", mae)

    baseline_predictions = x_test["Moisture"]
    baseline_mae = mean_absolute_error(y_test, baseline_predictions)
    print("Baseline MAE:", baseline_mae)

    print("Coefficients:", model.coef_)
    print("Intercept:", model.intercept_)

    return model, mae

train_and_evaluate("TrialDataOne")
train_and_evaluate("TrialDataTwo")
train_and_evaluate("TrialDataThree")