#TIL

#score와 score()의 차이?

#join 함수
"""
word = input()
a = list(word)
for i in range(a.count('a')):
    a.remove('a')
b = ''.join(a)
b
"""

#round 함수
"""
round(3.5-3.12,2) # 값을 소수점 아래 둘째자리까지로 반올림
"""

## string 3.5를 int로 변환할 수는 없습니다.
# 변수 a에 string 3.5를 저장하고 integer로
# 변환하고 오류를 확인해봅시다.

#형변환
"""
d = {'name': 'ssafy', 'year': 2020}
str(d),
list(d),tuple(d),set(d) - key값만 살아남.
# range(d)

negative_num = -4
print(-negative_num) #4 앞의 부호가 곱하기 취급된다.
"""

#논리연산자
"""
('b'and'a') in 'aeiou' #True
"""

#dictionary 키 값이 immutable인 이유?
"""
 개인적인 생각: mutable이면 값이 달라도 주소가 같기
  때문에 key 값이 겹쳐서 대응이 꼬일 수 있기 때문에.
"""
#lower, upper
"""
a = input('문자열을 입력하시오: ')

str_special = a.strip('@''#''~''$''!''>')
str_lower = str_special[1:].lower()
char_upper = str_special[0].upper()
print(char_upper+str_lower)
  """

#format을 이용한 천단위 ,찍기

""" steak = 50000
VAT = int(steak * 0.15)

print(f'''
스테이크    {format(steak,',')}
+ VAT       {format(VAT,',')}
총계 ₩      {format(steak+VAT,',')} 
''')   """

#
""" 
food = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]
food_price = {}
for i in range(len(food)):
    food_price[food[i][0]] = food[i][1]
#list형에 값이 두개 일때 dictionary에 바로 집어 넣기가능
"""

#카페 주문건수 출력하기 daily실습 2-1
"""
orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
order_list = orders.split(',')
#print(order_list)
print(len(order_list))
order_tuple = set(order_list)
print(sorted(order_tuple, reverse=True))

#아이스 음료 주문이 몇개 들어왔는지 확인
order_list = orders.split(',')
ice_count = 0
#print('아이스' in order_list[0]) -in 멤버연산자가 잘 작동하나 확인
for i in order_list: #range가 반복되는데 그것이 정수냐 문자열이나 구분.
    if('아이스' in i): 
        ice_count+=1

print(f'아이스 음료 주문은 {ice_count}잔 입니다.')

**리스트.sort()와 sorted(리스트)의 가장 큰 차이는
리스트.sort()는 본체의 리스트를 정렬해서 변환하는 것이고,
sorted(리스트)는 본체 리스트는 내버려두고, 
정렬한 새로운 리스트를 반환하는 것입니다.
  """
