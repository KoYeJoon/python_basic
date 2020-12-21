"""
f=open("sample.txt",'r')
sum=0
count=0
while True:
	line=f.readline()
	if not line : break
	count=count+1
	result=int(line)
	sum=sum+result

print(sum)
average=sum/count
f.close()

f=open("result.txt",'w')
f.write(str(average))
f.close()
"""

f=open("sample.txt")
lines=f.readlines()
f.close()

total=0
for line in lines :
	score = int(line)
	total += score

average=total/len(lines)
print(total)
f=open("result.txt",'w')
f.write(str(average))
f.close()

