s1 = [1, 2, 3, "kathan", 8.7, "8,754"]

s2 = [1, '4', 4.78, 1, 14, 'patel']

print("List 1 is:\n", s1)

print("List 2 is:\n", s2)

print("Appending list 2 to list 1 gives:")
s1.append(s2)
print(s1)

print("Extending list 2 to list 1 gives:")
s1.extend(s2)
print(s1)
