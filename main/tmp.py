def f(act, x, y):
    dic = {"+": lambda: x + y,
           "-": lambda: x - y,
           "*": lambda: x * y,
           "/": lambda: x / y,
           }

    return dic.get(act)()


print(f("+", 3, 2))
