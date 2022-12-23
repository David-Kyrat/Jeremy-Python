list1 = []

def f(x):
    return x if (x % 2) == 0 else None

list2 = [f(i) for i in range(0, 10, 2)]


for i in range(10):
    list1.append(f(i))


print(list1 == list2)

print("\n", list1)
print("\n", list2)


