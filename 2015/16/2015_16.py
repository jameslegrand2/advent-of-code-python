class Gift():
    def __init__(self,children,cats,samoyeds,pomeranians,akitas,vizslas,goldfish,trees,cars,perfumes):
        self.children = children
        self.cats = cats
        self.samoyeds = samoyeds
        self.pomeranians = pomeranians
        self.akitas = akitas
        self.vizslas = vizslas
        self.goldfish = goldfish
        self.trees = trees
        self.cars = cars
        self.perfumes = perfumes
        self.gifter_original = None
        self.gifter_new = None

class Sue():
    def __init__(self,number,properties):
        self.number = number
        self.properties = properties

    def possible_gifter_original(self,gift):
        for property in self.properties:
            if property == 'children':
                if self.properties[property] != gift.children:
                    return False
            if property == 'cats':
                if self.properties[property] != gift.cats:
                    return False
            if property == 'samoyeds':
                if self.properties[property] != gift.samoyeds:
                    return False
            if property == 'pomeranians':
                if self.properties[property] != gift.pomeranians:
                    return False
            if property == 'akitas':
                if self.properties[property] != gift.akitas:
                    return False
            if property == 'vizslas':
                if self.properties[property] != gift.vizslas:
                    return False
            if property == 'goldfish':
                if self.properties[property] != gift.goldfish:
                    return False
            if property == 'trees':
                if self.properties[property] != gift.trees:
                    return False
            if property == 'cars':
                if self.properties[property] != gift.cars:
                    return False
            if property == 'perfumes':
                if self.properties[property] != gift.perfumes:
                    return False
        return True

    def possible_gifter_new(self,gift):
        for property in self.properties:
            if property == 'children':
                if self.properties[property] != gift.children:
                    return False
            if property == 'cats':
                if self.properties[property] <= gift.cats:
                    return False
            if property == 'samoyeds':
                if self.properties[property] != gift.samoyeds:
                    return False
            if property == 'pomeranians':
                if self.properties[property] >= gift.pomeranians:
                    return False
            if property == 'akitas':
                if self.properties[property] != gift.akitas:
                    return False
            if property == 'vizslas':
                if self.properties[property] != gift.vizslas:
                    return False
            if property == 'goldfish':
                if self.properties[property] >= gift.goldfish:
                    return False
            if property == 'trees':
                if self.properties[property] <= gift.trees:
                    return False
            if property == 'cars':
                if self.properties[property] != gift.cars:
                    return False
            if property == 'perfumes':
                if self.properties[property] != gift.perfumes:
                    return False
        return True

try:
    inputfile = open('.\\2015\\16\\Input.txt','r')
    inputdata = inputfile.readlines()
    inputfile.close
except:
    print("Could not obtain input from file!")

sues = []
for line in inputdata:
    words = line.replace('\n','').replace(',','').replace(':','').split()
    properties = {}
    for i in range(2,7,2):
        properties[words[i]] = int(words[i + 1])
    sues.append(Sue(int(words[1]),properties))

gift = Gift(3,7,2,3,0,0,5,3,2,1)
for sue in sues:
    if sue.possible_gifter_original(gift) == True:
        gift.gifter_original = sue.number
    if sue.possible_gifter_new(gift) == True:
        gift.gifter_new = sue.number

try:
    output = open('.\\2015\\16\\Output.txt','w')
    output.write(f"{gift.gifter_original}\n{gift.gifter_new}")
    output.close()
except:
    print("Could not write output file!")