#조건 표현식 연습
"""
true인 경우의 값 if 조건 else false인 경우의 값 
value = num if num>=0 else -num
"""

#추가 메서드를 활용한 딕셔너리 순회 49p
""" 
items(): (Key, value)의 튜플로 구성된 결과
grades = {'john':80, 'eric':90}
print(grades.items())

for student, grade in grades.items():
    print(student, grade)
 """

#enumerate 순회 - idx 와 value 동시에 처리하고 싶을 때
"""
(index,value) 형태의 tuple로 구성된 열거 객체를 반환
members = ['민수', '영희', '철수']
for idx, number in enumerate(members):
    print(idx, number)
"""

#list Comprehension - 많이 씀.
"""
#map은 기존의 것을 이용 list comprehension은 새롭게 리스트 생성
[code for 변수 in iterable if 조건식]
cubic_list = []
for number in range(1,4):
    cubic_list.append(number **3)
print(cubic_list)
                ==
cubic_list = [number**3 for number in range(1,4)]
print(cubic_list)
"""

#Dictionary Comprehension도 있음.
"""
{key: value for 변수 in iterable if 조건식}
"""

#input의 종류 


# 정해지지 않은 여러 개의 arguments 처리 - asterisk(*)와 가변인자. 
""" 
가변인자란 여러 개의 positional argument를 하나의 필수 parameter로 받아서 사용.
def add(*arg):
    for arg in args:
        print(arg) add(2) or add(2,3,4,5)

가변인자를 이해하기 위해서는 패킹,언패킹을 이해해야 함.
numbers=(1,2,3,4,5) # 패킹
a,b,c,d,e, = numbers #언패킹 - 시퀀스 속의 요소들을 여러 개 변수에 나누어 할당하는 것.
a,b,*rest = numbers --> print(rest)#[2,3,4]
print(a,b,c,d,e) #1 2 3 4 5
"""

#map(function, iterable)
"""
순회 가능한 데이터구조(itrable)의 모든 요소에 함수(function)적용하고 그 결과를 map object로 반환
"""

#filter(function, iterable)
"""
순회 가능한 데이터 구조의 모든 요소에 함수 적용하고 그 결과가 true인 것들을 filter object로 반환 
def ood(n):
    return n % 2
numbers = [1,2,3]
result = filter(odd, numbers)
print(list(result)) #[1,3] 
#리스트 형변환을 통해 결과 직접 확인 할 수 있다.
"""

#zip(*iterables)
"""
girls = ['jane', 'ashley']
boys = ['justin', 'eric']
pair = zip(girls, boys)
print(list(pair))#[('jane','justin'), ('ashely', 'eric')]
#리스트 형변환을 통해 결과 직접 확인 
"""



