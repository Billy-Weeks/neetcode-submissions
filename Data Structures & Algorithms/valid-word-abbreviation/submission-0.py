class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # grab lengths of word/abbr
        lengthWord = len(word)
        lengthAbbr = len(abbr)

        # two pointers
        wordPointer = 0
        abbrPointer = 0

        # loop
        while wordPointer < lengthWord and abbrPointer < lengthAbbr:
            # return False if even a leading zero
            if abbr[abbrPointer] == '0':
                return False
            
            # check if same char
            if word[wordPointer] == abbr[abbrPointer]:
                wordPointer += 1
                abbrPointer += 1

            # they don't match BUT abbr is still a char
            elif abbr[abbrPointer].isalpha():
                return False
            
            # abbr[wordPointer] is currently a digit
            else:
                subLength = 0
                while abbrPointer < lengthAbbr and abbr[abbrPointer].isdigit():
                    subLength = subLength * 10 + int(abbr[abbrPointer])
                    abbrPointer += 1
                # increase wordPointer past the correct num of chars
                wordPointer += subLength
        return wordPointer == lengthWord and abbrPointer == lengthAbbr
