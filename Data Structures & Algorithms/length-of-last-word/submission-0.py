class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0

        for i in reversed(range(len(s))):
            if s[i] == " " and count == 0:
                continue

            if s[i] == " " and count > 0:
                break

            count += 1

        return count
 
   
 
           
              
          
        


          

       
        