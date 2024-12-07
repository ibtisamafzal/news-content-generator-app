import requests

def fetch_news(query):
    url = "https://api.bing.microsoft.com/v7.0/news/search"
    headers = {"Ocp-Apim-Subscription-Key": "43e1afb6027444ccb65fc829dbb08903"}
    params = {"q": query, "count": 10, "mkt": "en-US"}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.status_code}