"""
    This is the part of the Objects and Types

"""


def banner_around_message(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)
    pass


message, banner = input("Provide the message and banner separated with a comma : ").split(' , ')
banner_around_message(message)  # when nothing is passed as banner, it takes default value '-'
banner_around_message(message, banner)

"""
Sample inputs and outputs

Provide the message and banner separated with a comma : This is my message , *
------------------
This is my message
------------------
******************
This is my message
******************

"""
