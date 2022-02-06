from itertools import product 

class Ingredient():
    def __init__(self,name,capacity,durability,flavor,texture,calories):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories

class Recepie():
    def __init__(self,ingredientsandamounts):
        self.ingredientsandamounts = ingredientsandamounts
        self.capacity = 0
        self.durability = 0
        self.flavor = 0
        self.texture = 0
        self.calories = 0
        self.score = 0
    
    def calculate_properties(self):
        for ingredient,amount in self.ingredientsandamounts:
            self.capacity += ingredient.capacity * amount
            self.durability += ingredient.durability * amount
            self.flavor += ingredient.flavor * amount
            self.texture += ingredient.texture * amount
            self.calories += ingredient.calories * amount
        if self.capacity < 0:
            self.capacity = 0
        if self.durability < 0:
            self.durability = 0
        if self.flavor < 0:
            self.flavor = 0
        if self.texture < 0:
            self.texture = 0
        if self.calories < 0:
            self.calories = 0

    def calculate_score(self):
        self.score = self.capacity * self.durability * self.flavor * self.texture
            
class Cookbook():
    def __init__(self):
        self.ingredients = []
        self.recepies = []
        self.teaspoons = 100
        self.max_score = 0
        self.max_score_500 = 0

    def make_recepies(self):    
        for amounts in product(range(self.teaspoons+1),repeat = len(self.ingredients)):
            if sum(amounts) == 100:
                ingredientsandamounts = []
                for key in range(len(amounts)):
                    ingredientsandamounts.append((self.ingredients[key],amounts[key]))
                self.recepies.append(Recepie(ingredientsandamounts))
    
    def calculate_recepie_scores(self):
        for recepie in self.recepies:
            recepie.calculate_properties()
            recepie.calculate_score()

    def calculate_max_score(self):
        for recepie in self.recepies:
            if recepie.score > self.max_score:
                self.max_score = recepie.score
            if recepie.score > self.max_score_500 and recepie.calories == 500:
                self.max_score_500 = recepie.score

try:
    inputfile = open('.\\2015\\15\\Input.txt','r')
    inputdata = inputfile.readlines()
    inputfile.close
except:
    print("Could not obtain input from file!")

cookbook = Cookbook()
for line in inputdata:
    words = line.replace('\n','').replace(',','').replace(':','').split()
    cookbook.ingredients.append(Ingredient(words[0],int(words[2]),int(words[4]),int(words[6]),int(words[8]),int(words[10])))
cookbook.make_recepies()
cookbook.calculate_recepie_scores()
cookbook.calculate_max_score()

try:
    output = open('.\\2015\\15\\Output.txt','w')
    output.write(f"{cookbook.max_score}\n{cookbook.max_score_500}")
    output.close()
except:
    print("Could not write output file!")
