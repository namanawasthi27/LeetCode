class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        l=sorted(score)
        l.reverse()
        j=[]
        for i in range(0,len(score)):
            if score[i]==l[0]:
                j.append("Gold Medal")
            elif score[i]==l[1]:
                j.append("Silver Medal")
            elif score[i]==l[2]:
                j.append("Bronze Medal")
            else:
                h=score[i]
                j.append(str(l.index(h)+1))
        return j


