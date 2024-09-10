from collections import deque

def breadth_first_search(graph, start_node, end_node, parent):
    visited = {node: False for node in graph}
    
    if end_node not in visited:
        visited[end_node] = False

    queue = deque([start_node])
    visited[start_node] = True

    while queue:
        current_node = queue.popleft()

        for adj_node, capacity in graph[current_node].items():
            if not visited[adj_node] and capacity > 0:
                queue.append(adj_node)
                visited[adj_node] = True
                parent[adj_node] = current_node

                if adj_node == end_node:
                    return True
    return False

def ford_fulkerson(graph, start_node, end_node):
    parent = {}
    max_flow = 0

    residual_graph = {node: dict(neighbors) for node, neighbors in graph.items()}

    if end_node not in residual_graph:
        residual_graph[end_node] = {}

    while breadth_first_search(residual_graph, start_node, end_node, parent):
        path_flow = float('Inf')
        current_node = end_node

        while current_node != start_node:
            path_flow = min(path_flow, residual_graph[parent[current_node]][current_node])
            current_node = parent[current_node]

        current_node = end_node
        while current_node != start_node:
            parent_node = parent[current_node]
            residual_graph[parent_node][current_node] -= path_flow
            residual_graph[current_node][parent_node] = residual_graph.get(current_node, {}).get(parent_node, 0) + path_flow
            current_node = parent[current_node]

        max_flow += path_flow
    
    return max_flow


# Exemplos

graph1 = {
    'A' : {'B': 5, 'C': 8},
    'B' : {'C': 4, 'D': 6},
    'C' : {'D': 2},
}

graph2 = {
    'A': {'B': 10, 'D': 10},
    'B': {'C': 4, 'D': 2, 'E': 8},
    'C': {'F': 10}, 
    'D': {'E': 9},
    'E': {'C': 6, 'F': 10},
    'F': {}
}

# Saídas
# print(ford_fulkerson(graph1, 'A', 'D'))  # Saída Esperada: 7
# print(ford_fulkerson(graph2, 'A', 'F'))  # Saída Esperada: 19
