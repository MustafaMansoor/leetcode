from collections import defaultdict
def dijkstra(n, graph, start):
    dist = [float('inf')] * n
    dist[start] = 0
    count = [0] * n  # Count of shortest paths
    count[start] = 1
    pred = [[] for _ in range(n)]  # Predecessor list
    
    # Min-heap priority queue (Manually implemented using list)
    heap = [(0, start)]
    
    while heap:
        heap.sort()  # Sort heap to simulate priority queue
        d, u = heap.pop(0)
        
        if d > dist[u]:
            continue
        
        for v, weight in graph[u]:
            alt = dist[u] + weight
            if alt < dist[v]:
                dist[v] = alt
                count[v] = count[u]
                pred[v] = [u]
                heap.append((dist[v], v))
            elif alt == dist[v]:
                count[v] += count[u]
                pred[v].append(u)
    
    return dist, count, pred

def calculate_betweenness_centrality(n, graph):
    betweenness = [0] * n
    
    for s in range(n):
        dist, count, pred = dijkstra(n, graph, s)
        dependency = [0] * n
        
        stack = []
        for v in range(n):
            if v != s:
                stack.append(v)
        stack.reverse()
        
        while stack:
            w = stack.pop()
            for v in pred[w]:
                dependency[v] += (count[v] / count[w]) * (1 + dependency[w])
            if w != s:
                betweenness[w] += dependency[w]
    
    for i in range(n):
        betweenness[i] /= 2
    
    return betweenness

def main():
    T = int(input())  # Number of test cases
    for _ in range(T):
        n, m = map(int, input().split())  # Number of nodes and edges
        graph = defaultdict(list)
        
        for _ in range(m):
            u, v = map(int, input().split())
            graph[u-1].append((v-1, 1))
            graph[v-1].append((u-1, 1))  # Since the graph is undirected
        
        # Calculate Betweenness Centrality using Brandes' Algorithm
        betweenness = calculate_betweenness_centrality(n, graph)
        
        # Find top 5 nodes with highest betweenness centrality
        top_nodes = sorted(range(1, n + 1), key=lambda x: (-betweenness[x-1], x))
        
        print(" ".join(map(str, top_nodes[:5])))
    

if __name__ == "__main__":
    main()
