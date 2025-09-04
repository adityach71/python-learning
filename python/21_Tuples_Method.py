countries = ("India", "USA", "Japan", "Brazil", "Australia")
temp = list(countries)
temp.append("Russia")
temp.pop(3)
temp[2] = "Finland"
countries = tuple(temp)
print(countries)


# Example number 2

countries = ("India", "USA", "Japan", "Brazil", "Australia")
countries2 = ("Vietnam", "Pakistan", "China")
southEastAsia = countries + countries2
print(southEastAsia)

# Example number 3

tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
# res = tuple1.count(3)
# res = tuple1.index(3)
# res = tuple1.index(3, 4, 8)
res = len(tuple1)
print("Count of 3 in tuple1 is:", res)
