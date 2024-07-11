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
