#TIL

#변수의 값을 바꿔서 저장하기
#Pythonic!
x,y = 10,20
y,x = x,y
print(x,y) # 20,10

#실수 연산시 주의할 점(부동소수점) - 해결책
a = 3.2 - 3.1
b = 1.2 - 1.1
import math
print(math.isclose(a,b)) # True

#삼중 따옴표
print('''문자열 안에 '작음따옴표'나
"큰따옴표"를 사용할 수 있고
여러 줄을 사용할 때도 편리하다.''')

#Escape sequence
print("\r: 캐리지 리턴")
print("\0: null")
print("\\: \\")
print("\': 작은따옴표")

#논리 연산자 주의할 점 / not 연산자
"""
Falsy: False는 아니지만 False로 취급되는 다양한 값
- 0, 0.0, (), [], {}, None, ""(빈문자열)
논리연산자도 우선순위가 존재
- not, and, or순으로 우선순위가 높음
"""

#리스트
"""
[], list()를 통해 생성
값에 대한 접근은 list[i]
"""

#튜플
"""
불변자료형
(), tuple()을 통해 생성
값에 대한 접근은 my_tuple[i]

생성시 주의사항
단일 항목의 경우
- 값 뒤에 쉼표 tuple_a(1,)

 튜플 대입 -우변의 값을 좌변의 변수에 한번에 할당하는 과정
 x,y = 1,2
 print(x,y) # 1 2
"""

#Range
"""
기본형: range(n)
범위 지정: range(n,m)
범위 및 스텝 지정: range(n, m, s)
 - n부터 m-1까지 s만큼 증가시키며 숫자의 시퀀스
  """

#슬라이싱 연산자
"""
print([1,2,3,5][0:4:2]) # [1,3]
print([1,2,3,5][::-1]) # [5,3,2,1]
"""

#Set
"""
집합의 특성
{}, set()을 통해 생성
-빈 set을 만들기 위해서는 반드시 set()를 사용
-{} 빈 중괄호는 Dictionary
순서가 없으므로 인덱스로 접근할 수 없음
|: 합집합, &:교집합, -:차집합, ^:대칭차집합
"""

#Dictionary
"""
key-value쌍으로 이뤄진 자료형. 3.7부터는 ordered
key는 변경 불가능한 데이터만 활용가능.
{}, dict()을 통해 생성
"""

#HWS 관련
print("\"파일은 c:\\Windows\\Users\\내문서\\Python에 저장이 되었습니다.\"\n나는 생각했다. \'cd를 써서 git bash로 들어가 봐야지\'")

##가로로 출력하기
print(str(i+1) , end=' ')
