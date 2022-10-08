# EC601 PROJECT2
# Copyright Marcel Aubry 2022
# Collecting tweets from Twitter API v2
# Source: https://towardsdatascience.com/an-extensive-guide-to-collecting-tweets-from-twitter-api-v2-for-academic-research-using-python-3-518fcb71df2a

# For sending GET requests from the API
import requests
# For saving access tokens and for file management when creating and adding to the dataset
import os
# For dealing with json responses we receive from the API
import json


def auth():
    return os.getenv('TOKEN')

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

    
def create_url():
    query = "query=%23China lang:en -(is:retweet)"
    max_results = "max_results=10"
    tweet_fields = "tweet.fields=created_at,public_metrics,attachments,text"
    expansions = "expansions=attachments.media_keys,author_id"
    user_fields = "user.fields=id,name,username,description"
    url = "https://api.twitter.com/2/tweets/search/recent?{}&{}&{}&{}&{}".format(
        query, tweet_fields, max_results, expansions, user_fields
    )
    return url

def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def main():
    bearer_token = auth()
    url = create_url()
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(url, headers)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()