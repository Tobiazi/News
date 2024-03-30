import requests
from API_key import API_KEY


everything = "everything" #You can search trough milloins articles in Newsapi
top_headlines = "top-headlines" #Search trough breaking headlines

#Replace "everyting_or_top_headlines" with the variable everything or top_hedlines
URL = (f"https://newsapi.org/v2/{top_headlines}?")
print(URL)


def news_by_search(subject):
    parameters = {
        "q": subject,
        "searchIn": "title",
        "sortBy": "popularity",
        "language": "en",
        "apiKey": API_KEY
        
    }
    get_articles(parameters)


def get_articles(params):
    news = requests.get(url=URL, params=params)
    
    articles = news.json()["articles"]

    article_final = []

    for article in articles:
        article_final.append({
            "Title": article["title"],
            "Description": article["description"],
            "Date": article["publishedAt"],
            "Source": article["source"]["name"],
            "URL": article["url"]
        })

    for results in article_final:
        print(results["Title"])
        print("")
        print(str(results["Description"]).replace("\n", ""))
        print("")
        print(results["Source"])
        print(results["Date"][:10])
        print(results["URL"])
        print("")
        print("")
        print("***********************************************************************")
    
    
subject = input("Category  ")
print("")
print("")
print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")

news_by_search(subject)
