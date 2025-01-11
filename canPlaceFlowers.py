from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        
        if n == 0:
            return True
        
        for i in range(length):
            # Check if the current position can accommodate a flower
            if flowerbed[i] == 0:
                prev_empty = (i == 0 or flowerbed[i - 1] == 0)  # Check left
                next_empty = (i == length - 1 or flowerbed[i + 1] == 0)  # Check right
                
                if prev_empty and next_empty:
                    flowerbed[i] = 1  # Place a flower
                    n -= 1
                    if n == 0:  # If no more flowers need to be placed
                        return True
        
        return n == 0

# Test the function
sol = Solution()
print(sol.canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], 2))  # Expected output: True
