class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        a = len(str1)
        b=len(str2)
        if str1 + str2 != str2+str1:
            return ""
        rem = 0 
        while True:
            if a % b == 0:
                rem = b
                break
            rem = a % b
            a=b
            b=rem

        return str1[0:rem]
sol = Solution()
print(sol.gcdOfStrings("ABCABC","ABC") )