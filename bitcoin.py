import requests
# commented out but library for python 'pretty print' could run pprint(data) to make it look cleaner
#from pprint import pprint 


# mock url
bitcoin_api_url = 'https://claraj.github.io/mock-bitcoin/currentprice.json'

response = requests.get(bitcoin_api_url)
data = response.json()
#print(data)

# gets the rate float which is within USD within bpi
usd_exchange_rate = data['bpi']['USD']['rate_float'] 
print(usd_exchange_rate)

#ask user for input of bitcoin and convert to usd
bitcoin = float(input('Enter the number of bitcoin: '))

bitcoin_dollar_value = bitcoin * usd_exchange_rate

print(f'Your {bitcoin} bitcoin is worth ${bitcoin_dollar_value:.2f}')