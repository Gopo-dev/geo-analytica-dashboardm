
import requests

def fetch_tweets(query, bearer_token):
    headers = {"Authorization": f"Bearer {bearer_token}"}
    url = f"https://api.twitter.com/2/tweets/search/recent?query={query}&max_results=10&tweet.fields=created_at"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        tweets = response.json().get("data", [])
        return [t["text"] for t in tweets]
    else:
        print("Error:", response.status_code, response.text)
        return []
