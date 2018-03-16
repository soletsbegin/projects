import time

def get_file(file):
    new_file = list(open(file))
    new_list = [line.ljust(len(max(new_file, key=len))) for line in new_file]
    pattern = []
    for line in range(len(new_list)):
        pattern.append('')
        for ch in new_list[line]:
            if ch.isspace():
                pattern[line] += " "
            else:
                pattern[line] += '*'
    pattern.insert(0, ' '*len(new_list[0]))
    pattern.append(' '*len(new_list[0]))
    return [line.ljust(len(line) + 1, ' ').rjust(len(line) + 2, ' ') for line in pattern]


def print_world(list):
    print('\n'*40)
    for line in list:
        print(line)


def check_cell(list, line, ch):
    """Сумма в ячейках вокруг координат.

    >>> check_cell([' * ', '   ', '  *'], 1, 1)
    2
    >>> check_cell(['  *', ' **', '  *'], 1, 1)
    3
    """
    s = list[line-1][ch-1:ch+2] + list[line][ch-1:ch+2] + list[line+1][ch-1:ch+2]
    count = len([i for i in s if i == '*'])
    if list[line][ch] == '*': count -= 1
    return count


def check_char(check_list, line, ch):
    """Return ' ' or '*'

    >>> check_char([' * ', '   ', '  *'], 1, 1)
    ' '
    >>> check_char(['  *', ' **', '  *'], 1, 1)
    '*'
    >>> check_char(['  *', ' **', ' **'], 1, 1)
    ' '
    >>> check_char(['  *', '  *', '  *'], 1, 1)
    '*'
    """
    if check_list[line][ch] == ' ':
        if check_cell(check_list, line, ch) == 3:
            return '*'
        else:
            return ' '
    else:
        if check_cell(check_list, line, ch) < 2 or check_cell(check_list, line, ch) > 3:
            return ' '
        elif 2 <= check_cell(check_list, line, ch) <= 3:
            return  '*'


def born_or_die(list):
    """Создаёт новый массив:
    - появляется ячейка если рядом 3 не пустые;
    - остается не пустая если рядом 2 или 3 не пустые;
    - исчезает не пустая если рядом больше 3 не пустых или меньше 2.

    >>> born_or_die(['     ', '  *  ', '  *  ', '  *  ', '     '])
    ['     ', '     ', ' *** ', '     ', '     ']
    >>> born_or_die(['     ', ' *** ', '     ', ' *** ', '     '])
    ['     ', '  *  ', '     ', '  *  ', '     ']
    >>> born_or_die(['     ', ' *** ', ' *** ', ' *** ', '     '])
    ['     ', ' * * ', '     ', ' * * ', '     ']

    """

    new_list = []
    new_list.append(' '*len(list[0]))
    for l in range(1, len(list)-1):
        new_list.append(' ')
        for ch in range(1, len(list[l])-1):
            new_list[l] += check_char(list, l, ch)
        new_list[l] += ' '
    new_list.append(' ' * len(list[0]))
    return new_list


if __name__ == '__main__':
    # print(born_or_die(['     ',
    #                     '  *  ',
    #                     '  *  ',
    #                     '  *  ',
    #                     '     ']))
    import doctest
    doctest.testmod()
    #
    # ['###',
    #  ' ##',
    #  '###']