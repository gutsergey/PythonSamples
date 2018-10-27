try:
    file = open('lexample_text.txt', 'r')
    contents = file.read()
    print(contents)
except:
    print ("Error opening file");
else:
    file.close()
    print ('(Очистка: Закрытие файла)')
finally:
    print("Выполняется всегда и в последнюю очередь!")    

