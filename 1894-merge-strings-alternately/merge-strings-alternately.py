class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        merged = ""
        counter = 0

        while True:
            if counter < len(word1):
                merged += word1[counter]
            else:
                merged += word2[counter:]
                break
            if counter < len(word2):
                merged += word2[counter]
            else:
                merged += word1[counter+1:]
                break
            counter += 1

        return merged