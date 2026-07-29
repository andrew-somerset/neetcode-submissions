class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_freq = {}

        for i in s:
            if i not in char_freq:
                char_freq[i] = 1
            else:
                char_freq[i] += 1
            
        for i in t:
            if i not in char_freq:
                return False
            else: 
                char_freq[i] -= 1

        for i in char_freq:
            if char_freq[i] != 0:
                return False
            
        return True

        