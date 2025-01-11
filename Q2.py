T = int(input())  # Number of test cases
for _ in range(T):
    M, C = map(int, input().split())  # Budget and number of garment categories
    garments = []
    
    for _ in range(C):
        K = int(input())  # Number of models in this category (not used directly)
        prices = list(map(int, input().split()))  # Prices of models
        garments.append(prices)
    
    # DP approach
    dp = [set() for _ in range(C + 1)]
    dp[0].add(0)  # Starting with a cost of 0
    
    for g in range(1, C + 1):
        for price in garments[g - 1]:
            for cost in dp[g - 1]:
                if cost + price <= M:  # Ensure we don't exceed the budget
                    dp[g].add(cost + price)
    
    max_cost = max(dp[C]) if dp[C] else -1  # Maximum cost for all categories
    print(max_cost)
