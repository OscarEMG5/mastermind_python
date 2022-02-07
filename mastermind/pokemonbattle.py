
import os
import random
import math


cls = lambda: os.system('cls')

hpo_pikachu = 80        #Health of pikachu at the beginning
hpo_squirtle = 90       #Health of squirtle at the beginning
hpi_pikachu = 80        #Variable health points of pikachu
hpi_squirtle = 90       #Variable health points of squirtle

#Pikachu attacks:
#1 Bda_volts hits 10 hp
#2 Thunder_wave hits 11 hp

PikaA = "Pikachu choose Bda Volts attack [-10 HP]"
PikaB = 'Pikachu choose Thunder Wave attack [-11 HP]'

#Squirtle attacks:
#1 A: Placaje hits 10 hp
#2 B: Water gun hits 12 hp
#3 C: Bubble hits 9 hp
#4 D: Skip attack hits 0 hp

SqrA = 'Squirtle choose Placaje attack [-10 HP]'
SqrB = 'Squirtle choose Water gun attack [-12 HP]'
SqrC = 'Squirtle choose Bubbles [-9 HP]'
SqrD = 'Squirtle choose to skip the attack'

print("Pokemon Battle\n" 
     "Pikachu vs Squirtle\n"
      "the batlle begins\n")

while hpi_squirtle > 0 and hpi_pikachu > 0:

    # First turn for Pikachu
    print('Pikachu turn\n')

    pikachu_attack = random.randint(1,2)

    if pikachu_attack == 1 :
        print(PikaA)
        hpi_squirtle -= 10

    if pikachu_attack == 2 :
        print(PikaB)
        hpi_squirtle -= 11

    if hpi_squirtle <= 0:
        hpi_squirtle = 0


    health_bar_pikachu = int(hpi_pikachu/hpo_pikachu*10)
    health_bar_squirtle = int(hpi_squirtle/hpo_squirtle*10)

    print('Pikachu health is: {}. Squirtle health is: {}\n'.format(hpi_pikachu, hpi_squirtle))
    print('Pikachu:  ({}{}) {}/80\n'
          'Squirtle: ({}{}) {}/90\n'.format('O'*health_bar_pikachu, '~'*(10 - health_bar_pikachu), hpi_pikachu,
                                            'O'*health_bar_squirtle, '~'*(10 - health_bar_squirtle), hpi_squirtle))


    input('Press ENTER to continue')
    cls()

    # Pikachu turn finish

    if hpi_squirtle <= 0 :
        print('Pikachu defeats Squirtle\n\n'
              'PIKACHU IS THE CHAMPION\n'
              'Congratulations')
        exit()

    # Second turn for Squirtle

    print('Squirtle turn\n')
    squirtle_attack = None
    while squirtle_attack != "A" and squirtle_attack != "B" and squirtle_attack != "C" and squirtle_attack != "D" :
        squirtle_attack = input('What attack do you choose (A, B, C or D)\n'
                            'A: Placaje\n'
                            'B: Water gun\n'
                            'C: Bubble\n'
                            'D: Skip Attack\n\n')

    if squirtle_attack == "A":
        print(SqrA)
        hpi_pikachu -= 10

    elif squirtle_attack == "B":
        print(SqrB)
        hpi_pikachu -= 12

    elif squirtle_attack == "C":
        print(SqrC)
        hpi_pikachu -= 9

    elif squirtle_attack == "D":
        print(SqrD)
        hpi_pikachu -= 0

    if hpi_pikachu <= 0:
        hpi_pikachu = 0

    health_bar_pikachu = int(hpi_pikachu/hpo_pikachu*10)
    health_bar_squirtle = int(hpi_squirtle/hpo_squirtle*10)

    print ('Pikachu health is: {}. Squirtle health is: {}\n'.format(hpi_pikachu,hpi_squirtle))
    print('Pikachu:  ({}{}) {}/80\n'
          'Squirtle: ({}{}) {}/90\n'.format('O'*health_bar_pikachu, '~'*(10 - health_bar_pikachu), hpi_pikachu,
                                            'O'*health_bar_squirtle, '~'*(10 - health_bar_squirtle), hpi_squirtle))
    input('Press ENTER to continue')
    cls()

    #Squirtle turn finish

if hpi_pikachu < hpi_squirtle:
    print('Squirtle defeats Pikachu\n\n'
          'SQUIRTLE IS THE CHAMPION\n'
          'Congratulations')

else:
    print('Pikachu defeats Pikachu\n\n'
          'PIKACHU IS THE CHAMPION\n'
          'Congratulations')

input('Press ENTER to exit')
exit()