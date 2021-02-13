import plotly
import plotly.graph_objs as go
import lightgbm as lgb
import pandas as pd
import numpy as np
import json
import pickle
from sklearn.externals import joblib
import os
import sys

sys.path.append("..")

from AccessDB.AccessDB import *
from ElecFeeCalculator.ElecFeeCalculator import *
from InputDataGetter.InputDataGetter import *
from Predictor.Predictor import *
from GasFeeCalculator.GasFeeCalculator import *
# class Visualize:
    
#     # plot object getter
#     # type : 어떤 그래프를 그려야 되는지
#     # startDate : 시작 일자
#     # endDate : 종료 일자
#     def getPlot(self,type,startDate,endDate) :

#     # table object getter
#     def getTable(self,type,startDate,endDate) :
        
        
# class Table :
    
#     def createTableData(self,startDate,endDate) : 
    

# create plot object and return 
class Plot :
    
    # 1. 전력 사용량 패턴 분석 > 전력 사용량 분석 plot
    # startDate : 패턴 분석 시작 일자
    # endDate : 패턴 분석 종료 일자
    # contractElec : 계약 전력
    # payment : 요금제 유형
    # userId : 사용자 ID
    # period : 경제성 분석 주기(연, 월, 일)

    def createBarLinePlot(self,startDate,endDate,contractElec,payment,userId,period) : 
        
        connector = DBConnector()

        dataGetter = DataGetter(connector)

        # data type: dataFrame
        data = dataGetter.selectData(startDate,endDate)

        elecFeeCalculator = ElecFeeCalculator(data)

        finalData = elecFeeCalculator.calElecFee(contractElec,payment,period)
        
        print("createBarLinePlot execute")
        # print(finalData)

        graph = [
            go.Bar(x=finalData.index, y=finalData['consumption']),
            go.Layout(
                colorway=["#5E0DAC"],
                template='plotly_dark',
                paper_bgcolor='rgba(0, 0, 0, 0)',
                plot_bgcolor='rgba(0, 0, 0, 0)',
                #   margin={'autoexpand' : True},
                #   height=100,
                hovermode='x',
                #   autosize=True,
                title={'text': '전력 사용량 패턴 분석', 'font': {'color': 'white'}, 'x': 0.5},
                xaxis=dict(
                    rangeselector=dict(
                        buttons=list([
                            dict(count=1,
                                label="1m",
                                step="month",
                                stepmode="backward"),
                            dict(count=1,
                                label="1y",
                                step="year",
                                stepmode="backward"),
                            dict(step="all")
                        ]),
                        bgcolor='rgba(0,0,0,0)',
                        activecolor = 'rgba(0,0,0,1)'
                    ),
                    rangeslider=dict(
                    visible=True
                    ),
                    type="date"
                ),
                yaxis=dict(
                    title="전력 사용량 (kwh)",
                    tickformat = ".0f"
                )  
            ),
            go.Scatter(x=finalData.index,y=finalData['elecFee'],mode='lines+markers',marker=dict(
                    color='#2dce89',
                    size=7
            )),
            go.Layout(
                colorway=['#2dce89'],
                template='plotly_dark',
                paper_bgcolor='rgba(0, 0, 0, 0)',
                plot_bgcolor='rgba(0, 0, 0, 0)',
                #   margin={'autoexpand' : True},
                #   height=100,
                hovermode='x',
                #   autosize=True,
                title={'text': '전력 사용 요금 패턴 분석', 'font': {'color': 'white'}, 'x': 0.5},
                xaxis=dict(
                    rangeselector=dict(
                        buttons=list([
                            dict(count=1,
                                label="1m",
                                step="month",
                                stepmode="backward"),
                            dict(count=1,
                                label="1y",
                                step="year",
                                stepmode="backward"),
                            dict(step="all")
                        ]),
                        bgcolor='rgba(0,0,0,0)',
                        activecolor = 'rgba(0,0,0,1)'
                    ),
                    rangeslider=dict(
                    visible=True
                    ),
                    type="date"
                ),
                yaxis=dict(
                    title="전력 사용 요금 (원)",
                    tickformat = ".0f"
                ) 
            )
        ]

        graphJSON = json.dumps(graph, cls=plotly.utils.PlotlyJSONEncoder)
        # print("graphJSON : " + graphJSON)
        return graphJSON


    # 2. 전력 사용량 패턴 분석 > 예측 전력 사용량 비교 plot
    def createCompareBarPlot(self,startDate,endDate,contractElec,userId,payment,period,modelName) :
        
        modelDir = 'C:\\capstone\\backend\\PredictionModel\\' + modelName
        loadedModel = joblib.load(modelDir)

        connector = DBConnector()

        dataGetter = DataGetter(connector)

        # data type: dataFrame
        data = dataGetter.selectData(startDate,endDate)

        index = data.index

        data['month'] = index.month
        data['day'] = index.day
        data['hour'] = index.hour

        # Add a Day Ago Column
        aDayAgoConsumption = pd.DataFrame(data=None, index=index-dt.timedelta(days=1), columns=None, dtype=float, copy=False)
        aDayAgoConsumption['consumption'] = data['consumption']
        aDayAgoConsumption.index = aDayAgoConsumption.index+dt.timedelta(days=1)

        # Add two Days Ago Column
        twoDaysAgoConsumption = pd.DataFrame(data=None, index=index-dt.timedelta(days=2), columns=None, dtype=float, copy=False)
        twoDaysAgoConsumption['consumption'] = data['consumption']
        twoDaysAgoConsumption.index = twoDaysAgoConsumption.index+dt.timedelta(days=2)

        data['aDayAgoConsumption'] = aDayAgoConsumption
        data['twoDaysAgoConsumption'] = twoDaysAgoConsumption  

        data = data.fillna(data.mean())

        categorical_feature_name = ['weekday','isHoliday','month','hour']
        float_feature_name = ['temperature', 'humidity', 'windSpeed', 'aDayAgoConsumption','twoDaysAgoConsumption']

        for var in categorical_feature_name :
            data[var] = data[var].astype('category')

        for var in float_feature_name :
            data[var] = data[var].astype(float)

        feature_names = ['temperature','humidity','windSpeed','weekday','isHoliday',
                 'month','hour','aDayAgoConsumption','twoDaysAgoConsumption']
        
        # print(data)

        predictions = loadedModel.predict(data[feature_names])

        predictionData = pd.DataFrame()
        consumptionData = pd.DataFrame()

        predictionData['date'] = data.index
        consumptionData['date'] = data.index

        predictionData = predictionData.set_index('date')
        consumptionData = consumptionData.set_index('date')

        predictionData['consumption'] = predictions
        consumptionData['consumption'] = data['consumption'].astype(float)

        # print(predictionData)
        # print(consumptionData)

        # # 일간 통계
        # if(period==1) :
        #     predictionData = predictionData.groupby(pd.Grouper(freq='D')).sum()
            
        # # 월간 통계
        # elif(period==2) :
        #     predictionData = predictionData.groupby(pd.Grouper(freq='M')).sum()
            
        # # 연간통계
        # elif(period==3) :
        #     predictionData = predictionData.groupby(pd.Grouper(freq='M')).sum()
        #     predictionData = predictionData.groupby(pd.Grouper(freq='Y')).sum()

        predictionFeeCalculator = ElecFeeCalculator(predictionData)
        consumptionFeeCalculator = ElecFeeCalculator(consumptionData)

        newPrediction = predictionFeeCalculator.calElecFee(contractElec,payment,period)
        newConsumption = consumptionFeeCalculator.calElecFee(contractElec,payment,period)

        graph = [

            go.Bar(x=newConsumption.index, y=newConsumption['consumption'], name='실제 전력 사용량'),
            go.Bar(x=newPrediction.index, y=newPrediction['consumption'], name='예측 전력 사용량'),
            go.Layout(
                colorway=['#2dce89', '#5E0DAC'],
                template='plotly_dark',
                paper_bgcolor='rgba(0, 0, 0, 0)',
                plot_bgcolor='rgba(0, 0, 0, 0)',
                #   margin={'autoexpand' : True},
                #   height=100,
                hovermode='x',
                #   autosize=True,
                title={'text': '예측 전력 사용량 비교', 'font': {'color': 'white'}, 'x': 0.5},
                xaxis=dict(
                    rangeselector=dict(
                        buttons=list([
                            dict(count=1,
                                label="1m",
                                step="month",
                                stepmode="backward"),
                            dict(count=1,
                                label="1y",
                                step="year",
                                stepmode="backward"),
                            dict(step="all")
                        ]),
                        bgcolor='rgba(0,0,0,0)',
                        activecolor = 'rgba(0,0,0,1)'
                    ),
                    rangeslider=dict(
                    visible=True
                    ),
                    type="date"
                ),
                yaxis=dict(
                    title="전력 사용량 (kwh)",
                    tickformat = ".0f"
                ) 
            ),
            go.Scatter(x=newConsumption.index, y=newConsumption['elecFee'], name='실제 전력 사용 요금'),
            go.Scatter(x=newPrediction.index, y=newPrediction['elecFee'], name='예측 전력 사용 요금'),
            go.Layout(
                colorway=['#2dce89', '#5E0DAC'],
                template='plotly_dark',
                paper_bgcolor='rgba(0, 0, 0, 0)',
                plot_bgcolor='rgba(0, 0, 0, 0)',
                #   margin={'autoexpand' : True},
                #   height=100,
                hovermode='x',
                #   autosize=True,
                title={'text': '예측 전력 사용 요금 비교', 'font': {'color': 'white'}, 'x': 0.5},
                xaxis=dict(
                    rangeselector=dict(
                        buttons=list([
                            dict(count=1,
                                label="1m",
                                step="month",
                                stepmode="backward"),
                            dict(count=1,
                                label="1y",
                                step="year",
                                stepmode="backward"),
                            dict(step="all")
                        ]),
                        bgcolor='rgba(0,0,0,0)',
                        activecolor = 'rgba(0,0,0,1)'
                    ),
                    rangeslider=dict(
                    visible=True
                    ),
                    type="date"
                ),
                yaxis=dict(
                    title="전력 사용 요금 (원)",
                    tickformat = ".0f"
                ) 
            )
        ]

        graphJSON = json.dumps(graph, cls=plotly.utils.PlotlyJSONEncoder)
        # print("graphJSON : " + graphJSON)
        return graphJSON

    # 3. 전력 사용량 패턴 분석 > 입력변수 데이터 통계 plot
    def createLinePlot(self,startDate,endDate,userId,period) :
        
        connector = DBConnector()

        dataGetter = DataGetter(connector)

        # data type: dataFrame
        data = dataGetter.selectData(startDate,endDate)

        feature = ['consumption','temperature','humidity','windSpeed']

        newData = data[feature].astype(float)

        # 일간통계
        if period == 1 :
            newData = newData.groupby(pd.Grouper(freq='D')).mean()

        # 월간통계
        elif period == 2 :
            newData = newData.groupby(pd.Grouper(freq='M')).mean()

        elif period == 3 :
            newData = newData.groupby(pd.Grouper(freq='Y')).mean()

        graph = [
            go.Scatter(x=newData.index,y=newData['consumption'],name='평균 전력 사용량',mode='lines+markers',marker=dict(
                    color='#2dce89',
                    size=4
            )),

            go.Layout(
                colorway=['#2dce89'],
                template='plotly_dark',
                paper_bgcolor='rgba(0, 0, 0, 0)',
                plot_bgcolor='rgba(0, 0, 0, 0)',
                #   margin={'autoexpand' : True},
                #   height=100,
                hovermode='x',
                #   autosize=True,
                title={'text': '평균 전력 사용량', 'font': {'color': 'white'}, 'x': 0.5},
                xaxis=dict(
                    rangeselector=dict(
                        buttons=list([
                            dict(count=1,
                                label="1m",
                                step="month",
                                stepmode="backward"),
                            dict(count=1,
                                label="1y",
                                step="year",
                                stepmode="backward"),
                            dict(step="all")
                        ]),
                        bgcolor='rgba(0,0,0,0)',
                        activecolor = 'rgba(0,0,0,1)'
                    ),
                    rangeslider=dict(
                    visible=True
                    ),
                    type="date"
                ),
                yaxis=dict(
                    title="평균 전력 사용량 (kwh)",
                    tickformat = ".0f"
                ) 
            ),

            go.Scatter(x=newData.index,y=newData['temperature'],name='평균 기온', mode='lines+markers',marker=dict(
                    color='#5E0DAC',
                    size=4
            )),

            go.Layout(
                colorway=['#5E0DAC'],
                template='plotly_dark',
                paper_bgcolor='rgba(0, 0, 0, 0)',
                plot_bgcolor='rgba(0, 0, 0, 0)',
                #   margin={'autoexpand' : True},
                #   height=100,
                hovermode='x',
                #   autosize=True,
                title={'text': '평균 기온', 'font': {'color': 'white'}, 'x': 0.5},
                xaxis=dict(
                    rangeselector=dict(
                        buttons=list([
                            dict(count=1,
                                label="1m",
                                step="month",
                                stepmode="backward"),
                            dict(count=1,
                                label="1y",
                                step="year",
                                stepmode="backward"),
                            dict(step="all")
                        ]),
                        bgcolor='rgba(0,0,0,0)',
                        activecolor = 'rgba(0,0,0,1)'
                    ),
                    rangeslider=dict(
                    visible=True
                    ),
                    type="date"
                ),
                yaxis=dict(
                    title="평균 기온 (℃)",
                    tickformat = ".0f"
                ) 
            ),

            go.Scatter(x=newData.index,y=newData['humidity'],name='평균 습도',mode='lines+markers',marker=dict(
                    color='#2dce89',
                    size=4
            )),

            go.Layout(
                colorway=['#2dce89'],
                template='plotly_dark',
                paper_bgcolor='rgba(0, 0, 0, 0)',
                plot_bgcolor='rgba(0, 0, 0, 0)',
                #   margin={'autoexpand' : True},
                #   height=100,
                hovermode='x',
                #   autosize=True,
                title={'text': '평균 습도', 'font': {'color': 'white'}, 'x': 0.5},
                xaxis=dict(
                    rangeselector=dict(
                        buttons=list([
                            dict(count=1,
                                label="1m",
                                step="month",
                                stepmode="backward"),
                            dict(count=1,
                                label="1y",
                                step="year",
                                stepmode="backward"),
                            dict(step="all")
                        ]),
                        bgcolor='rgba(0,0,0,0)',
                        activecolor = 'rgba(0,0,0,1)'
                    ),
                    rangeslider=dict(
                    visible=True
                    ),
                    type="date"
                ),
                yaxis=dict(
                    title="평균 습도 %",
                    tickformat = ".0f"
                ) 
            ),

            go.Scatter(x=newData.index,y=newData['windSpeed'],name='평균 풍속',mode='lines+markers',marker=dict(
                    color='#5E0DAC',
                    size=4
            )),

            go.Layout(
                colorway=['#5E0DAC'],
                template='plotly_dark',
                paper_bgcolor='rgba(0, 0, 0, 0)',
                plot_bgcolor='rgba(0, 0, 0, 0)',
                #   margin={'autoexpand' : True},
                #   height=100,
                hovermode='x',
                #   autosize=True,
                title={'text': '평균 풍속', 'font': {'color': 'white'}, 'x': 0.5},
                xaxis=dict(
                    rangeselector=dict(
                        buttons=list([
                            dict(count=1,
                                label="1m",
                                step="month",
                                stepmode="backward"),
                            dict(count=1,
                                label="1y",
                                step="year",
                                stepmode="backward"),
                            dict(step="all")
                        ]),
                        bgcolor='rgba(0,0,0,0)',
                        activecolor = 'rgba(0,0,0,1)'
                    ),
                    rangeslider=dict(
                    visible=True
                    ),
                    type="date"
                ),
                yaxis=dict(
                    title="평균 풍속 (M/s)",
                    tickformat = ".0f"
                ) 
            )
        ]
        
        graphJSON = json.dumps(graph, cls=plotly.utils.PlotlyJSONEncoder)
        # print("graphJSON : " + graphJSON)
        return graphJSON

    # 4. CCHP 스케줄링 > 전력 사용량 예측 Plot
    def createPredictionPlot(self,predictDate,payment) : 

        modelDir = 'C:\\capstone\\backend\\PredictionModel\\sejong_power_consumption_model2.pkl'

        loadedModel = joblib.load(modelDir)

        inputDataGetter = InputDataGetter

        inputData = inputDataGetter.getInputData()

        predictor = Predictor(inputData)

        predictData = predictor.executePrediction(loadedModel)

        predictData = predictData.loc[predictDate]

        # 전기요금 계산 필드 추가
        elecFeeCalculator = ElecFeeCalculator(predictData)

        # period 0 : 시간 당 전기요금 계산
        # contractElec : 시간 당 전기요금이기 때문에 입력 필요 x->0으로 입력
        finalData = elecFeeCalculator.calElecFee(0,payment,0)

        # print(finalData)
        graph = [

            go.Bar(x=finalData.index,y=finalData['consumption'],name='예측 전력 사용량'),

            go.Layout(
                colorway=['#5E0DAC'],
                template='plotly_dark',
                paper_bgcolor='rgba(0, 0, 0, 0)',
                plot_bgcolor='rgba(0, 0, 0, 0)',
                #   margin={'autoexpand' : True},
                height=600,
                hovermode='x',
                #   autosize=True,
                title={'text': predictDate + ' 예측 전력 사용량', 'font': {'color': 'white'}, 'x': 0.5},
                xaxis=dict(
                    rangeselector=dict(
                        buttons=list([
                            dict(count=1,
                                label="1m",
                                step="month",
                                stepmode="backward"),
                            dict(count=1,
                                label="1y",
                                step="year",
                                stepmode="backward"),
                            dict(step="all")
                        ]),
                        bgcolor='rgba(0,0,0,0)',
                        activecolor = 'rgba(0,0,0,1)'
                    ),
                    rangeslider=dict(
                    visible=True
                    ),
                    type="date"
                ),
                yaxis=dict(
                    title="예측 전력 사용량 (kw)",
                    tickformat = ".0f"
                ) 
            ),
            go.Scatter(x=finalData.index,y=finalData['elecFee'],mode='lines+markers',marker=dict(
                    color='#2dce89',
                    size=7
            )),
            go.Layout(
                colorway=['#2dce89'],
                template='plotly_dark',
                paper_bgcolor='rgba(0, 0, 0, 0)',
                plot_bgcolor='rgba(0, 0, 0, 0)',
                #   margin={'autoexpand' : True},
                #   height=100,
                hovermode='x',
                #   autosize=True,
                title={'text': predictDate + ' 예측 전력 사용 요금', 'font': {'color': 'white'}, 'x': 0.5},
                xaxis=dict(
                    rangeselector=dict(
                        buttons=list([
                            dict(count=1,
                                label="1m",
                                step="month",
                                stepmode="backward"),
                            dict(count=1,
                                label="1y",
                                step="year",
                                stepmode="backward"),
                            dict(step="all")
                        ]),
                        bgcolor='rgba(0,0,0,0)',
                        activecolor = 'rgba(0,0,0,1)'
                    ),
                    rangeslider=dict(
                    visible=True
                    ),
                    type="date"
                ),
                yaxis=dict(
                    title="전력 사용 요금 (원)",
                    tickformat = ".0f"
                ) 
            )
        ]
        
        graphJSON = json.dumps(graph, cls=plotly.utils.PlotlyJSONEncoder)
        # print("graphJSON : " + graphJSON)
        return graphJSON

    # 5. CCHP 스케줄링 > CCHP 스케줄링 Plot
    def createStackBarPlot(self,predictDate,payment) : 

        modelDir = 'C:\\capstone\\backend\\PredictionModel\\sejong_power_consumption_model2.pkl'

        loadedModel = joblib.load(modelDir)

        inputDataGetter = InputDataGetter

        inputData = inputDataGetter.getInputData()

        predictor = Predictor(inputData)

        predictData = predictor.executePrediction(loadedModel)

        predictData = predictData.loc[predictDate]

        # 전기요금 계산 필드 추가
        elecFeeCalculator = ElecFeeCalculator(predictData)

        # period 0 : 시간 당 전기요금 계산
        # contractElec : 시간 당 전기요금이기 때문에 입력 필요 x->0으로 입력
        finalData = elecFeeCalculator.calElecFee(0,payment,0)

        finalData = calculateGasFee(finalData)

        # print(finalData)
        graph = [

            go.Bar(x=finalData.index,y=finalData['cElec'],name='CCHP 발전 전력 사용량'),
            go.Bar(x=finalData.index,y=finalData['kElec'],name='한전 전력 사용량'),

            go.Layout(
                colorway=['#5E0DAC','#2dce89'],
                template='plotly_dark',
                paper_bgcolor='rgba(0, 0, 0, 0)',
                plot_bgcolor='rgba(0, 0, 0, 0)',
                #   margin={'autoexpand' : True},
                #   height=100,
                hovermode='x',
                #   autosize=True,
                title={'text': 'CCHP 스케쥴링', 'font': {'color': 'white'}, 'x': 0.5},
                xaxis=dict(
                    rangeselector=dict(
                        buttons=list([
                            dict(count=1,
                                label="1m",
                                step="month",
                                stepmode="backward"),
                            dict(count=1,
                                label="1y",
                                step="year",
                                stepmode="backward"),
                            dict(step="all")
                        ]),
                        bgcolor='rgba(0,0,0,0)',
                        activecolor = 'rgba(0,0,0,1)'
                    ),
                    rangeslider=dict(
                    visible=True
                    ),
                    type="date"
                ),
                yaxis=dict(
                    title="예측 전력 사용량 (kwh)",
                    tickformat = ".0f"
                ),
                barmode='stack'
            ),
            go.Scatter(x=finalData.index, y=finalData['elecFee'], name='한국 전력 사용 요금',mode='lines+markers',marker=dict(
                    color='#2dce89',
                    size=7)
            ),
            go.Scatter(x=finalData.index, y=finalData['gasFee'], name='CCHP 발전 사용 요금',mode='lines+markers',marker=dict(
                    color='#5E0DAC',
                    size=7)),
            go.Layout(
                colorway=['#2dce89', '#5E0DAC'],
                template='plotly_dark',
                paper_bgcolor='rgba(0, 0, 0, 0)',
                plot_bgcolor='rgba(0, 0, 0, 0)',
                #   margin={'autoexpand' : True},
                #   height=100,
                hovermode='x',
                #   autosize=True,
                title={'text': '전력 사용 요금 비교', 'font': {'color': 'white'}, 'x': 0.5},
                xaxis=dict(
                    rangeselector=dict(
                        buttons=list([
                            dict(count=1,
                                label="1m",
                                step="month",
                                stepmode="backward"),
                            dict(count=1,
                                label="1y",
                                step="year",
                                stepmode="backward"),
                            dict(step="all")
                        ]),
                        bgcolor='rgba(0,0,0,0)',
                        activecolor = 'rgba(0,0,0,1)'
                    ),
                    rangeslider=dict(
                    visible=True
                    ),
                    type="date"
                ),
                yaxis=dict(
                    title="전력 사용 요금 (원)",
                    tickformat = ".0f"
                ) 
            )
        ]
        
        graphJSON = json.dumps(graph, cls=plotly.utils.PlotlyJSONEncoder)
        # print("graphJSON : " + graphJSON)
        return graphJSON

    
    # # 6. CCHP 스케줄링 > CCHP 운영 시간표
    # def createPiePlot(self,startDate,endDate) : 
    
    # 7. CCHP 스케줄링 > 입력 데이터 통계
    def createSchLinePlot(self,predictDate) :
        
        modelDir = 'C:\\capstone\\backend\\PredictionModel\\sejong_power_consumption_model2.pkl'

        loadedModel = joblib.load(modelDir)

        inputDataGetter = InputDataGetter

        inputData = inputDataGetter.getInputData().loc[predictDate]

        predictor = Predictor(inputData)

        predictData = predictor.executePrediction(loadedModel)

        # predictData = predictData.loc[predictDate]

        newData = inputData
        newData['consumption'] = predictData['consumption']

        # print(predictData)
        # print(inputData)


        feature = ['consumption','temperature','humidity','windSpeed']

        newData = newData[feature].astype(float)

        graph = [
            go.Scatter(x=newData.index,y=newData['consumption'],name='예측 전력 사용량',mode='lines+markers',marker=dict(
                    color='#2dce89',
                    size=4
            )),

            go.Layout(
                colorway=['#2dce89'],
                template='plotly_dark',
                paper_bgcolor='rgba(0, 0, 0, 0)',
                plot_bgcolor='rgba(0, 0, 0, 0)',
                #   margin={'autoexpand' : True},
                #   height=100,
                hovermode='x',
                #   autosize=True,
                title={'text': '예측 전력 사용량', 'font': {'color': 'white'}, 'x': 0.5},
                xaxis=dict(
                    rangeselector=dict(
                        buttons=list([
                            dict(count=1,
                                label="1m",
                                step="month",
                                stepmode="backward"),
                            dict(count=1,
                                label="1y",
                                step="year",
                                stepmode="backward"),
                            dict(step="all")
                        ]),
                        bgcolor='rgba(0,0,0,0)',
                        activecolor = 'rgba(0,0,0,1)'
                    ),
                    rangeslider=dict(
                    visible=True
                    ),
                    type="date"
                ),
                yaxis=dict(
                    title="예측 전력 사용량 (kwh)",
                    tickformat = ".0f"
                ) 
            ),

            go.Scatter(x=newData.index,y=newData['temperature'],name='기온', mode='lines+markers',marker=dict(
                    color='#5E0DAC',
                    size=4
            )),

            go.Layout(
                colorway=['#5E0DAC'],
                template='plotly_dark',
                paper_bgcolor='rgba(0, 0, 0, 0)',
                plot_bgcolor='rgba(0, 0, 0, 0)',
                #   margin={'autoexpand' : True},
                #   height=100,
                hovermode='x',
                #   autosize=True,
                title={'text': '기온', 'font': {'color': 'white'}, 'x': 0.5},
                xaxis=dict(
                    rangeselector=dict(
                        buttons=list([
                            dict(count=1,
                                label="1m",
                                step="month",
                                stepmode="backward"),
                            dict(count=1,
                                label="1y",
                                step="year",
                                stepmode="backward"),
                            dict(step="all")
                        ]),
                        bgcolor='rgba(0,0,0,0)',
                        activecolor = 'rgba(0,0,0,1)'
                    ),
                    rangeslider=dict(
                    visible=True
                    ),
                    type="date"
                ),
                yaxis=dict(
                    title="기온 (℃)",
                    tickformat = ".0f"
                ) 
            ),

            go.Scatter(x=newData.index,y=newData['humidity'],name='습도',mode='lines+markers',marker=dict(
                    color='#2dce89',
                    size=4
            )),

            go.Layout(
                colorway=['#2dce89'],
                template='plotly_dark',
                paper_bgcolor='rgba(0, 0, 0, 0)',
                plot_bgcolor='rgba(0, 0, 0, 0)',
                #   margin={'autoexpand' : True},
                #   height=100,
                hovermode='x',
                #   autosize=True,
                title={'text': '습도', 'font': {'color': 'white'}, 'x': 0.5},
                xaxis=dict(
                    rangeselector=dict(
                        buttons=list([
                            dict(count=1,
                                label="1m",
                                step="month",
                                stepmode="backward"),
                            dict(count=1,
                                label="1y",
                                step="year",
                                stepmode="backward"),
                            dict(step="all")
                        ]),
                        bgcolor='rgba(0,0,0,0)',
                        activecolor = 'rgba(0,0,0,1)'
                    ),
                    rangeslider=dict(
                    visible=True
                    ),
                    type="date"
                ),
                yaxis=dict(
                    title="습도 %",
                    tickformat = ".0f"
                ) 
            ),

            go.Scatter(x=newData.index,y=newData['windSpeed'],name='풍속',mode='lines+markers',marker=dict(
                    color='#5E0DAC',
                    size=4
            )),

            go.Layout(
                colorway=['#5E0DAC'],
                template='plotly_dark',
                paper_bgcolor='rgba(0, 0, 0, 0)',
                plot_bgcolor='rgba(0, 0, 0, 0)',
                #   margin={'autoexpand' : True},
                #   height=100,
                hovermode='x',
                #   autosize=True,
                title={'text': '풍속', 'font': {'color': 'white'}, 'x': 0.5},
                xaxis=dict(
                    rangeselector=dict(
                        buttons=list([
                            dict(count=1,
                                label="1m",
                                step="month",
                                stepmode="backward"),
                            dict(count=1,
                                label="1y",
                                step="year",
                                stepmode="backward"),
                            dict(step="all")
                        ]),
                        bgcolor='rgba(0,0,0,0)',
                        activecolor = 'rgba(0,0,0,1)'
                    ),
                    rangeslider=dict(
                    visible=True
                    ),
                    type="date"
                ),
                yaxis=dict(
                    title="풍속 (M/s)",
                    tickformat = ".0f"
                ) 
            )
        ]
        
        graphJSON = json.dumps(graph, cls=plotly.utils.PlotlyJSONEncoder)
        # print("graphJSON : " + graphJSON)
        return graphJSON

    # # 7. 경제성 분석 > 경제성 분석 : BarPlot, PieChart
    def createBarPiePlot(self,startDate,endDate,payment,period,contractElec) :

        connector = DBConnector()

        dataGetter = DataGetter(connector)

        # data type: dataFrame
        data = dataGetter.selectData(startDate,endDate)

        elecFeeCalculator = ElecFeeCalculator(data)

        # 시간 단위 한전요금 계산
        afterCalElecFeeData = elecFeeCalculator.calElecFee(0,payment,0)
        
        finalData = calculateGasFee(afterCalElecFeeData)

        # CCHP를 사용하는 시간대의 elecFee를 0으로 하는 컬럼 추가
        def addZElecFee(df):
            
            if df['kElec'] == 0 : 

                return 0
                
            else :
                return df['elecFee']
        finalData['zElecFee'] = finalData.apply(addZElecFee,axis=1)

        # 한전만을 사용하는 시간대의 gasFee를 0으로 하는 컬럼 추가
        def addZGasFee(df):
            
            if df['cElec'] == 0 : 

                return 0
                
            else :
                return df['gasFee']

        finalData['zGasFee'] = finalData.apply(addZGasFee,axis=1)

        # print("createBarLinePlot execute")
        # print(finalData)

        # 계약 전력 요금을 계산
        contractElecFee = float(getContractElecFee(contractElec,payment))
        # print(contractElecFee)
        # 일간 통계
        if(period==1) :
            finalData = finalData.groupby(pd.Grouper(freq='D')).sum()
            
        # 월간 통계
        elif(period==2) :
            finalData = finalData.groupby(pd.Grouper(freq='M')).sum()
            finalData['elecFee'] = finalData['elecFee'] + contractElecFee
            finalData['zElecFee'] = finalData['zElecFee'] + contractElecFee
        # 연간통계
        elif(period==3) :
            finalData = finalData.groupby(pd.Grouper(freq='M')).sum()
            finalData['elecFee'] = finalData['elecFee'] + contractElecFee
            finalData['zElecFee'] = finalData['zElecFee'] + contractElecFee
            finalData = finalData.groupby(pd.Grouper(freq='Y')).sum()

        # print(finalData)

        pieLabel = ['한전 전력 사용량 (kwh)', '열병합 발전 전력 사용량 (kwh)']
        pieValue =[finalData['kElec'].sum(), finalData['cElec'].sum()]

        pieFeeLabel = ['한전 전력 사용 요금(원)', '열병합 발전 요금(원)']
        pieFeeValue = [finalData['zElecFee'].sum(), finalData['zGasFee'].sum()]

        benefit = finalData['elecFee'].sum() - finalData['zElecFee'].sum() - finalData['zGasFee'].sum() + finalData['warmFee'].sum()
        graph = [

            go.Bar(x=finalData.index, y=finalData['elecFee'], name='한전 전력만 이용시 요금'),
            go.Bar(x=finalData.index, y=finalData['zElecFee']+finalData['zGasFee'], name='한전 전력 + CCHP발전 시 요금'),
            go.Bar(x=finalData.index, y=finalData['warmFee'], name='가스 냉난방 이득'),
            go.Layout(
                colorway=['#2dce89', '#5E0DAC','#f5365c'],
                template='plotly_dark',
                paper_bgcolor='rgba(0, 0, 0, 0)',
                plot_bgcolor='rgba(0, 0, 0, 0)',
                #   margin={'autoexpand' : True},
                #   height=100,
                hovermode='x',
                #   autosize=True,
                title={'text': startDate + " ~ " + endDate + ' 경제성 분석', 'font': {'color': 'white'}, 'x': 0.5},
                xaxis=dict(
                    rangeselector=dict(
                        buttons=list([
                            dict(count=1,
                                label="1m",
                                step="month",
                                stepmode="backward"),
                            dict(count=1,
                                label="1y",
                                step="year",
                                stepmode="backward"),
                            dict(step="all")
                        ]),
                        bgcolor='rgba(0,0,0,0)',
                        activecolor = 'rgba(0,0,0,1)'
                    ),
                    rangeslider=dict(
                    visible=True
                    ),
                    type="date"
                ),
                yaxis=dict(
                    title="전력 사용 요금 (원)",
                    tickformat = ".0f"
                ) 
            ),

            go.Pie(labels = pieLabel, values=pieValue),
            go.Layout(
                colorway=['#2dce89', '#5E0DAC','#f5365c'],
                template='plotly_dark',
                paper_bgcolor='rgba(0, 0, 0, 0)',
                plot_bgcolor='rgba(0, 0, 0, 0)',
                #   margin={'autoexpand' : True},
                #   height=100,
                hovermode='x',
                #   autosize=True,
                title={'text': startDate + " ~ " + endDate + ' 전력 사용량 분석', 'font': {'color': 'white'}, 'x': 0.5},
                xaxis=dict(
                    rangeselector=dict(
                        buttons=list([
                            dict(count=1,
                                label="1m",
                                step="month",
                                stepmode="backward"),
                            dict(count=1,
                                label="1y",
                                step="year",
                                stepmode="backward"),
                            dict(step="all")
                        ]),
                        bgcolor='rgba(0,0,0,0)',
                        activecolor = 'rgba(0,0,0,1)'
                    ),
                    rangeslider=dict(
                    visible=True
                    ),
                    type="date"
                ),
                yaxis=dict(
                    tickformat = ".0f"
                ) 
            ),

            go.Pie(labels = pieFeeLabel, values=pieFeeValue),
            go.Layout(
                colorway=['#2dce89', '#5E0DAC','#f5365c'],
                template='plotly_dark',
                paper_bgcolor='rgba(0, 0, 0, 0)',
                plot_bgcolor='rgba(0, 0, 0, 0)',
                #   margin={'autoexpand' : True},
                #   height=100,
                hovermode='x',
                #   autosize=True,
                title={'text': startDate + " ~ " + endDate + ' 전력 사용 요금 분석', 'font': {'color': 'white'}, 'x': 0.5},
                xaxis=dict(
                    rangeselector=dict(
                        buttons=list([
                            dict(count=1,
                                label="1m",
                                step="month",
                                stepmode="backward"),
                            dict(count=1,
                                label="1y",
                                step="year",
                                stepmode="backward"),
                            dict(step="all")
                        ]),
                        bgcolor='rgba(0,0,0,0)',
                        activecolor = 'rgba(0,0,0,1)'
                    ),
                    rangeslider=dict(
                    visible=True
                    ),
                    type="date"
                ),
                yaxis=dict(
                    tickformat = ".0f"
                ) 
            ),

            dict(
                benefit = benefit
            )

        ]

        graphJSON = json.dumps(graph, cls=plotly.utils.PlotlyJSONEncoder)
        # print("graphJSON : " + graphJSON)
        return graphJSON
