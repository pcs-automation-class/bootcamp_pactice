#list,
coordinates1a = [1, 2, 3, "candy", [11,22]]
coordinates = ["San Francisco", 37.7749, 122.4194]
fruits = ["banana", "apple", "mango", "cherry", "berry", "kiwi", "pear", "grapes"]
student = ["Alex", "Smith", 1995, 12, 25, 4]
print(type(fruits))
print(type(fruits[0]))
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[-1])
print(fruits[len(fruits)-1])
print(len(fruits))
fruits.append("pineapple")
print(fruits)
new_fruits = fruits   #new_fruits has more items
print(new_fruits)

for item in new_fruits:
    if item in fruits:
        print(item)
numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 121, 3333, 6000, 12000]
print(numbers)
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(numbers)

group_result = [True, True, True, False, True]   #if all students pass the exam
print(group_result)
print(len(group_result))
print(all(group_result)) #gives analogy of sum (if all true or all false)
print(any(group_result))

strings = ["aaa", "bbb", "ccc", "ddd", "eee", "fff"]
print(all(strings))
print(any(strings))
print(len(strings))


cars = ["toyota", "honda", "bmw", "mazda", "nissan", "chevy", "ford", "tesla", "buick", "audi", "mercedes"]
print(cars)
print(len(cars))
cars_by_country = [["toyota", "honda", "mazda"], ["bmw", "audi", "mercedes"], ["chevy", "ford", "tesla", "buick"]]
print(len(cars_by_country))
print(cars_by_country[0])
print(cars_by_country[0][1])
cars.reverse()
print(cars)

# tuple,
my_tuple = (1, )
# set,
my_set = (1, 2, 4, 6, )
# dictionary
my_dict = {"name": "Sam", "age": 23}
my_list = [1, 2, 3]

print(my_list)
print(my_set)
print(my_dict)
