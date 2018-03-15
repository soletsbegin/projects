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
                pattern[line] += '#'
    return pattern


world = get_file('pattern.txt')
for i in world:
    print(repr(i))