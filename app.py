# 컨트롤러 만들거임
from flask import Flask, render_template, request
from models import dbMgr
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import RobustScaler

# app에 플라스크 객체 선언. 컨트롤 할 수 있는 space를 만들었다.
app = Flask(__name__)

# main pape
@app.route('/')

def index():
    return render_template('index.html')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/team')
def team():
    return render_template('team.html')    


@app.route('/modeling_page')
def modeling_page():
    return render_template('modeling_page.html')

 
@app.route('/modeling', methods=['POST'])
def modeling():
    # name = request.form['name']
    age = request.form['age']
    weight = request.form['weight']
    runtime = request.form['runtime']
    maxpulse = request.form['maxpulse']
    runpulse = request.form['runpulse']
    rstpulse = request.form['rstpulse']
    
    data1 = [[age,weight,runtime,maxpulse,runpulse,rstpulse]]
    estimator = dbMgr.modeling_RF()
    df3 = pd.DataFrame(data=data1)
    predict = estimator.predict(df3)
    
    return render_template('modeling_page.html', predict=predict) 

# finished code
if __name__ == '__main__':
    # app.debug = True
    # app.run()
    app.run(host='0.0.0.0', port=5000, debug=True)
