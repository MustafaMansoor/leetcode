def can_sum(target_sum, numbers):
    table = [False] * (target_sum + 1)
    table[0] = True

    for i in range(target_sum + 1):
        if table[i] == True:
            for num in numbers:
                if i + num <= target_sum:
                    table[i + num] = True

    return table[target_sum]

# Example usage:
print(can_sum(7, [2, 3]))  # Example call, modify as needed
