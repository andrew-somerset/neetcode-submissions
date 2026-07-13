class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        Closed_to_Open = {"}": "{", "]": "[", ")": "("}
        for i in range(len(s)):
            if s[i] in Closed_to_Open and not stack:
                return False
            elif s[i] in Closed_to_Open and stack:
                if Closed_to_Open[s[i]] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(s[i])
        return True if not stack else False
            



            




            

        