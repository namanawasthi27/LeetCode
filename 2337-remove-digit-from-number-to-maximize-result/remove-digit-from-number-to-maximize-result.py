class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        ans=""
        
        for i in range(len(number)):
            if number[i]==digit:
                temp=number[:i]+number[i+1:]
                if temp>ans:
                    ans=temp
        return ans

