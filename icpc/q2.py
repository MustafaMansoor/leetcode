from collections import Counter
def minimum_movements_to_symmetry(t, test_cases):
    results = []
    
    for test_case in test_cases:
        s = list(test_case)
        n = len(s)
        moves = 0
        
        freq = Counter(s)
        odd_count = sum(1 for count in freq.values() if count % 2 != 0)
        if odd_count > 1:
            results.append(-1)  
            continue
        
        left = 0
        right = n - 1
        
        while left < right:
            if s[left] == s[right]:
                
                left += 1
                right -= 1
            else:
               
                k = right
                while k > left and s[k] != s[left]:
                    k -= 1
                if k == left:
                   
                    s[left], s[left+1] = s[left+1], s[left]
                    moves += 1
                    
                else:
                   
                    while k < right:
                        s[k], s[k+1] = s[k+1], s[k]
                        moves += 1
                        k += 1
                   
                    left += 1
                    right -= 1
        
        results.append(moves)
    
    return results

t = int(input())
test_cases = [input().strip() for _ in range(t)]

output = minimum_movements_to_symmetry(t, test_cases)
for res in output:
    print(res)