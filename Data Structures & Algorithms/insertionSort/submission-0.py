class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res = []

        for i in range(len(pairs)):
            j = i - 1

            # Bubble the current element left while it's smaller
            while j >= 0 and pairs[j].key > pairs[j + 1].key:
                pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
                j -= 1

            # Save state after insertion
            res.append(pairs[:])

        return res