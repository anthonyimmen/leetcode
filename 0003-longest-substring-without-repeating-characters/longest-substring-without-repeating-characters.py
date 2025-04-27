class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # kadane's algorithm?
        maxSum = 0

        # keep's track of the index where it occured at
        appeared = defaultdict(int)
        left = 0

        for right in range(len(s)):
            print(right-left + 1)
            if s[right] in appeared and appeared[s[right]] >= left:
                left = appeared[s[right]] + 1
                appeared[s[right]] = right
            else:
                appeared[s[right]] = right
                maxSum = max(maxSum, right-left + 1)
        
        return maxSum

            





        