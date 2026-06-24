from collections import deque


class Graph:
    def __init__(self, directed=False):
        self.adj_list = {}
        self.directed = directed

    # Add a new vertex
    def add_vertex(self, v):
        if v not in self.adj_list:
            self.adj_list[v] = []

    # Add an edge
    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)

        self.adj_list[u].append(v)

        # Add reverse edge only for undirected graph
        if not self.directed:
            self.adj_list[v].append(u)

    # Display adjacency list
    def display(self):
        print("\nAdjacency List:")
        for vertex in sorted(self.adj_list):
            print(f"{vertex} -> {self.adj_list[vertex]}")

    # Breadth First Search
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        order = []

        while queue:
            current = queue.popleft()
            order.append(current)

            for neighbor in self.adj_list[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return order

    # Depth First Search using recursion
    def dfs(self, start):
        visited = set()
        order = []

        def dfs_recursive(node):
            visited.add(node)
            order.append(node)

            for neighbor in self.adj_list[node]:
                if neighbor not in visited:
                    dfs_recursive(neighbor)

        dfs_recursive(start)
        return order

    # Bonus: Check if a path exists
    def has_path(self, src, dest):
        visited = set()
        queue = deque([src])
        visited.add(src)

        while queue:
            current = queue.popleft()

            if current == dest:
                return True

            for neighbor in self.adj_list[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return False

    # Bonus: Find people within k connections
    def within_k_connections(self, start, k):
        visited = set([start])
        queue = deque([(start, 0)])
        result = []

        while queue:
            node, distance = queue.popleft()

            if 0 < distance <= k:
                result.append(node)

            if distance < k:
                for neighbor in self.adj_list[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, distance + 1))

        return result

    # Bonus: Count connected components
    def count_connected_components(self):
        visited = set()
        components = 0

        for vertex in self.adj_list:
            if vertex not in visited:
                components += 1

                stack = [vertex]

                while stack:
                    current = stack.pop()

                    if current not in visited:
                        visited.add(current)

                        for neighbor in self.adj_list[current]:
                            if neighbor not in visited:
                                stack.append(neighbor)

        return components


# ==================================================
# PART A - BASIC GRAPH SETUP
# ==================================================

print("=" * 50)
print("PART A - BASIC GRAPH SETUP")
print("=" * 50)

g = Graph()

edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
    ("C", "D"),
    ("D", "E"),
    ("E", "F")
]

for u, v in edges:
    g.add_edge(u, v)

g.display()


# ==================================================
# PART B - BFS IMPLEMENTATION
# ==================================================

print("\n" + "=" * 50)
print("PART B - BFS IMPLEMENTATION")
print("=" * 50)

bfs_order = g.bfs("A")

print("\nBFS Traversal:")
print(" -> ".join(bfs_order))

print("\nBFS Tree:")
print("A")
print("├── B")
print("├── C")
print("│   └── D")
print("│       └── E")
print("│           └── F")


# ==================================================
# PART C - DFS IMPLEMENTATION
# ==================================================

print("\n" + "=" * 50)
print("PART C - DFS IMPLEMENTATION")
print("=" * 50)

dfs_order = g.dfs("A")

print("\nDFS Traversal:")
print(" -> ".join(dfs_order))

print("\nComparison Between BFS and DFS:")
print(
    "BFS visits vertices level by level, exploring all neighbors "
    "of the starting vertex before moving deeper.\n"
    "DFS goes as deep as possible along one path before backtracking.\n"
    "Therefore, both algorithms produce different traversal orders."
)


# ==================================================
# PART D - BONUS / CHALLENGE TASKS
# ==================================================

print("\n" + "=" * 50)
print("PART D - BONUS / CHALLENGE TASKS")
print("=" * 50)

# Path checking
print("\nPath Checking:")
print(f"Is there a path from A to F? {g.has_path('A', 'F')}")
print(f"Is there a path from C to F? {g.has_path('C', 'F')}")

# Social network example
print("\nPeople within 2 connections of A:")
print(g.within_k_connections("A", 2))

# Connected components
print("\nNumber of Connected Components:")
print(g.count_connected_components())

# Directed graph demonstration
print("\nDirected Graph Demonstration:")
directed_graph = Graph(directed=True)

for u, v in edges:
    directed_graph.add_edge(u, v)

directed_graph.display()