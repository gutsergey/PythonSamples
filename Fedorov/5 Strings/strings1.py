def strings1():
    a = "qwerty"
    b = 'qwerty123'
    c = '''comment1
text1
text2
text3

---- text 4 end of comment1-------
'''
    d = """comment 2
text 1
text2

text3

----- end of comment 2 ---------
'''
"""
    e = " somebody says: 'Hello' "
    f = ' somebody says: "Hello" '

    print (a)
    print (b)
    print (c)
    print (d)
    print (e)
    print (f)

    print("type of variable f:", type(f))
    
    print('''
escape sequences

\\n - переход на новую строку
\\t - знак табуляции
\\\\ - наклонная черта влево
\\' - символ одиночной кавычки
\\" - символ двойной кавычки

''')
    import sys
    print ("Hello", " ", 'World', "!", sep=' ', end='\n', file=sys.stdout, flush=False)
    print ("Hello", " ", 'World', "!", sep='-', end='*\n', file=sys.stdout, flush=False)
    print ("------");

    
