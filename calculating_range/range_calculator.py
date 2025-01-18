def range_calculator(movement_field):

    positions_amount = len(movement_field)
    max_range = 0
    current_position = 0

    while current_position < positions_amount and current_position <= max_range:

        move_range = movement_field[current_position]
        max_range = max(max_range, current_position + move_range)
        current_position += 1
    
    if current_position == positions_amount:
        return True
    else:
        return False
    
if __name__ == '__main__':
    movement_field = [2,3,2,0,0,2,0,1]
    print(range_calculator(movement_field))
