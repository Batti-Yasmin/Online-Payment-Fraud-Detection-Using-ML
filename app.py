
from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("fraud_model.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        step = float(request.form['step'])
        type_ = float(request.form['type'])
        amount = float(request.form['amount'])
        oldbalanceOrg = float(request.form['oldbalanceOrg'])
        newbalanceOrig = float(request.form['newbalanceOrig'])
        oldbalanceDest = float(request.form['oldbalanceDest'])
        newbalanceDest = float(request.form['newbalanceDest'])

        final_input = np.array([[step, type_, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest]])
        prediction = model.predict(final_input)

        if prediction[0] == 1:
            result = "⚠ Fraud Transaction Detected"
        else:
            result = "✅ Legitimate Transaction"

        return render_template("index.html", prediction_text=result)

    except Exception as e:
        print(e)
        return render_template("index.html", prediction_text="Invalid Input!")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)