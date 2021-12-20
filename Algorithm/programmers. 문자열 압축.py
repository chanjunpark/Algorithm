import collections


def compress_string(s, unit):
    start = 0
    new_s = []
    for idx, character in enumerate(s):
        if idx != 0 and idx % unit == 0:
            new_s.append(s[start:idx])
            start = idx
        if idx // unit >= (len(s) - 1) // unit:
            new_s.append(s[idx:])
            break
    return new_s


def solution(s):
    answer = 0
    min_len = 1001
    for unit in range(1, len(s) + 1):
        temp = ""
        candidate = compress_string(s, unit)
        count = 1
        for idx in range(1, len(candidate)):
            if candidate[idx] == candidate[idx - 1]:
                count += 1
            else:
                if count == 1:
                    temp = temp + candidate[idx - 1]
                else:
                    temp = temp + str(count) + candidate[idx - 1]
                count = 1
        if count > 1:
            temp = temp + str(count) + candidate[-1]
        else:
            temp = temp + candidate[-1]
        if len(temp) < min_len:
            min_len = len(temp)
    answer = min_len
    return answer