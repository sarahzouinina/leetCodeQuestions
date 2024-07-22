class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Transpose the grid to get the columns as rows
        grid_transpose = list(map(list, zip(*grid)))
        cpt = 0
        for g in grid:
            for ng in grid_transpose:
                if g == ng:
                    cpt += 1
        return cpt
