
print(2 == 3)
print(2 == 2 and 3 > 9)
print([2, 3] == [3, 2])
print([2, 3] == [2, 2])
print([2, 3] == [2, 3])

x = -1.789
y = -1.7890000001
eps = 1.e-15

if abs(x-y) <= eps*abs(y):
    print("YES")
else:
    print("NOPE")


