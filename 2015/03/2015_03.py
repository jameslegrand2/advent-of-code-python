from collections import Counter

class Santa():
    def __init__(self):
        self.location = [0,0] #x,y
        self.houses_visited = ['0,0']
    
    def visit_house(self):
        locationstring = str(self.location[0]) + "," + str(self.location[1])
        self.houses_visited.append(locationstring)
    
    def move_north(self):
        self.location[1] += 1
        self.visit_house()

    def move_south(self):
        self.location[1] -= 1
        self.visit_house()

    def move_east(self):
        self.location[0] += 1
        self.visit_house()
    
    def move_west(self):
        self.location[0] -= 1
        self.visit_house()

try:
    inputfile = open('.\\2015\\03\\Input.txt','r')
    inputdata = inputfile.read()
    inputfile.close
except:
    print("Could not obtain input from file!")

#Part 1
santa1 = Santa()   
for move in inputdata:
    if move == '^':
        santa1.move_north()
    elif move == 'v':
        santa1.move_south()
    elif move == '>':
        santa1.move_east()
    elif move == '<':
        santa1.move_west()

distinct_houses1 = Counter(santa1.houses_visited)
total1 = len(distinct_houses1)

#Part2
santa2 = Santa()
robosanta = Santa()
turn = 0
for move in inputdata:
    if turn % 2 == 0: #santa's turn
        if move == '^':
            santa2.move_north()
        elif move == 'v':
            santa2.move_south()
        elif move == '>':
            santa2.move_east()
        elif move == '<':
            santa2.move_west()
    else: #robosanta's turn
        if move == '^':
            robosanta.move_north()
        elif move == 'v':
            robosanta.move_south()
        elif move == '>':
            robosanta.move_east()
        elif move == '<':
            robosanta.move_west()
    turn += 1

all_houses = santa2.houses_visited + robosanta.houses_visited
distinct_houses2 = Counter(all_houses)
total2 = len(distinct_houses2)

try:
    output = open('.\\2015\\03\\Output.txt','w')
    output.write(f"{total1}\n{total2}")
    output.close()
except:
    print("Could not write output file!")