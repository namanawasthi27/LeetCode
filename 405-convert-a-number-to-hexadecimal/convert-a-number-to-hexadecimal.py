class Solution:
    def toHex(self, num: int) -> str:
        if num < 0:
            num = num & 0xFFFFFFFF
            
            
        elif num==0:
            return "0"
        ans=""
        while num>0:
            rem=num%16
            q=num//16
            if rem==10:
                rem="a"
            elif rem==11:
                rem="b"
            elif rem==12:
                rem="c"
            elif rem==13:
                rem="d"
            elif rem==14:
                rem="e"
            elif rem==15:
                rem="f"
            ans=str(rem)+ans
            num=q
        return ans