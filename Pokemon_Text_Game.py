# By submitting this assignment, I agree to the following:
#  Aggies do not lie, cheat, or steal, or tolerate those who do
#  I have not given or received any unauthorized aid on this assignment
#
# Name:         Anthony Matl Landon Matak Luca Maddaleni Nate Michaud
# Section:      273
# Assignment:   Lab Assignment 12
# Date:         11 October 2020
dashes = '-' * 30
divider = '-' * 100
#Note: For future reference, i should globalize the pokemon lists
import pathlib
#getting the number of player accounts
import csv
from numpy import random
from math import sqrt
#first thing seen when program begins:
def player_select():
    '''This function allows the user to choose a returning player or a new player'''
    print('{:-^100}'.format('Player Selection Menu'))
    print('\n1. New Player\n2. Returning Player'.format(dashes, dashes))
    acceptable = ['1', '2']
    selection = input()
    while not selection in acceptable:
        selection = input('Value Not accepted. Enter 1 or 2:\n')
    selection = int(selection)
    if selection == 1:
        create_new_player()
    elif selection == 2:
        num_accounts = 0
        playerbase = pathlib.Path('playerdatabase.txt')
        if playerbase.exists():
            with open('playerdatabase.txt', 'r') as playerdatabase:
                for line in playerdatabase:
                    num_accounts += 1
        if num_accounts == 0:
            print('No saved accounts found. Retrying player select')
            player_select()
        select_player()

#a potential path taken if user is not returning:
def create_new_player():
    '''This function creates a new player and adds it to file then creates a new player file then goes to main menu'''
    print('{:-^100}'.format('Player Creation Menu'))
    username = input('Enter your player username: ')
    filename = username + '.csv'
    starter = random.randint(1,151)
    pokedex = open('PokeList_v2.csv', 'r')
    pokeman = csv.reader(pokedex, delimiter=',')
    playerbase = pathlib.Path('playerdatabase.txt')
    if playerbase.exists():
        with open('playerdatabase.txt', 'a') as  playerdatabase:
            playerdatabase.write(username + '\n')
        playerdatabase.close()
    else:
        with open('playerdatabase.txt', 'w') as playerdatabase:
            playerdatabase.write(username + '\n')
        playerdatabase.close()
    for i in pokeman:
        if i[0] == str(starter):
            print('\n\nCongratulation {}!!!\nYou have received your first pokemon!!!\nAnd that pokemon is.....\nA {}!!!!!!'.format(username, i[1]))
            with open(filename, 'w') as playerfile:
                playerfile.write(username + '\n')
                playerfile.write('0' + ',' + 'candies\n')
                playerfile.write(i[0] + ',' + i[1] + ',' + '1' + ',' + i[2] + ',' + i[3])
    pokedex.close()
    main_menu(filename)
#here after player is selected
def main_menu(filename):
    '''This function displayes a main menu and runs the selected menu option. Only parameter is the name of the user which is the filename'''
    print('{:-^100}'.format('MAIN MENU'))
    print('\n1. View Pokemon and Items\n2. Battle Pokemon\n3. Catch New Pokemon\n4. Upgrade Pokemon\n5. Save and Exit\n6. Switch account'.format(dashes, dashes))
    selection = str(input())
    accepted = ['1', '2', '3', '4', '5', '6']
    while not selection in accepted:
        selection = str(input('Invalid. Enter a 1-6:\n'))
    selection = int(selection)
    if selection == 1:
        view_pokemon(filename)
    elif selection == 2:
        num_accounts = 0
        playerbase = pathlib.Path('playerdatabase.txt')
        if playerbase.exists():
            with open('playerdatabase.txt', 'r') as playerdatabase:
                for line in playerdatabase:
                    num_accounts += 1
        else:
            num_accounts = 0
        if num_accounts < 2:
            print('Unfortunately it takes two accounts to battle. Maybe try creating a new one?')
            main_menu(filename)
        battle_pokemon(filename)
    elif selection == 3:
        catch_pokemon(filename)
    elif selection == 4:
        upgrade_pokemon(filename)
    elif selection == 5:
        save_exit()
    elif selection == 6:
        player_select()
