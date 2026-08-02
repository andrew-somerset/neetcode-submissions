class Solution:
    def isHappy(self, n: int) -> bool:
        prev_guesses = {}
        z = 0
        while int(n) != 1:
            summ = 0
            n = str(n)
            for i in n:
                summ += int(i) * int(i)
            n = summ
            if n in prev_guesses.values():
                return False
            else:
                prev_guesses[z] = n
                z += 1
        return True

            

        