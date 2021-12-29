def is_prime(number):  # 조합된 수가 소수인지 아닌지 판별
    divisor = []
    if number == 0 or number == 1:
        return False
    else:
        for i in range(2, number + 1):
            if number % i == 0 and i != number:
                return False
    return True


def combinate_number(numbers, r, st):  # 문자를 이어 붙여 만들 수 있는 모든 조합을 생성
    global results
    if r == 1:
        for number in numbers:
            st.append(number)
            comb = ''.join(st)
            if len(comb) > 1:
                pointer = 0
                for idx, digit in enumerate(comb):
                    pointer = idx
                    if digit != "0":
                        break
                comb = comb[pointer:]
            if comb not in results:
                results.append(comb)
            st.pop()
    else:
        for idx, number in enumerate(numbers):
            if idx == len(numbers) - 1:
                st.append(number)
                combinate_number(numbers[:-1], r - 1, st)
                st.pop()
            else:
                st.append(number)
                combinate_number(numbers[:idx] + numbers[idx + 1:], r - 1, st)
                st.pop()
    return 1


def solution(numbers):
    global results
    results = []
    answer = 0
    for i in range(1, len(numbers) + 1):
        combinate_number(numbers, i, [])
    for result in results:
        if is_prime(int(result)):
            answer += 1

    return answer
