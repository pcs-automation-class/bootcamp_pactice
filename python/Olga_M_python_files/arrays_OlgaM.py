# List
coordinates = ["San Francisco", 37.7749, 122.4194]
new_list = list()

#             0        1         2
fruits = ["banana", "apple", "mango"]
#            - 3      -2        -1
student = ["Alex", "Doe", 1234, 2024]

print(fruits)
# print(fruits[-1])
# print(len(fruits))
# print(type(fruits))

fruits.append("carrot")
print(fruits)

good_for_salad = ["carrot", "mango", "melon"]

for item in fruits:
    if item in good_for_salad:
        print(item)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, 100, 3333, 65745]

print(numbers)
print(max(numbers))
print(min(numbers))
print(sum(numbers))

group_result = [False, True, False, False, False]
print(group_result)



# Dictionary
# Tuple
# Set
