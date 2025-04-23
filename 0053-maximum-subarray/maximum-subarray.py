class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # implement kadane's algorithm: T=O(n) S=O(1)

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

        # correct implementation of kadane's algo
        # maxSum = nums[0]
        # currSum = 0

        # for num in nums:
        #     if currSum < 0:
        #         currSum = 0
        #     currSum += num
        #     maxSum = max(currSum, maxSum)
        # return maxSum
        