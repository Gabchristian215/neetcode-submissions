class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for c, w in zip(pattern, words):
            # Existing character must map to the same word
            if c in char_to_word and char_to_word[c] != w:
                return False

            # Existing word must map to the same character
            if w in word_to_char and word_to_char[w] != c:
                return False

            # Add the mapping if it has not been seen
            char_to_word[c] = w
            word_to_char[w] = c

        return True

            
                       

                   

                
                

       

                
        



               

            
            


       
           
                    
                
        

         