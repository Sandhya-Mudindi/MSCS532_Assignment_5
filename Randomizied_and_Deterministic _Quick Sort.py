import random  # To generate random numbers
import time  # To measure runtime
import sys  # To modify system settings like recursion limit
sys.setrecursionlimit(10000)  # Increase recursion limit to handle large inputs

def randomized_partition(arr, low, high):
    """Partition the array with a randomly chosen pivot."""
    # Choose a random index for the pivot
    pivot_index = random.randint(low, high)
    # Swap the pivot with the last element in the range
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]  # Set the pivot value
    i = low - 1  # Index for smaller element

    # Rearrange elements around the pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place the pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # Return the pivot's final position

def randomized_quicksort(arr, low, high):
    """Recursively apply randomized quicksort on the array."""
    if low < high:
        # Partition the array and get the pivot index
        partition_index = randomized_partition(arr, low, high)
        # Recursively sort elements before and after the pivot
        randomized_quicksort(arr, low, partition_index - 1)
        randomized_quicksort(arr, partition_index + 1, high)

def deterministic_partition(arr, low, high):
    """Partition the array using the first element as the pivot."""
    pivot = arr[low]  # Choose the first element as the pivot
    i = low + 1  # Start index for elements greater than pivot
    for j in range(low + 1, high + 1):
        if arr[j] < pivot:  # If current element is smaller than pivot
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements
            i += 1  # Move index for greater element

    # Place the pivot in its correct position
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1  # Return the pivot's final position

def deterministic_quicksort(arr, low, high):
    """Recursively apply deterministic quicksort on the array."""
    if low < high:
        # Partition the array and get the pivot index
        partition_index = deterministic_partition(arr, low, high)
        # Recursively sort elements before and after the pivot
        deterministic_quicksort(arr, low, partition_index - 1)
        deterministic_quicksort(arr, partition_index + 1, high)

def quicksort_randomized(arr):
    """Helper function to sort an array using randomized quicksort."""
    if arr is None or len(arr) <= 1:  # Handle edge cases
        return arr
    randomized_quicksort(arr, 0, len(arr) - 1)  # Sort the array
    return arr

def quicksort_deterministic(arr):
    """Helper function to sort an array using deterministic quicksort."""
    if arr is None or len(arr) <= 1:  # Handle edge cases
        return arr
    deterministic_quicksort(arr, 0, len(arr) - 1)  # Sort the array
    return arr

def generate_test_cases():
    """Generate various test cases for sorting algorithms."""
    sizes = [100, 1000, 5000, 10000]  # Different input sizes
    test_cases = {
        "Random": [random.sample(range(1, size * 10), size) for size in sizes],  # Random arrays
        "Sorted": [list(range(size)) for size in sizes],  # Already sorted arrays
        "Reverse": [list(range(size, 0, -1)) for size in sizes],  # Reverse sorted arrays
        "Repeated": [[random.choice(range(10)) for _ in range(size)] for size in sizes]  # Arrays with repeated values
    }
    return sizes, test_cases

def measure_runtime(quicksort_fn, arrays):
    """Measure the runtime of a quicksort function on given test cases."""
    runtimes = []
    for arr in arrays:
        start_time = time.time()  # Record the start time
        quicksort_fn(arr[:])  # Use a copy to preserve the original array
        end_time = time.time()  # Record the end time
        runtimes.append(end_time - start_time)  # Calculate elapsed time
    return runtimes

def main():
    """Main function to compare the performance of quicksort algorithms."""
    sizes, test_cases = generate_test_cases()  # Generate test cases

    print("Empirical Comparison of Quicksort Algorithms:\n")

    # Iterate through each test case
    for case_name, arrays in test_cases.items():
        print(f"Test Case: {case_name}")

        # Measure runtimes for both algorithms
        random_runtimes = measure_runtime(quicksort_randomized, arrays)
        deterministic_runtimes = measure_runtime(quicksort_deterministic, arrays)

        # Print results
        print("Array Size\tRandomized Quicksort\tDeterministic Quicksort")
        for size, rand_time, det_time in zip(sizes, random_runtimes, deterministic_runtimes):
            print(f"{size}\t\t{rand_time:.6f}\t\t{det_time:.6f}")
        print()

if __name__ == "__main__":
    main()  # Execute the main function
