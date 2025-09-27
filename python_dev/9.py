# Strings are immutable
a = "Aditya?????????"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("?"))
print(a.replace("Aditya", "John"))
print(a.split(" "))
blogHeading = "introdustion to js"
print(blogHeading.capitalize())
str1 = "Welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50)))
print(a.count("?"))

print((str1.endswith("!!!")))

str1 = "He's name is Dan. He is an honest man"
# print(str1.index("ishh"))
str1 = "We wish you a Merry Chrismas\n"
print(str1.isprintable())
str1 = "            "
print(str1.isspace())
str2 = "   "
print(str2.isspace())

str1 = "Word Health Organization"
print(str1.istitle())
str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "His name is Dan. Dan is an honest man."
print(str1.title())  # v.important
