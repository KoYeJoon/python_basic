#vartest.py

a=1
def vartest(a):
	a=a+1


"""
그냥 vartest(a)하면 함수 밖의 a로 인식하여 그냥 그대로 원래의 a=1이 출력됨.
"""
vartest(a)
print(a)
