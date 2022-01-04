from collections import deque


graph = dict()
graph['A'] = ['B', 'D']
graph['B'] = ['C', 'E']
graph['C'] = []
graph['D'] = ['E', 'G', 'H']
graph['E'] = ['F']
graph['F'] = []
graph['G'] = ['H']
graph['H'] = []


def BFS(graph, start):
    queue.append(start)
    while queue:
        post = queue.popleft()
        if post not in is_visited:
            is_visited.append(post)
            if graph.get(post) is not None:
                queue.extend(graph.get(post))
    return is_visited


global is_visited
global stack
is_visited = []
queue = deque()
print(BFS(graph, 'A'))

