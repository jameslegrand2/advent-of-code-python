class Fighter():
    def __init__(self):
        self.name = ''
        self.initialhp = 0
        self.damage = 0
        self.armor = 0
        self.current_hp = self.initialhp

    def take_damage(self,damage):
        self.current_hp -= damage

    def is_alive(self):
        if self.current_hp > 0:
            return True
        else:
            return False

class Boss(Fighter):
    def __init__(self,initialhp,damage,armor):
        super().__init__()
        self.name = 'Boss'
        self.initialhp = initialhp
        self.damage = damage
        self.armor = armor
        self.current_hp = self.initialhp

class Player(Fighter):
    def __init__(self,initialhp):
        super().__init__()
        self.name = 'Player'
        self.initialhp = initialhp
        self.current_hp = self.initialhp
        self.weapon = None
        self.armoritem = None
        self.rings = None
        self.loadout_cost = 0

    def calculate_properties(self):
        self.damage += self.weapon.damage
        self.armor += self.weapon.armor
        self.loadout_cost += self.weapon.cost
        if self.armoritem is not None:
            self.damage += self.armoritem.damage
            self.armor += self.armoritem.armor
            self.loadout_cost += self.armoritem.cost
        if self.rings[0] is not None:
            self.damage += self.rings[0].damage
            self.armor += self.rings[0].armor
            self.loadout_cost += self.rings[0].cost
        if self.rings[1] is not None:
            self.damage += self.rings[1].damage
            self.armor += self.rings[1].armor
            self.loadout_cost += self.rings[1].cost

    def equip(self,weapon,armoritem = None,ring1 = None,ring2 = None):
        self.weapon = weapon
        self.armoritem = armoritem
        self.rings = (ring1,ring2)
        self.calculate_properties()

class Item():
    def __init__(self,name,type,cost,damage,armor):
        self.name = name
        self.type = type
        self.cost = cost
        self.damage = damage
        self.armor = armor

class Shop():
    def __init__(self):
        self.items = {'weapons': [],'armor': [],'rings': []}

        self.items['weapons'].append(Item('Dagger','weapon',8,4,0))
        self.items['weapons'].append(Item('Shortsword','weapon',10,5,0))
        self.items['weapons'].append(Item('Warhammer','weapon',25,6,0))
        self.items['weapons'].append(Item('Longsword','weapon',40,7,0))
        self.items['weapons'].append(Item('Greataxe','weapon',74,8,0))

        self.items['armor'].append(None)
        self.items['armor'].append(Item('Leather','armor',13,0,1))
        self.items['armor'].append(Item('Chainmail','armor',31,0,2))
        self.items['armor'].append(Item('Splintmail','armor',53,0,3))
        self.items['armor'].append(Item('Bandedmail','armor',75,0,4))
        self.items['armor'].append(Item('Platemail','armor',102,0,5))

        self.items['rings'].append(None)
        self.items['rings'].append(Item('Damage +1','ring',25,1,0))
        self.items['rings'].append(Item('Damage +2','ring',50,2,0))
        self.items['rings'].append(Item('Damage +3','ring',100,3,0))
        self.items['rings'].append(Item('Defense +1','ring',20,0,1))
        self.items['rings'].append(Item('Defense +2','ring',40,0,2))
        self.items['rings'].append(Item('Defense +3','ring',80,0,3))

    def generate_loadouts(self):
        for weapon in self.items['weapons']:
            for armor in self.items['armor']:
                for ring1 in self.items['rings']:
                    for ring2 in self.items['rings']:
                        if ring1 is None or ring2 is None:
                            yield weapon,armor,ring1,ring2
                        elif ring1.name != ring2.name:
                            yield weapon,armor,ring1,ring2
                    
def turn(attacker,defender):
    damage = attacker.damage - defender.armor
    if damage < 1:
        damage = 1
    defender.take_damage(damage)

def battle(player,boss):
    attacker = player
    defender = boss
    while True:
        turn(attacker,defender)
        if not defender.is_alive():
            break
        attacker,defender = defender,attacker
    return attacker,defender

try:
    inputfile = open('.\\2015\\21\\Input.txt','r')
    inputdata = inputfile.readlines()
    inputfile.close
except:
    print("Could not obtain input from file!")

for line in inputdata:
    pair = line.replace('\n','').split(': ')
    if pair[0] == 'Hit Points':
        bosshp = int(pair[1])
    if pair[0] == 'Damage':
        bossdamage = int(pair[1])
    if pair[0] == 'Armor':
        bossarmor = int(pair[1])

min_loadout_cost = 1000
max_loadout_cost = 0
shop = Shop()
for weapon,armor,ring1,ring2 in shop.generate_loadouts():
    boss = Boss(bosshp,bossdamage,bossarmor)
    player = Player(100)
    player.equip(weapon,armoritem = armor,ring1 = ring1,ring2 = ring2)
    winner,loser = battle(player,boss)
    if winner.name == 'Player' and winner.loadout_cost < min_loadout_cost:
        min_loadout_cost = winner.loadout_cost
    if loser.name == 'Player' and loser.loadout_cost > max_loadout_cost:
        max_loadout_cost = loser.loadout_cost

try:
    output = open('.\\2015\\21\\Output.txt','w')
    output.write(f"{min_loadout_cost}\n{max_loadout_cost}")
    output.close()
except:
    print("Could not write output file!")