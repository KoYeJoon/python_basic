#exercise2.py

def duplicateNumber(s):
	result = []
	for num in s:
		if num not in result:
			result.append(num)
		else:
			return False
	return len(result) == 10

print(duplicateNumber("0123456789"))
print(duplicateNumber("01234"))
print(duplicateNumber("01234567890"))
print(duplicateNumber("01223345"))
