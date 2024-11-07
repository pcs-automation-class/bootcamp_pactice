#Set   Set does not have duplicates!!!!!
fruits_set = {"apple", "cherry", "banana", "grapes", "pear"}
print(fruits_set)

#set is printed not in the order
logging = [0,0,0,0,0,0,0,0,1,1,0,3,0,0,1,0,0,0,0,0,0,0,1,0,0,0,4,0,0,0,0,0,1]
#what unique values do we have here?
unique = []
for i in logging:
    if i not in unique:
        unique.append(i)


print(unique)
print(set(logging))
new_unique_list = set(logging)
print(list(new_unique_list))
