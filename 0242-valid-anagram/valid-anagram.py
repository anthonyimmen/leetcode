class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # use a dictionary with letter and occurences compare if they are identical
        # use default dict to set the default type value for the keys

        sDict = defaultdict(int)
        tDict = defaultdict(int)

        for letter in s:
            sDict[letter] += 1
        
        for letter in t:
            tDict[letter] += 1

        return sDict == tDict
        