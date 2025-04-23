class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # implement kadane's algorithm

        smallest = 0
        maxSum = -float('inf')
        currSum = 0

        for num in nums:
            smallest = min(num, smallest)
            currSum += num
            if currSum < smallest:
                currSum = num
            elif num > currSum:
                currSum = num
            maxSum = max(currSum, maxSum)
        
        return maxSum
        