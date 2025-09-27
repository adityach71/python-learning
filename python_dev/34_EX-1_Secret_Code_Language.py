import random
import string

def random_string(length=3):
    # Generates a random string of given length (letters only)
    letters = string.ascii_letters  # a-zA-Z
    return ''.join(random.choice(letters) for _ in range(length))

st = input("Enter Message: ")
coding = input("1 for Coding or 0 for Decoding: ")
coding = True if (coding=="1") else False
words = st.split()
nwords = []

if coding:
    r1 = random_string(3)
    r2 = random_string(3)
    print(f"(Random Prefix: {r1}, Random Suffix: {r2})")  # Optional: show for decoding
    for word in words:
        if len(word) >= 3:
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
else:  # decoding
    r1 = input("Enter the prefix used during coding: ")
    r2 = input("Enter the suffix used during coding: ")
    for word in words:
        if len(word) >= 6 and word.startswith(r1) and word.endswith(r2):
            stnew = word[len(r1):-len(r2)]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])

print(" ".join(nwords))
