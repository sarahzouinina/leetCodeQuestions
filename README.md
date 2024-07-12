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
