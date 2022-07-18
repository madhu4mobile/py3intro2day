

"""
Strings are immutable
    Meaning, you can not modify them in place but you can do mathemetical operations like addition - concatenation.
    # When to add two strings, better to use str.join() instead of a + b.
        Concatenation with + results in temporaties.
        str.join() inserts a separator between a collection of strings.
    # Unwritten convention to use an unused separator as '_"
      origin, _, destination = "Seattle-Boston".partition('-')

"""
print('***********  importance of .join() method **********')
colors = ';'.join(['#45ff23', '#2321fa', '#1298a3', '#a32312'])
print('colors using joins as : ',colors)
print("''.join(['high','way','advertisement']) : --> ",''.join(['high','way','advertisement']))

print('--->partition<--- used to separate  a string before , self and after')
print("unforgetable".partition('forget'))
print(type("unforgetable".partition('forget')))
print(" ---> Tip <---")
departure, separator, arrival = "London:Eddinburgh".partition(':')
print((departure,separator,arrival))
print(" ---> Tip-2 <---")
city, _, state = "Boston@Massachusetts".partition('@')
print((city, _, state ))




