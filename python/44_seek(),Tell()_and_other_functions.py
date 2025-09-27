# with open('file.txt', 'r') as f:
#     print(type(f))
#     f.seek(10)

#     data = f.read(5)
#     print(data)
#     print(f.tell())

with open('sample.txt', 'w') as f:
    f.write("Hello World!")
    f.truncate(5)

with open('sample.txt', 'r') as f:
    print(f.read())