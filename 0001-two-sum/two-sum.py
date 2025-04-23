class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force: nested for loop comparing every number with each other
        # to see if it will add up to the target. T=o(n^2) S=o(1)

        # efficient: use a dictionary, if target-curr in dictionary and curr + dict val = target
        # return, else insert that value into the dictionary

        numDict = defaultdict(int)
        
        for i in range(len(nums)):
            if target-nums[i] in numDict.keys():
                return [i, numDict[target-nums[i]]]
            else:
                numDict[nums[i]] = i

        