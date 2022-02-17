from copy import deepcopy
from prototype import Prototype

class Barrack:
    def __init__(self):
        self.units={
            "knights":{
                "knight1":Knight(1),
                "knight2":Knight(2)

            },
            "archers":{
                "archer1":Archer(1),
                "archer2":Archer(2)

            }
        }
        
    def build_unit(self, unit_type, level):
        return self.units[unit_type+"s"][unit_type+str(level)].clone()


class Archer(Prototype):
    def __init__(self,level):
        self.unit_type="archer"
        self.level=level
        self.filename="{}{}.dat".format(self.unit_type,self.level)

        with open(self.filename, "r") as stats:

            stats=stats.readlines()    
            self.type=stats[0]
            self.life=stats[1]
            self.attack=stats[2]
            self.armor=stats[3]
            self.speed=stats[4]
            self.weapon=stats[5]
            self.range=stats[6]
    
    def clone(self):
        return deepcopy(self)

    def __str__(self):
        return "{}\n{}\n{}\n{}\n{}\n{}".format(self.type,self.life,self.attack,self.speed,self.armor,self.weapon,self.range)

class Knight(Prototype):

    def __init__(self,level):
        self.unit_type="knight"
        self.level=level
        self.filename="{}{}.dat".format(self.unit_type,self.level)

        with open(self.filename, "r") as stats:

            stats=stats.readlines()    
            self.type=stats[5]
            self.life=stats[2]
            self.attack=stats[1]
            self.speed=stats[4]
            self.weapon=stats[0]
            self.armor=stats[3]
    
    def clone(self):
        return deepcopy(self)
    
    
    def __str__(self):
        return "type: {0}\nlife: {1}\nattack: {2}\nlife: {3}\nlife: {4}\nweapon: {5}".format(self.type,self.life,self.attack,self.speed,self.armor,self.weapon,)



if __name__== "__main__":
    barrack=Barrack()
    knight1=barrack.build_unit("archer",1)
    print(knight1)
