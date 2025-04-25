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

            ANN[v] = {
                    "buy" : ann_buy,
                    "sell" : ann_sell,
                    #"10_on_pips" : ann_10_on_pips,
                    #"5_on_pips" : ann_5_on_pips,
                    #"pips" : ann_pips,
                    #"2_pips" : ann_2_pips,
                    "support" : Lr1,
                    "resistance" : Lr2

                    }
        return ANN

    def indicate(gama):
        bot_strategie = ta.Strategy(
            name="Bot strat",
            description="Bot strategy",
            ta=[
            {"kind": "ema", "length": 8},
            {"kind": "ema", "length": 21},
            {"kind": "rsi"},
            {"kind": "macd", "fast": 8, "slow": 21, "col_names": ("MACD", "MACD_H", "MACD_S")},
            {"kind": "rsi"},
            {"kind" : "bbands"},
            {"kind" : "psl"},
            {"kind" : "entropy"},
            {"kind" : "ebsw"},
            {"kind" : "kurtosis"}
            ]
            )
        analyses = []
        k = 0
        for s in self.daylys :
            df = s
            buy = []
            sell = []
            _10_on_pips = []
            _5_on_pips = []
            _pips = []
            _2_pips = []
            df = df.drop_duplicates()
            df.ta.strategy(bot_strategie,append=True)
            row_iterator = df.iterrows()
            j = 0
            for  m, row in row_iterator:
                if j < (len(df)-1) :
                    if  (df['close'][j+1]-row['close'])  <  (-1 * gama) :
                        buy.append(0)
                        sell.append(1)
                        #var = -1 * (df['close'][j+1] - row['close'])
                        #if var  > row['close'] / 1000 :
                            #_10_on_pips.append(1)
                        #else :
                            #_10_on_pips.append(0)
                        #if var  > row['close'] / 500 :
                            #_5_on_pips.append(1)
                        #else :
                            #_5_on_pips.append(0)
                        #if var  > row['close'] / 100 :
                            #_pips.append(1)
                        #else :
                            #_pips.append(0)
                        #if var  > row['close'] / 50 :
                            #_2_pips.append(1)
                        #else :
                            #_2_pips.append(0)

                    if (df['close'][j+1]-row['close'])  > ( 1 * gama) :
                        buy.append(1)
                        sell.append(0)
                        #var = ( df['close'][j+1] - row['close'])
                        #if var  > row['close'] / 1000 :
                            #_10_on_pips.append(1)
                        #else :
                            #_10_on_pips.append(0)
                        #if var  > row['close'] / 500 :
                            #_5_on_pips.append(1)
                        #else :
                            #_5_on_pips.append(0)
                        #if var  > row['close'] / 100 :
                            #_pips.append(1)
                        #else :
                            #_pips.append(0)
                        #if var  > row['close'] / 50 :
                            #_2_pips.append(1)
                        #else :
                            #_2_pips.append(0)

                    if  (-1 * gama) < (df['close'][j+1] - row['close']) < ( 1 * gama) :
                        buy.append(0)
                        sell.append(0)
                        #_10_on_pips.append(0)
                        #_5_on_pips.append(0)
                        #_pips.append(0)
                        #_2_pips.append(0)

                if j == (len(df)-1) :
                        buy.append("")
                        sell.append("")
                        #_10_on_pips.append("")
                        #_5_on_pips.append("")
                        #_pips.append("")
                        #_2_pips.append("")


                j += 1
            df["buy"]=buy
            df["sell"]=sell
            #df["10_on_pips"]= _10_on_pips
            #df["5_on_pips"] = _5_on_pips
            #df["pips"] = _pips
            #df["2_pips"] = _2_pips
            df["EMA"]= df["EMA_21"] - df["EMA_8"]
            df["macd"]= df["MACD_H"] - df["MACD_S"]
            df["bbands"] = df["BBM_5_2.0"] - df["EMA_8"]
            df["candle"] = (df["open"] - df["close"]) / (df["high"] - df["low"])
            df["support"] = df["open"] - df["low"]
            df["resistance"] = df["high"] - df["open"]
            analyses.append(df)
            df.to_csv('./analyse/'+self.symbols[k]+'.csv')
            k += 1
        return analyses

    def predict():
        prediction = {}
        for v in self.symbols :
            df = pd.read_csv('./analyse/'+v+'.csv')
            bottom = df.tail(1)
            x = bottom[["EMA","RSI_14","macd","bbands","PSL_12","ENTP_10","EBSW_40_10", "KURT_30","candle"]].to_numpy()
            buy = self.neurones[v]["buy"].predict(x)
            sell = self.neurones[v]["sell"].predict(x)
            #_10_on_pips = self.neurones[v]["10_on_pips"].predict(x)
            #_5_on_pips = self.neurones[v]["5_on_pips"].predict(x)
            #_pips = self.neurones[v]["pips"].predict(x)
            #_2_pips = self.neurones[v]["2_pips"].predict(x)
            support =   bottom["close"] - self.neurones[v]["support"].predict(x)
            resistance = self.neurones[v]["resistance"].predict(x) + bottom["close"]
            prediction[v] = {
                "buy" : buy,
                "sell": sell,
                #"10_on_pips" : _10_on_pips,
                #"5_on_pips" : _5_on_pips,
                #"pips" : _pips,
                #"2_pips" : _2_pips,
                "support" : support,
                "resistance" : resistance
            }
            return prediction




    self.start_date = start_date
    if symbol == "" :
        self.market = market.market(type)
        self.symbols = self.market.symbols
    if symbol != ""  :
        self.symbols = [symbol]
    self.daylys = save_data()
    self.analyse = indicate(0.01)
    self.neurones = learn()
    self.prediction = predict()


