import random
import numbers

"""
This file include functions for game 2048
"""


def start_game():
    """generate list 4*4 and adds 3 deuces randomly to the list[3]

    >>> start_game()
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    """
    field = [[0] * 4 for i in range(4)]
    return field


def chance():
    """ gives 2 - 91% and 4 9%"""
    if random.random() <= 0.91: return 2
    else: return 4


def empty_cells(field):
    """create list with coordinates of empty cells

    >>> empty_cells([[2, 0], [2, 0]])
    [(0, 1), (1, 1)]
    >>> empty_cells([[2, 2], [2, 2]])
    []
    """
    return [(x, y) for x in range(len(field)) for y in range(len(field[x])) if field[x][y] == 0]


def print_field(field):
    """Print list like a string"""
    print('\n'*40)
    print ('Use:     |5|     \n'
           '      |1||2||3|  \n')
    for line in field:
        for ch in line:
            print(ch, '  ', end='')
        print()
    print('-'*20)


def rotate(field):
    """Rotates list 90 degrees to the right"""
    new_l = zip(*field[::-1])
    field.clear()
    for i in new_l:
        field.append(list(i))
    return field


def add_2(field):
    """Add 2 in right side of list"""
    empty_list = []
    for i in range(4):
        if 0 in field[i]:
            empty_list.append(i)
        else: continue
    if len(empty_list) > 0:
        field[random.choice(empty_list)][3] = 2
    else: print('GAME OVER!!!')
    return field


def left_move(field: list):
    """Main def for move, we will use this def for move in all directions    """

    for line in field:
        for _ in range(4):
            for j in range(3):
                if line[j] == 0:
                    line.append(line.pop(j))
        for i in range(3):
            if line[i] == line[i+1] and line[i] > 0:
                line[i] *= 2
                line[i+1] = 0
        for _ in range(4):
            for j in range(3):
                if line[j] == 0:
                    line.append(line.pop(j))
    return field


def right_move(field: list):
    """reverse, use left_move and reverse again
    """
    for line in field:
        line.reverse()
    left_move(field)
    for line in field:
        line.reverse()
    return field


def down_move(field):
    """rotate, use left_move and rotate to the starting position"""
    rotate(field)
    left_move(field)
    for _ in '270': rotate(field)
    return field


def up_move(field):
    """rotate, use left_move and rotate to the starting position"""
    for _ in '270': rotate(field)
    left_move(field)
    rotate(field)
    return field


def draw_field(field):
    """This function draws a colored field with a module - numbers.py"""
    print('\n' * 40)
    print('Use:     |5|     \n'
          '      |1||2||3|  \n')
    for j in [0, 1, 2, 3]:
        for i in [0, 1, 2]:
            for n in [0, 1, 2, 3]:
                print(numbers.numbers[field[j][n]][i], end='  ')
            print()
        print()


if __name__ == '__main__':
    import doctest
    doctest.testmod()

#     main_field = start_game()
#     draw_field(main_field)
#     while True:
#         key = input('Move')
#         if key == '1':
#             left_move(main_field)
#             draw_field(main_field)
#         elif key == '3':
#             right_move(main_field)
#             draw_field(main_field)
#         elif key == '5':
#             up_move(main_field)
#             draw_field(main_field)
#         elif key == '2':
#             down_move(main_field)
#             draw_field(main_field)