#following functions are all potential paths from main_menu and then they return to main menu
#all except for the battle that calls player select once again
def view_pokemon1(filename):
    '''Displays a list of pokemon. Only parameter is the name of the user which is the filename'''
    pokemons = open(filename, 'r')
    pokelist = csv.reader(pokemons, delimiter=',')
    count = -2
    for line in pokelist:
        count += 1
    pokemons.close()
    num_pokemon = count
    count = 1
    pokemons = open(filename, 'r')
    pokelist = csv.reader(pokemons, delimiter=',')
    names = []
    cp = []
    count = 1
    for line in pokelist:
        #if len(line) == 2:
            #print('You have {} candies'.format(line[0]))
        if len(line) > 2:
            names.append(str(count) + '. ' + line[1] + ' Lv: ' + str(line[2]))
            cp.append('CP ' + line[3])
            count += 1
    pokemons.close()
    num_times = num_pokemon // 4
    num_extra = num_pokemon % 4
    n = 0
    print(divider)
    if num_pokemon >= 4:
        for i in range(num_times):
            print('{:<28}{:<28}{:<28}{:<28}'.format(names[n], names[n + 1], names[n + 2],names[n + 3]))
            print('{:<28}{:<28}{:<28}{:<28}'.format(cp[n], cp[n + 1], cp[n + 2], cp[n + 3]))
            print()
            n += 4
    if num_extra == 1:
        print('{:<28}'.format(names[n]))
        print('{:<28}'.format(cp[n]))
    if num_extra == 2:
        print('{:<28}{:<28}'.format(names[n], names[n +1]))
        print('{:<28}{:<28}'.format(cp[n], cp[n + 1]))
    if num_extra == 3:
        print('{:<28}{:<28}{:<28}'.format(names[n], names[n +1], names[n + 2]))
        print('{:<28}{:<28}{:<28}'.format(cp[n], cp[n + 1], cp[n + 2]))
    print(divider)
def view_pokemon(filename):
    '''Displays a list of pokemon. Only parameter is the name of the user which is the filename'''
    print('{:-^100}'.format('Current Pokemon'))
    pokemons = open(filename, 'r')
    pokelist = csv.reader(pokemons, delimiter=',')
    count = -2
    for line in pokelist:
        count += 1
    pokemons.close()
    num_pokemon = count
    count = 1
    pokemons = open(filename, 'r')
    pokelist = csv.reader(pokemons, delimiter=',')
    names = []
    cp = []
    count = 1
    candies = 0
    for line in pokelist:
        if len(line) == 2:
            candies = line[0]
        if len(line) > 2:
            names.append(str(count) + '. ' + line[1] + ' Lv: ' + str(line[2]))
            cp.append('CP ' + line[3])
            count += 1
    pokemons.close()
    num_times = num_pokemon // 4
    num_extra = num_pokemon % 4
    n = 0
    print(divider)
    if num_pokemon >= 4:
        for i in range(num_times):
            print('{:<28}{:<28}{:<28}{:<28}'.format(names[n], names[n + 1], names[n + 2],names[n + 3]))
            print('{:<28}{:<28}{:<28}{:<28}'.format(cp[n], cp[n + 1], cp[n + 2], cp[n + 3]))
            print()
            n += 4
    if num_extra == 1:
        print('{:<28}'.format(names[n]))
        print('{:<28}'.format(cp[n]))
    if num_extra == 2:
        print('{:<28}{:<28}'.format(names[n], names[n +1]))
        print('{:<28}{:<28}'.format(cp[n], cp[n + 1]))
    if num_extra == 3:
        print('{:<28}{:<28}{:<28}'.format(names[n], names[n +1], names[n + 2]))
        print('{:<28}{:<28}{:<28}'.format(cp[n], cp[n + 1], cp[n + 2]))
    print(divider)
    print('\nCandies : {}'.format(candies))
    print('\nPress enter to return to main menu')
    input()
    main_menu(filename)

    #print('1. Return to main menu\n2. Use candy')
