class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1
        next = 0

        # start from the bottom and work up to the top
        for i in range(n-1, 0, -1):
            next = one + two
            temp = one
            one = next
            two = temp
        
        return one