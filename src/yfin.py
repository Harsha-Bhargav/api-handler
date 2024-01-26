import yfinance as yahooFinance
import json


# We need to pass FB as argument for that
GetFacebookInformation = yahooFinance.Ticker("META")

#saving the data to facebook_info
facebook_info = GetFacebookInformation.info

#opening a json file and writting the data we got from the api to the file:
with open('data/facebook_info.json', 'w') as json_file:
    json.dump(facebook_info, json_file,indent=2)

print("Data saved to data/facebook_info.json")
