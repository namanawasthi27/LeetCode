class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator==0:
            return "0"
        ans=""
        if (numerator<0)!=(denominator<0):
            ans+="-"
        numerator=abs(numerator)
        denominator=abs(denominator)
        ans+=str(numerator//denominator)
        remainder=numerator%denominator
        if remainder==0:
            return ans
        ans+="."
        rem={}
        while remainder!=0:
            if remainder in rem:
                idx=rem[remainder]
                ans=ans[:idx]+"("+ ans[idx:]+")"
                return ans
            rem[remainder]=len(ans)
            remainder*=10
            ans+=str(remainder//denominator)
            remainder%=denominator
        return ans