# 순열, 조합 관련 툴
from itertools import permutations
permutations(list(), 2)

from itertools import combinations
combinations(list(), 2)

from itertools import product
# product(list(), 2)

# deque 호출
from collections import deque
de = deque()

# 우선순위큐(히프)
import heapq
li = [3, 4]
heapq.heapify(li)
heapq.heappop(li)
heapq.heappush(li, 5)

# 수학 관련
import math
math.ceil(3.14) # 올림
math.floor(3.14) # 내림
math.trunc(3.14) # 0으로 향하게 내림(절대값)

# 팩토리얼
math.factorial(5)

# 최대 공약수
print(math.gcd(5,10))

import re
text = "1%^@azerqDFS#52"
text2 = "abc123"
clean = re.sub('\W', '', text)
print(clean)
print(text2.isalnum())
print(text2.isalpha())
print(text2.isdigit())

import datetime
time_1 = datetime.timedelta(hours= 14 , minutes=30)
time_2 = datetime.timedelta(hours= 16, minutes=30)
standard = datetime.timedelta(hours= 1, minutes=30)
print(time_2 - time_1 > standard)
