# MSCS532_Assignment_5

This repository contains implementations of algorithms and data structures as part of Assignment 5. Each file demonstrates a specific concept with example usage and performance analysis.

---

## Files and How to Run Them

### 1. **`Quick_Sort.py`**
- **Description:** Implements Quicksort to sort arrays.
- **How to Run:**
  ```bash
  python Quick_Sort.py

### 2. **`Randomizied_Quick_Sort.py`**
- **Description:** Implements Randomized Quicksort using the first element as the pivot..
- **How to Run:**
  ```bash
  python Randomizied_Quick_Sort.py

### 3. **`Randomizied_and_Deterministic_Quick Sort.py`**
- **Description:** Implements Randomized and Deterministic Quicksort using the first element as the pivot and performance times for randomizied and deterministic partitioning across test cases..
- **How to Run:**
  ```bash
  python Randomizied_and_Deterministic_Quick Sort.py

###  **`Summary of Findings`**
QuickSort is a divide-and-conquer sorting algorithm that selects a pivot, partitions the array into elements smaller and larger than the pivot, and recursively sorts the subarrays. Its time complexity depends on partitioning efficiency: in the best and average cases, it achieves O(n log n) when partitions are balanced, while in the worst case, when partitions are highly unbalanced, it degrades to O(n²). The space complexity is O(log n) in the best and average cases due to recursion depth, but it can reach O(n) in the worst case. Randomized QuickSort improves performance by selecting a pivot randomly, reducing the likelihood of worst-case behavior and ensuring an expected time complexity of O(n log n). Empirical analysis shows that deterministic QuickSort performs poorly on sorted or reverse-sorted input, leading to O(n²) performance, whereas randomized QuickSort maintains O(n log n) efficiency across different input types. Optimization strategies such as random pivot selection, tail call optimization, or iterative implementations help improve QuickSort’s efficiency and stability in practical applications.
