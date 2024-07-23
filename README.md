# LeetCode Questions

## Problem #1: 1598. Crawler Log Folder

### Objective
Determine the minimum number of operations required to return to the main folder after performing a series of change folder operations.

### Initial Thoughts
To solve this problem, consider the following approach:
1. Loop through the logs to process each folder change operation.
2. Use numerical values to represent each type of operation, simplifying the computation of the steps needed to return to the main folder.

### Detailed Approach
- `../` represents moving up one directory. This can be symbolized by `-1` if there is a directory to move up to (i.e., the sum of the folders crawled so far is greater than 0).
- `./` represents staying in the current directory, which can be symbolized by `0` since no movement occurs.
- `x/` represents moving into a subdirectory. This can be symbolized by `+1`, as it always means entering a new directory.

Here's a more structured plan:
1. Initialize a variable to keep track of the current depth (initially set to 0).
2. Loop through each log entry:
   - If the entry is `../`, decrement the depth by 1, but only if the depth is greater than 0.
   - If the entry is `./`, do nothing (depth remains unchanged).
   - If the entry is a folder name (e.g., `x/`), increment the depth by 1.
3. The final value of the depth variable will be the minimum number of operations needed to return to the main folder.

### Example
Consider the following log entries:

["d1/", "d2/", "../", "d21/", "./"]

Processing these entries would result in the following steps:
- `d1/` -> +1 (current depth: 1)
- `d2/` -> +1 (current depth: 2)
- `../` -> -1 (current depth: 1)
- `d21/` -> +1 (current depth: 2)
- `./` -> 0 (current depth: 2)

Thus, the minimum number of operations needed to return to the main folder is 2.

## Problem #2: Roman to Integer

### Objective
Convert a given Roman numeral string to an integer.

### Approach
To solve this problem, the following approach can be implemented:

1. Create a dictionary that maps each Roman numeral symbol (including subtractive combinations like `IV` and `IX`) to its corresponding integer value.
2. Iterate through the string, checking for the presence of two-character subtractive combinations first. If found, append them to a list and skip the next character.
3. If a subtractive combination is not found, append the single character to the list.
4. After processing the entire string, sum up the values of the characters and combinations using the dictionary.

### Detailed Plan
1. Initialize a dictionary `roman_to_int` with the mappings from Roman numeral symbols to integers.
2. Initialize a variable `sum` to keep track of the total integer value.
3. Initialize an empty list `new_roman` to store the processed Roman numeral symbols.
4. Use a while loop to iterate through the string:
   - If a subtractive combination (two characters) is found in the dictionary, append it to `new_roman` and skip the next character.
   - If not, append the single character to `new_roman`.
5. Iterate through the `new_roman` list and sum up the values using the dictionary.
6. Return the total sum.

### Example
Given the Roman numeral string `s = "MCMXCIV"`:

1. `M` -> 1000
2. `CM` -> 900
3. `XC` -> 90
4. `IV` -> 4

Total: 1000 + 900 + 90 + 4 = 1994

## Problem #3: Move Zeroes

### Problem Statement

The task is to move all zeros in a given list to the end while maintaining the relative order of the non-zero elements. The solution must modify the list in-place without using extra space for another list.

### Initial Attempt

My initial attempt was to create a new list, `res`, to store the non-zero elements and then append zeros to it until it matched the length of the original list. The code looked like this:

```python
def moveZeroes(self, nums):
    i = 0
    res = []
    for i in nums:
        if i != 0:
            res.append(i)

    j = len(res)
    while j < len(nums):
        res.append(0)
        j += 1
    return res 
```
Issues with Initial Attempt
Not In-Place: This approach creates a new list res instead of modifying the original list nums in-place.
Return Value: The problem specifies not to return anything, but to modify the list directly.
## Problem #4: Find Maximum Average Subarray
Given an array of integers nums and an integer k, find the maximum average value of a subarray of length k.

### Input
nums: List of integers.
k: Integer representing the length of the subarray.
### Output
The function should return a float representing the maximum average value of a subarray of length k.
### Solution
Sliding Window Algorithm
To solve this problem efficiently, we can use the sliding window algorithm. The idea is to maintain a window of size k and slide it across the array while updating the sum and maximum average.
# Highest Altitude Problem

