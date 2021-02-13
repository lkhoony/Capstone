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

def calculateGasFee(data) :

    # data : dataframe['consumption','elecFee']

    # gasFeeW : 동절기 가스 요금
    gasFeeW = 10.5132 
    # gasFeeS : 하절기 가스 요금
    gasFeeS = 8.9578
    # gasFeeF : 그 외의 기간
    gasFeeF = 9.0899

    data.index.name = 'date'
    data = data.reset_index()
    
    afterCalFeeData = pd.DataFrame()
    afterCalFeeData['date'] = data['date']
    afterCalFeeData['consumption'] = data['consumption'].astype(float)
    afterCalFeeData['elecFee'] = data['elecFee'].astype(float)
    afterCalFeeData['gasFee'] = 0
    afterCalFeeData['kElec'] = 0
    afterCalFeeData['cElec'] = 0
    afterCalFeeData['warmFee'] = 0

    def calGasFee(df):
        
        # 겨울철
        if df['date'].month in [12,1,2,3] :
                
            return df['consumption'] * 11.77 * gasFeeW
        
        # 여름철
        elif df['date'].month in [6,7,8,9] :
            
            return df['consumption'] * 11.77 * gasFeeS
        
        # 봄,가을철
        else :
            
            return df['consumption'] * 11.77 * gasFeeF

    def calWarmFee(df):
        
        # 겨울철
        if df['elecFee'] > df['gasFee'] : 

            if df['date'].month in [12,1,2,3] :
                    
                return df['consumption'] * 1.43 * 84.69
            
            # 여름철
            elif df['date'].month in [6,7,8,9] :
                
                return df['consumption'] * 1.43 * 84.69
            
            # 봄,가을철
            else :
                
                return df['consumption'] * 1.43 * 84.69
        else :
            return 0


    afterCalFeeData['gasFee'] = afterCalFeeData.apply(calGasFee,axis=1)
    afterCalFeeData['warmFee'] = afterCalFeeData.apply(calWarmFee,axis=1)

    afterCalFeeData = afterCalFeeData.set_index('date')

    # afterCalFeeData['cchpFee'] = afterCalFeeData['gasFee'] - afterCalFeeData['warmFee']
    # afterCalFeeData['cchpFee'] = afterCalFeeData['gasFee'] - afterCalFeeData['warmFee']

    def kElecScheduling(df) :

        # # 예측 전력 사용량이 계약 전력보다 클 경우 : 계약 전력량을 초과 하는 부분은 CCHP 발전을 사용
        # if df['consumption'] > contractElec :

        #     return contractElec

        if df['elecFee'] > df['gasFee'] :
            return 0

        else :
            return df['consumption']

    def cElecScheduling(df) :

        # if df['consumption'] > contractElec :

        #     return df['consumption'] - contractElec

        if df['elecFee'] > df['gasFee'] :

            return df['consumption']

        else :
            return 0

    afterCalFeeData['kElec'] = afterCalFeeData.apply(kElecScheduling,axis=1)
    afterCalFeeData['cElec'] = afterCalFeeData.apply(cElecScheduling,axis=1)

    return afterCalFeeData