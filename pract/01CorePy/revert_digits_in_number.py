
"""
This is to revert the digits of a given number from user
"""



# Logic to keep asking user to input a positive value
nonNegativeAndNonZero = True
while nonNegativeAndNonZero:
    myNumber = int(input('Provide a number : '))
    if (myNumber <= 0):
        print('The number you provided is invalid. \nPlease provide a positive number greater than zero \n')
    elif(myNumber < 10):
        nonNegativeAndNonZero = False
        print('Your number is a single digit.\n When reverted it will be the same : ', myNumber)
    else:
        nonNegativeAndNonZero = False

## logic to revert number
def reverted_number(myNumber):
    reverted = 0
    tempNumber = myNumber
    while tempNumber > 0:
        reminder = int(tempNumber % 10)
        reverted = (reverted*10)  + reminder
        tempNumber = tempNumber // 10
        # print("tempNumber :",tempNumber)
        # print("reverted",reverted)
    return reverted

print("Here is the reverted number : ", reverted_number(myNumber))







