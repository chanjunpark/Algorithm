# Algorithm
Practice algorithm
하루 세 문제씩 공부하는 알고리즘(Python, Java)
리트코드 문항 순서 : 문자열 -> 배열 -> 연결리스트 
참고서적 : 파이썬 알고리즘 인터뷰(박상길, 책만)

주요 메서드 정리

[자료형별 구분]

String(문자열)
 - isalnum() : 문자열이 영문자와 숫자만으로 구성되어 있는지 판별 / isalpha(), isdigit(), islower(), isupper()
 - reverse() : 문자열의 순서를 뒤집어서 반환
 - import re : 정규식 사용 가능

Datetime(날짜)
 - datetime.timedelta()

Deque(데크)
 - popleft() : O(1) 시간에 맨 앞 삭제 가능. 파이썬에서 큐를 구현할 경우 from collections import deque
 - appendleft() : 왼쪽에 삽입

Priority Queue(우선순위 큐)
 - import heapq : 파이썬에서는 heapq를 이용해 우선순위 큐를 쉽게 구현할 수 있음
 - heapq.heqpify(list) : list를 우선순위 큐로 만듦
 - heapq.heappop(list) : 우선순위 큐에서 우선 순위가 가장 높은(가장 최소) 값을 인출
 - heapq.heappush(list, item) : 우선순위 큐에 요소를 삽입

Hash(해시)
 - collections.Counter(list) : list의 요소별 갯수를 Counter 객체에 반환
 - collections.defaultdict(list) : 존재하지 않는 키 삽입 경우 에러가 발생하지 않도록 할 수 있음. dict() 사용 하는 경우 dict().get(key) is not None: 으로 써도 오류 안 생김
 - 

[알고리즘별 구분]

Math(수학)
 - import math
 - math.ceil(3.14)
 - math.floor(3.14)
 - math.trunc(3.14)

BruteForce(완전탐색)
 - combinations(list, r) : list에서 r개의 요소로 만들 수 있는 모든 조합을 생성하여 iterable로 반환. from itertools import combinations
 - permutations(list, r) : list에서 r개의 요소로 만들 수 있는 모든 순열을 생성하여 iterable로 반환. from itertools import permutations

Sorting(정렬) 
 - sorted(list, key = lambda x : x[0]) : key 조건대로 정렬된 리스트를 반환, 모든 iterable 객체에 적용 가능
 - list.sort(key = ) : key 조건대로 list 자체를 정렬, list에만 적용 가능

 













