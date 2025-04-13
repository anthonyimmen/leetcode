class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = defaultdict(int)

        # create the hash map
        for letter in s:
            letters[letter] += 1

        print(letters)
        
        longest = 0
        for key, value in letters.items():
            if value % 2 == 0:
                longest += value
            else:
                longest += value - 1

        # essentially means that it had an odd value
        if longest < len(s):
            longest += 1

        return longest
        