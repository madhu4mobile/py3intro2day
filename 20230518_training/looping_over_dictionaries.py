prices = {100, 200, 300, 400}

for price in prices:
    print(price)

client_1 = {'Name': "Adam", 'Age': 40, "Gender": "Male"}

for key, value in client_1.items():
    print(key, value)

stocks_2 = {'B': 200, 'C': 300, 'D': 400}

for stock, price in stocks_2.items():
    print(stock, price)

# Loop over the stocks2 and each time, print  out using f-string 'The stock X has price Y'
for x, y in stocks_2.items():
    print(f'The stock {x} has price {y}')

total = 0
for x,y in stocks_2.items():
    total = total + y

print(f'The total of stock price is {total}')

#### ----> Imp : If you want to run a loop only accross the values in the loop,

total2 = 0
for value in stocks_2.values():
    total2 = total2 + value
print(f'The total of stock price is {total2}')

