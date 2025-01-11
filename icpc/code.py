import sys
import heapq

def solve_network_planning(N, M, edges):
    INF = float('inf')
    adj = [[] for _ in range(N + 1)]
    
    # Build the graph from the edges list
    for U, V, D in edges:
        adj[U].append((V, D))
        adj[V].append((U, D))
    
    min_avg_delay = INF
    best_router = -1
    
    # Try each router as the source
    for s in range(1, N + 1):
        D = [INF] * (N + 1)
        D[s] = 0
        heap = [(0, s)]
        
        while heap:
            dist_v, v = heapq.heappop(heap)
            if dist_v > D[v]:
                continue
            for w, weight in adj[v]:
                new_dist = D[v] + weight
                if D[w] > new_dist:
                    D[w] = new_dist
                    heapq.heappush(heap, (D[w], w))
        
        total_delay = 0
        reachable_nodes = 0
        # Calculate total delay for all reachable nodes
        for i in range(1, N + 1):
            if i != s and D[i] != INF:
                total_delay += D[i]
                reachable_nodes += 1
        
        # Only compute average delay if there are reachable nodes
        if reachable_nodes > 0:
            avg_delay = total_delay / reachable_nodes
            if avg_delay < min_avg_delay or (avg_delay == min_avg_delay and s < best_router):
                min_avg_delay = avg_delay
                best_router = s
    
    return best_router

# Input reading section
input = sys.stdin.read().split()
idx = 0
t = int(input[idx])
idx += 1
results = []

for _ in range(t):
    N = int(input[idx])
    M = int(input[idx + 1])
    idx += 2
    edges = []
    for _ in range(M):
        U = int(input[idx])
        V = int(input[idx + 1])
        D = float(input[idx + 2])
        edges.append((U, V, D))
        idx += 3
    best_router = solve_network_planning(N, M, edges)
    results.append(best_router)

# Output the result for each test case
print('\n'.join(map(str, results)))
