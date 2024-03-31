def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    
    # Compare elements from both arrays and add the smaller one to the result
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    
    # Add remaining elements from left array
    while left_idx < len(left):
        result.append(left[left_idx])
        left_idx += 1
    
    # Add remaining elements from right array
    while right_idx < len(right):
        result.append(right[right_idx])
        right_idx += 1
    
    return result

# Example usage:
arr = list(input("enter terms:\n").split())
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
