import matplotlib as mpl
from matplotlib import pyplot as plt
import sys
import math
import numpy as np
import pandas as pd
import openpyxl
import datetime as dt
import seaborn as sns
from scipy import stats

def getElecFeeCol(data,payment) :
    
    # klSummer : 저압전력 - 여름철 요금
    # klWinter : 저압전력 - 겨울철 요금
    # klSpringAndFall : 저압전력 - 봄, 가을철 요금
    klSummer = 96.9
    klWinter = 84.1
    klSpringAndFall = 59.7
    
    # kA1Summer : 고압A1 - 여름철 요금
    # kA1Winter : 고압A1 - 겨울철 요금
    # kA1SpringAndFall : 고압A1 - 봄, 가을철 요금
    kA1Summer = 96.6
    kA1Winter = 82.6
    kA1SpringAndFall = 59.8
    
    # kA2Summer : 고압A2 - 여름철 요금
    # kA2Winter : 고압A2 - 겨울철 요금
    # kA2SpringAndFall : 고압A2 - 봄, 가을철 요금
    kA2Summer = 92.1
    kA2Winter = 55.4
    kA2SpringAndFall = 78.1
    
    # kB1Summer : 고압B1 - 여름철 요금
    # kB1Winter : 고압B1 - 겨울철 요금
    # kB1SpringAndFall : 고압B1 - 봄, 가을철 요금
    kB1Summer = 95.9
    kB1Winter = 59.4
    kB1SpringAndFall = 81.8
    
    # kB2Summer : 고압B2 - 여름철 요금
    # kB2Winter : 고압B2 - 겨울철 요금
    # kB2SpringAndFall : 고압B2 - 봄, 가을철 요금
    kB2Summer = 91.4
    kB2Winter = 54.9
    kB2SpringAndFall = 77.3
    
    # eA1Summer : 고압A1 - 여름철 요금
    # eA1Winter : 고압A1 - 겨울철 요금
    # eA1SpringAndFall : 고압A1 - 봄, 가을철 요금
    eA1SummerL = 49.8
    eA1SummerM = 94.5
    eA1SummerH = 160.4
    eA1WinterL = 53.8
    eA1WinterM = 93.0
    eA1WinterH = 131.7
    eA1SpringAndFallL = 49.8
    eA1SpringAndFallM = 64.2
    eA1SpringAndFallH = 84.70
    
    # eA2Summer : 고압A2 - 여름철 요금
    # eA2Winter : 고압A2 - 겨울철 요금
    # eA2SpringAndFall : 고압A2 - 봄, 가을철 요금
    eA2SummerL = 45.3
    eA2SummerM = 90.0
    eA2SummerH = 155.9
    eA2WinterL = 49.3
    eA2WinterM = 88.5
    eA2WinterH = 127.2
    eA2SpringAndFallL = 45.3
    eA2SpringAndFallM = 59.7
    eA2SpringAndFallH = 80.2
    
    # eB1Summer : 고압B1 - 여름철 요금
    # eB1Winter : 고압B1 - 겨울철 요금
    # eB1SpringAndFall : 고압B1 - 봄, 가을철 요금
    eB1SummerL = 48.3
    eB1SummerM = 91.8
    eB1SummerH = 154.7
    eB1WinterL = 52.1
    eB1WinterM = 90.1
    eB1WinterH = 127.4
    eB1SpringAndFallL = 48.3
    eB1SpringAndFallM = 62.5
    eB1SpringAndFallH = 82.3
    
    # eB2Summer : 고압B2 - 여름철 요금
    # eB2Winter : 고압B2 - 겨울철 요금
    # eB2SpringAndFall : 고압B2 - 봄, 가을철 요금
    eB2SummerL = 43.8
    eB2SummerM = 87.3
    eB2SummerH = 150.2
    eB2WinterL = 47.6
    eB2WinterM = 85.6
    eB2WinterH = 122.9
    eB2SpringAndFallL = 43.8
    eB2SpringAndFallM = 58.0
    eB2SpringAndFallH = 77.8
    
    # calData = 0

    print(payment)

    if(payment in [1,2,3,4,5]) :
        
        if(payment == 1) :
            calData = calKContract(data,klSummer,klWinter,klSpringAndFall)
            
        elif(payment == 2) :
            calData = calKContract(data,kA1Summer,kA1Winter,kA1SpringAndFall)
            
        elif(payment == 3) :
            calData = calKContract(data,kA2Summer,kA2Winter,kA2SpringAndFall)
            
        elif(payment == 4) :
            calData = calKContract(data,kB1Summer,kB1Winter,kB1SpringAndFall)
            
        elif(payment == 5) :
            calData = calKContract(data,kB2Summer,kB2Winter,kB2SpringAndFall)
            
    else :
        
        if(payment == 6) :
            calData = calEContract(data,eA1SummerL,eA1SummerM, eA1SummerH, eA1WinterL, eA1WinterM, eA1WinterH ,eA1SpringAndFallL, eA1SpringAndFallM, eA1SpringAndFallH )
        
        elif(payment == 7) :
            calData = calEContract(data,eA2SummerL,eA2SummerM, eA2SummerH, eA2WinterL, eA2WinterM, eA2WinterH ,eA2SpringAndFallL, eA2SpringAndFallM, eA2SpringAndFallH )
        
        elif(payment == 8) :
            calData = calEContract(data,eB1SummerL,eB1SummerM, eB1SummerH, eB1WinterL, eB1WinterM, eB1WinterH ,eB1SpringAndFallL, eB1SpringAndFallM, eB1SpringAndFallH )      
        
        elif(payment == 9) :
            calData = calEContract(data,eB2SummerL,eB2SummerM, eB2SummerH, eB2WinterL, eB2WinterM, eB2WinterH ,eB2SpringAndFallL, eB2SpringAndFallM, eB2SpringAndFallH )

    
    return calData

