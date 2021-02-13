import requests
from bs4 import BeautifulSoup
from dateutil.relativedelta import relativedelta
import datetime
import json
import pandas as pd
import sys

sys.path.append("..")

class Predictor :

    def __init__(self,data) : 

        self.data = data

    def executePrediction(self, model) :

        feature_names = ['temperature','humidity','windSpeed','weekday','isHoliday',
                 'month','hour']
        categorical_feature_name = ['weekday','isHoliday','month','hour']
        index = self.data.index
        self.data['month'] = index.month
        self.data['hour'] = index.hour

        for var in categorical_feature_name :
            self.data[var] = self.data[var].astype('category')

        predictions = model.predict(self.data[feature_names])

        predictionData = pd.DataFrame()
        predictionData['date']= self.data.index
        predictionData = predictionData.set_index('date')

        predictionData['consumption'] = predictions
        # print(predictionData)
        return predictionData

