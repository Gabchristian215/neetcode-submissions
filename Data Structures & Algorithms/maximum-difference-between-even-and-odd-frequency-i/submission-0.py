class Solution:
    def maxDifference(self, s: str) -> int:
        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        max_odd = 0
        min_even = float("inf")

        for freq in count.values():

            if freq % 2 == 1:
                max_odd = max(max_odd, freq)

            if freq % 2 == 0:
                min_even = min(min_even, freq)

        return max_odd - min_even

       
        




        