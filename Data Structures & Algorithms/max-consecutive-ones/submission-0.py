class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        count = 0
        high_count = 0

        for i in range(len(nums)):
            current_num = nums[i]
            

            if current_num == 1:
                count += 1
            else:
                count = 0
                
            if count > high_count:
                high_count = count
                
            

        return high_count


      
       
            
            
          
              

            

            














        # return the max number in the array how many number is a row before they change to a diffrent number 
        
        