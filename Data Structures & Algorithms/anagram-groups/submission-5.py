class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # mapping each charcount to a list 
        res = defaultdict(list)

        #loop thur the words
        for word in strs:
            # grap all letters in abcs
            count = [0] * 26 

             # loop thur each charcater in the word
            for c in word:
             #
                count[ord(c) - ord("a")] += 1

                #append res with word
            res[tuple(count)].append(word)
              #return res as list
        return list(res.values())
            
                

       

       
            