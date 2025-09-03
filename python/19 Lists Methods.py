l = [1, 2, 3,4 ,5 ,6 ,7 ,8 ,9,2]
# print(l)
# l.append(7)
# l.sort(reverse=True)
# l.revers()
# print(l.count(2))
# m = l.copy()
# m[0] = 0
# l.insert(1, 899)
m = [900, 1000, 1100]
k = l + m
l.extend(m)
print(l)