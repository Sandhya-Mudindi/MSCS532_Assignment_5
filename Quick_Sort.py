def quicksort(arr):
    """
    Sorts an array using the Quicksort algorithm.

    Args:
        arr (list): The list of elements to be sorted.

    Returns:
        list: The sorted list.
    """
    if len(arr) <= 1:
        # Base case: An array with 0 or 1 elements is already sorted.
        return arr

    # Step 1: Choose a pivot.
    # Here, we are choosing the last element as the pivot.
    pivot = arr[-1]

    # Step 2: Partition the array.
    # Elements smaller than the pivot go to the 'less' list.
    # Elements greater than the pivot go to the 'greater' list.
    less = []  # Subarray of elements less than the pivot.
    greater = []  # Subarray of elements greater than the pivot.

    for element in arr[:-1]:  # Iterate through all elements except the pivot.
        if element <= pivot:
            less.append(element)
        else:
            greater.append(element)

    # Step 3: Recursively apply Quicksort to the subarrays.
    sorted_less = quicksort(less)  # Sort the 'less' subarray.
    sorted_greater = quicksort(greater)  # Sort the 'greater' subarray.

    # Step 4: Combine the sorted subarrays and the pivot.
    return sorted_less + [pivot] + sorted_greater

# Example usage
if __name__ == "__main__":
    sample_array = [34, 7, 23, 32, 5, 62]
    print("Original array:", sample_array)
    sorted_array = quicksort(sample_array)
    print("Sorted array:", sorted_array)
