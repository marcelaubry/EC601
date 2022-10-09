# https://github.com/IUNetSci/botometer-python

import botometer



bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)

# Check a single account by screen name
accounts = ['@hello__marcel', '@aksel_laudon', '@AndreweTrapp', '@KylieJenner', '@AthleticsCanada']
for screen_name, result in bom.check_accounts_in(accounts):
  print(screen_name, result["display_scores"]["universal"])
  if float(result["cap"]["universal"]) > 0.8:
    print("This account is most likely a bot!!!")

# # Check a single account by id
# result = bom.check_account(1548959833)

# # Check a sequence of accounts
# accounts = ['@clayadavis', '@onurvarol', '@jabawack']
# for screen_name, result in bom.check_accounts_in(accounts):
#     # Do stuff with `screen_name` and `result`