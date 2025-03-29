class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        exists = defaultdict(int)

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in exists:
                return [i, exists[diff]]
            else:
                exists[nums[i]] = i
        