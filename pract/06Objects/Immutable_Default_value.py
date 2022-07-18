

'''
It is always a better idea to take default value as None in an immutable list

'''

def add_spam(menu=None):
    if menu is None:
        menu = []
    menu.append('spam')
    return menu

print(add_spam())

print(add_spam())

breakfast = ['eggs', 'cereal']
print(add_spam(breakfast))
print(add_spam(breakfast))

breakfast = ['eggs', 'cereal', 'spam']
print(add_spam(breakfast))




