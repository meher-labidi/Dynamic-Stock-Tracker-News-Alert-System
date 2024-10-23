import requests
from twilio.rest import Client
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY ="your api key"
NEWS_API_KEY = " your news api key"
account_sid = 'your auth_sid'
auth_token = "your auth token"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

parameters = {
    "apikey": API_KEY,
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME


}
response = requests.get(STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()

YCP_data = data["Time Series (Daily)"]

new_data = [value for (key, value) in YCP_data.items()]
yesterday_close_price = new_data[0]["4. close"]

day_before_yesterday_close_price = new_data[1]["4. close"]


difference = round(float(yesterday_close_price)-float(day_before_yesterday_close_price))
up_down = None
if difference > 0:
    up_down = "🔺"
else:

    up_down = "🔻"


percentage_difference = (difference/float(yesterday_close_price))*100


if abs(percentage_difference) > 1:
    parameters1 = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME,
        "searchIn": "title",

    }
    news_response = requests.get(NEWS_ENDPOINT, params=parameters1)
    news_response.raise_for_status()
    news_data = news_response.json()
    three_articles = news_data["articles"][:3]

    formatted_articles =[f"{STOCK_NAME}: {up_down}{percentage_difference}%\nHeadline: {article['title']}. \nBrief: {article['description']}"for article in three_articles ]

    client = Client(account_sid, auth_token)

    for article in formatted_articles:
        message = client.messages.create(
            from_='phone number',
            body=article,
            to='phone number'
        )

        print(message.status)




