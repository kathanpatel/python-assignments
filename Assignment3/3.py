l = [1, 2, 'kathan', 'patel', [3, ['hello world'], 4], ]
print("l =", l)

d = {"1": 'pyhton', "2": 'java', "3": 'c++'}

l.append(d)
print(" l with d ", l)
for x in l:
    if type(x) == dict:
        print("keys", d.keys())
        print("values", d.values())
