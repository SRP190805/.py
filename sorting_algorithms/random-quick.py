import random

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def random_partition(arr, low, high):
    random_index = random.randint(low, high)
    arr[random_index], arr[high] = arr[high], arr[random_index]
    return partition(arr, low, high)

def random_quick_sort(arr, low, high):
    if low < high:
        pi = random_partition(arr, low, high)
        random_quick_sort(arr, low, pi - 1)
        random_quick_sort(arr, pi + 1, high)

# Example usage:
arr = list(input("enter terms:\n").split())
n = len(arr)
random_quick_sort(arr, 0, n - 1)
print("Sorted array is:", arr)
