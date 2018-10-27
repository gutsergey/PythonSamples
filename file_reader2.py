try:
    # менеджер контекста:(инструкцию with), не требует ручного освобождения ресурсов
    with open('example_text.txt', 'r') as file:
        contents = file.read()
    print(contents)
except:
    print ("Error opening file")

