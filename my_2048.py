import random


def print_field(field):
    print('\n'*40)
    print ('Use:     |5|     \n'
           '      |1||2||3|  \n')
    for line in field:
        for ch in line:
            print(ch, '  ',   end='')
        print()
    print('-'*20)


def start_game(field: list):
    for i in range(3):
        field[3][i] = 2
    random.shuffle(field[3])
    return field


def rotate(field):
    new_l = zip(*field[::-1])
    field.clear()
    for i in new_l:
        field.append(list(i))


def left_move(field: list):
    empty_cell = 0
    for line in field:
        for i in range(3):
            if line[i] == line[i+1] and line[i] > 0:
                line[i] = line[i]*2
                line[i+1] = 0
        for _ in range(4):
            for j in range(3):
                if line[j] == 0:
                    line.append(line.pop(j))
        empty_cell += line.count(0)
    if empty_cell > 0:
        random.choice(field)[3] = 2
    else:
        print('GAME OVER!')
    return field


def right_move(field: list):
    for line in field:
        line.reverse()
    left_move(field)
    for line in field:
        line.reverse()
    return field


def down_move(field):
    rotate(field)
    left_move(field)
    for _ in '270': rotate(field)
    return field


def up_move(field):
    for _ in '270': rotate(field)
    left_move(field)
    rotate(field)
    return field


main_field = [[0] * 4 for i in range(4)]
start_game(main_field)
print_field(main_field)
while True:
    key = input('Move')
    if key == '1':
        left_move(main_field)
        print_field(main_field)
    elif key == '3':
        right_move(main_field)
        print_field(main_field)
    elif key == '5':
        up_move(main_field)
        print_field(main_field)
    elif key == '2':
        down_move(main_field)
        print_field(main_field)
