l = [2, 3, 5, 45, 7, 9, 11]
print(l)

l.append(7)
print(l)

l.sort(reverse = True)
print(l)

l.reverse()
print(l)

print(l.index(5))
print(l.count(7))

m = l.copy()
m[0] = 0
print(m)

l.insert(1, 56) 
print(l)

m = [34, 65,52]
l.extend(m)
print(l)

k = l + m # concatenate two lists to join to list
print(k)