class Solution:
    def isPalindrome(self, s: str) -> bool:
        # do the same thing but using functional programming instead of imperative
        filtered = "".join(filter(str.isalnum, s)).lower()
        return filtered == filtered[::-1]
