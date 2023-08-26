def recursive_dfs(graph, node, visited):
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbor in graph[node]:
            recursive_dfs(graph, neighbor, visited)
def iterative_dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            # Push unvisited neighbors onto the stack
            stack.extend(neighbor for neighbor in graph[node] if neighbor not in visited)
def main():
    # Input the graph as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
        }
    # n = int(input("Enter the number of nodes: "))
    # for _ in range(n):
    #     node, neighbors = input("Enter node and its neighbors (space-separated): ").split()
    #     neighbors = neighbors.split(',')
    #     graph[node] = neighbors
    # start_node = input("Enter the starting node: ")
    start_node='A'
    print("\nDFS (Recursive):")
    visited_recursive = set()
    recursive_dfs(graph, start_node, visited_recursive)
    print("\nDFS (Iterative):")
    iterative_dfs(graph, start_node)
if __name__ == "__main__":
    main()
