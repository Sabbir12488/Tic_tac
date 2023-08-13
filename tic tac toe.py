import os

colb = 20
row = 6

count = 0

#while True:
for c in range(6):
    print(' '*row + '|' + ' '*row + '|'+' '*row)
    count += 1
    if count == 2:
        print('-'*colb)
    if count == 4:
        print('-'*colb)
    
command = input('press 1 through 9: ')

if command == '3':
    os.system('cls')
    for c in range(6):
        print(' '*row + '|' + ' '*row + '|'+ ' X ')
        count += 1
        if count == 2:
            print('-'*colb)
        if count == 4:
            print('-'*colb)
