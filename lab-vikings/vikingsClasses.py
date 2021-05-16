import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - damage
        return
        
        

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def attack(self):
        return self.strength

    def receiveDamage(self, damage): # estos métodos tienen que ser reimplentados ==> esto, si no he entenido mal se hace sobreeribiendo la variable como se hace a continuación
        #Basicamente, estoy llamando a la clase constructora para definir todos los valores, pero luego anulo el valor (health y damage) de esta clase
        self.damage = damage 
        self.health = self.health - damage


        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"

        else:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"
          
# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - damage

        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"

        else:
            return f"A Saxon has died in combat"
    
# War

class War:
    def __init__(self):
        self.vikingArmy = []        
        self.saxonArmy = []
    
    def addViking(self, viking):
        self.vikingArmy.append(viking)        

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)        
    
    def vikingAttack(self):
        v = random.choice(self.vikingArmy)  #con esto genero un vikingo al azar 
        s = random.choice(self.saxonArmy)
    
        # v.attack() => con esto lo que hago es generar un ataque del vikingo que he creado anteriormente
        # s.receiveDamage () => el daño que recibe un sajón
        
        attack_v = s.receiveDamage(v.attack()) #el daño que recibe Saxon es igual a v.attack()

        if s.health <= 0:
            self.saxonArmy.remove(s)
        return attack_v
   
    def saxonAttack(self):
        v = random.choice(self.vikingArmy)
        s = random.choice(self.saxonArmy)

        attack_s = v.receiveDamage(s.attack())

        if v.health <= 0:
            self.vikingArmy.remove(v)
        return attack_s
    
    def showStatus(self):
        if len(self.saxonArmy) == 0 and len(self.vikingArmy) > 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0 and len(self.saxonArmy) > 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle." 

    
