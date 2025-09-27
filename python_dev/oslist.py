import os
folders = os.listdir("data")
os.chdir("/Users")
print(os.getcwd())

for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))