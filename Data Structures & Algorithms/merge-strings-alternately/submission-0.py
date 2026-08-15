class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # grab one letter from each string and make a new one

        # Grab lengths of strings
        string1_length = len(word1)
        string2_length = len(word2)

        print(string1_length)
        print(string2_length)

        # Use two pointers, one for each word
        word1_index = 0
        word2_index = 0

        # Blank output string
        output = ""
        
        # use while loop to make sure we aren't at end of eithe string
        while word1_index < string1_length and word2_index < string2_length:
            # Concatenate char to existing string
            output += word1[word1_index]
            output += word2[word2_index]

            #increment indices
            word1_index += 1
            word2_index += 1
        # Add remaining characters, if any    
        output += word1[word1_index: ]
        output += word2[word2_index: ]

        return output