## Problem #5: Highest Altitude Problem

A biker is on a road trip consisting of `n + 1` points at different altitudes, starting at point 0 with an altitude of 0.

Given an integer array `gain` of length `n`, where `gain[i]` represents the net gain in altitude between points `i` and `i + 1` (for `0 <= i < n`), return the highest altitude reached.

#### Example 1
- **Input:** `gain = [-5, 1, 5, 0, -7]`
- **Output:** `1`
- **Explanation:** The altitudes are `[0, -5, -4, 1, 1, -6]`. The highest is `1`.

#### Example 2
- **Input:** `gain = [-4, -3, -2, -1, 4, 3, 2]`
- **Output:** `0`
- **Explanation:** The altitudes are `[0, -4, -7, -9, -10, -6, -3, -1]`. The highest is `0`.

## Solution

#### Method: `largestAltitude`

```python
def largestAltitude(self, gain):
    """
    :type gain: List[int]
    :rtype: int
    """
    i = len(gain)
    sum_element = []
    highest = 0
    while i > 0:
        sum_element.append(sum(gain[0:i]))
        i -= 1
    highest = max(sum_element)
    return max(highest, 0)
```
### Problem 6: Reverse Vowels of a String

This program reverses the vowels in a given string while preserving the positions of all non-vowel characters. It handles both lowercase and uppercase vowels.

#### Problem Statement

Given a string, reverse only the vowels and keep all other characters in their original positions.

The solution involves the following steps:

1. **Collecting Vowels**: Traverse the string and collect all vowels into a list.
2. **Reversing the Vowels**: Reverse the list of collected vowels.
3. **Constructing the Output**: Traverse the original string again and replace each vowel with the corresponding vowel from the reversed list while keeping non-vowel characters in their original positions.
 
 The solution needs more optimization 


### Problem 7: Reverse Words in a String
Given a string, reverse all the words without returning extra space.

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

### Problem 8: String Compression

This script implements a character compression algorithm that compresses an array of characters based on consecutive repetitions. Each group of consecutive characters is represented by the character followed by the number of times it appears consecutively, but only if it appears more than once. The compression is done in-place to utilize space efficiently, and the result modifies the original array of characters.

#### How It Works
The algorithm uses two pointers (read and write) to traverse and modify the array in-place. As the read pointer goes through the array, it counts occurrences of each character until a different character is encountered. The write pointer is used to write the character and its count (if greater than one) back into the array. This approach ensures that the space complexity remains constant, as no additional significant space is used apart from the input array.

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

### Problem 9: Distinct Elements Finder

This Python script helps in finding distinct elements between two lists. It effectively identifies and returns a list of integers that are present in one list but not in the other. The result is given in two sublists, where the first sublist contains elements unique to the first input list and the second sublist contains elements unique to the second input list.

#### Features

- Identify elements in `nums1` not present in `nums2`.
- Identify elements in `nums2` not present in `nums1`.
- Handles duplicate values within each list.
- Returns results in any order.


### Problem 10: Equal Row and Column Pairs

This project contains a solution to the [Equal Row and Column Pairs](https://leetcode.com/problems/equal-row-and-column-pairs/) problem from LeetCode.

#### Problem Description

Given a `n x n` matrix `grid`, the task is to return the number of pairs `(ri, cj)` such that row `ri` and column `cj` are equal.

#### Solution Approach
* Transpose the Matrix: Convert the columns of the matrix into rows.
* Compare Rows and Columns: Compare each row with each column to find matches.
* Count Matches: Count the number of pairs where a row and a column are equal.

### Problem 11: Max Number of K-Sum Pairs
#### Problem Statement
Given an integer array nums and an integer k, in one operation, you can pick two numbers from the array whose sum equals k and remove them from the array. Return the maximum number of operations you can perform on the array.

#### Solution: Two-Pointer Approach
This approach involves sorting the array and using two pointers to find pairs that sum up to k.
