print("Lab 3 - Software Unit Testing with PyTest")

SORT_ASCENDING = 0
SORT_DESCENDING = 1


def bubble_sort(arr, sorting_order):

    # REQ-05: If any value entered is not an integer, return 2
    for value in arr:
        if not isinstance(value, int):
            return 2

    # Get number of elements in the list
    n = len(arr)

    # REQ-04: If 0 numbers are entered, return 0
    if n == 0:
        return 0

    # REQ-03: If >= 10 numbers are entered, return 1
    if n >= 10:
        return 1

    # Copy input list to results list
    arr_result = arr.copy()

    # REQ-01 and REQ-02: Sort only if fewer than 10 integers are entered
    for i in range(n - 1):
        for j in range(0, n - i - 1):

            if sorting_order == SORT_ASCENDING:
                if arr_result[j] > arr_result[j + 1]:
                    arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]

            elif sorting_order == SORT_DESCENDING:
                if arr_result[j] < arr_result[j + 1]:
                    arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]

            else:
                # If sorting order is invalid, return an empty list
                return []

    return arr_result


def main():
    # Driver code to test above
    arr = [64, 34, 25, 12, 22, 11, 90]

    # Sort in ascending order
    result = bubble_sort(arr, SORT_ASCENDING)
    print("\nSorted array in ascending order:")
    print(result)

    # Sort in descending order
    result = bubble_sort(arr, SORT_DESCENDING)
    print("\nSorted array in descending order:")
    print(result)

    # Test 0 numbers
    result = bubble_sort([], SORT_ASCENDING)
    print("\nResult when 0 numbers are entered:")
    print(result)

    # Test >= 10 numbers
    result = bubble_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], SORT_ASCENDING)
    print("\nResult when 10 or more numbers are entered:")
    print(result)

    # Test non-integer values
    result = bubble_sort([5, 3, "a", 1], SORT_ASCENDING)
    print("\nResult when non-integer values are entered:")
    print(result)


if __name__ == "__main__":
    main()