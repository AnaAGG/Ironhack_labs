from vikingsClasses import Soldier, Viking, Saxon, War
import random

# lo primero que tengo que hacer es definir cuantos soldados tiene cada uno de los ejercitos:

v = str(input("How many soldiers does the Viking army have? "))

s = str(input("How many soldiers does the Saxon army have?"))


#luego defino la fuerza y la salud de los soldados de forma aleatoria: 
vikingos = Viking(v + "str", random.randint(0,100), random.randint(0,100))

sajones = Saxon(random.randint(0,100), random.randint(0,100))


# defino la guerra 

war = War()


# lo siguiente es añadir los los vikingos y sajones creado aleatoriamente a saxonArmy

for vik in range(0, v):
    vikingos = Viking(v, random.randint(0,100), random.randint(0,100))
    war.addViking(vikingos)


for sax in range(0, s):
    sajones = Saxon(random.randint(0,100), random.randint(0,100))
    war.addSaxon(sajones)


#EL MOMENTO DE LA GUERRA:

    #lo primero que tiene que ocurrir es que la salud de los dos contrincantes sea mayor que 0

while len(vikingos) > 0 and len(sajones) > 0:
    sax_attack = war.saxonAttack
    vik_attack = war.vikingAttack
