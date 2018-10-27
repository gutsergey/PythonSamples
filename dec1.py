def bold(fun_hello):
    def inner(who):
        print ("<b>")
        fun_hello(who)
        print ("</b>")
    return inner
def italic(fun_hello):
    def inner(who):
        print ("<i>")
        fun_hello(who)
        print ("</i>")
    return inner
@italic
@bold
def hello(who):
    print ("Hello", who)
