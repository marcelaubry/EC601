# EC601 PROJECT2
# Copyright Marcel Aubry 2022

# For sending GET requests from the API
import requests
# For saving access tokens and for file management when creating and adding to the dataset
import os
# For dealing with json responses we receive from the API
import json
import botometer
from google.cloud import language_v1


def auth():
    return os.getenv('TOKEN')

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

user_input = input("Enter the cryptocurrency you are interested in!\n")

maxresults = 20
def create_url():
    query = "query=%23{} lang:en".format(user_input)
    max_results = "max_results={}".format(maxresults)
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


bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)

def use_botometer(json_response):  
    count = 0
    sentiment_count = 0
    sentiment_score = 0
    for i in range(maxresults):
        user_id = int(json.dumps(json_response["data"][i]["author_id"], indent=4, sort_keys=True)[1:-1])
        result = bom.check_account(user_id)
        if float(result["cap"]["universal"]) > 0.85:
            count += 1
        else:
            sentiment_count += 1
            sentiment_score += analyze_sentiment(json.dumps(json_response["data"][i]["text"], indent=4, sort_keys=True))
    avg_sent = sentiment_score/sentiment_count
    perc_bot = count/maxresults*100

    print(f'{perc_bot}% of account are most likely bots. \nOut of the {100-perc_bot}% real accounts that tweeted, their average sentiment score is: {avg_sent}')

def analyze_sentiment(text_content):
    
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/marce/Downloads/project2-365114-4a2eb989b280.json"

    client = language_v1.LanguageServiceClient()

    type_ = language_v1.Document.Type.PLAIN_TEXT

    language = "en"
    document = {"content": text_content, "type_": type_, "language": language}

    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_sentiment(request = {'document': document, 'encoding_type': encoding_type})
    return response.document_sentiment.score


def main():
    bearer_token = auth()
    url = create_url()
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(url, headers)
    use_botometer(json_response)


if __name__ == "__main__":
    main()
