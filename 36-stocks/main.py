import requests
from twilio.rest import Client

STOCK = "TSLA"
API_KEY = "0C4YOOGX1QICQWUY"
COMPANY_NAME = "Tesla Inc"
NEWS_API_KEY = "24ea1829785644adb7527b85b7e532ed"
account_sid = "AC81f2671430dc9505aaed34057ce8f306"
auth_token = ""



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
    percentage = (float(data["yesterday_close"])/float(data["day_before_yesterday_close"]) - 1) 
    if abs(percentage) > 0.05:
        headlines = get_news()
        client = Client(account_sid, auth_token)
        message = client.messages.create(body=f"Change of {round(percentage * 100, 2)}%. Here the relevant news:\n{headlines[0]}\n{headlines[1]}\n{headlines[2]}",
                            from_='+14303051259',
                            to='+525548017016')
        
stock_gazer(closes) 