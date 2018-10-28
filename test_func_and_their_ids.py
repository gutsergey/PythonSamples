def f(x):
    print("1.x=" + str(x))
    print(id(x))
    x = 2 * x
    print(id(x))
    print("2.x=" + str(x))
    return x

x = 1
print(id(x))
x = f(x + 1) + f(x + 2)
print(id(x))
