#house.py

class HousePark:
	lastname = "박"
	def __init__(self,name):
		self.fullname = self.lastname + name
	def travel(self,where) : 
		print("%s, %s 여행을 가다."%(self.fullname,where))
	def love(self,other) :
		print("%s,%s 사랑에 빠졌네" %(self.fullname,other.fullname))
	def fight(self,other) :
		print("%s,%s 싸웠네" %(self.fullname,other.fullname))
	def __sub__(self,other):
		print("%s,%s 이혼했네" %(self.fullname,other.fullname))
	def __add__(self,other) :
		print("%s,%s 결혼했네" %(self.fullname, other.fullname))




#def __add__ : 연산자 오버로딩


class HouseKim(HousePark) :
	lastname = "김"
	def travel(self, where, day) :
		print("%s, %s여행 %d일 가네"  %(self.fullname,where,day))



"""
HouseKim은HousePark을 상속하였으므로
HousePark안에 있는 함수를 사용할 수 있는 듯하다.
HousePark에 정의된 함수를 HouseKim에서는 재정의(오버라이딩)하여 travel함수를 수정하였다.
"""
pey = HousePark("응용")
juliet = HouseKim("줄리엣")
pey.travel("부산")
juliet.travel("부산",3)
pey.love(juliet)
pey+juliet
juliet.fight(pey)
pey-juliet
