def digital_root(num:int) -> int:

    while num > 9:
        num = 1 + ((num - 1) % 9)
    else:
        return num

if __name__ == '__main__':
    num = 354 # Number from which the digital root will be calculated
    print(f'Digital root for number {num} is {digital_root(num)}.')