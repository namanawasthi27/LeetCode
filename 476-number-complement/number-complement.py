class Solution:
    def findComplement(self, num: int) -> int:
        binary=bin(num)
        v=str(binary[2:])
        ans=""
        for i in range(0,len(v)):
            if v[i]=="1":
                ans+="0"
            else:
                ans+="1"
        return int(ans,2)
