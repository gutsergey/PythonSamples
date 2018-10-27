try:
    with open('planets.txt', 'r') as file:
        planets = file.readlines()
    print(planets)
    for planet in reversed(planets):
        print(planet.strip())


    with open('planets.txt', 'r') as file:
        for line in file:
            print(line)
            print(len(line.strip()))        
except:
    print ("Error opening file")

