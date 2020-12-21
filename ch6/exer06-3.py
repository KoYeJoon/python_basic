#exer06-3.py
"""
게시물의 총 건수와 한페이지에 보여줄 게시물 수를 입력으로 주었을 때 총페이지 수를 출력하는 프로그램
"""

def getTotalPage(m,n) :
	if m%n == 0 :
		return m//n
	else :
		return m//n + 1

print(getTotalPage(5,10))
print(getTotalPage(15,10))
print(getTotalPage(25,10))
print(getTotalPage(30,10))
