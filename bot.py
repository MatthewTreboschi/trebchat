# bot.py
from os.path import join, dirname
from dotenv import load_dotenv
import os
import requests
from urllib.parse import quote
import finnhub

dotenv_path = join(dirname(__file__), 'sql.env')
load_dotenv(dotenv_path)

finnhub_client = finnhub.Client(api_key = os.environ['STOCK_KEY'])

class mattbot():
    
    def __init__(self):
        self.response="Not a command."
        
    def message(self, string):
        self.response="Not a command."
        if (string[:2]=="!!"):
            if (string[2:]=="about"):
                self.response = ("Hello, I am MattBot, your translation assistant. " +
                                "I do make translations and jokes. type !!help for more.")
            elif (string[2:]=="help"):
                self.response = ("Type !!funtranslate with a sentence for" +
                                "a translation to shakespearean english, " +
                            "!!joke for a joke, or !!STONKS for facebook stock info.")
            elif (string[2:]=="joke"):
                self.response = ("why dont you see elephants hiding in trees? " +
                                "Because theyre so good at it.")
            elif (string[2:14]=="funtranslate"):
                quote = string[15:]
                apiResponse = requests.get('https://api.funtranslations.com/translate/'+
                                            'shakespeare.json?text='+quote).json()
                print(str(apiResponse))
                translation = apiResponse['contents']['translated']
                self.response = translation
            elif (string[2:] == "STONKS"):
                stockdata=finnhub_client.quote('FB')
                change = (stockdata['c'] - stockdata['o'])
                price = stockdata['c']
                self.response = ("Facebook currently costs $" + str(price) + 
                                " which is a change of " + str(change) + " today.")
            else:
                self.response = "The command is not recognized."
        return self.response