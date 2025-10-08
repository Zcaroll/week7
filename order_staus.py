import requests
import os

ORDER_STATUS_KEY = '123456654321'
order_number = input('Enter your order number: ') #any number works i think

# URLs are strings
url = f'https://mock-order-status.uc.r.appspot.com/orders/status/{order_number}?API_KEY={ORDER_STATUS_KEY}'

response = requests.get(url).json()
print(response)

status = response['status']
print(f'Order status: {status}')

#TODO print order number and the order items neatly

print(f'Your order number is: {order_number}')
print()

items = response['items']
#print(items)

print('Your items are: ')

for item in items:
    print(item)
