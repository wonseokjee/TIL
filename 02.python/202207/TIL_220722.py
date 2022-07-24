#dictionary get함수 사용하기.
""" dictionary.get 은 key가 없으면 none을 출력
있는지 없는지 모르는 상황에 쓰면 좋음. 없어도 에러가 안남.
get('price' , '비상장주식입니다') 없으면 ,옆의 문자열 출력
dict['key']는 없으면 실행하면 안되는 상황. 에러가 나면 프로그램 멈춤. """

# list indices must be integers or slices, not str 에러
""" 
파이썬에서 자료형이 명시적으로 나타나지 않으니 생기는 문제
numbers = ['one', 'two', 'three', 'four', 'five']
for n in numbers:
    print(n)
    
n이 어떻게 쓰이는 지 잘생각하고 쓰자.
딕셔너리는 복잡하니까 딕셔너리 안에 딕셔너리가 있을때
내가 지금 쓰고 있는 n이 어떤 자료형인지 어떻게 생겼는지
하나하나씩 쪼개서 생각해보자. 
"""


# 폴더 하위에 있는 각각의 파일에 접근하기
#os란? problem_d 
"""
import os로 사용
함수명: os.listdir('path')
    동작:path내의 모든 폴더와 파일을 list 형태로 반환
함수명: os.path.isdir('path)
    동작: path가 directory라면 True를 반환. False를 반환.

for id in movies_json:
    folder_open = open('data/movies/'+id, encoding='utf-8')
    folder_json = json.load(folder_open)
json이 열릴때 open('문자열이면 된다.')- 그래서 +가능.

"""


#딕셔너리에 끼워 넣기
"""
dict = {}
dict['a'] = b
->dict = {'a':b}
movies_json_revenue[folder_json.get('revenue')] = folder_json.get('title')
"""


#value로 키 찾기
"""
aa = {'0': 'AA', 
      '1': 'BB', 
      '2': 'CC'}
[k for k, v in aa.items() if v == 'CC']

value를 이용해서 자주 key를 찾는다면
매번 딕셔너리 전체를 순회하면서 가져오기 때문에 비효율적.
그래서 딕셔너리 키 밸류 바꾸기 활용 가능.
"""

# 딕셔너리 키 밸류 바꾸기
"""
aa = {'0': 'AA', '1': 'BB', '2': 'CC'}
bb = {v:k for k,v in aa.items()} 
    ->{'AA': '0', 'BB': '1', 'CC': '2'}
bb.get('CC')
    ->'2'
"""

# 5adadda번
"""
이중 for문일 때 너무 많이 출력되면 
이중 for문을 쓰는게 맞는 건지 잘 파악하고 쓰자
"""

# if i in (release_reverse.keys()[5:7])
"""
  -키, 밸류는 슬라이싱 불가.
"""