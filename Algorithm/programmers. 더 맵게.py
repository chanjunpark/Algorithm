import heapq


def solution(scoville, K):
    answer = 0
    scoville = sorted(scoville)

    while True:
        if len(scoville) < 2 and scoville[0] < K:
            answer = -1
            break
        else:
            if scoville[0] >= K:
                break
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            new_food = first + 2 * second
            heapq.heappush(scoville, new_food)
            answer += 1

    return answer