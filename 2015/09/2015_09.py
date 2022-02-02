from itertools import permutations

class City():
    def __init__(self,name):
        self.name = name
        self.destinations = {}

    def add_destination(self,destinationname,distance):
        self.destinations[destinationname] = distance

    def distance_to_destination(self, destinationname):
        return self.destinations[destinationname]

    def __str__(self):
        return self.name

class Route():
    def __init__(self,routetuple):
        self.name = ''
        for city in routetuple:
            self.name += city
        self.route = routetuple
        self.total_distance = 0
        
    def calculate_distance(self,map):
        departurecityname = self.route[0]
        for arrivalcitykey in range(1,len(self.route)):
            arrivalcityname = self.route[arrivalcitykey]
            departurecity = map.cities[departurecityname]
            arrivalcity = map.cities[arrivalcityname]
            self.total_distance += departurecity.distance_to_destination(arrivalcityname)
            departurecityname = arrivalcityname

class Map():
    def __init__(self):
        self.cities = {}
        self.routes = {}

    def add_city(self,city):
        if city.name not in self.cities:
            self.cities[city.name] = city
            return city
        else:
            return self.cities[city.name]

try:
    inputfile = open('.\\2015\\09\\Input.txt','r')
    inputdata = inputfile.readlines()
    inputfile.close
except:
    print("Could not obtain input from file!")

map = Map()
for line in inputdata:
    words = line.replace('\n','').split()
    city1 = City(words[0])
    city2 = City(words[2])
    city1 = map.add_city(city1)
    city2 = map.add_city(city2)
    distance = int(words[4])
    city1.add_destination(city2.name,distance)
    city2.add_destination(city1.name,distance)

for routetuple in list(permutations(map.cities)):
    route = Route(routetuple)
    route.calculate_distance(map)
    map.routes[route.name] = route.total_distance

shortestdistance = min(map.routes.values())
longestdistance = max(map.routes.values())

try:
    output = open('.\\2015\\09\\Output.txt','w')
    output.write(f"{shortestdistance}\n{longestdistance}")
    output.close()
except:
    print("Could not write output file!")