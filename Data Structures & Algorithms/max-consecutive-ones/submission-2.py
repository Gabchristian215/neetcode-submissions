class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        total = 0 
        max_num = 0

        for num in nums:
            if num == 1:
                total += num
            if num == 0:
                total = 0
            if total > max_num:
                max_num = total

        return max_num
        