# 교육용 갑 요금 계산
def calKContract(data,summer,winter,springAndFall) :
    
    data.index.name = 'date'
    data = data.reset_index()
    
    afterCalFeeData = pd.DataFrame()
    afterCalFeeData['date'] = data['date']
    afterCalFeeData['consumption'] = data['consumption'].astype(float)
    afterCalFeeData['elecFee'] = 0
    
    print(afterCalFeeData)

    def calElecFee(df):
        # 겨울철
        if df['date'].month in [11,12,1,2] :
            return df['consumption']*(winter)
        
        # 여름철
        elif df['date'].month in [6,7,8] :
            return df['consumption'] * summer
        
        # 봄,가을철
        else :
            return df['consumption'] * springAndFall

    afterCalFeeData['elecFee'] = afterCalFeeData.apply(calElecFee,axis=1)
    
    return afterCalFeeData

    
    
# 교육용 을 요금 계산
def calEContract(data,summerL,summerM, summerH, winterL, winterM, winterH ,springAndFallL, springAndFallM, springAndFallH ) : 
    
    data.index.name = 'date'
    data = data.reset_index()
    
    afterCalFeeData = pd.DataFrame()
    afterCalFeeData['date'] = data['date']
    afterCalFeeData['consumption'] = data['consumption'].astype(float)
    afterCalFeeData['elecFee'] = 0
    
    def calElecFee(df):
        
        # 겨울철
        if df['date'].month in [11,12,1,2] :
            
            if df['date'].hour in [0,1,2,3,4,5,6,7,8,9] :
                
                return df['consumption'] * winterL
            
            elif df['date'].hour in [10,13,14,15,16,17,21,22] :
                
                return df['consumption'] * winterM
            
            else :
                
                return df['consumption'] * winterH
        
        # 여름철
        elif df['date'].month in [6,7,8] :
            
            if df['date'].hour in [0,1,2,3,4,5,6,7,8,9] :
                
                return df['consumption'] * summerL
            
            elif df['date'].hour in [10,13,18,19,20,21,22,23] :
                
                return df['consumption'] * summerM
            
            else :
                
                return df['consumption'] * summerH
        
        # 봄,가을철
        else :
            
            if df['date'].hour in [0,1,2,3,4,5,6,7,8,9] :
                
                return df['consumption'] * springAndFallL
            
            elif df['date'].hour in [10,13,18,19,20,21,22,23] : 
                
                return df['consumption'] * springAndFallM
            
            else :
                
                return df['consumption'] * springAndFallH

    afterCalFeeData['elecFee'] = afterCalFeeData.apply(calElecFee,axis=1)

    return afterCalFeeData

