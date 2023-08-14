import os
import random

class perameters(object):
    game_over = False
    grid_size = 7
    spacing = grid_size - 4
    def creat_grid():
        for c in range(7):  
            if c == 1:       
                print(' '*perameters.spacing + "{}".format(cells[0])+ ' '*perameters.spacing +'|' + ' '*perameters.spacing + "{}".format(cells[1]) + ' '*perameters.spacing + '|' + ' '*perameters.spacing + "{}".format(cells[2]))
            elif c == 3:
                print(' '*perameters.spacing + "{}".format(cells[3])+ ' '*perameters.spacing +'|' + ' '*perameters.spacing + "{}".format(cells[4]) + ' '*perameters.spacing + '|' + ' '*perameters.spacing + "{}".format(cells[5]))
            elif c == 5:
                print(' '*perameters.spacing + "{}".format(cells[6])+ ' '*perameters.spacing +'|' + ' '*perameters.spacing + "{}".format(cells[7]) + ' '*perameters.spacing + '|' + ' '*perameters.spacing + "{}".format(cells[8]))
            else:
                print(' '*perameters.grid_size + '|' + ' '*perameters.grid_size + '|'+' '*perameters.grid_size)
            if c == 1 or c == 3:
                print('_'*perameters.grid_size + '|' + '_'*perameters.grid_size + '|'+'_'*perameters.grid_size)

cells = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

command = 0

X = 'X'
O = 'O'


x_won = 'X WON!!!'
o_won = 'O WON!!!'


print('-----------------------------------------')
print('||            tic tac toe              ||')
print('-----------------------------------------\n')
input("Press Enter to continue...")
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
        if cells.count(' ') == 1 and perameters.game_over == False:
            print("Game is a draw!!")
            game_over()

def Game():

    perameters.creat_grid()

    turns = False
    while ' ' in cells and not perameters.game_over:
        if not turns:
            command = input('Press 1 through 9 [ X ]: ').strip()
            turns = True
            if command.strip().isnumeric() and cells[int(command[0].strip()) - 1] == ' ':
                cells[int(command[0].strip()) - 1] = X
                ## AI
                os.system('cls')
                perameters.creat_grid()
                game_state()
            elif command.lower() == 'quit':
                game_over()
            else:
                print('Wrong command!! Try again')
                turns = False
        else:
            command = input('Press 1 through 9 [ O ]: ')
            turns = False
            if command.strip().isnumeric() and cells[int(command[0].strip()) - 1] == ' ':
                cells[int(command[0].strip()) - 1] = O
                ## AI
                os.system('cls')
                perameters.creat_grid()
                game_state()
            elif command.lower().strip() == 'quit':
                game_over()
            else:
                print('Wrong command!! Try again')
                turns = True
    
Game()        

