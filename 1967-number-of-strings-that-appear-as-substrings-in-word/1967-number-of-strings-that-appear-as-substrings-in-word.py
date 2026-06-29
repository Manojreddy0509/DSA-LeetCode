class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        n=0
        for wo in patterns:
            if wo in word:
                n+=1
        return n

        