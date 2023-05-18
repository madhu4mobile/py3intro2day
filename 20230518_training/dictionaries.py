bonds = {'X': 1, 'Y': 3, 'Z': 5}

print(bonds)

client_1 = {'Name': "Adam", 'Age': 40, "Gender": "Male"}

print(client_1["Age"])

# if I wanted to add 'Net Worth'
client_1['Net Worth'] = 5

print(client_1)

## If you want to update the age increasing every year
client_1['Age'] = client_1['Age'] + 1
print(client_1)
client_1
print(client_1)

A = {'price': 100, 'quantity': 1}
B = {'price': 200, 'quantity': 2}
C = {'price': 300, 'quantity': 3}

print(B['price'])

# create a new dictionary called portfolio and it in place the 3 dicts you just created.
# keys should go as postion_A, position_B and position_c

# portfolio = {
#     'position_A': {'price': 100, 'quantity': 1},
#     'position_B': {'price': 200, 'quantity': 2},
#     'position_C': {'price': 300, 'quantity': 3}
# }
portfolio = {'position_A': A, 'position_B': B, 'position_C': C}

print(portfolio)

# how to call? Total of position_C
print(portfolio['position_C'])

# how to call? price of Position_B
print(portfolio['position_B']['price'])
#quantity of position_B
print(portfolio['position_B']['quantity'])

# assign a new value by mutliplying the same value by 2
portfolio['position_B']['quantity'] = portfolio['position_B']['quantity'] * 2
print(portfolio['position_B']['quantity'])
print("********************************")