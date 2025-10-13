import requests

try:
    response = requests.get('https://catfact.ninja/fact') # Pulling from the api 

    print(response.status_code)

    response.raise_for_status() # raise an exception for 400 or 500 code
    print(response.text)
    print(response.json())

    data = response.json()
    fact = data['fact'] #pulling the fact from the dictionary
    print(f'A random cat fact is {fact}')

except Exception as e:
    print(e)
    print('there was an error making the request')
