def solution(numbers):
    answer = ''
    temp = []
    for number in numbers:
        temp.append(str(number))
    temp.sort(reverse=True, key=lambda x: x*3)
    for number in temp:
        answer = answer + number
    if answer.count("0") == len(answer):
        answer = "0"
    return answer
