def kn(a):
    def inner(): # замыкание не использует аргументов
        return a + 5 # но использует внешний параметр kn()
    return inner #
