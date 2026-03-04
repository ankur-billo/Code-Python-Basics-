import requests

query = input("What is the topic you want to read ?\n")
api="e7b4c265317245e9b550c89dee33170b"

url=f"https://newsapi.org/v2/everything?q={query}&from=2026-02-03&sortBy=publishedAt&apiKey={api}"


print(url)
r =  requests.get(url)

data = r.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print(index + 1, article["title"], article["url"])
    print("\n****************************************\n")
