class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        result=[]
        for i,w in enumerate(words):
            prefix=1
            for j,v in enumerate(words):
                if i==j or len(w)!=len(v) or w[-1]!=v[-1]:continue
                k=0
                while w[k]==v[k]:k+=1
                prefix=max(prefix,k+1)
            result.append(w if prefix>=len(w)-2 else w[:prefix]+str(len(w)-prefix-1)+w[-1])
        return result
