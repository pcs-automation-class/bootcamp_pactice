#list
coordinates = [1, 2, 3]
fruits = ["banana", "apple", "mango"]

print(fruits[2])
print(type(fruits))
print(fruits[len(fruits)-1])
print(fruits[-1])

fruits.append("orange")

for items in fruits:
    print(items)
good_for_salad = ["carrot", "mango", "melon"]

for item in fruits:
    if item in good_for_salad:
        print(item)
#
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, 100, 3333, 65745]

print(numbers)
print(max(numbers))
print(min(numbers))
print(sum(numbers))

group_result = [False, True, False, False, False]
print(group_result)
print(all(group_result))
print(any(group_result))

strings = ["", "", ""]
print(all(strings))
print(any(strings))

cars = [["Toyota", "Honda"], ["BMW", "Mercedes", "Audi"], ["Chevy", "Ford", "Tesla", "Rivian"]]
print(cars[2][-1])
print(len(cars[2]))
print(cars)
cars.reverse()
print(cars)

#Tuple
tuple_example = (1, 2, "jdgfujedgfjed")
print(tuple_example)
print(type(tuple_example))
coordinates = ("San Francisco", 37.7749, 122.4194)
print(coordinates[1])

cars = ("Honda", "Toyota")
new_cars = list(cars)
new_cars.append("BMW")
print(tuple(new_cars))


#Set
fruits = {"apple", "carrot", "banana", "cherry", "banana", "cherry"}
print(fruits)
log = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 3, 1, 0, 1, 1, 1, 4, 0, 4, 4, 4, 4, 4]
unique = []
for i in log:
    if i not in unique:
        unique.append(i)
print(unique)

new_val = set(log)
print(list(new_val))

#Dictionary
key:value
item = {"A"}
print(type(item))

students = {
    "Cities": ["San Francisco", "New York"],
    "State": "CA",
    "My state": "Texas",
    1: 12,
    2: 45,
    "states": {"CA": "California", "TX": "Texas", "MA": "Massachusetts",},
}

students["Name"] = "Andrey"
print(students.keys())
print(students.values())
print(students["states"]["TX"])
print(students["Cities"][0])

my_list = ["uhjdgfhjdgfhjdgf"]
my_tuple = (1, )

print(len(my_list))
#
environments = {
    "dev": "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com",
    "prod": "https://linkmygear.com",
    "qa": "https://test:FjeKB9ySMzwvDUs2XACpfu@qa.linkmygear.com",
    "uat": "https://test:FjeKB9ySMzwvDUs2XACpfu@uat.linkmygear.com"}

