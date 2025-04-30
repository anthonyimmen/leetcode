class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # dfs in all directions

        original = image[sr][sc]

        def fill(box, r, c):
            print(box, r, c)
            if box[r][c] == color:
                return box
            if box[r][c] == original:
                box[r][c] = color
                if r+1 < len(box):
                    fill(box, r+1, c)
                if c+1 < len(box[0]):
                    fill(box, r, c+1)
                if r-1 >= 0:
                    fill(box, r-1, c)
                if c-1 >= 0:
                    fill(box, r, c-1)
            return box
        
        return fill(image, sr, sc)





        