def upgrade_pokemon(filename):
    '''Upgrades pokemon for the user entered in parameter (filename) and allows user to select the pokemon they would like to upgrade.
    Only parameter is the name of the user which is the filename'''
    print('{:-^100}'.format('Poke Evolution Center'))
    pokemons = open(filename, 'r')
    pokelist = csv.reader(pokemons, delimiter=',')
    num_pokemon = 0
    candies = 0
    for line in pokelist:
        num_pokemon += 1
        if len(line) == 2:
            candies = line[0]
    pokemons.close()
    view_pokemon1(filename)
    print('You have ' + str(candies) + ' candies')
    print('Choose Pokemon to level up')
    choice = input()
    accepted = []
    for i in range(num_pokemon):
        accepted.append(str(i))
    while not choice in accepted:
        choice = input('Invalid. Please a number from the list of pokemon:\n')
    choice = int(choice)
    valid_lvUp = False
    while not valid_lvUp:
        pokemons = open(filename, 'r')
        pokelist = csv.reader(pokemons, delimiter=',')
        count = -1
        for line in pokelist:
            if count == 0:
                candies = int(line[0])
            if count == choice:
                level = int(line[2])
                if int(line[2]) <= 30:
                    needed_candies = 1
                else:
                    needed_candies = 2
            count += 1
        pokemons.close()
        if needed_candies <= candies and level < 40:
                candies -= needed_candies
                valid_lvUp = True
        else:
            if candies == 0:
                print('Sorry you are out of candies try to earn some more by catching another pokemon!!')
                main_menu(filename)
            print('You either do not have enough candies or the pokemon is already max level. Please select another to upgrade.')

            print('Press Enter to continue to main menu')
            input()
            main_menu(filename)


    pokemons = open(filename, 'r')
    pokelist = csv.reader(pokemons, delimiter=',')
    count = -1
    for line in pokelist:
        if len(line) > 4:
            if count == choice:
                p_chosen = line[1]
                cp = float(line[3])
                level = int(line[2])
                new_line = line
                if int(line[2]) <= 30:
                    cp += (cp * .0094) / (.095 * sqrt(level))
                else:
                    cp += (cp * .0045) / (.095 * sqrt(level))
                if cp > float(line[4]):
                    cp = float(line[4])

        count += 1
    pokemons.close()
    level += 1
    cp = round(cp, 3)
    new_line.pop(2)
    new_line.pop(2)
    new_line.insert(2, str(level))
    new_line.insert(3, str(cp))
    pokemons = open(filename, 'r')
    duplicate = open('duplicate', 'w')
    count = -1
    for line in pokemons:
        if count == 0:
            duplicate.write(str(candies) + ',' + 'candies\n')
        elif count == choice:
            duplicate.write('{},{},{},{},{}\n'.format(new_line[0],new_line[1],new_line[2],new_line[3],new_line[4]))
        else:
            duplicate.write(line)
        count += 1
    pokemons.close()
    duplicate.close()
    pokemons = open(filename, 'w')
    duplicate = open('duplicate', 'r')
    count = -1
    for line in duplicate:
        pokemons.write(line)
    duplicate.close()
    pokemons.close()
    print('Congratulations!!! You upgraded {} to level {}!\n{} has a new cp of {}!'.format(p_chosen, level, p_chosen, cp))
    print('1. Return to main menu\n2. Upgrade Another Pokemon')
    accepted = ['1', '2']
    choice = input()
    while not choice in accepted:
        choice = input('Invalid. Please enter 1 or 2\n')
    choice = int(choice)
    if choice == 2:
        upgrade_pokemon(filename)
    else:
        main_menu(filename)
