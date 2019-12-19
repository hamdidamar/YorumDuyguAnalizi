from flask import Flask,render_template,url_for,request
from flask_bootstrap import Bootstrap
import pandas as pd 
import numpy as np 
import veriservis as verigetir




app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
	return render_template('veritopla.html')



@app.route('/veritopla',methods=['POST'])
def veritopla():
	if request.method == 'POST':
		kategori = request.form['kategori']
		verigetir(kategori)

	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)