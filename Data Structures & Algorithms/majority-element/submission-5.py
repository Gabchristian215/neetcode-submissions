class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1
            half = len(nums) // 2
            if count[n] > half:
                return n
        

       
            
                
               
               
               
            
            
            

        