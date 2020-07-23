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

 
@app.route('/modeling', methods=['POST'])
def modeling():
    Temp_OXid = request.form['Temp_OXid']
    ppm = request.form['ppm']
    Pressure = request.form['Pressure']
    Oxid_time = request.form['Oxid_time']
    N2_HMDS = request.form['N2_HMDS']
    pressure_HMDS = request.form['pressure_HMDS']
    temp_HMDS = request.form['temp_HMDS']
    Temp_Etching = request.form['Temp_Etching']
    temp_HMDS_bake = request.form['temp_HMDS_bake']
    time_HMDS_bake= request.form['time_HMDS_bake']
    temp_softbake = request.form['temp_softbake']
    pr_thickness = request.form['pr_thickness']
    Wavelength = request.form['Wavelength']
    exp_time = request.form['exp_time']
    lense = request.form['lense']
    Thin_F4 = request.form['Thin_F4']
    Source_Power = request.form['Source_Power']
    Flux840s = request.form['Flux840s']
    input_Energy = request.form['input_Energy']
    Temp_implantation = request.form['Temp_implantation']
    Furance_Temp = request.form['Furance_Temp']
    RTA_Temp = request.form['RTA_Temp']
    flux_rate1 = request.form['flux_rate1']
    flux_rate2 = request.form['flux_rate2']
    flux_rate3 = request.form['flux_rate3']
    flux_rate4 = request.form['flux_rate4']
    target_bool = request.form['target_bool']
    type_dry = request.form['type_dry']
    type_wet = request.form['type_wet']
    Vapor_H2O = request.form['Vapor_H2O']
    Vapor_O2= request.form['Vapor_O2']
    
    data1 = [[Temp_OXid,ppm,Pressure,Oxid_time,N2_HMDS,pressure_HMDS,temp_HMDS,temp_HMDS_bake,time_HMDS_bake,temp_softbake,	pr_thickness,Wavelength,exp_time,lense,Thin_F4,Temp_Etching,Source_Power,Flux840s,input_Energy,Temp_implantation,Furance_Temp,RTA_Temp,flux_rate1,flux_rate2,flux_rate3,flux_rate4,target_bool,type_dry,type_wet,Vapor_H2O,Vapor_O2]]
    estimator = dbMgr.modeling_RF()
    df3 = pd.DataFrame(data=data1)
    predict = estimator
    
    return render_template('result.html', predict=predict) 

# finished code
if __name__ == '__main__':
    # app.debug = True
    # app.run()
    app.run(host='0.0.0.0', port=5000, debug=True)
