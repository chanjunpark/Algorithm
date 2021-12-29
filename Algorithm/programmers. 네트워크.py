def solution(n, computers):
    visited = []
    next_ = []

    def find_network(current, computers):
        if current not in visited:
            visited.append(current)
            for idx, network in enumerate(computers[current]):
                if idx == current:
                    continue
                if network == 1 and idx not in visited:
                    next_.append(idx)
            while next_:
                find_network(next_.pop(), computers)
        return 1

    answer = 0
    for header, _ in enumerate(computers):
        if header not in visited:
            find_network(header, computers)
            answer += 1

    return answer
