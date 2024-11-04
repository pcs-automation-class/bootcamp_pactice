#dry = do not repeat yourself
#functions

def print_result(number):
    print(number)
    print('********')

one = int(input("Enter a number: "))
two = int(input("Enter a number again: "))

result = one + two
print_result(result)

result = one - two
print_result(result)

result = one * two
print_result(result)

result = one / two
print_result(result)