from typing import List

def q7(q: int, queries: List[List[int]]) -> List[int]:
    totalHeros = []
    totalAttri = []
    
    def calculate_rounds():
        totalHeros.sort(reverse=True)
        totalAttri.sort(reverse=True)
        
        rounds = 0
        hero = 0
        attri = 0
        
        while hero < len(totalHeros):
            health = totalHeros[hero]
            
            if attri < len(totalAttri):
                artifact = totalAttri[attri]
                
                while health > 0 and artifact > 0:
                    a = len(totalHeros)
                    b = attri + 1  
                    deduction = 1 / (a + b)
                    health -= deduction
                    artifact -= deduction
                    rounds += 1
                
                if artifact <= 0:
                    attri += 1
            
            while health > 0:
                health -= 1
                rounds += 1
            
            hero += 1
        
        return rounds

    result = []
    
    for t, v in queries:
        if t == 1:
            totalHeros.append(v)
        elif t == 2:
            totalAttri.append(v)
        
        result.append(calculate_rounds())
    
    return result

q = int(input())
queries = [list(map(int, input().split())) for _ in range(q)]

output = q7(q, queries)
for rounds in output:
    print(rounds)
