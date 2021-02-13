from flask import Flask, jsonify, redirect, url_for, render_template, request, session
from flask_cors import CORS
from AccessDB.AccessDB import *
from Plot.Plot import *
from ElecFeeCalculator.ElecFeeCalculator import *
from Scheduler.Scheduler import *
import plotly
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import json
import os,string

# instantiate the app
app = Flask(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# login route
# @app.route('/login', methods=['GET','POST'])
# def login():
#     # if request.method == 'POST':

#         # session에 id,pw를 저장
#         # session['id'] = request.form['id']
#         # session['password'] = request.form['password']

#     # 요청 url로 다시 redirect
#     return redirect(url_for("http://localhost:8080"))

# # logout route
# @app.route('/logout', methods=['GET','POST'])
# def logout():
#     if request.method == 'POST':
#         session.pop('id',None)
#         # return redirect(url_for(request.url))
#     return redirect(url_for("http://localhost:8080/#/electric"))

# # isLogOn route
# # login 상태인지 확인
# @app.route('/isLogOn', methods=['GET','POST'])
# def isLogOn():

#     if 'id' in session :
#         id = session['id']
#         # 세션에 있을 경우
#         # return True
#     else :
#         print('test')
#         # return False


# start scheduler
startScheduler()

# 1. electric/pattern 요청에 대한 그래프를 반환
@app.route('/electric/pattern', methods=['GET','POST'])
def createBarLinePlot():
    
    if(request.method== 'POST') :
        data = request.get_json()
        startDate = data['startDate']
        endDate = data['endDate']
        payment = int(data['payment'])
        period = int(data['period'])
        contractElec = float(data['contractElec'])

    plotCreator = Plot()
    graphJSON = plotCreator.createBarLinePlot(startDate,endDate,contractElec,payment,'abc',period)

    # print(request.url) #localhost:5000/electric/pattern
    # print(a)
    return graphJSON
 
# 2. electric/compare요청에 대한 그래프를 반환
@app.route('/electric/compare', methods=['GET','POST'])
def createCompareBarPlot():
    
    if(request.method== 'POST') :
        data = request.get_json()
        # print(data)
        startDate = data['startDate']
        endDate = data['endDate']
        payment = int(data['payment'])
        period = int(data['period'])
        contractElec = float(data['contractElec'])

    plotCreator = Plot()

    modelName = 'sejong_power_consumption_model.pkl'  
    graphJSON = plotCreator.createCompareBarPlot(startDate,endDate,contractElec,'abc',payment,period,modelName)

    print(request.url) #localhost:5000/electric/pattern
    return graphJSON

# 3. electric/input요청에 대한 그래프를 반환
@app.route('/electric/input', methods=['GET','POST'])
def createLinePlot():

    if(request.method== 'POST') :
        data = request.get_json()
        startDate = data['startDate']
        endDate = data['endDate']
        period = int(data['period'])

    plotCreator = Plot()

    graphJSON = plotCreator.createLinePlot(startDate,endDate,'abc',period)

    print(request.url) #localhost:5000/electric/pattern
    return graphJSON

# 4. /scheduling/prediction요청에 대한 그래프를 반환
@app.route('/scheduling/prediction', methods=['GET','POST'])
def createPredictionPlot():

    if(request.method== 'POST') :
        data = request.get_json()
        predictDate = data['predictDate']
        payment = data['payment']

    plotCreator = Plot()

    graphJSON = plotCreator.createPredictionPlot(predictDate,payment)

    print(request.url) #localhost:5000/electric/pattern
    return graphJSON

# 5. /scheduling/cchpsch요청에 대한 그래프를 반환
@app.route('/scheduling/cchpsch', methods=['GET','POST'])
def createStackBarPlot():

    if(request.method== 'POST') :
        data = request.get_json()
        predictDate = data['predictDate']
        payment = data['payment']

    plotCreator = Plot()

    graphJSON = plotCreator.createStackBarPlot(predictDate,payment)

    # print(request.url) #localhost:5000/electric/pattern
    # print(a)
    return graphJSON

# 6. electric/input요청에 대한 그래프를 반환
@app.route('/scheduling/input', methods=['GET','POST'])
def createSchLinePlot():

    print('schLinePlot')
    if(request.method== 'POST') :
        data = request.get_json()
        predictDate = data['predictDate']

    plotCreator = Plot()

    graphJSON = plotCreator.createSchLinePlot(predictDate)

    print(request.url) #localhost:5000/electric/pattern
    return graphJSON


# 7. economics/analysis요청에 대한 그래프를 반환
@app.route('/economics/analysis', methods=['GET','POST'])
def createBarPiePlot():

    if(request.method== 'POST') :

        data = request.get_json()
        startDate = data['startDate']
        endDate = data['endDate']
        payment = data['payment']
        period = data['period']
        contractElec = float(data['contractElec'])

    plotCreator = Plot()

    graphJSON = plotCreator.createBarPiePlot(startDate,endDate,payment,period,contractElec)

    print(request.url) #localhost:5000/electric/pattern
    return graphJSON   


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=os.getenv('FLASK_RUN_PORT'),debug=os.getenv('FLASK_DEBUG'))
