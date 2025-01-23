from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

# Load model parameters
with open("models/model_params.pkl", "rb") as f:
    model_params = pickle.load(f)
    W = model_params["Weight"]
    b = model_params["Bias"]

# Load scaler
with open("models/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Sigmoid function
def sig(x):
    return 1 / (1 + np.exp(-x))

# Prediction function
def predict(X, W, b):
    return sig(np.dot(X, W) + b)

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    if request.method == 'POST':
        # Get form inputs
        pclass = float(request.form.get('Pclass'))
        age = float(request.form.get('Age'))
        sbsp = float(request.form.get('SibSp'))
        parch = float(request.form.get('Parch'))
        fare = float(request.form.get('Fare'))
        sex = request.form.get('Sex')
        port = request.form.get('Port')

        # Convert categorical inputs to numerical values
        Sex_male = 1 if sex.lower() == 'male' else 0
  
        if port.upper() == "C":
            Embarked_Q = 0
            Embarked_S = 0
        elif port.upper() == "Q":
            Embarked_Q = 1
            Embarked_S = 0
        else:
            Embarked_Q = 0
            Embarked_S = 1

        # Prepare input data
        data_dict = [{
            "Pclass": pclass,
            "Age": age,
            "SibSp": sbsp,
            "Parch": parch,
            "Fare": fare,
            "Sex_male": Sex_male,
            "Embarked_Q": Embarked_Q,
            "Embarked_S": Embarked_S
        }]
        
        df = pd.DataFrame(data_dict)

        # Ensure feature names match with the scaler's expectations
        expected_features = ['Age', 'Fare']
        df[expected_features] = scaler.transform(df[expected_features])
        
        # Convert to numpy array for prediction
        X = df.to_numpy()
        
        # Make prediction
        pred = predict(X, W, b)

        # Interpret prediction result
        prediction = "Survived" if pred[0] >= 0.5 else "Did not Survive"

    return render_template('index.html', prediction=prediction)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
