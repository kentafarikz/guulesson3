def binary_search(arr, target):
    """
    Бинарный поиск в упорядоченном массиве.

    :param arr: Упорядоченный массив чисел.
    :param target: Значение, которое нужно найти.
    :return: Индекс значения в массиве, если найдено; -1, если не найдено; количество операций.
    """
    left, right = 0, len(arr) - 1
    operations = 0

    while left <= right:
        operations += 1  # Увеличить счетчик операций

        mid = (left + right) // 2

        if arr[mid] == target:
            return mid, operations
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, operations


# Пример использования
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 9

    index, operations = binary_search(arr, target)

    if index != -1:
        print(f"Значение {target} найдено на индексе {index}.")
    else:
        print(f"Значение {target} не найдено в массиве.")

    print(f"Количество операций: {operations}")
