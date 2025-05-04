class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visitedLand = set()

        def spread(row, col):
            if grid[row][col] == "1" and (row,col) not in visitedLand:
                visitedLand.add((row,col))
                if row+1 < len(grid):
                    spread(row+1, col)
                if row-1 >= 0:
                    spread(row-1, col)
                if col+1 < len(grid[0]):
                    spread(row, col+1)
                if col-1 >= 0:
                    spread(row, col-1)
            else:
                return

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row,col) in visitedLand or grid[row][col] == "0":
                    continue
                else:
                    islands += 1
                    spread(row, col)

        return islands