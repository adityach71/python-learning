print(
    "Q1. Which planet is known as the Red Planet?\nA. Venus\nB. Mars\nC. Jupiter\nD. Saturn"
)

a = input("Enter your Option: ")


total = 0
prize = 3333333.34


valid = ["A", "B", "C", "D", "a", "b", "c", "d"]

if a not in valid:
    print("ARE YOU CRAZY??")
elif a.upper() == "B":
    print(f"✅ You have won ₹{prize:,}!")
    total += prize
else:
    print("❌ YOU HAVE LOOSED ₹3,333,333.34!")

print(
    "Q2. Who was the first Prime Minister of independent India?\nA. Mahatma Gandhi\nB. Jawaharlal Nehru\nC. Sardar Vallabhbhai Patel\nD. Subhas Chandra Bose"
)
b = input("Enter your Option: ")
if b not in valid:
    print("ARE YOU CRAZY??")
elif b.upper() == "B":
    print(f"✅ You have won ₹{prize:,}!")
    total += prize
else:
    print("❌ YOU HAVE LOOSED ₹3,333,333.34!")

print(
    "Q3. Which is the largest river in India by length?\nA. Ganga\nB. Brahmaputra\nC. Yamuna\nD. Godavari"
)
c = input("Enter your Option: ")
if c not in valid:
    print("ARE YOU CRAZY??")
elif c.upper() == "A":
    print(f"✅ You have won ₹{prize:,}!")
    total += prize
else:
    print("❌ YOU HAVE LOOSED ₹3,333,333.34!")

print(f"\n🏆 Game Over! Your total winnings are: ₹{total:,}")
