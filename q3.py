from collections import deque, defaultdict

def find_centroids(n, connections):
    if n == 1:  # Special case for a single node
        return [0]
    
    # Step 1: Build the adjacency list
    graph = defaultdict(list)
    degrees = [0] * n
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)
        degrees[u] += 1
        degrees[v] += 1
    
    # Step 2: Initialize the queue with all leaf nodes
    leaves = deque([i for i in range(n) if degrees[i] == 1])
    
    # Step 3: Remove leaf nodes iteratively
    remaining_nodes = n
    while remaining_nodes > 2:
        leaf_count = len(leaves)
        remaining_nodes -= leaf_count
        
        for _ in range(leaf_count):
            leaf = leaves.popleft()
            for neighbor in graph[leaf]:
                degrees[neighbor] -= 1
                if degrees[neighbor] == 1:
                    leaves.append(neighbor)
    
    # Step 4: Remaining nodes are centroids
    return list(leaves)

# Input Handling
def main():
    t = int(input())  # Number of test cases
    results = []
    
    for _ in range(t):
        n = int(input())  # Number of nodes
        connections = []
        
        for __ in range(n - 1):
            u, v = map(int, input().split())
            connections.append([u, v])
        
        # Find centroids for this test case
        centroids = find_centroids(n, connections)
        results.append(len(centroids))  # Count of centroids
    
    # Print all results
    for result in results:
        print(result)

# Run the main function
main()