def getContractElecFee(contractElec,payment) :

    # k : 교육용(갑)
    
    # kl : 교육용(갑) - 저압전력 기본요금
    # kA1 : 교육용(갑) - 고압 A-1 기본요금
    # kA2 : 교육용(갑) - 고압 A-2 기본요금
    # kB1 : 교육용(갑) - 고압 B-1 기본요금
    # kB2 : 교육용(갑) - 고압 B-2 기본요금
    
    kl = 5230
    kA1 = 5550
    kA2 = 6370
    kB1 = 5550
    kB2 = 6370
    
    # e : 교육용(을)
    # eA1 : 교육용(을) - 고압 A-1 기본요금
    # eA2 : 교육용(을) - 고압 A-2 기본요금
    # eB1 : 교육용(을) - 고압 B-1 기본요금
    # eB2 : 교육용(을) - 고압 B-2 기본요금
    
    eA1 = 6090
    eA2 = 6980
    eB1 = 6090
    eB2 = 6980

    if(payment == 1) :
        contractElecFee = contractElec * kl
    elif(payment == 2) :
        contractElecFee = contractElec * kA1
    elif(payment == 3) :
        contractElecFee = contractElec * kA2
    elif(payment == 4) :
        contractElecFee = contractElec * kB1
    elif(payment == 5) :
        contractElecFee = contractElec * kB2
    elif(payment == 6) :
        contractElecFee = contractElec * eA1
    elif(payment == 7) :
        contractElecFee = contractElec * eA2
    elif(payment == 8) :
        contractElecFee = contractElec * eB1
    elif(payment == 9) :
        contractElecFee = contractElec * eB2
    
    return contractElecFee

class ElecFeeCalculator :
    
    # k : 교육용(갑)
    
    # kl : 교육용(갑) - 저압전력 기본요금
    # kA1 : 교육용(갑) - 고압 A-1 기본요금
    # kA2 : 교육용(갑) - 고압 A-2 기본요금
    # kB1 : 교육용(갑) - 고압 B-1 기본요금
    # kB2 : 교육용(갑) - 고압 B-2 기본요금
    
    kl = 5230
    kA1 = 5550
    kA2 = 6370
    kB1 = 5550
    kB2 = 6370
    
    # e : 교육용(을)
    # eA1 : 교육용(을) - 고압 A-1 기본요금
    # eA2 : 교육용(을) - 고압 A-2 기본요금
    # eB1 : 교육용(을) - 고압 B-1 기본요금
    # eB2 : 교육용(을) - 고압 B-2 기본요금
    
    eA1 = 6090
    eA2 = 6980
    eB1 = 6090
    eB2 = 6980
    
    def __init__(self,data) :
        
        self.data = data
        
    def calElecFee(self, contractElec, payment, period) :
        
        # data : 전력사용량 데이터
        # contractElec : 계약 전력량
        # payment : 계약 유형
        # 1 : 교육용(갑) 저압전력
        # 2 : 교육용(갑) 고압A 1 
        # 3 : 교육용(갑) 고압A 2 
        # 4 : 교육용(갑) 고압B 1
        # 5 : 교육용(갑) 고압B 2
        # 6 : 교육용(을) 고압A 1 
        # 7 : 교육용(을) 고압A 2 
        # 8 : 교육용(을) 고압B 1
        # 9 : 교육용(을) 고압B 2
        
        if(payment == 1) :
            contractElecFee = contractElec * self.kl
        elif(payment == 2) :
            contractElecFee = contractElec * self.kA1
        elif(payment == 3) :
            contractElecFee = contractElec * self.kA2
        elif(payment == 4) :
            contractElecFee = contractElec * self.kB1
        elif(payment == 5) :
            contractElecFee = contractElec * self.kB2
        elif(payment == 6) :
            contractElecFee = contractElec * self.eA1
        elif(payment == 7) :
            contractElecFee = contractElec * self.eA2
        elif(payment == 8) :
            contractElecFee = contractElec * self.eB1
        elif(payment == 9) :
            contractElecFee = contractElec * self.eB2
        
       
        newData = getElecFeeCol(self.data,payment)
        # print(newData)
        newData = newData.set_index('date')
        
        # 일간 통계
        if(period==1) :
            newData = newData.groupby(pd.Grouper(freq='D')).sum()
            
        # 월간 통계
        elif(period==2) :
            newData = newData.groupby(pd.Grouper(freq='M')).sum()
            newData['elecFee'] = newData['elecFee'] + contractElecFee
            
        # 연간통계
        elif(period==3) :
            newData = newData.groupby(pd.Grouper(freq='M')).sum()
            newData['elecFee'] = newData['elecFee'] + contractElecFee
            newData = newData.groupby(pd.Grouper(freq='Y')).sum()
   
        return newData
    

    