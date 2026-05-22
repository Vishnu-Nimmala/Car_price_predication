from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('mini_project_2.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    feature1 = float(request.form['feature1'])
    feature2 = float(request.form['feature2'])
    feature3 = float(request.form['feature3'])
    feature4 = float(request.form['feature4'])

    features = np.array([[feature1, feature2, feature3, feature4]])

    prediction = model.predict(features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text=f'Predicted Value : {output}')

if __name__ == '__main__':
    app.run(debug=True)