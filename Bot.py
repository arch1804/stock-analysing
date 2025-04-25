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


    def learn():
        ANN = {}
        for v in self.symbols :
            df = pd.read_csv('./analyse/'+v+'.csv')
            df = df.dropna(axis=0)
            x = np.matrix(df[["EMA","RSI_14","macd","bbands","PSL_12","ENTP_10","EBSW_40_10", "KURT_30", "candle"]].to_numpy() )
            y1 = np.matrix(df[["buy"]].to_numpy())
            y2 = np.matrix(df[["sell"]].to_numpy())
            #y3 = np.matrix(df[["10_on_pips"]].to_numpy())
            #y4 = np.matrix(df[["5_on_pips"]].to_numpy())
            #y5 = np.matrix(df[["pips"]].to_numpy())
            #y6 = np.matrix(df[["2_pips"]].to_numpy())
            lrX = np.matrix(df.iloc[:-1 , :][["EMA","RSI_14","macd","bbands","PSL_12","ENTP_10","EBSW_40_10", "KURT_30", "candle"]].to_numpy() )
            lrY1 =  np.matrix(df.iloc[1: , :][["support"]].to_numpy())
            lrY2 =  np.matrix(df.iloc[1: , :][["resistance"]].to_numpy())
            Lr1 = linearregression.linearregression(lrX,lrY1)
            Beta1, rss1 = Lr1.leastsquare()
            Lr2 = linearregression.linearregression(lrX,lrY2)
            Beta2, rss2 = Lr2.leastsquare()
            ann_sell = artificialneuralnetwork_classifier.artificialneuralnetwork_classifier(x,y1)
            ann_buy = artificialneuralnetwork_classifier.artificialneuralnetwork_classifier(x,y2)
            #ann_10_on_pips = artificialneuralnetwork_classifier.artificialneuralnetwork_classifier(x,y3)
            #ann_5_on_pips = artificialneuralnetwork_classifier.artificialneuralnetwork_classifier(x,y4)
            #ann_pips = artificialneuralnetwork_classifier.artificialneuralnetwork_classifier(x,y5)
            #ann_2_pips = artificialneuralnetwork_classifier.artificialneuralnetwork_classifier(x,y6)
