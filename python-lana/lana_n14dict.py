#Dictionary
students00 = dict()
student1 = {
    "name":"John", "lastname": "Smith", "age": 21, "city": "San Francisco", "state": "CA", "country": "USA"
}
print(student1)
print(student1["name"])
print(student1["city"])
print(student1.keys())
print(student1.values())
print(student1.items())

student2 = {
    "name":"Jack",
    "lastname": "Frost",
    "age": 22,
    "city": "Los Angeles",
    "states": {"CA": "California", "TX": "Texas"},
    "country": "USA" }

print(student2)
print(student2["name"])
print(student2["city"])
print(student2["states"])
print(student2["states"]["CA"])
environments = {
    "dev": "dev.url.com",
    "stage": "stg.url.com",
    "uat": "uat.url.com",
    "prod": "url.com" }

