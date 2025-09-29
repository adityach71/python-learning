def shoutouts(filename):
    try:
        with open(filename, "r") as f:
            names = f.readlines()
        for name in names:
            name = name.strip()
            if name:
                print(f"Shoutout to {name} 🎉")
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please create it and add names.")

if __name__ == "__main__":
    shoutouts("python_dev/names.txt")
