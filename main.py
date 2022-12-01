# dictionary = {"a": 1, "b": 2, "c": 3}

# st = set([1, 2, 3, 4, 5])
# print(type(st))
# print(len(st))

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
fb = frozenset (b)

# c = a.intersection(b)
# c = a.union(b)
# c = a.difference(b)
# c = b.difference(a)
# c = a.symmetric_difference(b)
print(a)
a.intersection_update()
print(a)
