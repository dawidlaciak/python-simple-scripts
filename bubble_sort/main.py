def bubble_sort(obj:list) -> list:

    for i in range(len(obj)):
        for j in range(0, len(obj) - 1):
            if obj[j] > obj[j+1]:
                obj[j], obj[j+1] = obj[j+1], obj[j]

    return obj

def median(obj:list) -> float:

    if len(obj) % 2 == 1:
        median_value = obj[len(obj) // 2]
    else:
        median_value = (obj[len(obj) // 2] + obj[len(obj) // 2 - 1]) / 2
    
    return median_value

if __name__ == '__main__':
    sorted_list = bubble_sort([20, 7, 5, 8, 9, 22, 34, 6, 18, 15])
    print(f'Sorted list: {sorted_list}')
    median_value = median(sorted_list)
    print(f'Median value of sorted list is {median_value}.')
