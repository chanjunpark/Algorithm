def solution(answers):
    person_1 = [1, 2, 3, 4, 5]
    person_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = {1: 0, 2: 0, 3: 0}

    for idx, answer in enumerate(answers):
        if person_1[idx % 5] == answer:
            count[1] += 1
        if person_2[idx % 8] == answer:
            count[2] += 1
        if person_3[idx % 10] == answer:
            count[3] += 1

    result = [key for key in count.keys() if count[key] == max(count.values())]

    return result
