from operator import itemgetter

listOfTuples = [
    ("Razi", 22),
    ("Javaid", 24),
    ("Mozam", 23),
    ("Taha", 21),
]

print(listOfTuples)
print()

# alters the original list and returns nothing
# sortedList1 = listOfTuples.sort(key=lambda x: x[1])
# print(sortedList1)
# print()

# creates a new sorted list and returns it
sortedList2 = sorted(listOfTuples, key=itemgetter(1))
print(sortedList2)
print()