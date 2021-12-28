def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book, key = lambda x : (x, len(x)))
    for idx, number in enumerate(phone_book):
        if idx == len(phone_book) - 1:
            break
        else:
            if number == phone_book[idx+1][:len(number)]:
                answer = False
                break
    return answer