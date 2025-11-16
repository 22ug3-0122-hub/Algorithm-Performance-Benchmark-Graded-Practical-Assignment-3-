#22ug3-0122

def _partition(arr, low, high):
    """Partitions the sub-array around the pivot (last element)."""
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i] # Swap
            
    arr[i + 1], arr[high] = arr[high], arr[i + 1] # Swap pivot into correct position
    return i + 1

def quick_sort(arr, low, high):
    """
    Implements the Quick Sort algorithm.
    Average Time Complexity: O(n log n)

    Args:
        arr (list): The array to be sorted (modified in place).
        low (int): The starting index.
        high (int): The ending index.
    """
    if low < high:
        pivot_index = _partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def sort_quick(arr):
    """
    Wrapper function to call the recursive quick_sort with initial indices.
    
    Args:
        arr (list): The array to be sorted (modified in place).
    """
    quick_sort(arr, 0, len(arr) - 1)