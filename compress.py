from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        rep ,curr ,count = 0,0,1
        while curr < len(chars):
            if curr + 1 >= len(chars) or chars[curr] != chars[curr + 1]:
                chars[rep] = chars[curr]
                rep += 1
                if count > 1:
                    for digit in str(count):
                        chars[rep] = digit
                        rep += 1
                count = 1
            else:
                count += 1
            curr += 1
            
        return rep

sol = Solution()
print(sol.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b","a","a","a"]))