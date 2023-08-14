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




perameters.creat_grid()


#def AI():
#    if random.randint(1, 100) < 70 and values[4] == ' ':
#        values[4] = O
#    else:
#        values[3] = O
        

def game_state():
    ## to check if X won
    if set(cells[0:3]) == {X}:
        print(x_won)  
        perameters.game_over = True    
    elif set(cells[3:6]) == {X}:
        print(x_won)
        perameters.game_over = True
    elif set(cells[6:9]) == {X}:
        print(x_won)
        perameters.game_over = True
    elif cells[0] == X and cells[3] == X and cells[6] == X:
        print(x_won)
        perameters.game_over = True
    elif cells[0] == X and cells[4] == X and cells[8] == X:
        print(x_won)
        perameters.game_over = True
    elif cells[0] == X and cells[4] == X and cells[8] == X:
        print(x_won)
        perameters.game_over = True
    elif cells[2] == X and cells[5] == X and cells[8] == X:
        print(x_won)
        perameters.game_over = True
    elif cells[2] == X and cells[4] == X and cells[6] == X:
        print(x_won)
        perameters.game_over = True
    elif cells[1] == X and cells[4] == X and cells[7] == X:
        print(x_won)  
        perameters.game_over = True

    ## To check if O won
    if set(cells[0:3]) == {O}:
        print(o_won)
        perameters.game_over = True
    elif set(cells[3:6]) == {O}:
        print(o_won)
        perameters.game_over = True
    elif set(cells[6:9]) == {O}:
        print(o_won)
        perameters.game_over = True
    elif cells[0] == O and cells[3] == O and cells[6] == O:
        print(o_won)
        perameters.game_over = True
    elif cells[0] == O and cells[4] == O and cells[8] == O:
        print(o_won)
        perameters.game_over = True
    elif cells[0] == O and cells[4] == O and cells[8] == O:
        print(o_won)
        perameters.game_over = True
    elif cells[2] == O and cells[5] == O and cells[8] == O:
        print(o_won)
        perameters.game_over = True
    elif cells[2] == O and cells[4] == O and cells[6] == O:
        print(o_won)
        perameters.game_over = True
    elif cells[1] == O and cells[4] == O and cells[7] == O:
        print(o_won)
        perameters.game_over = True

    ##Check if its a draw
    if cells.count(' ') == 1 and perameters.game_over == False:
        print("Game is a draw!!")
        perameters.game_over = True


def Game():
    turns = False
    while ' ' in cells and not perameters.game_over:
        if not turns:
            command = int(input('Press 1 through 9 [ X ]: '))
            turns = True
            if command and cells[command - 1] == ' ':
                cells[command - 1] = X
                ## AI
                os.system('cls')
                perameters.creat_grid()
                game_state()
            else:
                print('Wrong command!! Try again')
        else:
            command = int(input('Press 1 through 9 [ O ]: '))
            turns = False
            if command and cells[command - 1] == ' ':
                cells[command - 1] = O
                ## AI
                os.system('cls')
                perameters.creat_grid()
                game_state()
            else:
                print('Wrong command!! Try again')

Game()        


