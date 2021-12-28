import heapq
from collections import deque


def solution(jobs):
    current = 0
    ready = []
    finished = []
    jobs = deque(sorted(jobs))
    first = jobs.popleft()
    finished.append(first[1])
    current = first[0] + first[1]
    while len(jobs) > 0:
        ready = []
        for idx, job in enumerate(jobs):
            if job[0] > current:
                break
            heapq.heappush(ready, [job[1], current - job[0] + job[1], idx])  # Shortest Job Next Scheduling
        # print(jobs)
        # print(current, "--", ready, "--", finished)
        # print()
        if len(ready) == 0:  # 먼저 실행된 프로세스의 종료시점까지 새로 요청한 프로세스가 없는 경우
            running = jobs.popleft()  # 가장 가까운 시점에 요청한 프로세스부터 실행
            finished.append(running[1])  # 요청부터 종료까지 프로세스 수행시간만큼만 소요
            current = running[0] + running[1]  # 실행중인 프로세스의 종료시점으로 바로 이동
        else:
            running = heapq.heappop(ready)
            finished.append(running[1])
            current = current + running[0]
            del jobs[running[2]]

    answer = sum(finished) // len(finished)

    return answer


'''
요청부터 종료까지 예상되는 시간이 가장 작은 프로세스를 다음 프로세스로 실행
요청부터 종료까지 예상되는 시간 = 기다린시간(이전 프로세스 수행 종료시간 - 요청시간) + 수행시간

'''