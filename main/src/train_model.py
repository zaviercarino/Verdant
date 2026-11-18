# Load and prepare your first trial using your existing MLDataset class.
# Split X and y chronologically into 80% training and 20% testing.
# Initialize a LinearRegression model.
# Train it using .fit(X_train, y_train).
# Generate predictions using .predict(X_test).
# Calculate the mean absolute error (MAE).

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from prepare_ml_data import create_new_ml_dataset

# trial_data_files = {
#     "TrialDataOne" : pd.read_csv(current_dir.parent / "data" / "raw" / f"trial1data.csv"),
#     "TrialDataTwo" : pd.read_csv(current_dir.parent / "data" / "raw" / f"trial2data.csv")
# }

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

    return model, mae

train_and_evaluate("TrialDataOne")