class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)  # the number of row
        n = len(grid[0])  # the number of column
        vertice = []  # list which contain flattened grid(2d list)
        stack = []  # list which contain next search space
        is_visited = [False for f in range(m * n)]  # list which contain whether vertex is visited or not
        answer = 0  # the number of island

        for x in grid:  # flatten the grid to 1D list
            vertice.extend(x)

        for index in range(len(vertice)):  # iterate all vertex in vertice(DFS)
            if is_visited[index] == True or vertice[index] == "0":
                continue
            else:
                stack.append(index)
                while stack:
                    v = stack.pop()
                    try:
                        if is_visited[v] == False and vertice[v] == "1":
                            is_visited[v] = True
                            if v // m == 0:  # if v at upper side
                                if v % n == 0:
                                    adjacent = [v + n, v + 1]
                                elif v % n == n - 1:
                                    adjacent = [v + n, v - 1]
                                else:
                                    adjacent = [v + n, v + 1, v - 1]
                            elif v // m == m - 1:  # if v at bottom side
                                if v % n == 0:
                                    adjacent = [v - n, v + 1]
                                elif v % n == n - 1:
                                    adjacent = [v - n, v - 1]
                                else:
                                    adjacent = [v - n, v + 1, v - 1]
                            elif v % n == 0:  # if v at left side
                                adjacent = [v + n, v - n, v + 1]
                            elif v % n == n - 1:  # if v at right side
                                adjacent = [v + n, v - n, v - 1]
                            else:
                                adjacent = [v + n, v - n, v + 1, v - 1]
                            stack.extend(adjacent)
                    except:
                        continue
                answer += 1

        return answer