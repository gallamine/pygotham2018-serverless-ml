from flask import Flask
from flask import request, render_template, make_response
import gzip
import json
import pickle 

from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RandomizedSearchCV
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

import validate_data as vd

app = Flask(__name__)


def _load_model() -> Pipeline:
	with gzip.open('model.pkl.gzip', 'rb') as f:
		model = pickle.load(f)

	return model


def _predict_bad_event(features):
	return list(model.predict_proba([features])[0])

@app.route("/predict")
def predict():

	features = vd.validate_data(request)
	print(f"Features: {features}")

	return f"{_predict_bad_event(features)[1]}"

@app.route("/")
def start():

	return render_template('index.html')


model = _load_model()	# This runs as soon as the Lambda container starts
