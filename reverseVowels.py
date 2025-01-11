class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        left , right =0, len(s_list)-1
        while left <=right:
            s_list[left] ,s_list[right] = s_list[right], s_list[left]
            left+=1
            right-=1
        return " ".join(s_list)
sol = Solution()
print(sol.reverseWords("hello world"))