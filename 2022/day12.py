from collections import defaultdict, deque

FILEPATH = "./data/day12.txt"


def parse_input(filepath: str):
    # Create and return a grid structure
    grid = {}
    bottom_elevations = []
    with open(filepath) as f:
        for i, line in enumerate(f.readlines()):
            for j, char in enumerate(line.strip()):
                grid[i, j] = char
                if char == "S":
                    start = (i, j)
                    grid[i, j] = "a"
                    bottom_elevations.append((i, j))
                if char == "E":
                    end = (i, j)
                    grid[i, j] = "z"
                if char == "a":
                    bottom_elevations.append((i, j))

    return grid, start, end, bottom_elevations


# 1. Each step we take, we want to be moving toward the target as best we can
# 2. There is a set of valid moves and a set of invalid moves for each position
# 3. The grid is similar to a graph, where we have an edge between two vertices only if the
#    elevation difference is 1 or less.
# 4. We can make out all possible routes via a graph traversal algorithm
# 5. We can find the shortest route with a pathfinding algorithm on the resulting graph.


def build_graph(grid, start, reversed=False):
    def valid_path(a, b):
        # Check if we can move from a to b by converting letter to numeric representation
        delta = ord(b) - ord(a)

        return delta in [-1, 0, 1, 2] if reversed else delta in [-2, -1, 0, 1]

    DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    # Create the graph using BFS, use dict to store since adjacency matrix will be so big and sparse
    graph = defaultdict(list)
    visited = []

    # Start at the start node and
    Q = deque()
    Q.append(start)

    while Q:
        node = Q.popleft()
        visited.append(node)

        for di, dj in DIRS:
            neighbor = (node[0] + di, node[1] + dj)
            if grid.get(neighbor):  # to avoid out of bounds
                if valid_path(grid.get(node), grid.get(neighbor)):
                    graph[node].append(neighbor)
                if neighbor not in visited and neighbor not in Q:
                    Q.append(neighbor)

    return graph


def shortest_path(graph, start, end=None):
    # Use Dijkstras since I don't know A* (let's be real I don't know Dijkstras either!)
    Q = deque()

    distances = {}
    previous = {}
    for vertex in graph:
        distances[vertex] = float("inf")
        previous[vertex] = None
        Q.append(vertex)

    distances[start] = 0

    while Q:
        # Find the vertex with shortest distance that is in the Q and remove it
        node = min(Q, key=distances.get)
        Q.remove(node)

        for neighbor in graph[node]:
            if neighbor in Q:
                new_dist = distances[node] + 1
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    previous[neighbor] = node

        if node == end:
            break

    return distances[end] if end else distances


grid, start, end, bottom_elevations = parse_input(FILEPATH)

print(start, end)

# Part 1
graph = build_graph(grid, start)
# print(graph)
res_1 = shortest_path(graph, start, end)
print("Part 1:", res_1)

# Part 2
# Brute force might work with a better shortest path algo but not here
reverse_graph = build_graph(grid, end, reversed=True)
distances = shortest_path(reverse_graph, end)

bottom_distances = [distances[node] for node in bottom_elevations if node in distances]
res_2 = min(bottom_distances)
print("Part 2:", res_2)
