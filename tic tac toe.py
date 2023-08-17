import os
import random

class perameters(object):
    game_over = False
    grid_size = 7
    spacing = grid_size - 4
    def creat_grid():
        print('-----------------------')
        print('{}    [X] | [O]    {}'.format(p_1_d, p_2_d))
        print('-----------------------\n')

        for l in range(perameters.grid_size):  
            if l == 1:       
                print(' '*perameters.spacing + "{}".format(cells[0])+ ' '*perameters.spacing +'|' + ' '*perameters.spacing + "{}".format(cells[1]) + ' '*perameters.spacing + '|' + ' '*perameters.spacing + "{}".format(cells[2]))
            elif l == 3:
                print(' '*perameters.spacing + "{}".format(cells[3])+ ' '*perameters.spacing +'|' + ' '*perameters.spacing + "{}".format(cells[4]) + ' '*perameters.spacing + '|' + ' '*perameters.spacing + "{}".format(cells[5]))
            elif l == 5:
                print(' '*perameters.spacing + "{}".format(cells[6])+ ' '*perameters.spacing +'|' + ' '*perameters.spacing + "{}".format(cells[7]) + ' '*perameters.spacing + '|' + ' '*perameters.spacing + "{}".format(cells[8]))
            elif l == 6:
                print(' '*perameters.grid_size + '|' + ' '*perameters.grid_size + '|'+' '*perameters.grid_size + '\n')
            else:
                print(' '*perameters.grid_size + '|' + ' '*perameters.grid_size + '|'+' '*perameters.grid_size)
            if l == 1 or l == 3:
                print('_'*perameters.grid_size + '|' + '_'*perameters.grid_size + '|'+'_'*perameters.grid_size)          

cells = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

command = 0

X = 'X'
O = 'O'


x_won = ''
o_won = ''

os.system('cls')
print('-----------------------------------------')
print('||            tic tac toe              ||')
print('-----------------------------------------\n')
input("Press Enter to continue...")
os.system('cls')


## Player name
player_1 = input("Name (player_1): ")
player_2 = input("Name (player_2): ")

p_1_d = player_1.upper()[:3]
p_2_d = player_2.upper()[:3]

if len(player_1) != 0 and len(player_1) < 3:
    p_1_d = player_1.upper() + ' '.ljust(3 - len(player_1))
elif player_1.strip() == "":
    p_1_d = 'P_1'
    player_1 = 'P_1'

if len(player_2) != 0 and len(player_2) < 3:
    p_2_d = ' '.ljust(3 - len(player_2)) + player_2.upper()
elif player_2.strip() == "":
    p_2_d = 'P_2'
    player_2 = 'P_2'

    

x_won = str(player_1.strip()) + ' won\n'
o_won = str(player_2.strip()) + ' won\n'
os.system('cls')

#def AI():


def game_over():
    perameters.game_over = True
    restart = input('Want to play again?[y/n]: ')
    if restart.lower().strip() == 'y':
        for i in range(int(len(cells))):
            cells[i] = ' '
        perameters.game_over = False
        os.system('cls')
        Game()
    else:
        exit()

def game_state():
    ## To check if X won
    if set(cells[0:3]) == {X}:
        print(x_won)  
        game_over()
    elif set(cells[3:6]) == {X}:
        print(x_won)
        game_over()
    elif set(cells[6:9]) == {X}:
        print(x_won)
        game_over()
    elif cells[0] == X and cells[3] == X and cells[6] == X:
        print(x_won)
        game_over()
    elif cells[0] == X and cells[4] == X and cells[8] == X:
        print(x_won)
        game_over()
    elif cells[0] == X and cells[4] == X and cells[8] == X:
        print(x_won)
        game_over()
    elif cells[2] == X and cells[5] == X and cells[8] == X:
        print(x_won)
        game_over()
    elif cells[2] == X and cells[4] == X and cells[6] == X:
        print(x_won)
        game_over()
    elif cells[1] == X and cells[4] == X and cells[7] == X:
        print(x_won)
        game_over()  

    ## To check if O won
    if set(cells[0:3]) == {O}:
        print(o_won)
        game_over()
    elif set(cells[3:6]) == {O}:
        print(o_won)
        game_over()
    elif set(cells[6:9]) == {O}:
        print(o_won)
        game_over()
    elif cells[0] == O and cells[3] == O and cells[6] == O:
        print(o_won)
        game_over()
    elif cells[0] == O and cells[4] == O and cells[8] == O:
        print(o_won)
        game_over()
    elif cells[0] == O and cells[4] == O and cells[8] == O:
        print(o_won)
        game_over()
    elif cells[2] == O and cells[5] == O and cells[8] == O:
        print(o_won)
        game_over()
    elif cells[2] == O and cells[4] == O and cells[6] == O:
        print(o_won)
        game_over()
    elif cells[1] == O and cells[4] == O and cells[7] == O:
        print(o_won)
        game_over()

    ## Check if its a draw
    if cells.count(' ') == 0 and perameters.game_over == False:
        print("\nGame is a draw!!")
        game_over()

def Game():

    perameters.creat_grid()

    turns = False
    while ' ' in cells and not perameters.game_over:
        if not turns:
            command = input('Press 1 through 9 [{}]: '.format(p_1_d)).strip()
            turns = True
            if command.strip().isnumeric() and cells[int(command[0].strip()) - 1] == ' ':
                cells[int(command[0].strip()) - 1] = X
                ## AI
                os.system('cls')
                perameters.creat_grid()
                game_state()
            elif command.lower() == 'quit':
                exit()
            else:
                print('Wrong command!! Try again')
                turns = False
        else:
            command = input('Press 1 through 9 [{}]: '.format(p_2_d)).strip()
            turns = False
            if command.strip().isnumeric() and cells[int(command[0].strip()) - 1] == ' ':
                cells[int(command[0].strip()) - 1] = O
                ## AI
                os.system('cls')
                perameters.creat_grid()
                game_state()
            elif command.lower().strip() == 'quit':
                exit()
            else:
                print('Wrong command!! Try again')
                turns = True
    
Game()        