if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description='Yahoo Finance Bot : A tool that predict the dayly tendance of a market (Sell VS Buy) on the basis of Exponential Mooving Average, MACD and RSI.')
    parser.add_argument("-market" , "-m", help=" Precise the market you wish to analayse. This function implement (nasdaq , nyse , world_indice , forex , crypto , mutual_fund, comodities) .")
    parser.add_argument("-value", "-v",help=" Precise a market value to analyse. Exemple : BTC-USD ")
    parser.add_argument("-out", "-o", help=" Precise the file in witch you want to save the result. By default result.txt")
    parser.add_argument("-day", "-d", help=" Start-date : Precise the start day ")
    parser.add_argument("-month", "-mo", help=" Start-date : Precise the start month ")
    parser.add_argument("-year", "-y", help=" Start-date : Precise the start year ")
    args = parser.parse_args()

    if args.market == None :
        print(" No market fill")
    else :
        print("\n-----------------------------\n |"," Market Study : ",args.market,"|\n-----------------------------" )
        if args.day == None :
            print(" You should precise at less a day from wish to start the analyse .")
        if args.month == None :
            print(" You should precise at less a month from wish to start the analyse .")
        if args.year == None :
            print(" You should precise at less a years from wish to start the analyse .")
        else :
            print(" |Start DATE :",args.day,"/", args.month,"/", args.year,"|\n-----------------------------\n" )
            Bot = bot(type=args.market,start_date=datetime.datetime(int(args.year), int(args.month) , int(args.day) ))
            print("\n-----------------------------\n |"," SIMPLE SUPPORT FORCAST : ",float(Bot.prediction[v]["support"]),"|\n-----------------------------\n" )
            print("\n-----------------------------\n |"," SIMPLE RESISTANCE FORCAST : ",float(Bot.prediction[v]["resistance"]),"|\n-----------------------------\n" )
            for v in Bot.symbols :
                print("\n-----------------------------\n |"," Value Study : ",v,"|\n-----------------------------\n" )
                print("\n-----------------------------\n |","Bot says buy bit is :", int(Bot.prediction[v]["buy"]),"|\n-----------------------------\n" )
                print("\n-----------------------------\n |","Bot says sell bit is :", int(Bot.prediction[v]["sell"]),"|\n-----------------------------\n" )
                if int(Bot.prediction[v]["buy"]) == 0 and int(Bot.prediction[v]["sell"]) == 1 :
                    print("\n-----------------------------\n |"," You should sell it","|\n-----------------------------\n" )
                if int(Bot.prediction[v]["buy"]) == 1 and int(Bot.prediction[v]["sell"]) == 0 :
                    print("\n------------------------\n |"," You should buy it","|\n------------------------\n" )
                if int(Bot.prediction[v]["buy"]) == 0 and int(Bot.prediction[v]["sell"]) == 0 :
                    print("\n------------------------\n |"," You should wait ","|\n------------------------\n" )
                #if int(Bot.prediction[v]["10_on_pips"]) == 0 :
                    #print("\n------------------------\n |"," The variation should be less then 0.1 pips ","|\n------------------------\n")
                #else :
                    #print("\n------------------------\n |"," The variation should be more then 0.1 pips ","|\n------------------------\n")
                #if int(Bot.prediction[v]["5_on_pips"]) == 0 :
                    #print("\n------------------------\n |"," The variation should be less then 0.2 pips ","|\n------------------------\n")
                #else :
                    #print("\n------------------------\n |"," The variation should be more then 0.2 pips ","|\n------------------------\n")
                #if int(Bot.prediction[v]["pips"]) == 0 :
                    #print("\n------------------------\n |"," The variation should be less then 1 pips ","|\n------------------------\n")
                #else :
                    #print("\n------------------------\n |"," The variation should be more then 1 pips ","|\n------------------------\n")
                #if int(Bot.prediction[v]["2_pips"]) == 0 :
                    #print("\n------------------------\n |"," The variation should be less then 2 pips ","|\n------------------------\n")
                #else :
                    #print("\n------------------------\n |"," The variation should be more then 2 pips ","|\n------------------------\n")

    if args.value == None :
        print(" No value choose ")
    else :
        print("\n-----------------------------\n |"," Value Study : ",args.value,"|\n-----------------------------\n" )
        if args.day == None :
            print(" You should precise at less a day from wish to start the analyse .")
        if args.month == None :
            print(" You should precise at less a month from wish to start the analyse .")
        if args.year == None :
            print(" You should precise at less a years from wish to start the analyse .")
        else :
            print(" |Start DATE :",args.day,"/", args.month,"/", args.year,"|\n-----------------------------\n" )
            Bot = bot(symbol=args.value,start_date= datetime.datetime(int(args.year), int(args.month) , int(args.day) ))
            print("\n-----------------------------\n |"," SIMPLE Low FORCAST : ",float(Bot.prediction[args.value]["support"]),"|\n-----------------------------\n" )
            print("\n-----------------------------\n |"," SIMPLE High FORCAST : ",float(Bot.prediction[args.value]["resistance"]),"|\n-----------------------------\n" )
            print("\n-----------------------------\n |","Bot says buy bit is :", int(Bot.prediction[args.value]["buy"]),"|\n-----------------------------\n" )
            print("\n-----------------------------\n |","Bot says sell bit is :", int(Bot.prediction[args.value]["sell"]),"|\n-----------------------------\n" )
            if int(Bot.prediction[args.value]["buy"]) == 0 and int(Bot.prediction[args.value]["sell"]) == 1 :
                print("\n-----------------------------\n |"," You should sell it","|\n-----------------------------\n" )
            if int(Bot.prediction[args.value]["buy"]) == 1 and int(Bot.prediction[args.value]["sell"]) == 0 :
                print("\n------------------------\n |"," You should buy it","|\n------------------------\n" )
            if int(Bot.prediction[args.value]["buy"]) == 0 and int(Bot.prediction[args.value]["sell"]) == 0 :
                print("\n------------------------\n |"," You should wait ","|\n------------------------\n" )
            #if int(Bot.prediction[args.value]["10_on_pips"]) == 0 :
                #print("\n------------------------\n |"," The variation should be less then 0.1 pips ","|\n------------------------\n")
            #else :
                #print("\n------------------------\n |"," The variation should be more then 0.1 pips ","|\n------------------------\n")
            #if int(Bot.prediction[args.value]["5_on_pips"]) == 0 :
                #print("\n------------------------\n |"," The variation should be less then 0.2 pips ","|\n------------------------\n")
            #else :
                #print("\n------------------------\n |"," The variation should be more then 0.2 pips ","|\n------------------------\n")
            #if int(Bot.prediction[args.value]["pips"]) == 0 :
                #print("\n------------------------\n |"," The variation should be less then 1 pips ","|\n------------------------\n")
            #else :
                #print("\n------------------------\n |"," The variation should be more then 1 pips ","|\n------------------------\n")
            #if int(Bot.prediction[args.value]["2_pips"]) == 0 :
                #print("\n------------------------\n |"," The variation should be less then 2 pips ","|\n------------------------\n")
            #else :
                #print("\n------------------------\n |"," The variation should be more then 2 pips ","|\n------------------------\n")
    if args.value == None and args.market == None :
        print(" You should precise at less a value or a market.")
    #Bot = bot('ninja',datetime.datetime(2021, 12, 1))
