from flask import Flask, render_template

import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    try:
       df = pd.read_csv("logs/log.csv")
       logs = df.values.tolist()
    except pd.errors.EmptyDataError:
       logs = []
    return render_template('index.html', logs = logs[::-1])
