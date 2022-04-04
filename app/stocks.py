

from app.alphavantage_service import fetch_stocks_data


print("STOCKS REPORT...")

#import os
#from dotenv import load_dotenv
#from pandas import read_csv
#
#load_dotenv()
#
#ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")

symbol = input("Please input a stock symbol (default: 'NFLX'): ") or "NFLX"
#url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}&datatype=csv"




df = fetch_stocks_data(symbol)
#print(df.columns)
#breakpoint()

latest = df.iloc[0]

print(symbol)
print(latest["timestamp"])
print(latest["close"])
print('${:,.2f}'.format(latest["close"]))
