import pandas as pd

A = {'price': 100, 'quantity': 1}
B = {'price': 200, 'quantity': 2}
C = {'price': 300, 'quantity': 3}

portfolio = {'position_A': A, 'position_B': B, 'position_C': C}

# pandas DataFrame is to print the data as table
df = pd.DataFrame(portfolio)

print(df)

print(df['position_A'])

print(df['position_A']['price'])

#If you want to transpose the Matrix
print(df.T)
print(df)

#if you want to change the Transpose permanently
df=df.T
print(df)


### mitosheet
import mitosheet
mitosheet.sheet(df)
