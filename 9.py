s = set()
# print(type(s))
# l = {1, 2, 3, 4}
# s_from_list = set(l)
# s_from_list = {1, 2, 3, 4}
# print(s_from_list)
# print(type(s_from_list))
s.add(1)
s.add(1)
s.add(2)
s1 = s.union({1,5})
s2 = s.intersection({1, 7, 2})
print(s, s1, s2)