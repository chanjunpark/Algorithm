class Solution:

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        global flight
        global cities
        global path
        global is_visited
        global stack

        flight = dict()
        cities = set([])
        path = ["JFK"]
        is_visited = set(["JFK"])
        stack = list()

        for ticket in tickets:
            if flight.get(ticket[0]):
                flight.get(ticket[0]).append(ticket[1])
            else:
                flight[ticket[0]] = [ticket[1]]
            cities = cities.union(ticket)

        def lexical_dfs(current):
            global is_visited
            global cities
            global answer
            if len(path) == len(tickets) + 1:
                if len(set(path)) == len(cities):
                    answer = path.copy()
                    return True
                else:
                    return False
            else:
                if flight.get(current):
                    candidates = sorted(flight.get(current))
                    for idx_city, destination in enumerate(candidates):
                        path.append(destination)
                        stack.append(destination)
                        post = stack.pop()
                        flight.get(current).remove(post)
                        valid_path = lexical_dfs(post)
                        if valid_path:
                            return True
                        flight.get(current).append(post)
                        path.pop()
                else:
                    return False

        lexical_dfs("JFK")

        return answer
