from re import template
from flask import Flask,render_template,url_for,request,jsonify
from flask_cors import cross_origin
import pandas as pd
import numpy as np
import datetime
import pickle



app = Flask(__name__,template_folder="template")
model = pickle.load(open("models/cat.pkl", "rb"))
print("Model Loaded")

@app.route("/",methods=['GET'])
@cross_origin()
def home():
	return render_template("index.html")

@app.route("/predict",methods=['GET', 'POST'])
@cross_origin()
def predict():
	if request.method == "POST":
		# DATE
		date = request.form['date']
		day = float(pd.to_datetime(date, format="%Y-%m-%dT").day)
		month = float(pd.to_datetime(date, format="%Y-%m-%dT").month)
		# MinTemp
		minTemp = float(int(request.form['mintemp']))
		# MaxTemp
		maxTemp = float(int(request.form['maxtemp']))
		# Rainfall
		rainfall = float(int(request.form['rainfall']))
		# Evaporation
		evaporation = float(int(request.form['evaporation']))
		# Sunshine
		sunshine = float(int(request.form['sunshine']))
		# Wind Gust Speed
		windGustSpeed = float(int(request.form['windgustspeed']))
		# Wind Speed 9am
		windSpeed9am = float(int(request.form['windspeed9am']))
		# Wind Speed 3pm
		windSpeed3pm = float(int(request.form['windspeed3pm']))
		# Humidity 9am
		humidity9am = float(int(request.form['humidity9am']))
		# Humidity 3pm
		humidity3pm = float(int(request.form['humidity3pm']))
		# Pressure 9am
		pressure9am = float(int(request.form['pressure9am']))
		# Pressure 3pm
		pressure3pm = float(int(request.form['pressure3pm']))
		# Temperature 9am
		temp9am = float(int(request.form['temp9am']))
		# Temperature 3pm
		temp3pm = float(int(request.form['temp3pm']))
		# Cloud 9am
		cloud9am = float(int(request.form['cloud9am']))
		# Cloud 3pm
		cloud3pm = float(int(request.form['cloud3pm']))
		# Cloud 3pm
		location = request.form['location']
		# Wind Dir 9am
		winddDir9am = request.form['winddir9am']
		# Wind Dir 3pm
		winddDir3pm = request.form['winddir3pm']
		# Wind Gust Dir
		windGustDir = request.form['windgustdir']
		# Rain Today
		rainToday = request.form['raintoday']

		input_lst = [location , minTemp , maxTemp , rainfall , evaporation , sunshine ,
					 windGustDir , windGustSpeed , winddDir9am , winddDir3pm , windSpeed9am , windSpeed3pm ,
					 humidity9am , humidity3pm , pressure9am , pressure3pm , cloud9am , cloud3pm , temp9am , temp3pm ,
					 rainToday , month , day]
		pred = model.predict(input_lst)
		output = pred
		if output == 0:
			return render_template("after_sunny.html")
		else:
			return render_template("after_rainy.html")
	return render_template("predictor.html")

if __name__=='__main__':
	app.run(debug=True)
