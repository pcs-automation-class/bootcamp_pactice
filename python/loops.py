from email.utils import make_msgid

my_list = []
s = "andreybaykov"

for char in s:
    if char != 'a':
        my_list.append(char + '!')
print(my_list)


my_list2 = [char + '!' for char in s if char != 'a']
print(my_list2)


list_cars = [['Toyota', 2024, 4], ['Audi', 2015, 2], ['BMW', 2020, 4], ['Tesla', 2019, 4]]

new_car_list = []

# for car in list_cars:
#     if car[1] >= 2020:
#         new_car_list.append(car[0])

for make, year, _ in list_cars:
    if year >= 2020:
        new_car_list.append(make)

print(new_car_list)

new_car_list2 = [make for make, year, _ in list_cars if year >= 2020]
print(new_car_list2)

# for _ in range(10):
#     print("Hello!")


print(s[:2])
