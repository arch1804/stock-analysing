from lib import market
import datetime
from datetime import  timedelta
import pandas_datareader.data as web
import pandas_datareader as pdr
import pandas_ta as ta
from math4machinelearning.artificialneuralnetwork import artificialneuralnetwork_classifier
from math4machinelearning.artificialneuralnetwork import linearregression
import pandas as pd
import numpy as np
import argparse

class bot:

  def __init__(self,type="",start_date=datetime.datetime(2021,1,1),symbol=""):

    def save_data():
      daylys = []
      for v in self.symbols :
        start = self.start_date
        end = datetime.date.today() #- timedelta(days=1)
        try:
            #df = web.DataReader(v, "yahoo", start , end)
            df = pdr.get_data_yahoo(v, start , end, interval='d')
            daylys.append(df)
            df.to_csv('./data/'+v+'.csv')
        except Exception as e:
            print(e)
            pass
      return daylys


