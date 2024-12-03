string = "abbdeabcc"

result = {}

for char in string:
    if char not in result.keys():
        result[char] = 0
    result[char] += 1

print(result)
