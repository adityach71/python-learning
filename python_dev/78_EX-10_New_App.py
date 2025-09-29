import requests
import json
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_news():
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=a56b942be62b4da6a0aa74a81ad56efb"
    response = requests.get(url)
    news = json.loads(response.text)

    # Debugging: check if 'articles' exists
    if "articles" not in news:
        print("⚠️ Error from API:", news)
        return
    
    articles = news["articles"]

    for i, article in enumerate(articles[:5], start=1):  # show only 5 news
        title = article.get("title", "No title available")
        print(f"{i}. {title}")
        speak(title)

if __name__ == "__main__":
    get_news()
