class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # iterate over magazine and construct the dict

        mag = defaultdict(int)

        for letter in magazine:
            mag[letter] += 1

        for letter in ransomNote:
            if letter in mag and mag[letter] > 0:
                mag[letter] -= 1
            else:
                return False

        return True
        