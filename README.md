# leetcode Questions
### Problem n°1: 1598. Crawler Log Folder
we need to return the minimum number of operations needed to go back to the main folder after the change folder operations.
first thoughts
* Loop over the logs
* Maybe use some regex
* Since the output is the sum of the steps needed to go from main to the last folder, why not replace the logs by a numerical value symbolizing the step taken
  Example: "../" is -1 if there is a folder beforehands (meaning the sum of the folders crawled is >0)
           "./" is always 0 because we remain in the same folder
           "x/" is +1 because it means all the other folders (the folder is guaranteed to exist so no regex needed and it will be the else of the other cases)


  
