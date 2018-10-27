import time
def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print ("Время выполнения функции: %f" % (time.time()-t))
        return res
    return tmp
# декоратор, выполняющий задержку переданной функции на 1 секунду
def pause(f):
    def tmp(*args, **kwargs):
        time.sleep(1)
        return f(*args, **kwargs)
    return tmp

@timer
@pause
def func(x, y):
	return x + y
