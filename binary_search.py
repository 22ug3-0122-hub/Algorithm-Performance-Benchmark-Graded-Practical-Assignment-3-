#22ug3-0604 

def binary_search(arr, target):
    """
    Implements the Binary Search algorithm (requires a sorted array).
    Time Complexity: O(log n)

    Args:
        arr (list): The sorted array to search through.
        target (int): The element to find.

    Returns:
        int: The index of the target element, or -1 if not found.
    """
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1