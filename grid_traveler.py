def grid_traveler(m, n):
    # Create a (m+1) x (n+1) table initialized with 0s
    table = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Set base case
    table[1][1] = 1

    # Iterate through the grid
    for i in range(m + 1):
        for j in range(n + 1):
            current = table[i][j]
            if j + 1 <= n:
                table[i][j + 1] += current  # Move right
            if i + 1 <= m:
                table[i + 1][j] += current  # Move down

    return table[m][n]

# Example usage
print(grid_traveler(3, 3))  # Output: 1
