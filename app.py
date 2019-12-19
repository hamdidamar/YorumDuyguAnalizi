from flask import Flask,render_template,url_for,request
from flask_bootstrap import Bootstrap
import pandas as pd 
import numpy as np 
from sklearn.externals import joblib
import json
import model_egitim as m
from sklearn.feature_extraction.text import CountVectorizer

vocabulary = joblib.load('models/feature_list.pkl')
vect = CountVectorizer(encoding ='utf8',vocabulary = vocabulary)


#paketler
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.externals import joblib

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/predict',methods=['POST']) 
def predict():
	LR = joblib.load('models/LogistigRegressionModel.pkl')
	columns_model = joblib.load('models/model_columns.pkl')
	
	if request.method == 'POST':
		yorum = request.form['yorum']
		sonuc = m.analiz(yorum)
		if sonuc == True:
			return render_template('results.html',prediction = 'OLUMLU',yorum = yorum)
		else :
			return render_template('results.html',prediction = 'OLUMSUZ',yorum = yorum)




if __name__ == '__main__':
	app.run(debug=True)