class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=set("aeiou")
        maxVow =0
        left,right=0,k
        for i in range(0,k):
            if s[i] in vowels:
                maxVow+=1

        curr=maxVow
        while right < len(s):
            if(s[left] in vowels):
                curr-=1
           
            if(s[right] in vowels):
                curr+=1
            maxVow = max(maxVow,curr)
            left+=1
            right+=1
        return maxVow
sol= Solution()

print(sol.maxVowels("abciiidef",3))
        