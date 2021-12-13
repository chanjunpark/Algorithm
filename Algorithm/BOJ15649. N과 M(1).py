def permutation(n, r, st):
    if r <= 1:
        for i in n:
            if i not in st:
                st.append(i)
                temp = st.copy()
                answers.append(temp)
                st.pop()

    else:
        for number in n:
            if number not in st:
                st.append(number)
                permutation(n, r-1, st)
                st.pop()
    return answers


n, r = map(int, input().split(" "))
n = [number for number in range(1,n+1)]
answers = []
st = []
permutation(n, r, st)
for answer in answers:
    for number in answer:
        print(number, end=' ')
    print()