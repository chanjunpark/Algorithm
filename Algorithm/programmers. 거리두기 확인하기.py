def hasNeighbor(place, row, col, dist):
    global flag
    if (row < 0 or row > 4) or (col < 0 or col > 4) or dist == 3:
        return False
    else:
        if is_visited[row][col] == True:
            return False
        else:
            # print("row :", row, "col :", col, place[row][col], dist)
            # print(flag)
            if place[row][col] == "P":
                is_visited[row][col] = True
                # print("Here")
                flag = True
                return True
            elif place[row][col] == "X":
                is_visited[row][col] = True
                return False
            else:
                is_visited[row][col] = True
                hasNeighbor(place, row - 1, col, dist + 1)
                hasNeighbor(place, row + 1, col, dist + 1)
                hasNeighbor(place, row, col + 1, dist + 1)
                hasNeighbor(place, row, col - 1, dist + 1)


def solution(places):
    global is_visited
    global flag
    answer = []
    for place in places:
        flag = False
        for idx_row, row in enumerate(place):
            for idx_col, col in enumerate(row):
                if col == "P":
                    is_visited = [[False, False, False, False, False] for row in place]
                    # print(idx_row, idx_col)
                    is_visited[idx_row][idx_col] = True
                    hasNeighbor(place, idx_row - 1, idx_col, 1)
                    hasNeighbor(place, idx_row + 1, idx_col, 1)
                    hasNeighbor(place, idx_row, idx_col - 1, 1)
                    hasNeighbor(place, idx_row, idx_col + 1, 1)
                    # print(flag)
        if not flag:
            answer.append(1)
        else:
            answer.append(0)
        flag = False

    return answer