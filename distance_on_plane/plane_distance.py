def plane_distance_calculator(moves:int, pos_x:list, pos_y:list) -> str:

    base_x = 0 # Point X of the base
    base_y = 0 # Point Y of the base

    if len(pos_x) != len(pos_y):
        return 'Bad input: lists with positions X and Y do not have the same number of elements.'
    
    for i in range(len(pos_x)-1):
        distance_to_travel = ((abs(base_x + pos_x[i])) + (abs(base_y + pos_y[i]))) * 2

        if moves > distance_to_travel:
            moves -= distance_to_travel

            print(f'Travelling from base to point [{pos_x[i]}, {pos_y[i]}]. Length of trip is {distance_to_travel}.')
            print(f'Moves left: {moves}.')
            print('=======================')

        else:
            return f'Distance to travel is {distance_to_travel}. We are short {abs(moves-distance_to_travel)} moves.'

if __name__ == '__main__':
    moves = 60 # Number of units how many can be travelled
    pos_x = [6, -4, -7, -2, 7, 3, -3, 4, -5] # List of X positions
    pos_y = [2, -5, -2, 4, -5, 2, 5, -2, -1] # List of Y positions
    print(plane_distance_calculator(60, pos_x, pos_y))