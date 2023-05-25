p = "hello how are you"
d = {}
for ch in p:
    if d.keys().__contains__(ch):
        d[ch] += 1
    else:
        d[ch] = 1
print(d)

# Duplicates

for x, y in d.items():
    if(y>1):
        print(x, end=" ")
print()

# Unique

for x, y in d.items():
    if y == 1:
        print(x, end=" ")


