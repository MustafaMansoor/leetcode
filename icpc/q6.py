from collections import deque, defaultdict

def mango_forest_analysis(test_cases):
    results = []
    for test in test_cases:
        V = test["V"]
        edges = test["edges"]

        adj = [[] for _ in range(V)]
        degrees = [0] * V  
        for u, v in edges:
            if u == v or not (0 <= u < V) or not (0 <= v < V):

                raise ValueError(f"Invalid edge between {u} and {v}")
            adj[u].append(v)
            adj[v].append(u)
            degrees[u] += 1
            degrees[v] += 1
        

        if not is_tree(adj, V):
            raise ValueError("The graph is not a tree")

        depth = tree_depth(adj, V)
        
        sorted_degrees = sorted(degrees, reverse=True)
        highest_degree = sorted_degrees[0]
        second_highest_degree = sorted_degrees[1] if V > 1 else 0

        results.append((depth, highest_degree, second_highest_degree))
    
    return results

def is_tree(adj, V):
    visited = [False] * V
    parent = [-1] * V
    queue = deque()
    queue.append(0)
    visited[0] = True
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                queue.append(v)
            elif parent[u] != v:
                
                return False

    return all(visited)

def tree_depth(adj, V):
    _, far_node = bfs(0, adj, V)

    max_dist, _ = bfs(far_node, adj, V)
    return max_dist

def bfs(start, adj, V):
    visited = [False] * V
    distance = [0] * V
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                distance[v] = distance[u] + 1
                queue.append(v)

    max_dist = max(distance)
    far_node = distance.index(max_dist)
    return max_dist, far_node

t = int(input())
test_cases = []
for _ in range(t):
    V = int(input())
    edges = []
    for _ in range(V - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
    test_cases.append({"V": V, "edges": edges})

results = mango_forest_analysis(test_cases)
for result in results:
    print(" ".join(map(str, result)))