def battle_pokemon(filename):
    '''Allows another player to be selected then initiates battle.
    Only parameter is the name of the user which is the filename'''
    print('{:-^100}'.format('Pokemon Arena'))
    print('\n{:!^100}'.format("GET READY TO RUMBLEEE"))
    print('Press enter to begin battle')
    input()
    view_pokemon1(filename)
    #this is to account for some user error
    pokemons = open(filename, 'r')
    pokelist = csv.reader(pokemons, delimiter=',')
    num_pokemon = 0
    for line in pokelist:
        num_pokemon += 1
    pokemons.close()
    print('Player one, choose your pokemon')
    choice = input()
    accepted = []
    for i in range(num_pokemon):
        accepted.append(str(i))
    while not choice in accepted:
        choice = input('Invalid. Please a number from the list of pokemon:\n')
    pokemon1 = int(choice)

    pokemons = open(filename, 'r')
    pokelist = csv.reader(pokemons, delimiter=',')
    count = pokemon1 + 1
    for line in pokelist:
        if count == 0:
            poke1 = line
        count -= 1
    pokemons.close()
    print('You have chosen {}'.format(poke1[1]))
    print('\n\n')
    print('Player Two, choose your account')
    counter = 1
    with open('playerdatabase.txt', 'r') as playerdatabase:
        for line in playerdatabase:
            print('{}. {}'.format(counter, line), end='')
            counter += 1
        counter = 1
        selected_player = int(input())
    with open('playerdatabase.txt', 'r') as playerdatabase:
        for line in playerdatabase:
            if selected_player == counter:
                player2 = line[:-1]
            counter += 1
    view_pokemon1(player2 + '.csv')
    print('Player Two choose your pokemon')
    pokemons = open(player2 + '.csv', 'r')
    pokelist = csv.reader(pokemons, delimiter=',')
    pokemon2 = int(input())
    count = pokemon2 + 1
    for line in pokelist:
        if count == 0:
            poke2 = line
        count -= 1
    pokemons.close()
    print('You have chosen {}'.format(poke2[1]))
    print('{:-^100}'.format('TIME TO BATTTTLEEEEEE'))
    poke1name = poke1[1]
    poke2name = poke2[1]
    poke1CP = float(poke1[3])
    poke2CP = float(poke2[3])
    poke1lv = int(poke1[2])
    poke2lv = int(poke2[2])
    strcp1 = 'CP: ' + str(poke1CP)
    strcp2 = 'CP: ' + str(poke2CP)
    versus = '|||'
    poke1info = poke1name + ' Lv: ' + str(poke1lv)
    poke2info = poke2name + ' Lv: ' + str(poke2lv)
    print('{:<20}{:^20}{:<20}'.format(poke1info, versus, poke2info))
    print('{:<20}{:^20}{:<20}'.format(strcp1, versus, strcp2))
    print()
    print('Press Enter To Begin THE FIGHT')
    input()
    while poke1CP > 0 or poke2CP > 0:
        damage = random.randint(0, poke1lv * 2 + 50)
        print(divider)
        poke2CP -= damage
        message = str(poke1name) + ' dealt ' + str(damage) + ' damage'
        print('{:^60}'.format(message))
        if poke2CP <= 0:
            poke2CP = 0
        strcp2 = 'CP: ' + str(poke2CP)
        print('{:<20}{:^20}{:<20}'.format(poke1info, versus, poke2info))
        print('{:<20}{:^20}{:<20}'.format(strcp1, versus, strcp2))
        if poke2CP <= 0:
            poke2CP = 0
            print('{} fainted'.format(poke2name))
            winner = poke1name
            break
        damage = random.randint(0, poke2lv * 2 + 50)
        poke1CP -= damage
        if poke1CP <= 0:
            poke1CP = 0
        strcp1 = 'CP: ' + str(poke1CP)
        print(divider)
        message = str(poke2name) + ' dealt ' + str(damage) + ' damage'
        print('{:^60}'.format(message))
        print('{:<20}{:^20}{:<20}'.format(poke1info, versus, poke2info))
        print('{:<20}{:^20}{:<20}'.format(strcp1, versus, strcp2))
        if poke1CP <= 0:
            poke1CP = 0
            print('{} fainted'.format(poke1name))
            winner = poke2name
            break
        print(divider)
        print('Enter any key to continue with the battle')
        cont = input()
    print(divider + '\n')
    print('{:>48} is the WINNER\n\n'.format(winner))
    print('Enter any number to return to player select')
    input()
    select_player()

