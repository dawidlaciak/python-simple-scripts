from random import randint

def generate_board(size):
    
    board = [[0] * size for x in range(size)]  
    layers = (size + 1) // 2 
    
    for layer in range(layers):
        for i in range(layer, size - layer):
            for j in range(layer, size - layer):
                board[i][j] = layer
                
    return board

def throw_dart(board, darts_type):
    row_num = randint(0, len(board) - 1)
    column_num = randint(0, len(board[0]) - 1)

    print(f'You threw dart hitting point [{row_num+1}, {column_num+1}].')

    points_card = []

    radius = 1 if darts_type == 3 else 2

    for i in range(row_num - radius, row_num + radius + 1):
        for j in range(column_num - radius, column_num + radius + 1):
            if 0 <= i < len(board) and 0 <= j < len(board[0]):
                points_card.append(board[i][j])
    
    print(f"Points in area: {points_card}")
    return sum(points_card)


if __name__ == '__main__':

    board_size = 13 # Number of columns and rows in board
    darts_type = 3 # What radius from the point of impact player scores points - 3x3 for 3 and 5x5 for 5
    board = generate_board(board_size)

    for row in board:
        print(' '.join(map(str, row)))

    print(f'Total points scored: {throw_dart(board, darts_type)}')
    
