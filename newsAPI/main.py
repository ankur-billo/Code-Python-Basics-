import requests

sources= input("What is the topic you want to read ?\n")
# api="e7b4c265317245e9b550c89dee33170b"

# url="https://newsapi.org/v2/everything?q=tesla&from=2026-02-04&sortBy=publishedAt&apiKey=e7b4c265317245e9b550c89dee33170b"

# url=f"https://newsapi.org/v2/top-headlines?sources={sources}&apiKey=e7b4c265317245e9b550c89dee33170b"

url =f"https://newsapi.org/v2/everything?q={sources}&from=2026-02-05&sortBy=publishedAt&apiKey=e7b4c265317245e9b550c89dee33170b"


print(url)
r =  requests.get(url)

data = r.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print(index + 1, article["title"], article["url"])
    print("\n****************************************\n")
