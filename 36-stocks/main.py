import requests

STOCK = "TSLA"
API_KEY = "0C4YOOGX1QICQWUY"
COMPANY_NAME = "Tesla Inc"
NEWS_API_KEY = "24ea1829785644adb7527b85b7e532ed"

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

news_url_params = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
    "language": "en",
    "sortBy": "relevancy"
    }
news_url = "https://newsapi.org/v2/everything"

def get_news():
    news_r = requests.get(news_url, params=news_url_params)
    latest_three_news = news_r.json()["articles"][:3]
    return [headline["title"] for headline in latest_three_news]

def stock_gazer(data):
    print(float(data["yesterday_close"]))
    print(float(data["day_before_yesterday_close"]))
    percentage = (float(data["yesterday_close"])/float(data["day_before_yesterday_close"]) - 1) 
    if abs(percentage) >  0:
        print(get_news())

stock_gazer(closes) 

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

