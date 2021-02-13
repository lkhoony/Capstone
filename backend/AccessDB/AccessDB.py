import scipy.io
import csv
import pymysql
import pandas as pd
from sqlalchemy import create_engine
import datetime
# db 연결을 얻어오는 클래스
class DBConnector:
    
#   private member variable

    __host = '127.0.0.1'
    __user = 'root'
    __password = '1234'
    __db = 'capstone'
    __charset = 'utf8'
        
    def __init__(self) :
        
        print('init DBConnector')
        
    def getDBConnection(self) :
        
        cursorclass = pymysql.cursors.DictCursor
        
        conn = pymysql.connect(host=self.__host, user=self.__user, password=self.__password,

                       db=self.__db, charset=self.__charset,cursorclass=cursorclass)
        
        return conn

    def getDBEngine(self) :
        
        engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user=self.__user,
                               pw=self.__password,
                               db=self.__db))
        
        return engine
    

# table로 부터 데이터를 얻어오는 클래스
class DataGetter:
    
#   DBConnector를 인수로 전달

    def __init__(self,connector) :
        
        self.connector = connector

    def selectData(self,start,end) :
        
        conn = self.connector.getDBConnection()
          
        curs = conn.cursor()
        
        query = "SELECT * FROM test_data WHERE date >= '" +  start +  "' AND date < '" + end + "'"
        
        curs.execute(query)
        
        result = curs.fetchall()
        
        data = pd.DataFrame(result).set_index(['date'])

        return data

    def insertData(self,dataVO) : 

        try :
            conn = self.connector.getDBConnection()
          
            curs = conn.cursor()

            date = dataVO.getDate()
            consumption = float(dataVO.getConsumption())
            temperature = float(dataVO.getTemperature())
            humidity = float(dataVO.getHumidity())
            windSpeed = float(dataVO.getWindSpeed())
            weekday = dataVO.getWeekday()
            isHoliday = dataVO.getIsHoliday()

            print(consumption)
            print(temperature)
            print(humidity)
            print(windSpeed)
            print(weekday)
            print(isHoliday)
            print(date.strftime('%Y-%m-%d %H:%M:%S'))
 
            query = """INSERT INTO test_data(date,consumption,temperature,humidity,windSpeed,weekday,isHoliday)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            curs.execute(query, (date.strftime('%Y-%m-%d %H:%M:%S'), consumption, temperature,humidity,windSpeed,weekday,isHoliday))

            print('before commited')
            conn.commit()

            print('commited')

        except :
            print('error except')
            conn.rollback()

        finally : 

            conn.close()
