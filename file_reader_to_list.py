try:
    #  получить список, состоящий из строк
    with open('example_text.txt', 'r') as file:
        lines = file.readlines()
    print(lines)
except:
    print ("Error opening file")

