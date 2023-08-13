import os

colb = 7
row = 7

values = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

X = 'X'
O = 'O'

def creat_grid():
    for c in range(7):  
        if c == 1:       
            print(' '*3 + "{}".format(values[0])+ ' '*3+'|' + ' '*3 + "{}".format(values[1]) + ' '*3 + '|' +' '*3+ "{}".format(values[2]))
        elif c == 3:
            print(' '*3 + "{}".format(values[3])+ ' '*3+'|' + ' '*3 + "{}".format(values[4]) + ' '*3 + '|' +' '*3+ "{}".format(values[5]))
        elif c == 5:
            print(' '*3 + "{}".format(values[6])+ ' '*3+'|' + ' '*3 + "{}".format(values[7]) + ' '*3 + '|' +' '*3+ "{}".format(values[8]))
        else:
            print(' '*row + '|' + ' '*row + '|'+' '*row)
        if c == 1 or c == 3:
            print('_'*colb + '|' + '_'*colb + '|'+'_'*colb)

creat_grid()

command = int(input('press 1 through 9: '))

if command:
    values[command - 1] = X
    os.system('cls')
    creat_grid()
else:
    print('Wrong command')
#
#if command == '3':
#    os.system('cls')
#    for c in range(6):
#        print(' '*row + '|' + ' '*row + '|'+ ' X ')
#        count += 1
#        if count == 2:
#            print('-'*colb)
#        if count == 4:
#            print('-'*colb)
#