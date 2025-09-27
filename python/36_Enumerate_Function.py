marks = [12,56,32,98,12,45,1,4]
index = 0
for mark in marks:
    if index == 3:
        print(mark,"Harry is good")
    else:
        print(mark)
    index += 1


for index, mark in enumerate(marks, start=1):
    if(index == 4):
        print(mark,"Harry is good")
    else:
        print(mark)
