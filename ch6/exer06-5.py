#exer06-5.py
"""
문서파일을 읽어서 파일 내의 탭을 공백 4개로 바꿔주는 스크립트
필요한 기능은 ? 문서 파일 읽어 들이기, 문자열 변경하기
입력받는 값은 ? 탭을 포함한 문서파일
출력하는 값은 ? 탭이 공백으로 수정된 문서 파일
"""
import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace("\t"," "*4)

f = open(dst,'w')
f.write(space_content)
f.close()
