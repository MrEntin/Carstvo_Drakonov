import random
import time

def displayIntro():
    print('''Вы находитесь в землях, заселённых драконами.
Перед собой вы видите две пещеры. В одной из них - дружелюбный дракон,
который готов поделиться с вами своими сокровищами. Во второй - жадный
и голодный дракон, который мигом вас съест.
Добро пожаловать в игру "Царство Драконов"
                                    by 2254''')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('В какую пещеру вы войдёте?(нажмите клавишу 1 или 2, а потом Enter)')
        cave = input()
    return cave
def checkCave(chosenCave):
    print('Вы приближаетесь к пещере...')
    time.sleep(2)
    print('Её темнота заставляет вас дрожать от страха...')
    time.sleep(2)
    print('Огромный дракон появляется из темноты! Он смотрит на вас своими глазами и...')
    time.sleep(2)

    friendlyCave = random.randint(1,2)

    if chosenCave == str(friendlyCave):
        print('...делится с вами своими сокровищами!')
    else:
        print('...мигом вас пожирает!')

playAgain = 'да'
while playAgain == 'да' or playAgain == 'д':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print("Попытаете удачу ещё раз?(да или нет)")
    playAgain = input()