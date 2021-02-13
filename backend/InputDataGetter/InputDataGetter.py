# get forecasting data

import requests
from bs4 import BeautifulSoup
from dateutil.relativedelta import relativedelta
import datetime
import json
import pandas as pd

class InputDataGetter :

    def getInputData() :


        today = datetime.datetime.now()

        if today.hour < 20 :

            theDay = today-datetime.timedelta(days=1)

        else :

            if today.hour == 20 and today.minute < 10 :
                theDay = today-datetime.timedelta(days=1)

            else :
                theDay = today

        # print(theDay)
        base_time = '2000'
        base_date = str(theDay.year) + str(theDay.month).zfill(2) + str(theDay.day).zfill(2)

        serviceKey = "52s6pZxbOiLmg7H76y%2BN1Rs2tXn4ru798V6iWXFOFWzwKDzqkzuVuxdhol%2FuBCEYc9IOUIKfeJBn2XcEzKXZbg%3D%3D"
        url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst'

        queryParams = '?ServiceKey=' + serviceKey + '&pageNo=1&numOfRows=50000&dataType=JSON&base_date=' + base_date + '&base_time='+base_time + '&nx=62&ny=126'

        response = requests.get(url+queryParams)

        html = response.text
        # print(base_date)
        # print(html)
        data = json.loads(html)
        res = pd.DataFrame(data['response']['body']['items']['item'])

        res['date'] = res['fcstDate'] + res['fcstTime']
        res['date'] = pd.to_datetime(res['date'])
        res = res.set_index('date')

        # REH : 습도
        # T3H : 기온
        # WSD : 풍속

        # 1. 습도
        humidity = res[(res['category']=='REH')][['fcstValue']].astype(float)
        humidity = humidity.resample('1H').first()
        humidity = humidity.interpolate()

        # 2. 기온
        temperature = res[(res['category']=='T3H')][['fcstValue']].astype(float)
        temperature = temperature.resample('1H').first()
        temperature = temperature.interpolate()

        # 3. 풍속
        windSpeed = res[(res['category']=='WSD')][['fcstValue']].astype(float)
        windSpeed = windSpeed.resample('1H').first()
        windSpeed = windSpeed.interpolate()

        # crate dataframe

        newData = pd.DataFrame()
        newData['date'] = humidity.index
        newData = newData.set_index('date')
        newData['temperature'] = temperature['fcstValue']
        newData['humidity'] = humidity['fcstValue']
        newData['windSpeed'] = windSpeed['fcstValue']
        newData['weekday'] = newData.index.weekday
        

        # get holiday and join isHoliday in consumpData

        serviceKey = "52s6pZxbOiLmg7H76y%2BN1Rs2tXn4ru798V6iWXFOFWzwKDzqkzuVuxdhol%2FuBCEYc9IOUIKfeJBn2XcEzKXZbg%3D%3D"
        url = 'http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/getRestDeInfo'

        startDate = newData.index[0]
        endDate = newData.index[len(newData)-1]

        start = datetime.date(startDate.year, startDate.month,1)
        end = datetime.date(endDate.year, endDate.month,1)

        # get holiday list
        # 0:월, 1:화, 2:수, 3:목, 4:금, 5:토, 6:일

        holidayList = []
        while(start<=end) :

            queryParams = '?ServiceKey=' + serviceKey + '&pageNo=1&numOfRows=100&solYear='+str(start.year)+'&solMonth='+str(start.month).zfill(2)
            
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
                
            start = start + relativedelta(months=1)

        newData['isHoliday'] = 0
        newData.loc[newData['weekday']==5,'isHoliday'] = 1
        newData.loc[newData['weekday']==6,'isHoliday'] = 1

        for i in range(0,len(holidayList)) :
            newData[(newData.index)==i] = int(1)
            
        newData = newData.astype({'isHoliday' : 'int'})

        # print(newData)

        return newData