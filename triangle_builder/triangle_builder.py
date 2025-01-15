import random

def generate_numbers_to_file(filename, triangles_num):
    with open(filename, 'w') as file:
        for i in range(triangles_num):
            for j in range(3):
                number = random.randint(1, 10)
                if j == 2:
                    file.write(f'{number}\n')
                else:
                    file.write(f'{number},')

def triangle_builder(filename, filename_correct, filename_incorrect):
    with open(filename, 'r') as file:
        for line in file:
            processed_line = [int(num) for num in line.strip().split(',')]
            if max(processed_line) / sum(processed_line) >= 0.5:
                with open(filename_incorrect, 'a') as file_incorrect:
                    file_incorrect.write(f"{','.join(map(str, processed_line))}\n")
            else:
                with open(filename_correct, 'a') as file_correct:
                    file_correct.write(f"{','.join(map(str, processed_line))}\n")

if __name__ == '__main__':
    filename = 'result/data.txt' # Destination for list of all randomly generated potential triangles
    triangles_num = 100 # Number of generated potential triangles
    filename_correct = 'result/triangle_correct.txt' # Destination for list of correct triangles
    filename_incorrect = 'result/triangle_incorrect.txt' # Destination for list of incorrect triangles
    generate_numbers_to_file(filename, triangles_num)
    triangle_builder(filename, filename_correct, filename_incorrect)