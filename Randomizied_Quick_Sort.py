import random

def randomized_quicksort(arr):
    """
    Sorts an array using the Randomized Quicksort algorithm.

    Args:
        arr (list): The list of elements to be sorted.

    Returns:
        list: The sorted list.
    """
    if len(arr) <= 1:
        # Base case: An array with 0 or 1 elements is already sorted.
        return arr

    # Step 1: Choose a random pivot.
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    # Step 2: Partition the array.
    # Elements smaller than the pivot go to the 'less' list.
    # Elements greater than the pivot go to the 'greater' list.
    less = []  # Subarray of elements less than the pivot.
    greater = []  # Subarray of elements greater than the pivot.

    for i, element in enumerate(arr):
        if i == pivot_index:
            continue  # Skip the pivot itself.
        if element <= pivot:
            less.append(element)
        else:
            greater.append(element)

    # Step 3: Recursively apply Quicksort to the subarrays.
    sorted_less = randomized_quicksort(less)  # Sort the 'less' subarray.
    sorted_greater = randomized_quicksort(greater)  # Sort the 'greater' subarray.

    # Step 4: Combine the sorted subarrays and the pivot.
    return sorted_less + [pivot] + sorted_greater

# Example usage
if __name__ == "__main__":
    sample_array = [34, 7, 23, 32, 5, 62]
    print("Original array:", sample_array)
    sorted_array = randomized_quicksort(sample_array)
    print("Sorted array:", sorted_array)
