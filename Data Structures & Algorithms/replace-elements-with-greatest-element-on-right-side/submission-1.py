class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        r_max = -1
        for i in range(len(arr)-1, -1, -1):
            curr = arr[i]
            arr[i] = r_max
            if r_max < curr:
                r_max = curr
        return arr