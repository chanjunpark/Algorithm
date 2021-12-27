def find_minimum(N, number, count, dp_table):
    if count == 9:
        return -1
    elif count == 1:
        if number == N:
            return count
        else:
            count += 1
            return find_minimum(N, number, count, dp_table)
    solution_count = list()
    for i in range(1, (count // 2) + 1):
        solution_plus = [N + M for M in dp_table.get(i) for N in dp_table.get(count - i)]
        solution_minus1 = [N - M for M in dp_table.get(i) for N in dp_table.get(count - i)]
        solution_minus2 = [M - N for M in dp_table.get(i) for N in dp_table.get(count - i)]
        solution_multiply = [N * M for M in dp_table.get(i) for N in dp_table.get(count - i)]
        solution_divide1 = [N // M for M in dp_table.get(i) for N in dp_table.get(count - i) if M != 0]
        solution_divide2 = [M // N for M in dp_table.get(i) for N in dp_table.get(count - i) if N != 0]
        if i == 1:
            solution_count = solution_plus + solution_minus1 + solution_minus2 + solution_multiply + solution_divide1 + solution_divide2
        else:
            solution_count = solution_count + solution_plus + solution_minus1 + solution_minus2 + solution_multiply + solution_divide1 + solution_divide2
    splicing = int(str(N) * count)
    solution_count.append(splicing)
    if number in solution_count:
        return count
    else:
        dp_table[count] = solution_count
        count += 1
        return find_minimum(N, number, count, dp_table)


def solution(N, number):
    dp_table = {1: [N]}
    answer = find_minimum(N, number, 1, dp_table)
    return answer