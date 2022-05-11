
from collections import defaultdict, deque, Counter


TEST_INPUT = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

TEST_INPUT2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

TEST_INPUT3 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
"""

with open('./data/day12.txt') as f:
    raw_input = f.read()

# raw_input = TEST_INPUT3

graph = defaultdict(list)
# create a graph data structure
for line in raw_input.splitlines():
    node1, node2 = line.split('-')
    graph[node1].append(node2)
    graph[node2].append(node1)
    # print(node1, node2)


all_paths = []

# track visited nodes via the path list itself, in part based on solution in 
# https://www.geeksforgeeks.org/print-paths-given-source-destination-using-bfs/

# do some kind of pathfinding algorithm that tracks the sequence of nodes taken.
path = []
Q = deque()

path.append('start')
Q.append(path.copy())

def is_valid(child, path):
    # handles the visit one small cave twice condition from part 2, very slow though
    if child == 'start': # returning to start is never valid
        return False

    path_counts = Counter(path)
    two_or_more = [(x,y) for (x,y) in path_counts.items() if x.islower() and y >= 2]

    if len(two_or_more)==0:
        return True
    elif len(two_or_more)==1:
        if two_or_more[0][1]==2:
            return True
    else:
        return False


while Q:
    path = Q.popleft()
    # print('path :', path)
    node = path[-1]
    # print('node: ', node)
    # print(Q)
    
    for child in graph[node]:
        # print('child: ', child)
        if is_valid(child, path): # by using lower we are implicitly never adding the capitalized nodes to the visit list, can be reused
            # print('testing from:', child)

            if child == 'end':
                # we have found the end, extend the path and save it in the list of all paths
                terminal_path = path.copy()
                terminal_path.append(child)
                all_paths.append(terminal_path)

            if child != 'end':
                # if it's not the end, create a cop of the path that inlcudes this visited node and then explore from there
                new_path = path.copy()
                new_path.append(child)
                # print('adding to deque: ', new_path)
                Q.append(new_path)
    

# print(graph)
for path in all_paths:
    print(path)
print(len(all_paths))