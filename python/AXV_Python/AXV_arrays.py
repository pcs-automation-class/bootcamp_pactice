# List - [] - square brackets
# lists are useful to store data if you need to work with it as one object.
# coordinates = ["San Francisco", 37.7749, 122.4194]
# new_list = list()
# new_list_2 = []
#
# #           0          1        2         3             4 <-- positive value - go left to right
# fruits = ["banana" , "apple", "mango", "strawberry", "carrot"]
# #          -5         -4       -3        -2            -1 <-- negative value - go from right to left
#
#
# student = ["Alex", "Jones", "1234", "2024"]
#
# print(fruits)
# print(type(fruits))
#
# # what if we want to print the first element?  Note first element in a list is 0
#
# print(fruits[-4])
#
# # if we want to print the number of elements in the list.  We'll use the len function
#
# print(len(fruits))
#
# # if we want to print the last element on the list
#
# print(fruits[len(fruits) -1])
#
# #Add values to the list
#
# fruits.append("Cherry")
# print(fruits)
#
# #use for loop
#
# good_for_salad = ["carrot", "mango", "melon"]
#
# for item in fruits:
#     if item in good_for_salad:
#         print(item)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, 100, 3333, 65745]
#
# print(numbers)
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))

# group_result = [False, True, False, False, False]
# print(group_result)
# print(all(group_result))
# print(any(group_result))

# group_result = [True, True, True, True, True]
# print(group_result)
# print(all(group_result))
# print(any(group_result))
#
# strings = ["", "", ""]
# print(all(strings))
# print(any(strings))
#
# cars = [["Toyota", "Honda"], ["BMW", "Mercedes", "Audi"], ["Chevy", "Ford", "Tesla", "Rivian","Buick"]]
# print(cars[1][0])
# print(len(cars[-2]))
# print(cars)
# cars.reverse()
# print(cars)

#lists are flexible

# Tuple

# Tuples are similar to lists, but they cannot be modified.
# Lists take a lot of computer memory
# Tuples can save computer memory

# tuple_example = (1, 2, "jdgfujedgfjed")
# print(tuple_example)
# print(type(tuple_example))
# coordinates = ("San Francisco", 37.7749, 122.4194)
# print(coordinates[1])
# print(coordinates[2])
# print(coordinates[0])

# cars = ("Honda", "Toyota")
# new_cars = list(cars)    # this converts tuple to a list
# new_cars.append("BMW")
# print(tuple(new_cars))   # this converts list to a tuple

# Set

# Sets may not necessarily be ordered.
# fruits = {"apple", "carrot", "banana", "cherry", "banana", "cherry", "apple", "strawberry"}
# print(fruits)

# log = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 3, 1, 0, 1, 1, 1, 4, 0, 4, 4, 4, 4, 4]
# unique = [] # <-- empty list
# for i in log:
#     if i not in unique:
#         unique.append(i)
# print(unique)
# print(set(log)) # <-- prints log as a set
#
# new_val = set(log)
# print(list(new_val)) # <-- prints log as a list
#
# new_val1 = tuple(log)
# print(tuple(new_val1))

# Only unique values are shown in the output

# Dictionary
# key:value
# item = {"A"}
# print(type(item))

students = {
    "Cities": ["San Francisco", "New York"],
    "State": "CA",
    "My state": "Texas",
    1: 12,
    2: 45,
    "states": {"CA": "California", "TX": "Texas", "MA": "Massachusetts", },
}

students["Name"] = "Andrey"
print(students.keys())
print(students.values())
print(students["states"]["TX"])
print(students["Cities"][0])

my_list = ["uhjdgfhjdgfhjdgf", "asdgy"]
my_tuple = (1,)

print(len(my_list))
print(len(my_tuple))

environments = {
    "dev": "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com",
    "prod": "https://linkmygear.com",
    "qa": "https://test:FjeKB9ySMzwvDUs2XACpfu@qa.linkmygear.com",
    "uat": "https://test:FjeKB9ySMzwvDUs2XACpfu@uat.linkmygear.com"
}
