graph = dict()
graph['A'] = ['B', 'D']
graph['B'] = ['C', 'E']
graph['C'] = ['']
graph['D'] = ['E', 'G', 'H']
graph['E'] = ['F']
graph['F'] = ['']
graph['G'] = ['H']
graph['H'] = ['']


def DFS(graph, start):
    if start not in is_visited:
        print(start)
        is_visited.append(start)
        for vertex in graph.get(start):
            if vertex:
                stack.append(vertex)
                post = stack.pop()
                DFS(graph, post)


global is_visited
global stack
is_visited = []
stack = []
DFS(graph, 'A')

