import random
import time
from copy import copy

from linear_search import linear_search
from binary_search import binary_search
from bubble_sort import bubble_sort
from quick_sort import sort_quick 

# --- Configuration ---
TEST_SIZES = [100, 500, 1000]
# Use a target value guaranteed NOT to be in the array (0-10000) 
# to measure worst-case time for search algorithms.
TARGET_NOT_FOUND = 10001 


def generate_random_data(size):
    """Generates an array of random integers."""
    return [random.randint(0, 10000) for _ in range(size)]

def run_tests():
    """Runs all algorithm tests and prints the results."""

    # --- MEMBER 1: LINEAR SEARCH ---
    print("--- Member 1 Results ---")
    print("Algorithm: Linear Search")
    print("Input Size | Time (ms)")
    print("----------------------")
    
    for size in TEST_SIZES:
        arr = generate_random_data(size)
        
        # Linear Search timing
        start_time = time.perf_counter_ns()
        linear_search(arr, TARGET_NOT_FOUND)
        end_time = time.perf_counter_ns()
        
        time_in_ms = (end_time - start_time) / 1_000_000.0
        print(f"{size:<10} | {time_in_ms:.2f}")

    print("\n" + "="*30 + "\n")


    # --- MEMBER 2: BINARY SEARCH ---
    print("--- Member 2 Results ---")
    print("Algorithm: Binary Search")
    print("Input Size | Time (ms)")
    print("----------------------")

    for size in TEST_SIZES:
        # We need to test the search time on a sorted array.
        # We use a copy of the random data, sort it, and then measure the search.
        base_arr = generate_random_data(size)
        sorted_arr = sorted(base_arr) # Use built-in sort for speed and reliability

        # Binary Search timing
        start_time = time.perf_counter_ns()
        binary_search(sorted_arr, TARGET_NOT_FOUND)
        end_time = time.perf_counter_ns()
        
        time_in_ms = (end_time - start_time) / 1_000_000.0
        print(f"{size:<10} | {time_in_ms:.2f}")

    print("\n" + "="*30 + "\n")


    # --- MEMBER 3: BUBBLE SORT ---
    print("--- Member 3 Results ---")
    print("Algorithm: Bubble Sort")
    print("Input Size | Time (ms)")
    print("----------------------")

    for size in TEST_SIZES:
        # Generate the list and make a copy to pass to the sort function
        base_arr = generate_random_data(size)
        arr_to_sort = copy(base_arr)
        
        # Bubble Sort timing
        start_time = time.perf_counter_ns()
        bubble_sort(arr_to_sort)
        end_time = time.perf_counter_ns()
        
        time_in_ms = (end_time - start_time) / 1_000_000.0
        print(f"{size:<10} | {time_in_ms:.2f}")
        
    print("\n" + "="*30 + "\n")


    # --- MEMBER 4: QUICK SORT ---
    print("--- Member 4 Results ---")
    print("Algorithm: Quick Sort")
    print("Input Size | Time (ms)")
    print("----------------------")
    
    for size in TEST_SIZES:
        # Generate the list and make a copy to pass to the sort function
        base_arr = generate_random_data(size)
        arr_to_sort = copy(base_arr)

        # Quick Sort timing
        start_time = time.perf_counter_ns()
        sort_quick(arr_to_sort)
        end_time = time.perf_counter_ns()
        
        time_in_ms = (end_time - start_time) / 1_000_000.0
        print(f"{size:<10} | {time_in_ms:.2f}")

    print("\n" + "="*30 + "\n")


if __name__ == "__main__":
    run_tests()