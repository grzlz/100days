import requests

STOCK = "TSLA"
API_KEY = "0C4YOOGX1QICQWUY"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
url_params = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": API_KEY
}
url = "https://www.alphavantage.co/query"
r = requests.get(url, params = url_params)
data = r.json()["Time Series (60min)"]
last_48hours_data = {key: data[key] for key in list(data)[:33]}

closes = {
    "yesterday_close": last_48hours_data[list(last_48hours_data)[0]].get("4. close"),
    "day_before_yesterday_close": last_48hours_data[list(last_48hours_data)[16]].get("4. close")
}

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def stock_gazer(data):
    print(float(data["yesterday_close"]))
    print(float(data["day_before_yesterday_close"]))
    percentage = (float(data["yesterday_close"])/float(data["day_before_yesterday_close"]) - 1) 
    if abs(percentage) >  .06:
        print(percentage)
        print("Va jalando")

stock_gazer(closes)


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

