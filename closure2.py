def f():
    x=0
    def g(x):
        x = x+2
        return x
    return g  # Return a closure.
