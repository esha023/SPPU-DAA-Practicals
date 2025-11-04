import random

def partition_lomuto(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def partition_random(arr, low, high):
    pivot_idx = random.randint(low, high)
    arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
    return partition_lomuto(arr, low, high)

def quicksort(arr, low, high, partition_function):
    if low < high:
        pi = partition_function(arr, low, high)
        quicksort(arr, low, pi - 1, partition_function)
        quicksort(arr, pi + 1, high, partition_function)

while True:
    try:
        print("\nPress Ctrl+C to exit...")
        array_str = input("Enter array (space-separated numbers): ")
        original_array = [int(i) for i in array_str.split()]

        if not original_array:
            continue

        arr_deterministic = original_array.copy()
        arr_randomized = original_array.copy()

        print("Deterministic variant:")
        quicksort(arr_deterministic, 0, len(arr_deterministic) - 1, partition_lomuto)
        print(arr_deterministic)
        
        print("Randomized variant:")
        quicksort(arr_randomized, 0, len(arr_randomized) - 1, partition_random)
        print(arr_randomized)

    except (KeyboardInterrupt, EOFError):
        print("\nExiting...")
        break
    except ValueError:
        print("Invalid input. Please enter only space-separated numbers.")