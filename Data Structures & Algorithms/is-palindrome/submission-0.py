class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alp = []
        reverse = []
        for i in s:
            if i.isalnum():
                s_alp.append(i.lower())
        
        for j in range(len(s_alp) - 1, -1, -1):
            reverse.append(s_alp[j])
        
        if s_alp == reverse:
            return True
        return False