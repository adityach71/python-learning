dic = {
    "Harry": "Human being",
    "Spoon": "Object"
}
print(dic["Harry"])

info = {'name': 'Karan', 'age':19, 'eligible':True}
print(info)
print(info['name'])
print(info.get('name'))
print(info.keys())
print(info.values()) # this and the down forin loop are doing a same work
for key in info.key():
    print(info[key])
for key in info.key():
    print(f"The value corresponding to the key {key} is {info[key]}")

print(info.items())
for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")