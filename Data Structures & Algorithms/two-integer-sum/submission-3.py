class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     hash_map = {}

     for i, num in enumerate(nums):
        needs = target - num
        if needs in hash_map:
            return [hash_map[needs], i]

        hash_map[num] = i

        