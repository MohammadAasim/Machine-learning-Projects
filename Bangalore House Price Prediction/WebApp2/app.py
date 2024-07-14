import pandas as pd
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

data = pd.read_csv('Cleaned_data.csv')
with open('RidgeModel.pkl', 'rb') as file:
    pipe = pickle.load(file)

@app.route("/")
def index():
    locations = sorted(data['location'].unique())
    return render_template('index.html', locations=locations)

@app.route('/predict', methods=['POST'])
def predict():
    location = request.form.get('location')
    bhk = request.form.get('bhk')
    bath = request.form.get('bath')
    sqft = request.form.get('total_sqft')

    input_data = pd.DataFrame([[location, sqft, bath, bhk]], columns=['location', 'total_sqft', 'bath', 'bhk'])
    prediction = pipe.predict(input_data)[0] * 1e5

    return str(prediction)

if __name__ == "__main__":
    app.run(debug=True)
