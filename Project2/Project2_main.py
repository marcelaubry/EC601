# EC601 PROJECT2
# Copyright Marcel Aubry 2022

# For sending GET requests from the API
import requests
# For saving access tokens and for file management when creating and adding to the dataset
import os
# For dealing with json responses we receive from the API
import json
import botometer


def auth():
    return os.getenv('TOKEN')

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

user_input = input("Enter the cryptocurrency you are interested in!\n")

maxresults = 10
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
    for i in range(maxresults):
        user_id = int(json.dumps(json_response["data"][i]["author_id"], indent=4, sort_keys=True)[1:-1])
        result = bom.check_account(user_id) 
        print(result["display_scores"]["universal"])
        if float(result["cap"]["universal"]) > 0.8:
            print("This account is most likely a bot!!!")

def main():
    bearer_token = auth()
    url = create_url()
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(url, headers)
    use_botometer(json_response)
    #print(json.dumps(json_response, indent=4, sort_keys=True))
    

if __name__ == "__main__":
    main()

# # Check a single account by id
# result = bom.check_account(1548959833)

# # Check a sequence of accounts
# accounts = ['@clayadavis', '@onurvarol', '@jabawack']
# for screen_name, result in bom.check_accounts_in(accounts):
#     # Do stuff with `screen_name` and `result`