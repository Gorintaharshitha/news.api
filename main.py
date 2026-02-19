
import requests
query="mobile phone"
api="e2f30b7c5fd54dfca07c04b815497bb2"
url=f"https://newsapi.org/v2/everything?q={query}&from=2025-09-31&sortBy=publishedAt&apiKey={api}"
print(url)
c=requests.get(url).json()
print(c)
articles=c["articles"]
for index, article in enumerate(articles):
    print( index+1,article["title"], article["url"])
    print("\n***********************************\n")