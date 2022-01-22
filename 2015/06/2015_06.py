class Light():
    def __init__(self,x,y):
        self.lit = False
        self.position = (x,y)
        self.brightness = 0
    
    def turn_on(self):
        self.lit = True
    
    def turn_off(self):
        self.lit = False

    def toggle(self):
        self.lit = not self.lit
    
    def brighten(self,lumens=1):
        self.brightness += lumens

    def dim(self):
        if self.brightness > 0:
            self.brightness -= 1

def parse_instruction(string):
    words = string.replace('\n','').split()
    if words[0] == 'turn':
        if words[1] == 'on':
            instruction = 1
        else:
            instruction = -1
        coord1 = words[2]
        coord2 = words[4]
    else:
        instruction = 0
        coord1 = words[1]
        coord2 = words[3]
    x1y1 = coord1.split(",")
    x2y2 = coord2.split(",")
    return instruction,int(x1y1[0]),int(x1y1[1]),int(x2y2[0]),int(x2y2[1])

def run_instruction1(instruction,x1,y1,x2,y2):
    global lights
    for x in range(x1,x2 + 1):
        for y in range(y1,y2 + 1):
            if instruction == 1:
                lights[x][y].turn_on()
            elif instruction == -1:
                lights[x][y].turn_off()
            else:
                lights[x][y].toggle()

def run_instruction2(instruction,x1,y1,x2,y2):
    global lights
    for x in range(x1,x2 + 1):
        for y in range(y1,y2 + 1):
            if instruction == 1:
                lights[x][y].brighten()
            elif instruction == -1:
                lights[x][y].dim()
            else:
                lights[x][y].brighten(2)

try:
    inputfile = open('.\\2015\\06\\Input.txt','r')
    inputdata = inputfile.readlines()
    inputfile.close
except:
    print("Could not obtain input from file!")

#Part 1
lights = []
for x in range(1000):
    lights.append([])
    for y in range(1000):
        lights[x].append(Light(x,y))

for line in inputdata:
    instruction,x1,y1,x2,y2 = parse_instruction(line)
    run_instruction1(instruction,x1,y1,x2,y2)

total1 = 0
for x in range(1000):
    for y in range(1000):
        if lights[x][y].lit:
            total1 += 1

#part 2
lights = []
for x in range(1000):
    lights.append([])
    for y in range(1000):
        lights[x].append(Light(x,y))

for line in inputdata:
    instruction,x1,y1,x2,y2 = parse_instruction(line)
    run_instruction2(instruction,x1,y1,x2,y2)

total2 = 0
for x in range(1000):
    for y in range(1000):
        total2 += lights[x][y].brightness

try:
    output = open('.\\2015\\06\\Output.txt','w')
    output.write(f"{total1}\n{total2}")
    output.close()
except:
    print("Could not write output file!")