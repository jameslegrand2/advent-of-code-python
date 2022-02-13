from copy import deepcopy

verbose = False

class InsufficientManaError(Exception):
    def __init__(self):
        super().__init__('Insufficient mana to cast spell')

class Fighter():
    def __init__(self,name,hitpoints,damage):
        self.name = name
        self.hitpoints = hitpoints
        self.damage = damage
        self.armor = 0
        self.mana = 0

    def is_alive(self):
        if self.hitpoints > 0:
            return True
        else:
            return False
    
    def take_damage(self,damage):
        global verbose
        if self.armor > 0:
            damage = damage - self.armor
            if damage < 1:
                damage = 1
            if verbose:
                print(f'Armor decreases damage to {damage}!')
        self.hitpoints -= damage

    def apply_effects(self):
        pass

    def attack(self,defender,spell = None):
        pass

    def take_turn(self,defender,spell = None, hardmode = False):
        global verbose
        if verbose:
            print(f'{self.name} turn')
            print(self)
            print(defender)
        self.apply_effects(hardmode)
        if not self.is_alive():
            if verbose:
                print(f'{self.name} died, {defender.name} wins!')
            return defender
        defender.apply_effects()
        if not self.is_alive():
            if verbose:
                print(f'{defender.name} died, {self.name} wins!')
            return self
        try:
            self.attack(defender,spell)
        except InsufficientManaError:
            raise
        if not self.is_alive():
            if verbose:
                print(f'{defender.name} died, {self.name} wins!')
            return self
        if verbose:
            print()
        return None

    def __str__(self):
        return '{} has {} hit points, {} armor, and {} mana'.format(self.name,self.hitpoints,self.armor,self.mana)

class Boss(Fighter):
    def __init__(self,hitpoints,damage):
        super().__init__('Boss',hitpoints,damage)
        self.poisoned = False
        self.poisonduration = 0

    def apply_poison(self):
        global verbose
        if self.poisoned:
            self.take_damage(3)
            self.poisonduration -= 1
            if verbose:
                print(f'Poison deals 3 damage, its timer is now {self.poisonduration}.')
            if self.poisonduration == 0:
                self.poisoned = False
                if verbose:
                    print('Poison wears off.')
        
    def apply_effects(self,hardmode = False):
        self.apply_poison()

    def attack(self,player,spell = None):
        global verbose
        if verbose:
            print(f'Boss attacks Player for {self.damage} damage!')
        player.take_damage(self.damage)
      
class Player(Fighter):
    spells = ['magic missile','drain','shield','poison','recharge']

    def __init__(self,hitpoints,mana):
        super().__init__('Player',hitpoints,0)
        self.mana = mana
        self.mana_spent = 0
        self.shielded = False
        self.shieldduration = 0
        self.recharging = False
        self.rechargeduration = 0

    def heal(self,amount):
        self.hitpoints += amount

    def apply_shield(self):
        global verbose
        if self.shielded:
            self.shieldduration -=1
            if verbose:
                print(f'Shield\'s timer is now {self.shieldduration}.')
            if self.shieldduration == 0:
                self.shielded = False
                self.armor = 0
                if verbose:
                    print('Shield wears off, decreasing armor by 7.')

    def apply_recharge(self):
        global verbose
        if self.recharging:
            self.mana += 101
            self.rechargeduration -=1
            if verbose:
                print(f'Recharge provides 101 mana, its timer is now {self.rechargeduration}.')
            if self.rechargeduration == 0:
                self.recharging = False
                if verbose:
                    print('Recharge wears off.')

    def apply_effects(self,hardmode = False):
        if hardmode:
            self.take_damage(1)
        self.apply_shield()
        self.apply_recharge()

    def pay_mana(self,mana):
        if self.mana >= mana:
            self.mana -= mana
            self.mana_spent += mana
        else:
            raise InsufficientManaError

    def magic_missile(self,boss):
        global verbose
        try: 
            self.pay_mana(53)
            boss.take_damage(4)
            if verbose:
                print('Player casts Magic Missile, dealing 4 damage.')
        except InsufficientManaError:
            raise 

    def drain(self,boss):
        global verbose
        try:
            self.pay_mana(73)
            boss.take_damage(2)
            self.heal(2)
            if verbose:
                print('Player casts Drain, dealing 2 damage and healing 2 hit points.')
        except InsufficientManaError:
            raise 

    def shield(self):
        global verbose
        try:
            self.pay_mana(113)
            self.shielded = True
            self.shieldduration = 6
            self.armor = 7
            if verbose:
                print('Player casts Shield, increasing armor by 7.')
        except InsufficientManaError:
            raise 

    def poison(self,boss):
        global verbose
        try:
            self.pay_mana(173)
            boss.poisoned = True
            boss.poisonduration = 6
            if verbose:
                print('Player casts Poison.')
        except InsufficientManaError:
            raise 

    def recharge(self):
        global verbose
        try:
            self.pay_mana(229)
            self.recharging = True
            self.rechargeduration = 5
            if verbose:
                print('Player casts Recharge.')
        except InsufficientManaError:
            raise 

    def attack(self,boss,spell):
        try:
            if spell == 'magic missile':
                self.magic_missile(boss)
            elif spell == 'drain':
                self.drain(boss)
            elif spell == 'shield':
                self.shield()
            elif spell == 'poison':
                self.poison(boss)
            elif spell == 'recharge':
                self.recharge()
        except InsufficientManaError:
            raise

class Battle():
    def __init__(self,player,boss,hardmode = False):
        self.player = player
        self.boss = boss
        self.spellsequence = []
        self.winner = None
        self.hardmode = hardmode

    def run_round(self,spell):
        try:
            winner = self.player.take_turn(self.boss,spell,self.hardmode)
            self.spellsequence.append(spell)
        except InsufficientManaError:
            self.spellsequence.append(spell)
            raise
        if winner is not None:
            self.winner = winner
            return 
        winner = self.boss.take_turn(self.player)
        if winner is not None:
            self.winner = winner
            return

def run_ongoing_battle_rounds():
    global ongoing_battles
    global min_mana_cost
    continue_battles = []
    for ongoing_battle in ongoing_battles:
        for spell in Player.spells:
            new_battle = deepcopy(ongoing_battle)
            try:
                new_battle.run_round(spell)
            except InsufficientManaError:
                continue
            if new_battle.winner is not None:
                if new_battle.winner.name == 'Player' and new_battle.winner.mana_spent < min_mana_cost:
                    min_mana_cost = new_battle.winner.mana_spent
            else:
                if new_battle.player.mana_spent < min_mana_cost:
                    continue_battles.append(new_battle)
    ongoing_battles = continue_battles

def run_all_battle_branches():
    global original_player
    global original_boss
    global ongoing_battles
    round = 0
    while len(ongoing_battles) > 0:
        run_ongoing_battle_rounds()
        round += 1

try:
    inputfile = open('.\\2015\\22\\Input.txt','r')
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

original_player = Player(50,500)
original_boss = Boss(bosshp,bossdamage)

ongoing_battles = [Battle(original_player,original_boss)]
min_mana_cost = 10e10
run_all_battle_branches()
easy_min_mana_cost = min_mana_cost

ongoing_battles = [Battle(original_player,original_boss,True)]
min_mana_cost = 10e10
run_all_battle_branches()
hard_min_mana_cost = min_mana_cost

try:
    output = open('.\\2015\\22\\Output.txt','w')
    output.write(f"{easy_min_mana_cost}\n{hard_min_mana_cost}")
    output.close()
except:
    print("Could not write output file!")