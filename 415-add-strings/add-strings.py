
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num = 0
        mun = 0
        carry = 0
        ans = ""

        i = len(num1) - 1
        j = len(num2) - 1

        while i >= 0 or j >= 0:
            if i >= 0:
                num = ord(num1[i]) - ord('0')
            else:
                num = 0

            if j >= 0:
                mun = ord(num2[j]) - ord('0')
            else:
                mun = 0

            total = num + mun + carry

            rem = total % 10
            carry = total // 10

            ans = str(rem) + ans

            i -= 1
            j -= 1

        if carry:
            ans = str(carry) + ans

        return ans

