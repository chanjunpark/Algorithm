import sys
sys.setrecursionlimit(10 ** 5)


def DFS(current, numbers, target, st, result):
    global count
    idx, number = current[-2], current[-1]
    if idx == len(numbers) - 1:  # 인덱스가 끝까지 왔을 때
        if result + number == target:  # 방문한 노드의 합이 target과 같으면 count 증가
            count += 1
    else:
        DFS(current + (idx + 1, -numbers[idx + 1]), numbers, target, st, result + number)
        DFS(current + (idx + 1, numbers[idx + 1]), numbers, target, st, result + number)
    return 1


def solution(numbers, target):
    global count
    count = 0
    root = (-1, 0)  # 루트가 되는 노드를 만들어 줌(하나의 수에 대해 +, - 탐색을 해야하므로).
    DFS(root, numbers, target, [], 0)
    answer = count
    return answer


'''
-1 , +1 
'''