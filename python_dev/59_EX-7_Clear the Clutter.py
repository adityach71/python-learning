import os

def clearClutter(folder):
    files = os.listdir(folder)
    i = 1
    for file in files:
        file_ext = os.path.splitext(file)[1]
        new_name = f"{i}{file_ext}"
        old_path = os.path.join(folder, file)
        new_path = os.path.join(folder, new_name)
        os.rename(old_path, new_name)
        i += 1
        print("✅ Clutter cleared and files renamed successfully!")

if __name__ == "__main__":
    folder = "C:\\Users\\aditya\\Desktop\\clutter"
    clearClutter(folder)