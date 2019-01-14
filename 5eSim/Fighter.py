
import random
import InfoTables

#Create a fighter class with a specific subclass, weapon and fighting style
class fighterClass:

    def __init__(self, subclass, weapon, style):
        self.subclass = subclass
        #self.hasCombatDie = checkClass()
        self.diceLeft = 4 if subclass == "battlemaster" else 0
        self.rageDamage = 2 if subclass == "berserker" else 4
        self.stats = [4, 2, 3, 2, 2, 1]
        self.attacks = 2
        self.weapon = weapon
        self.history = []
        random.seed(a=None)

    def checkClass(self):
        if self.subclass == "battlemaster":
            return True
        else:
            return False

    #Battlemasters consume combat die to improve hit chances
    def battlemaster(self, use):
        attackBonus = 0
        #print("Dice Left: " + str(self.diceLeft), "Using Precision Attack?: " + str(use))
        if (self.diceLeft and use):
            self.diceLeft -= 1
            attackBonus = random.randint(1,8)

        bruteDamage = random.randint(1,4)
        return([attackBonus, bruteDamage])

    def attack(self, ac):
        attacksMade = 0
        round = ["AC: "+str(ac)]
        while attacksMade < self.attacks:
                attacksMade += 1
                hit = random.randint(1,20)+self.stats[0]
                damage = random.randint(1, self.weapon)+self.stats[0]+self.rageDamage
                if self.subclass == "battlemaster":
                    use = False
                    if hit < ac:
                        use = True
                    BM = self.battlemaster(use)
                    hit += BM[0]
                    damage += BM[1]
                final = ["Hit!" if hit >= ac else "Missed", "Attack: " + str(hit), "Damage: " + str(damage) ]
                round.append(final)
        self.history.append(round)

testFighter = fighterClass("battlemaster", 12, 2)

for x in range(5):
    testFighter.attack(19)

for x in testFighter.history:
    print(x)
