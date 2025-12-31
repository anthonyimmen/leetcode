class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = defaultdict(int)
        for i in range(len(nums)):
            if target-nums[i] in numDict.keys():
                return [i, numDict[target-nums[i]]]
            else:
                numDict[nums[i]] = i


        