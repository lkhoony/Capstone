# import plotly
# import plotly.graph_objs as go
# import lightgbm as lgb
# import pandas as pd
# import numpy as np
# import json
# import pickle
# # from sklearn.externals import joblib
import joblib
import os
import sys

sys.path.append(".")

def getModel(modelName) :

    loadedModel = joblib.load(modelName)

    return loadedModel
