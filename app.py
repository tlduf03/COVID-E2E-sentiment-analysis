import pickle
from flask import Flask, request, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)
# load the model
regmodel = pickle.load(open('finalmodel.pkl', 'rb'))
vectorizer = pickle.load(open('countvectorizer.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

#make a prediction
@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.form['stringdata']
    # print("input datatype:", type(input_data))
    # print("User text : ", input_data)
    final_input = vectorizer.transform([input_data])
    output = regmodel.predict(final_input)
    res = ""
    if output == 0:
        res = "Negative"
    elif output == 1:
        res = "Neutral"
    else: # if output is 2
        res = "Positive"
        
    return render_template('home.html',input_text=input_data, prediction_text="The sentence sentiment is {}".format(res))

if __name__ == '__main__':
    app.run(debug=True)
