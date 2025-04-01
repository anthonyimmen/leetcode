class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # simple binary search, keep halving until you reach the number you are looking for
        # do not change the list, just change the search indices
        # when the window is length 1, stop and check

        start, end = 0, len(nums)-1
        half = round((end - start)/2)
        while start <= end:
            if nums[half] == target:
                return half
            if nums[half] > target:
                end = half - 1
                half = round((end - start)/2)
            else:
                start = half + 1
                half = round((end + start)/2)
        
        return -1

        