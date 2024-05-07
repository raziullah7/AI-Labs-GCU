s1 = "ABCDEF"

## Approach 1 (range)
s2 = s1[::-1]
# print(s2)

## Approach 2 ("".join(reversed())
# reversed() returns an iterator that reads back from the original
# string hence altering it
s3 = s1
s3 = "".join(reversed(s3))
# print(s3)

## Approach 3 (iterate through the iterator that reversed() returns)
s4 = s1
finalStr = ""
myIterator = reversed(s4)
for chararcter in myIterator:
    finalStr += chararcter
print(finalStr)