class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        allCaps=word.upper()
        allLower=word.lower()
        firstCaps=word.title()
        return word==allCaps or word==allLower or word==firstCaps