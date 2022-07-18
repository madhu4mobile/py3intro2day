import collections

Person = collections.namedtuple('Person', 'first_name last_name')

print(Person)

p1 = Person('John', 'Doe')
p2 = Person('Henry','Will')

print(p1.first_name,p1.last_name)
print(p2.first_name,p2.last_name)


User = collections.namedtuple('User', 'user_id password uid gid full_name home_dir shell')

users = []

with open('../resources/py3jpmcadv/DATA/password.txt') as fh:
    for line in fh:
        if not line.startswith('#'):
            flds = line.strip().split(':')
            u = User(*flds)
            users.append(u)
## one liner for the above for loop logic.
    #users = [User( *line.strip().split(':')) for line in fh if not line.strtswith('#')]
for u in users:
    print(u.user_id, '->', u.full_name)

print(dir(u))
