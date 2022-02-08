from itertools import count


class Light():
    def __init__(self,position,initial_state):
        self.position = position
        self.current_state = initial_state
        self.next_state = None

    def change_state(self):
        self.current_state = self.next_state
        self.next_state = None

    def __str__(self):
        if self.current_state == True:
            return '#'
        else:
            return '.'

class Grid():
    def __init__(self,inputdata):
        self.lights = []
        for x in range(len(inputdata)):
            line = inputdata[x].replace('\n','')
            self.lights.append([])
            for y in range(len(line)):
                char = line[y]
                if char == '#':
                    initial_state = True
                elif char == '.':
                    initial_state = False
                self.lights[x].append(Light((x,y),initial_state))

    def calculate_next_states(self):
        for x in range(len(self.lights)):
            for y in range(len(self.lights[x])):
                light = self.lights[x][y]
                possible_neighbors = {'1': (x-1,y-1), '2':(x-1,y), '3': (x-1,y+1), '4': (x,y-1), '6': (x,y+1), '7': (x+1,y-1), '8': (x+1,y), '9': (x+1,y+1)}
                if x == 0:
                    del possible_neighbors['1']
                    del possible_neighbors['2']
                    del possible_neighbors['3']
                    if y == 0:
                        del possible_neighbors['4']
                        del possible_neighbors['7']
                    elif y == len(self.lights[x]) - 1:
                        del possible_neighbors['6']
                        del possible_neighbors['9']
                elif x == len(self.lights) - 1:
                    del possible_neighbors['7']
                    del possible_neighbors['8']
                    del possible_neighbors['9']
                    if y == 0:
                        del possible_neighbors['1']
                        del possible_neighbors['4']
                    elif y == len(self.lights[x]) - 1:
                        del possible_neighbors['3']
                        del possible_neighbors['6']
                else:
                    if y == 0:
                        del possible_neighbors['1']
                        del possible_neighbors['4']
                        del possible_neighbors['7']
                    elif y == len(self.lights[x]) - 1:
                        del possible_neighbors['3']
                        del possible_neighbors['6']
                        del possible_neighbors['9']
                
                neighbors_on = 0
                for key in possible_neighbors:
                    neighborx,neighbory = possible_neighbors[key]
                    if self.lights[neighborx][neighbory].current_state == True:
                        neighbors_on += 1
                        
                if light.current_state == True:
                    if neighbors_on == 2 or neighbors_on == 3:
                        light.next_state = True
                    else:
                        light.next_state = False
                else:
                    if neighbors_on == 3:
                        light.next_state = True
                    else:
                        light.next_state = False

    def reset_four_corners(self):
        self.lights[0][0].current_state = True
        self.lights[0][-1].current_state = True
        self.lights[-1][0].current_state = True
        self.lights[-1][-1].current_state = True

    def change_states(self):
        for x in range(len(self.lights)):
            for y in range(len(self.lights[x])):
                self.lights[x][y].change_state()

    def count_on(self):
        count = 0
        for x in range(len(self.lights)):
            for y in range(len(self.lights[x])):
                if self.lights[x][y].current_state == True:
                    count += 1
        return count

    def __str__(self):
        output = ''
        for x in range(len(self.lights)):
            for y in range(len(self.lights[x])):
                output += str(self.lights[x][y])
            output += '\n'
        return output

try:
    inputfile = open('.\\2015\\18\\Input.txt','r')
    inputdata = inputfile.readlines()
    inputfile.close
except:
    print("Could not obtain input from file!")

grid = Grid(inputdata)
for step in range(100):
    grid.calculate_next_states()
    grid.change_states()
count1 = grid.count_on()

grid = Grid(inputdata)
for step in range(100):
    grid.reset_four_corners()
    grid.calculate_next_states()
    grid.change_states()
grid.reset_four_corners()
count2 = grid.count_on()

try:
    output = open('.\\2015\\18\\Output.txt','w')
    output.write(f"{count1}\n{count2}")
    output.close()
except:
    print("Could not write output file!")