# Reading a file

# f = open('myfile.txt', 'r') #the read mode is default
# # print(f)
# text = f.read()
# print(text)
# f.close()

# Writing a file

f = open('myfile.txt', "w")
f.write('Hello, World!')
f.close()

with open('myfile.txt', 'a')as f:
    f.write("Hey I am inside with")