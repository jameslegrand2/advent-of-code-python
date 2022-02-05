class Reindeer():
    def __init__(self,name,speed,flyingduration,restduration):
        self.name = name
        self.speed = speed
        self.flyingduration = flyingduration
        self.restduration = restduration
        self.flying = True
        self.timeremaininginstate = flyingduration
        self.distance = 0
        self.score = 0

    def one_second_action(self):
        if self.flying and self.timeremaininginstate > 0:
            self.distance += self.speed
            self.timeremaininginstate -= 1
        elif self.flying and self.timeremaininginstate == 0:
            self.flying = False
            self.timeremaininginstate = self.restduration - 1
        elif not self.flying and self.timeremaininginstate > 0:
            self.timeremaininginstate -= 1
        elif not self.flying and self.timeremaininginstate == 0:
            self.flying = True
            self.distance += self.speed
            self.timeremaininginstate = self.flyingduration - 1

class Race():
    def __init__(self):
        self.reindeers = []
        self.duration = 2503
        self.leader_distance = 0
        self.max_score = 0

    def calculate_leader_distance(self):
        for reindeer in self.reindeers:
            if reindeer.distance > self.leader_distance:
                self.leader_distance = reindeer.distance

    def award_points(self):
        for reindeer in self.reindeers:
            if reindeer.distance == self.leader_distance:
                reindeer.score += 1

    def calculate_max_score(self):
        for reindeer in self.reindeers:
            if reindeer.score > self.max_score:
                self.max_score = reindeer.score
    
    def run_one_second(self):
        for reindeer in self.reindeers:
            reindeer.one_second_action()
        self.calculate_leader_distance()
        self.award_points()

    def run(self):
        while self.duration > 0:
            self.run_one_second()
            self.duration -= 1
        self.calculate_max_score()

try:
    inputfile = open('.\\2015\\14\\Input.txt','r')
    inputdata = inputfile.readlines()
    inputfile.close
except:
    print("Could not obtain input from file!")

race = Race()
for line in inputdata:
    words = line.replace('\n','').split()
    race.reindeers.append(Reindeer(words[0],int(words[3]),int(words[6]),int(words[13])))
race.run()

try:
    output = open('.\\2015\\14\\Output.txt','w')
    output.write(f"{race.leader_distance}\n{race.max_score}")
    output.close()
except:
    print("Could not write output file!")

        