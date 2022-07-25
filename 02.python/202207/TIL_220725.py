#python data구조 및 활용

#문자열
"""
문자열 조회/탐색 및 검증 메서드
    s.find(x) - x의 첫번째 위치를 반환, 없으면 -1
    s.index(x) - x의 첫번째 위치를 반환 없으면 에러
문자열 관련 검증 메서드
    isdecimal = 진짜 숫자가
    isdigit = 우리가 수라고 부르는
    isnumeric = 숫자도 볼수도 있지 않나? 
    전화번호부는 isdecimal
문자열 변경 메서드
s.replace(old, new[,count])
s.strip([])공백이나 특정 문자를 제거
s.capitalize - 첫번째 문자를 대문자로
'separator'.join([iterable]) - 반복가능한 컨테이너 요소들읠 separator로 합쳐 문자열 반환

  """

  #리스트
"""
L.append(x) - 리스트 마지막에 항목 x를 추가
L.insert(i,x) - 리스트 인덱스 i에 항목 x를 삽입
L.remove(x) - 리스트 가장 왼쪽에 있는 항목(첫 번째) x를 제거
                항목이 존재하지 않을 경우, ValueError
L.pop() - 리스트 가장 오른쪽에 있는 항목(마지막)을 반환 후 제거
L.pop() - 리스트 인덱스 i에 있는 항목을 반환 후 제거
L.extend(m) - 순회형 m의 모든 항목들의 리스트 끝에 추가(+=과 같은 기능)
L.index(x,start,end) - 리스트에 있는 항목 중 가장 왼쪽에 있는 항목 x의 인덱스를 반환
L.reverse() - 순서를 반대로 뒤집을. 정렬하는 것이 아님. 원본을 뒤집는 것.
L.sort() - 리스트를 정렬 sorted와 다른 점은 리스트 자체를 변경한다는 것.
            sorted()는 새로운 리스트 만듬.
L.count(x) - 리스트에서 항목 x가 몇개 존재하는지 갯수를 반환

"""

#튜플
"""
튜플은 변경할 수 없기 대문에 값에 영향을 미치지 않는 메서드만을 지원
리스트 메서드 중 항목을 변경하는 메서드들을 제외하고 대부분 동일

"""

#셋
"""
s.copy() - 셋의 얕은 복사본을 반환
s.add(x) - 항목 x가 셋 s에 없다면 추가
s.pop - 셋 s에서 랜덤하게 항목을 반환하고 해당 항목을 제거 
        set이 비어 있을 경우 keyerror
s.remove(x) - 항목 x를 셋 s에서 삭제.
s.discard(x) - 항목 x가 셋 s에 있는 경우 항목 x를 셋s에서 삭제.
s. update(t) - 셋 t에 있는 모든 항목 중 셋 s에 없는 항목을 추가
s.clear() - 모든 항목을 제거

"""
#딕셔너리
"""
d.clear
d.copy
d.key()
d.values()
d.items()
d.get(k) - 키 k의 값을 반환하는데, 키 k가 딕셔너리 d에 없을 경우 none을 반환
d.get(k,v) - 키 k의 값을 반환하는데, 키 k가 딕셔너리 d에 없을 경우 v를 반환(default 설정 가능)
d.pop(k) - 키 k의 값을 반환하고 키 k인 항목을 딕셔너리 d에서 삭제하는데, 키 k가
        딕셔너리 d에 없을 경우 keyError을 발생.
d.pop(k,v) - 키 k의 값을 반환하고 키 k인 항목을 딕셔너리 d에서 삭제하는데, 키 k가
        딕셔너리 d에 없을 경우 v를 반환.
"""

#얕은 복사와 깊은 복사
""" 
이차원 배열일때 얕은 복사를 하면 원본 리스트가 수정된다.
방지하기 위해서는 깊은 복사 copy.deepcopy()를 사용
무분별하게 사용하면 리소스를 많이 잡아먹음. 
"""