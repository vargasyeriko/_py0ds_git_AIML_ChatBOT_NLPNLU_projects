
from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the model and scaler at the start to avoid loading them multiple times
model = load_model('my_model.h5')
scaler = joblib.load('scaler.joblib')

# This endpoint processes requests and returns predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract JSON data from POST request
        data = request.get_json()

        # Convert region to one-hot encoding
        regions = ['North', 'South', 'East', 'West']
        region_input = regions.index(data['region'])  # Get the index of the region
        region_one_hot = np.zeros((1, len(regions)))
        region_one_hot[0, region_input] = 1

        # Collect the rest of the numerical values
        numerical_data = np.array([[data['month'], data['marketing_spend'], data['economic_index'],
                                    data['competitor_activity'], data['historical_sales']]])

        # Create a DataFrame with the correct feature names for scaling
        feature_names = ['Month', 'Marketing Spend', 'Economic Index', 'Competitor Activity', 'Historical Sales']
        numerical_inputs_df = pd.DataFrame(numerical_data, columns=feature_names)

        # Normalize the numerical inputs
        numerical_inputs_normalized = scaler.transform(numerical_inputs_df)

        # Combine the one-hot encoded region with the normalized numerical features
        final_input = np.hstack((region_one_hot, numerical_inputs_normalized))

        # Make a prediction
        predicted_sales = model.predict(final_input)

        # Convert the prediction to a Python float (standard type)
        prediction = float(predicted_sales[0][0])

        # Return the prediction as a JSON response
        return jsonify({'prediction': prediction})

    except Exception as e:
        # If any error occurs, send an error message
        return jsonify({'error': str(e), 'message': 'Error processing request'}), 400

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False for production mode
