# task_1

my_string = '0123456789'
for i in range(10):
    for j in range(10):
        print(int(my_string[i] + my_string[j]), end=' ')

# task_2
figure_height = int(input('\n\nInput figure height: '))

# figure A
for i in range(figure_height + 1):
    for j in range(figure_height):
        if j == figure_height - i:
            if i == 1:
                print('*', end='')
            elif 1 < i < figure_height:
                print('*' + ((i * 4) - 5) * ' ' + '*', end='')
            else:
                print('* ' * (i + figure_height - 1))
        else:
            print(' ', end=' ')
    print()

# figure B
for i in range(figure_height + 1):
    for j in range(figure_height):
        if j == figure_height - i:
            if i == 1:
                print('*', end='')
            else:
                print('*' + ((i * 2) - 2) * ' *', end='')
        else:
            print(' ', end=' ')
    print()

# figure C
for i in range(figure_height + 1):
    for j in range(figure_height):
        if j == figure_height - i:
            if i == 1:
                print('*', end='')
            else:
                print('*' + ((i * 2) - 2) * ' *', end='')
        else:
            print(' ', end=' ')
    print()
for i in range(figure_height - 1, 0, -1):
    if i == 1:
        print('  ' * (figure_height - 1) + '*')
    else:
        print('  ' * (figure_height - i) + '*' + ' ' * (i * 4 - 5) + '*')

# figure D
for i in range(figure_height + 1):
    for j in range(figure_height):
        if j == figure_height - i:
            if i == 1:
                print('*', end='')
            else:
                print('*' + ((i * 2) - 2) * ' *', end='')
        else:
            print(' ', end=' ')
    print()
for i in range(figure_height - 1, 0, -1):
    if i == 1:
        print('  ' * (figure_height - 1) + '*')
    else:
        print('  ' * (figure_height - i) + '*' + ' ' * int((i * 4 - 5) / 2) + '*' + ' ' * int((i * 4 - 6) / 2) + '*')