def catch_pokemon(filename):
    '''Allows user to select a pokemon and battle/catch a random pokemon.
    Only parameter is the name of the user which is the filename'''
    print('{:-^100}'.format('Entered the Wild Forest Be Prepared'))
    print('\nPress enter to advance')
    input()
    wildpk = random.randint(1, 151)
    pokedex = open('PokeList_v2.csv', 'r')
    pokeman = csv.reader(pokedex, delimiter=',')
    for i in pokeman:
        if i[0] == str(wildpk):
            print('\nA wild {} has appeared'.format(i[1]))
            wildpokemon = i
    pokedex.close()
    view_pokemon1(filename)
    print('{:-^100}'.format('Select Pokemon for BATTLE'))
    pokemon1 = int(input())
    pokemons = open(filename, 'r')
    pokelist = csv.reader(pokemons, delimiter=',')
    count = pokemon1 + 1
    for line in pokelist:
        if count == 0:
            poke1 = line
        count -= 1
    pokemons.close()
    wildCp = float(wildpokemon[2])
    wildname = wildpokemon[1]
    poke1Cp = float(poke1[3])
    poke1Lv = int(poke1[2])
    poke1name = poke1[1]
    faint = False
    while not faint:
        #print('{} CP: {}     VS.     {} CP: {}'.format(poke1[1], poke1Cp, wildpokemon[1], wildCp))
        strcp1 = 'CP: ' + str(poke1Cp)
        strcp2 = 'CP: ' + str(wildCp)
        versus = '|||'
        poke1info = poke1name + ' Lv: ' + str(poke1Lv)
        poke2info = wildname + ' Lv: 1'
        print(divider)
        print('{:<20}{:^20}{:<20}'.format(poke1info, versus, poke2info))
        print('{:<20}{:^20}{:<20}'.format(strcp1, versus, strcp2))
        print(divider)
        print('\nWhat would you like to do:\n1. Attack\n2. Throw PokeBall')
        choice = int(input())
        if choice != 2:
            damage = random.randint(0, poke1Lv + 50)
            print('\n{} dealt {} damage to {}'.format(poke1name, damage, wildname))
            wildCp -= damage
            if wildCp <= 0:
                print('Oh No!!! {} fainted'.format(wildname))
                poke1Cp = 0
                faint = True
                break
            damage = random.randint(0,50)
            print('{} dealt {} damage to {}'.format(wildname, damage, poke1name))
            poke1Cp -= damage
            if poke1Cp <= 0:
                poke1Cp = 0
                print('Oh No!!! {} fainted'.format(poke1name))
                faint = True
                break
        else:
            print('\n{:^100}'.format('Throwing Pokeball Now!!!'))
            factor = random.randint(0, wildCp)
            print('Press enter to see catch results')
            input()
            if factor < 45:
                catch = True
            else:
                catch = False
                print('{:^100}'.format('CATCH FAILED'))
                damage = random.randint(0, 50)
                print('{} dealt {} damage to {}'.format(wildname, damage, poke1name))
                poke1Cp -= damage
                if poke1Cp <= 0:
                    poke1Cp = 0
                    faint = True
                    print('Oh No!!! {} fainted'.format(poke1name))
                    break
                # strcp1 = 'CP: ' + str(poke1Cp)
                # strcp2 = 'CP: ' + str(wildCp)
                # versus = '|||'
                # poke1info = poke1name + ' Lv: ' + str(poke1Lv)
                # poke2info = wildname + ' Lv: 1'
                # print(divider)
                # print('{:<20}{:^20}{:<20}'.format(poke1info, versus, poke2info))
                # print('{:<20}{:^20}{:<20}'.format(strcp1, versus, strcp2))
                # print(divider)
            if catch == True:
                message = 'Congratulations {} was caught'.format(wildname)
                print('{:-^100}'.format(message))
                break
    if faint == True:
        print('That catch attempt was a fail.\nPress enter to return to main menu')
        input()
        main_menu(filename)
    if catch == True:
        pokemon = open(filename, 'a')
        candies = random.randint(1,4)
        if candies == 1:
            candies = 3
        if candies == 2:
            candies = 5
        if candies == 3:
            candies = 10
        print('You were awarded {} candies'.format(candies))
        pokemon.write('\n')
        pokemon.write(wildpokemon[0] + ',' + wildpokemon[1] + ',' + '1' + ',' + wildpokemon[2] + ',' + wildpokemon[3])
        pokemon.close()
        pokemons = open(filename, 'r')
        duplicate = open('duplicate', 'w')
        count = -1
        for line in pokemons:
            if count == 0:
                duplicate.write(str(candies) + ',' + 'candies\n')
            else:
                duplicate.write(line)
            count += 1
        pokemons.close()
        duplicate.close()
        pokemons = open(filename, 'w')
        duplicate = open('duplicate', 'r')
        count = -1
        for line in duplicate:
            pokemons.write(line)
        duplicate.close()
        pokemons.close()
    print('{} was added to your pokemon team'.format(wildname))
    print('\n\n\n\n\n\nPress Enter to return to main menu')
    input()
    main_menu(filename)
def select_player():
    '''This function displays a list from the player file and allows user to select a player, returns that player then goes to main menu'''
    print('{:-^100}'.format('Player Selection Menu'))
    counter = 1
    with open('playerdatabase.txt', 'r') as playerdatabase:
        for line in playerdatabase:
            print('{}. {}'.format(counter, line), end='')
            counter += 1
        acceptable = []
        for i in range(counter):
            acceptable.append(str(i))

        selected_player = input()
        while not selected_player in acceptable:
            selected_player = input('Value not recognized. Please enter a valid option:\n')
        selected_player = int(selected_player)
    counter = 1
    with open('playerdatabase.txt', 'r') as playerdatabase:
        for line in playerdatabase:
            if selected_player == counter:
                filename = line[:-1]
            counter += 1
    filename += '.csv'
    main_menu(filename)
#exits the program
def save_exit():
    '''Exits program'''
    print('Thank you for playing!!')
    exit()
#starts here
player_select()