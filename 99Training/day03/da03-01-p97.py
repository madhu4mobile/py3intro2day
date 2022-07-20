class Person:

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f'Hellow {self.name}')


p1 = Person('John Doe')
p2 = Person('Sally Smith')

p1.say_hello()
p2.say_hello()


def foo(self):
    print(f'GoodBye {self.name}')


setattr(Person, 'say_hello', foo)  # dynamically changes the class method to a new one

p1.say_hello()
p2.say_hello()
