import os
import random

values = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

command = 0

X = 'X'
O = 'O'

class perameters(object):
    grid_size = 7
    spacing = grid_size - 4
    def creat_grid():
        for c in range(7):  
            if c == 1:       
                print(' '*perameters.spacing + "{}".format(values[0])+ ' '*perameters.spacing +'|' + ' '*perameters.spacing + "{}".format(values[1]) + ' '*perameters.spacing + '|' + ' '*perameters.spacing + "{}".format(values[2]))
            elif c == 3:
                print(' '*perameters.spacing + "{}".format(values[3])+ ' '*perameters.spacing +'|' + ' '*perameters.spacing + "{}".format(values[4]) + ' '*perameters.spacing + '|' + ' '*perameters.spacing + "{}".format(values[5]))
            elif c == 5:
                print(' '*perameters.spacing + "{}".format(values[6])+ ' '*perameters.spacing +'|' + ' '*perameters.spacing + "{}".format(values[7]) + ' '*perameters.spacing + '|' + ' '*perameters.spacing + "{}".format(values[8]))
            else:
                print(' '*perameters.grid_size + '|' + ' '*perameters.grid_size + '|'+' '*perameters.grid_size)
            if c == 1 or c == 3:
                print('_'*perameters.grid_size + '|' + '_'*perameters.grid_size + '|'+'_'*perameters.grid_size)


perameters.creat_grid()


def AI():
    if values[2] == X:
        if random.randint(1, 100) < 70 and values[4] == ' ':
            values[4] = O
        else:
            values[3] = O
        

def Game():

    while ' ' in values:
        command = int(input('Press 1 through 9: '))

        if command and values[command - 1] == ' ':
            values[command - 1] = X
            ## AI
            AI()

            os.system('cls')
            perameters.creat_grid()
        else:
            print('Wrong command!! Try again')

Game()        


