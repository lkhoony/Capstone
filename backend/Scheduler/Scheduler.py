import os
import sys
from apscheduler.schedulers.background import BackgroundScheduler
import requests
from bs4 import BeautifulSoup
from dateutil.relativedelta import relativedelta
import datetime
import json
import pandas as pd
import json
from sklearn.externals import joblib
from Predictor.Predictor import *
from AccessDB.AccessDB import *

sys.path.append("..")

from DataVO.DataVO import *

sched = BackgroundScheduler()

def startScheduler() :

    def addData() :

        today = datetime.datetime.now()-datetime.timedelta(hours=1)

        # weekday
        weekday = today.weekday()

        # isHoliday : weekday가 주말이면 1
        isHoliday=0

        if weekday==5 or weekday==6 :
            isHoliday = 1
            
            
        # 초단기 실황 : api 제공시간 - 정각 + 40분
        base_date = str(today.year) + str(today.month).zfill(2) + str(today.day).zfill(2)
        # base_time = str(today.hour).zfill(2) + '00'
        base_time = str(today.hour).zfill(2) + '00'

        # date
        date = datetime.datetime.strptime(base_date+base_time,'%Y%m%d%H%M')

        # get weather data
        serviceKey = "52s6pZxbOiLmg7H76y%2BN1Rs2tXn4ru798V6iWXFOFWzwKDzqkzuVuxdhol%2FuBCEYc9IOUIKfeJBn2XcEzKXZbg%3D%3D"
        url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService/getUltraSrtNcst'

        queryParams = '?ServiceKey=' + serviceKey + '&pageNo=1&numOfRows=50000&dataType=JSON&base_date=' + base_date + '&base_time='+base_time + '&nx=62&ny=126'

        response = requests.get(url+queryParams)

        html = response.text

        data = json.loads(html)

        tempData = data['response']['body']['items']['item']

        for i in range(0,len(tempData)) :
            
            item = tempData[i]
            
            category = item['category']

            # temperature
            if category == 'T1H' :
                temperature = item['obsrValue']
                
            # humidity
            elif category =='REH' :
                humidity = item['obsrValue']
                
            # windSpeed
            elif category =='WSD' :
                windSpeed = item['obsrValue']

        # set isHoliday
        serviceKey = "52s6pZxbOiLmg7H76y%2BN1Rs2tXn4ru798V6iWXFOFWzwKDzqkzuVuxdhol%2FuBCEYc9IOUIKfeJBn2XcEzKXZbg%3D%3D"
        url = 'http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/getRestDeInfo'

        holidayList = []

        queryParams = '?ServiceKey=' + serviceKey + '&pageNo=1&numOfRows=100&solYear='+str(today.year)+'&solMonth='+str(today.month).zfill(2)

        response = requests.get(url+queryParams)
        html = response.text
        soup = BeautifulSoup(html,'html.parser')
        holiday = soup.find_all('locdate')

        for i in range(0,len(holiday)) :

            holidayStr = holiday[i].text
            year = holidayStr[0:4]
            month = holidayStr[4:6]
            day = holidayStr[6:8]

            holidayList.append(year+'-'+month+'-'+day)

        for i in range(0,len(holidayList)) :
            dateStr = str(today.year) + '-' + str(today.month).zfill(0) + '-' + str(today.day).zfill(0)
            
            if dateStr == holidayList[i] :
                isHoliday = 1

        # change type
        temperature = float(temperature)
        humidity = float(humidity)
        windSpeed = float(windSpeed)

        # prediction

        modelDir = 'C:\\capstone\\backend\\PredictionModel\\sejong_power_consumption_model2.pkl'
        loadedModel = joblib.load(modelDir)

        month = date.month
        hour = date.hour

        dataDict = {"temperature": [temperature], "humidity": [humidity], "windSpeed": [windSpeed], \
                    "weekday" : [weekday], "isHoliday" : [isHoliday], "date" : [date], "month" : [month], \
                    "hour" : [hour]}

        dataDf = pd.DataFrame(dataDict).set_index('date')

        predictor = Predictor(dataDf)

        predictData = predictor.executePrediction(loadedModel)

        dataDf['consumption'] = predictData['consumption']
        
        consumption = dataDf.loc[date]['consumption']
        
        dataVO = DataVO(date,consumption,temperature,humidity,windSpeed,weekday,isHoliday)

        connector = DBConnector()

        dataGetter = DataGetter(connector)

        # data type: dataFrame
        dataGetter.insertData(dataVO)
        # print(consumption)
        # print(temperature)
        # print(humidity)
        # print(windSpeed)
        # print(weekday)
        # print(isHoliday)
        # print(date)
        # print(month)
        # print(hour)


    sched.start()

    sched.add_job(addData, 'cron', minute="50", id="addData")
