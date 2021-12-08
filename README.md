# Algorithm
Practice algorithm
하루 세 문제씩 공부하는 알고리즘(Python, Java)

### '21. 12. 6.Mon Leetcode

125. Valid Palindrome(Easy) : 주어진 문자열이 팰린드롬인지 확인하는 문제 (Python)
 - isalnum() 메서드를 알게 됨. 문자열 객체에 사용가능한 메서드이며, 문자열이 영문자와 숫자로 구성되어 있는지 판별함. 비슷한 메서드로 isalpha(), isdigit(), islower(), isupper() 가 있음.
 - import collections 후 strs: Deque = collections.deque()를 이용해 데크 자료형을 선언할 수 있다. 파이썬에서 리스트의 경우 맨 앞의 요소를 제거하는데 O(n)이 소요되는 반면 데크 자료형의 popleft()는 O(1)이 소요됨. 
 - 이 외에도 정규식과 슬라이싱을 통해 간단히 구현도 가능하다. 정규식으로 불필요한 문자를 제거한 후 return s == s[::-1]로 간단하게 팰린드롬 검사가 가능함.

344. Reverse String(Easy) : 주어진 문자열을 역순으로 출력하는 문제 (Python)
 - string 객체에 사용하는 reverse() 메서드를 사용해 간단하게 풀이 가능.
 
937. Reorder Log File(Easy) : 주어진 기준에 따라 로그 파일을 재정렬 하는 문제 -> 티스토리에 정리해놓음 (Python)
 - sorted() 함수 내에 iterable 객체와 함께 key를 파라미터로 전달해줄 수 있는데, 이 key 를 함수로 전달할 수 있음. 함수로 전달하는 경우 먼저 앞선 리턴 값으로 정렬 후 이어지는 리턴 값 기준으로 정렬함. 
 
### '21. 12. 7.Tue Leetcode
 
819. Most Common Word(Easy) : 금지된 단어(banned)를 제외하고 가장 흔하게 등장하는 단어를 출력하는 문제 (Python)
 - collections.Counter(list) 를 이용해 쉽게 단어의 개수를 구할 수 있음 -> 티스토리에 정리할 예정
 - 나는 딕셔너리 자료구조를 이용해 풀었으며, word를 key로 하고 개수를 value로 하는 딕셔너리를 만든 뒤 item을 언팩킹하여 value가 가장 큰 값을 찾아 리턴했음.

49. Group Anagram(Medium) : 문자열을 받아 애너그램 단위로 그룹화하여 리턴하는 문제 (Python)
 - collections.defaultdict(list) 를 이용해 존재하지 않는 키를 삽입하는 경우 발생하는 에러를 안 나도록 할 수 있음. 이후 .values()를 리턴해주면 됨. -> 티스토리에 정리할 예정
 - 나는 딕셔너리 자료구조를 이용해 풀었으며, 딕셔너리 key에 sorted word가 없다면 sorted word를 key, index를 value로 하는 값을 삽입한 뒤, 딕셔너리 key에 sorted word가 있는 경우 index를 value로 받아와 해당 index의 이중리스트에 word를 삽입했음.

5. Longest Palindrome Substring(Medium) : 가장 긴 팰린드롬 부분 문자열을 출력하는 문제 (Python)
 - 이전에 이미 혼자 풀었음
 - 반복문을 통해 index를 1씩 증가시키며 문자열 내 index에 해당하는 글자를 중심으로(가운데) 최대로 유효한 팰린드롬을 찾았음.

### '21. 12. 8.Wed LeetCode

42. Trapping Rain Water(Hard) ★ : 비 온 후 쌓인 물의 양 구하기 (Python)
 - 투 포인터를 이용하거나 스택을 이용해서 풀이 가능
 - 스택을 이용해서 푸는 쪽으로 방향은 잘 잡았었는데, 스택에 (index, height)로 넣다보니 너무 수식이 복잡해져 한참을 헤맸다.
 - 책을 보니 index를 스택에 넣고 height는 height[index]로 구하면 되는 거였는데 아직 디테일이 부족하다.
 - 나중에 다시 한번 풀어보자 

15. 3Sum(Medium) ★ : 리스트 내에서 요소 3개의 합이 0이 되는 모든 요소를 출력 (Python)
 - 브루트 포스(from itertools import combinations) 쓰면 쉽게 풀 수 있지만 시간 초과가 나오는 문제
 - 리스트를 정렬한 후 투 포인터로 합을 계산해야 함. 투 포인터 기법에 대한 연습을 좀 더 해봐야할 것 같음
 - 풀이법을 알고도 구현이 쉽지 않으니 주말에 연습해보기

561. Array Partition 1(Easy) : n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력 (Python)

238. Product of Array Except Self(Medium) : 배열을 입력 받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력 (Python)
 - 시간 제한(O(N))과 나눗셈을 쓰지 못하는 제한이 걸려있어 풀이가 까다롭다.
 - 좌우측 각각으로부터 차례로 수를 곱한 값을 배열에 저장한 뒤 요소의 위치 i 에 따라 left_side[i-1], right_side[-i-2] 를 곱해서 output을 만들어주면 됨.

121. Best Time to Buy and Sell Stock(Easy) : 한 번의 거래로 낼 수 있는 최대 이익을 산출 (Python)

234. Palindrome Linked List(Easy) : 연결 리스트가 팰린드롬 구조인지 판별 (Python, JAVA)
 - Deque 자료구조를 이용해 풀이했음. 
 - 연결 리스트 모든 요소를 Deque에 차례대로 삽입한 뒤, 양 끝부터 제거해가면서 다른 값이 있다면 false를 리턴



