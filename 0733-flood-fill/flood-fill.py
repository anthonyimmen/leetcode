class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        startColor = image[sr][sc]

        print(len(image), len(image[0]))
        def fill(x, y, grid):
            if x < len(grid) and x >= 0 and y < len(grid[0]) and y >= 0: 
                if grid[x][y] == startColor and grid[x][y] != color:
                    grid[x][y] = color
                    fill(x+1, y, grid)
                    fill(x-1, y, grid)
                    fill(x, y+1, grid)
                    fill(x, y-1, grid)
            return grid
        
        return fill(sr, sc, image)
        