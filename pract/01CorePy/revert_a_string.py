


nonNegativeAndNonZero = True
while nonNegativeAndNonZero:
    myString = input('What string you want to see in reverse ? : ')
    if (myString == "" or myString == ' ' ):
        print('The string you provided is Null. \nPlease provide a valid string \n')
    elif(len(myString) == 1):
        nonNegativeAndNonZero = False
        print('You entered a character.\n When reverted it will be the same : ', myString)
    else:
        nonNegativeAndNonZero = False

def reverted_string(tempString):
    # using string sliging , [len(tempString)::-1]
    return tempString[len(tempString)::-1]

print('Here is the reverted string : ', reverted_string(myString).lower())