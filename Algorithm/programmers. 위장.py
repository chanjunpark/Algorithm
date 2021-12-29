def solution(clothes):
    answer = 1
    categories = {}
    for cloth in clothes:
        if categories.get(cloth[1]):
            categories.get(cloth[1]).append(cloth[0])
        else:
            categories[cloth[1]] = [cloth[0]]

    for value in categories.values():
        answer *= (len(value) + 1)

    return answer - 1
