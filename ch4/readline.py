"""
#readlinee.py
f=open("newFile.txt",'r')
line = f.readline()
print(line)
f.close()
"""
#readline_all.py
f=open("newFile.txt",'r')
"""
while True:
	line=f.readline()
	if not line : break
	print(line)

while 1:
	data=input()
	if not data: break
	print(data)

lines=f.readlines()
for line in lines :
	print(line)
"""
data=f.read()
print(data)
f.close()
