class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        global prereqs
        global stack
        global has_cycle
        global path
        prereqs = dict()
        stack = list()
        has_cycle = False
        path = list()
        is_visited = list()

        for prerequisite in prerequisites:
            if prereqs.get(prerequisite[0]):
                prereqs.get(prerequisite[0]).append(prerequisite[1])
            else:
                prereqs[prerequisite[0]] = [prerequisite[1]]

        def DFS(current):
            global has_cycle
            global path

            if current in path:
                has_cycle = True
            else:
                if current not in is_visited:
                    is_visited.append(current)
                    if prereqs.get(current):
                        for prereq in prereqs.get(current):
                            path.append(current)
                            stack.append(prereq)
                            post = stack.pop()
                            DFS(post)
                            path.pop()
                            if has_cycle:
                                break

        for header in prereqs.keys():
            if header not in is_visited:
                DFS(header)
                if has_cycle:
                    break

        return not has_cycle
