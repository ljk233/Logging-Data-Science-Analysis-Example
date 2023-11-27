"""main.py

Main script for simulating data and performing linear regression analysis.

This script:
- sets up a logger
- simulates a dataset
- splits the data into training and testing sets
- creates a linear regression model
- trains the model
- makes predictions on the test set
- evaluates the model's performance.

The progress is logged in log.txt using a custom logging module.
"""

from src import logger
from sklearn import datasets, model_selection, linear_model, metrics


SIMULATE_RANDOM_STATE = 42
TEST_SIZE = 0.2
TRAIN_TEST_SEED = 18
PRECISION = 6


logger.setup_logger()

# Simulate the data
try:
    X, y = datasets.make_regression(
        n_samples=100, n_features=2, random_state=SIMULATE_RANDOM_STATE
    )
    logger.log_info(
        f"Data loaded successfully using random_state={SIMULATE_RANDOM_STATE}."
    )
except Exception as e:
    logger.log_error(f"Error loading data: {str(e)}")

# Split the data into training and testing sets
try:
    X_train, X_test, y_train, y_test = model_selection.train_test_split(
        X, y, test_size=TEST_SIZE, random_state=TRAIN_TEST_SEED
    )
    logger.log_info(
        "Data split into training and testing sets"
        + f" (test_size={TEST_SIZE}, random_state={TRAIN_TEST_SEED})"
    )
except Exception as e:
    logger.log_info(f"Error splitting data: {str(e)}")

# Create a linear regression model
lin_regress_model = linear_model.LinearRegression()

# Train the model
try:
    lin_regress_model.fit(X_train, y_train)
    logger.log_info("Model trained successfully.")
except Exception as e:
    logger.log_error(f"Error training model: {str(e)}")

# Make predictions on the test set
try:
    y_pred = lin_regress_model.predict(X_test)
    logger.log_info("Predictions made on the test set.")
except Exception as e:
    logger.log_error(f"Error making predictions: {str(e)}")

# Evaluate the model
try:
    mse = metrics.mean_squared_error(y_test, y_pred)
    logger.log_info(
        f"Mean Squared Error: {round(mse, ndigits=PRECISION)} ({PRECISION}dp)"
    )
except Exception as e:
    logger.log_info(f"Error evaluating model: {str(e)}")
