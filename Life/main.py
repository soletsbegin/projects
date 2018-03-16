import time
import life

world = life.get_file('pattern.txt')
life.print_world(world)
while True:
    time.sleep(0.2)
    world = life.born_or_die(world)
    life.print_world(world)
