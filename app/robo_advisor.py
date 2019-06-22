# app/robo_advisor.py

#imports

import requests
import json
import csv
import os

#functions

def moneyformat(price):
    return '${:,.2f}'.format(price) 

#URLs
url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo"
response = requests.get(url)

#print(response.status_code) #> 200
#print(type(response)) #> <class 'requests.models.Response'>
#print(response.text)

#Info Inputs

parsed_response = json.loads(response.text)
time_series = parsed_response["Time Series (Daily)"]
date = list(time_series.keys())
last_day = date[0]
last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
latest_close = time_series[last_day]["4. close"]

large_prices = []
small_prices = []

for chosen_date in date:
    large_price = time_series[chosen_date]["2. high"]
    large_prices.append(float(large_price))
    small_price = time_series[chosen_date]["3. low"]
    small_prices.append(float(small_price))

latest_high = max(large_prices)
latest_low = min(small_prices)

#breakpoint()

#Info Outputs

#csv_file_path = "data/stock_prices.csv" # a relative filepath
csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "stock_prices.csv")

with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=["city", "name"])
    writer.writeheader() # uses fieldnames set above
    writer.writerow({"city": "New York", "name": "Yankees"})
    writer.writerow({"city": "New York", "name": "Mets"})
    writer.writerow({"city": "Boston", "name": "Red Sox"})
    writer.writerow({"city": "New Haven", "name": "Ravens"})

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm") #DO ON OWN
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {moneyformat(float(latest_close))}")
print(f"RECENT HIGH: {moneyformat(float(latest_high))}")
print(f"RECENT LOW: {moneyformat(float(latest_low))}")
print("-------------------------")
print("RECOMMENDATION: BUY!") #if statements required
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print(f"WRITING DATA TO CSV: {csv_file_path}...")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
