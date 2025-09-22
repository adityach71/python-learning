s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
print(s1.union(s2))
s1.update(s2)
print(s1,s2)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection_update(cities2)
print(cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference_update(cities2)
print(cities3)

cities = {"Tokyo2", "Madrid2", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))

cities = {"Tokyo2", "Madrid2", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.issuperset(cities2))

cities = {"Tokyo2", "Madrid2", "Berlin", "Delhi"}
cities.add("Parish")
print(cities)

cities = {"Tokyo2", "Madrid2", "Berlin", "Delhi"}
cities.update("Parish", "Nayak")
print(cities)

cities = {"Tokyo2", "Madrid2", "Berlin", "Delhi"}
cities.discard("Tokyo2")
print(cities)

cities = {"Tokyo2", "Madrid2", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)