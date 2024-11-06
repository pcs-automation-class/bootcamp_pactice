tuple_example = (1, 2, 3, 4, 5, "bbb")
print(tuple_example)
coordinates = ("San Francisco", 37.7749, 122.4194)
print(coordinates)
print(type(coordinates))
print(coordinates[0])
print(coordinates[1])
print(coordinates[2])

cars_tuple = ("toyota", "honda", "bmw", "mazda", "nissan", "chevy", "ford", "tesla", "buick", "audi", "mercedes")

cars_tuple = list(cars_tuple)  #we convert tuple into list, can add items and then convert it back to tuple

cars_tuple.append("bicycle")
print(tuple(cars_tuple))


