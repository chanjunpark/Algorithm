from collections import deque


def solution(n, edge):
    graph = dict()
    for e in edge:
        if graph.get(e[0]):
            graph.get(e[0]).append(e[1])
        else:
            graph[e[0]] = [e[1]]
        if graph.get(e[1]):
            graph.get(e[1]).append(e[0])
        else:
            graph[e[1]] = [e[0]]

    answer = 1
    queue = deque([1])
    is_visited = [True, True] + [False for i in range(n)]

    while queue:
        queue_size = len(queue)
        for i in range(queue_size):
            current = queue.popleft()
            if graph.get(current):  # 현재 정점과 이어진 간선이 존재한다면,
                for v in graph.get(current):  # 간선으로 연결되어 있으며, 아직 방문하지 않은 모든 정점을 queue에 추가
                    if not is_visited[v]:
                        queue.append(v)
                        is_visited[v] = True
        answer = queue_size

    return answer
