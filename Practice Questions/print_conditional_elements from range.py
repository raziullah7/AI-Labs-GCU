# using ranged loop
# for i in range(1, 1001):
#     if i % 3 == 0 and i % 5 == 0:
#         count += 1
#         print(i)
# print(f"\nCount: {count}")


# using List Comprehension
theList = [i for i in range(1, 1001) if i%3 == 0 and i%5 == 0]
print(sum(theList))

