class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        left = 0
        right = 0

        while right < len(strs[0]):
            for word in strs:
                if strs[0][left:right+1] == word[left:right+1]:
                    continue
                else:
                    return strs[0][left:right]
            right += 1
        
        return strs[0][left:right]

               
        