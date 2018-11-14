def dispatch_dic(operator, x, y):
    return {
            'add': lambda:
                            x + y,
            'sub': lambda: x - y,
            'mul': lambda: x * y,
            'div': lambda: x / y
            }.get(operator, lambda: None)()

ww = dispatch_dic('add', 2, 3)
print (ww)
