#아스키 코드
"""
숫자를 알파벳으로 chr()
알파벳을 숫자로 ord()
#4_5_WS 숫자의 의미
def get_secret_word(x):
    print(''.join(list(map(chr, x))))
get_secret_word([83,115,65,102,89])

#4_6 내 이름은 몇일까?
def get_secret_number(x):
    print(sum(list(map(ord,x))))
get_secret_number('happy')
"""

""" 
#기본인자
def greeting(age, name='peter'): #키워드 인자가 기본 인자 보다 먼저 올수는 없다.
    return f'{name}은 {age}살입니다.'
"""

#가변 키워드 인자
"""
def my_dict(**kwargs):
    return kwargs
print(my_dict(한국어='안녕', 영어='hi', 독일어='Guten Tag'))
#{'한국어': '안녕', '영어': 'hi', '독일어': 'Guten Tag'}

"""

#list comprehension 다시 연습하기
""" numbers = [1 ,2, 3]
numbers_list = []
'for i in range(len(numbers)):
    numbers_list.append(str(numbers[i]))
print(''.join(numbers_list)) '
numbers_list = [str(numbers[i]) for i in range(len(numbers))]
print(''.join(numbers_list)) """

"""
num = sum(list(map(int, input('숫자를 입력하시오: ').split(' '))))
print(num)
"""

#dictionary 값 value로 정렬하기
""" 
사전의 value값으로 정렬하는 방법은 sorted 함수를 사용합니다.
sorted함수는 key를 받을 수 있는데, 여기서 lamda 식을 사용해서
 튜플에서 1번째 index를 기준으로 정렬
>>>d={'A':3,'C':1,'G':5,'T':2}>>>d{'A':3,'C':1,'G':5,'T':2}
#d.items()를 하여 각 key,value가 tuple로들어있는
# ##리스트 (dict_items 객체)로 만듭니다>>>
# d.items()dict_items([('A',3),('C',1),('G',5),('T',2)])
# ##dict_items객체를 lambda식을 활용하여 정렬을 하는 거지요 
# ## 오름차순 정렬>>>
# sorted(d.items(),key=lambda x:x[1])
# [('C',1),('T',2),('A',3),('G',5)]
# ##내림차순 정렬
# >>>sorted(d.items(),key=lambda x:x[1],reverse=True)
# [('G',5),('A',3),('T',2),('C',1)]

 """

 #enumerate 다시 보기 
