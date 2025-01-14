from polygon_calculator import polygon_all_data

if __name__ == '__main__':
    for i in range(2, 101):
        print('==============================================')
        print(f'Polygon with {i} sides')
        print('==============================================')
        polygon_all_data(i, 2)