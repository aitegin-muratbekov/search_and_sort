def binary_search(a, list_for_search):
    lowest = list_for_search[0]
    highest = len(list_for_search) - 1
    result_is_found = False
    while True:
        if lowest < highest:
            middle = (lowest + highest) // 2
            if a == list_for_search[middle]:
                lowest = middle
                highest = lowest
                result_is_found = True
            elif a > list_for_search[middle]:
                lowest = middle + 1
            else:
                highest = highest - 1
        else:
            if result_is_found == True:
                print(middle)
                return f'Найден элемент'

            else:
                return f'Элемент не найден'

def bubble_sort(your_list):
    for counter in range(0, 7):
        for i in your_list:
            numb_index = your_list.index(i)
            next_numb_index = numb_index + 1
            if (len(your_list)-1)-counter >= next_numb_index:
                if i > your_list[next_numb_index]:
                    your_list[numb_index] = your_list[next_numb_index]
                    your_list[next_numb_index] = i
                else:
                    pass
            else:
                pass
    return your_list

print(bubble_sort([2, 42, 12, 23, 235, 1023, 43, 11, 43]))

print(binary_search(4, list(range(50))))







