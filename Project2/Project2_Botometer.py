# https://github.com/IUNetSci/botometer-python

import botometer

rapidapi_key = "8f94654418msh6c89be25901f112p1bac74jsnf448fcba7411"
twitter_app_auth = {
    'consumer_key': 'AzTuOpP5FHR8ynx3JmpRE85OI',
    'consumer_secret': 'pPpOStP2XhqrxqHpBcSSUGII5UFddJLGjPn9NWWSj0Pi0u5Ayv',
  }
bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)

# Check a single account by screen name
result = bom.check_account('@clayadavis')
print(result)

# # Check a single account by id
# result = bom.check_account(1548959833)

# # Check a sequence of accounts
# accounts = ['@clayadavis', '@onurvarol', '@jabawack']
# for screen_name, result in bom.check_accounts_in(accounts):
#     # Do stuff with `screen_name` and `result`