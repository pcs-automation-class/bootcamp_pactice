def kilometers_to_miles(kilometers):
  return kilometers * 0.621371

while True:
  try:
    kilometers = float(input("Enter the distance in kilometers (or type 'exit' to quit): "))
    miles = kilometers_to_miles(kilometers)
    print(f"{kilometers} kilometers is equal to {miles:.2f} miles.")
  except ValueError:
    print("Exiting the program. Goodbye!")
    break

print('********************')


def miles_to_kilometers(miles):
  return miles * 1.60934

mile_values = [10, 25, 50, 100]

for miles in mile_values:
  kilometers = miles_to_kilometers(miles)
  print("{} miles is equal to {:.2f} kilometers.".format(miles, kilometers))

# for x in ['onion','potato','cucumber','tomato','pumpkin']:
#
#     if x == 'cherry':
#         break
#     else:
#         if x == 'cucumber':
#             continue
#         print(x)
# print('***************')
#
# veggie = ['onion','potato','cucumber','tomato','pumpkin']
# for x in veggie:
#     print(x)
# print('***************')
#
# for x in "12345":
#     if x == '3':
#         break
#     print(x)
# print('***************')
#
# for x in range(0, 10, 3):
#     print(x)
# print('***************')
#
# for x in range(2, 5,):
#     print(x)
# else:
#     print("Finally finished!")
#     print('***************')
#
# color = ['red','white','yellow','green','blue','black']
# car = ['toyota', 'bmw','audi', 'ford']
# for x in color:
#     for y in car:
#         print(x,y)
#     print('***************')
#
# i = 1
# while i <= 5:
#   print(i)
#   i += 1
# print('***************')
#
# i = 1
# while i < 10:
#   print(i)
#   i += 1
#   if i == 2:
#     break
# print(i)
# print('***************')


