import my_2048

main_field = my_2048.start_game()
for _ in range(3):
    my_2048.add_2(main_field)
my_2048.draw_field(main_field)
while True:
    key = input('Move')
    if key == '1':
        my_2048.left_move(main_field)
        my_2048.add_2(main_field)
        my_2048.draw_field(main_field)
    elif key == '3':
        my_2048.right_move(main_field)
        my_2048.add_2(main_field)
        my_2048.draw_field(main_field)
    elif key == '5':
        my_2048.up_move(main_field)
        my_2048.add_2(main_field)
        my_2048.my_2048.draw_field(main_field)
    elif key == '2':
        my_2048.down_move(main_field)
        my_2048.add_2(main_field)
        my_2048.draw_field(main_field)