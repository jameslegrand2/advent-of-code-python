from itertools import permutations

class Attendee():
    def __init__(self,name):
        self.name = name
        self.happiness_modifiers = {}

    def set_happiness_modifier(self,neighborname,amount):
        self.happiness_modifiers[neighborname] = amount

    def get_happiness_modifier(self,neighborname):
        return self.happiness_modifiers[neighborname]

class Arrangement():
    def __init__(self,attendeetuple):
        self.name = ''
        for attendee in attendeetuple:
            self.name += attendee
        self.attendeeorder = attendeetuple
        self.totalhappiness = 0

    def calculate_happiness(self,table):
        for key in range(len(self.attendeeorder)):
            attendee1name = self.attendeeorder[key]
            attendee2name = self.attendeeorder[key-1]
            self.totalhappiness += table.attendees[attendee1name].get_happiness_modifier(attendee2name)
            self.totalhappiness += table.attendees[attendee2name].get_happiness_modifier(attendee1name)
        return self.totalhappiness

class Table():
    def __init__(self):
        self.attendees = {}
        self.arrangements = {}
        self.arrangementhappinessindex = {}

    def add_attendee(self,attendee):
        if attendee.name not in self.attendees:
            self.attendees[attendee.name] = attendee
        return self.attendees[attendee.name]

    def add_arrangement(self,arrangement):
        self.arrangements[arrangement.name] = arrangement

    def calculate_arrangement_happinesindex(self):
        for arrangementname in self.arrangements:
            self.arrangementhappinessindex[arrangementname] = self.arrangements[arrangementname].calculate_happiness(self)

try:
    inputfile = open('.\\2015\\13\\Input.txt','r')
    inputdata = inputfile.readlines()
    inputfile.close
except:
    print("Could not obtain input from file!")

table1 = Table()
for line in inputdata:
    words = line.replace('\n','').split()
    attendee1 = Attendee(words[0])
    attendee2 = Attendee(words[10].replace('.',''))
    if words[2] == 'gain':
        happiness_modifier = int(words[3])
    elif words [2] == 'lose':
        happiness_modifier = -int(words[3])
    attendee1 = table1.add_attendee(attendee1)
    attendee2 = table1.add_attendee(attendee2)
    attendee1.set_happiness_modifier(attendee2.name,happiness_modifier)

for attendeetuple in list(permutations(table1.attendees)):
    arrangement = Arrangement(attendeetuple)
    table1.add_arrangement(arrangement)

table1.calculate_arrangement_happinesindex()
maxhappiness1 = max(table1.arrangementhappinessindex.values())

table2 = Table()
for line in inputdata:
    words = line.replace('\n','').split()
    attendee1 = Attendee(words[0])
    attendee2 = Attendee(words[10].replace('.',''))
    if words[2] == 'gain':
        happiness_modifier = int(words[3])
    elif words [2] == 'lose':
        happiness_modifier = -int(words[3])
    attendee1 = table2.add_attendee(attendee1)
    attendee2 = table2.add_attendee(attendee2)
    attendee1.set_happiness_modifier(attendee2.name,happiness_modifier)
me = Attendee('me')
me = table2.add_attendee(me)
for attendeename in table2.attendees:
    if attendeename != 'me':
        me.set_happiness_modifier(attendeename,0)
        table2.attendees[attendeename].set_happiness_modifier(me.name,0)

for attendeetuple in list(permutations(table2.attendees)):
    arrangement = Arrangement(attendeetuple)
    table2.add_arrangement(arrangement)

table2.calculate_arrangement_happinesindex()
maxhappiness2 = max(table2.arrangementhappinessindex.values())

try:
    output = open('.\\2015\\13\\Output.txt','w')
    output.write(f"{maxhappiness1}\n{maxhappiness2}")
    output.close()
except:
    print("Could not write output file!")
