
def maximun_distance(n):
    if n%2 == 0:
        return (n//2)*((n//2)+1)
    else:
        return ((n-1)//2)*((((n-1)//2))+1) + (n+1)//2

def solution(start, destination):
    total_distance = destination - start
    moving_distance = 0
    count = 0

    while moving_distance < total_distance:
        count += 1
        moving_distance += 2*(count)

    count = count*2

    if total_distance > maximun_distance(count-1):
        return count
    else:
        return count-1


length = int(input())
answers = []
for i in range(length):
    s, d = map(int, input().split(" "))
    answers.append(solution(s,d))
for answer in answers:
    print(answer)


