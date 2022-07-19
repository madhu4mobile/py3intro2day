#!/usr/bin/python

with open("../../resources/py3jpmcadv/DATA/presidents.txt") as pres_in:
    count_of = {}
    for rec in pres_in:
        flds = rec.split(":")
        state = flds[9]
        # party = flds[9]
        if state in count_of:
            count_of[state] += 1
        else:
            count_of[state] = 1

        # if party in count_of:
        #     count_of[party] += 1
        # else:
        #     count_of[party] = 1

# for state, count in sorted(count_of.items()):
#     print("%-20s %2d" % (state, count))

for party, count in sorted(count_of.items()):

    party = party.replace("\n",'')
    print("%-25s %10d" % (party, count))
    # print(party,count)
