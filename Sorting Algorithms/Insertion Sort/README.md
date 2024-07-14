# Insertion Sort Algorithm in Python

This repository contains an implementation of the insertion sort algorithm in Python. The insertion sort algorithm is a simple and efficient sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

## Implementation

The implementation of the insertion sort algorithm is provided in the `insertion_sort` function. The function takes a list of numbers as input and returns the sorted list.

# Insertion Sort Algorithm Implementation

The implementation of the insertion sort algorithm is provided in the `insertion_sort` function. The function takes a list of numbers as input and returns the sorted list.

## Explanation

### Function Definition

- The function `insertion_sort` is defined to take a list of numbers `nums` as its parameter.

### Outer Loop

- The outer loop starts at the second element (index 1) and iterates through each element of the list until the last element.
- `for i in range(1, len(nums)):` iterates through the list starting from the second element.

### Key Element

- The key is set to the current element being considered in the outer loop.
- `key = nums[i]` stores the current element.

### Inner Loop

- The inner `while` loop compares the key with elements before it in the list.
- It shifts elements one position to the right if they are greater than the key.
- `while j >= 0 and nums[j] > key:` checks if the previous elements are greater than the key.

### Element Shifting

- If the element at `nums[j]` is greater than `key`, it is moved one position to the right.
- `nums[j + 1] = nums[j]` shifts the element to the right.
- `j -= 1` decrements the index to continue comparing with the previous elements.

### Insert Key

- When the correct position for the key is found, it is inserted into the list.
- `nums[j + 1] = key` places the key in its correct position.

### Return Sorted List

- The sorted list `nums` is returned after the outer loop has processed all elements.
- `return nums` returns the sorted list.
