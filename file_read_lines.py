import urllib.request
try:
    i=0
    with open('example_text.txt', 'r') as file:
        for line in file:
            print(i)
            if i==0:
                i=i+1
                continue
            print(line.strip())
    i=0
    with open('example_text.txt', 'r') as file:
          for line in file:
            print(i)
            if i==0:
                print(line.strip())
                i=i+1
                break
                 

    url = " http://dfedorov.spb.ru/python/files/tutchev.txt"
    with urllib.request.urlopen(url) as webpage:
        for line in webpage:
            line = line.strip()
            line = line.decode('utf-8')
            print(line)
    url = " http://dfedorov.spb.ru/python/files/tutchev.txt"
    i=0
    with urllib.request.urlopen(url) as webpage:
        for line in webpage:
            if i==0:
                i=i+1
                continue
            line = line.strip()
            line = line.decode('utf-8')
            print(line)            
except:
    print ("Error opening file")	    
