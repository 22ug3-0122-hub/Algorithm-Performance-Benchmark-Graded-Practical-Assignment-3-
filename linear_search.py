#22ug3-0474

def linear_search(arr, target):
    """
    Implements the Linear Search algorithm.
    Time Complexity: O(n)
    
    Args:
        arr (list): The array to search through.
        target (int): The element to find.

    Returns:
        int: The index of the target element, or -1 if not found.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1