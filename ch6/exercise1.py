#exercise1.py
#문자열 압축하기
def compress_string(s):
	_c=""
	count = 0
	result = ""
	for c in s:
		if c != _c :
			_c = c
			if count:
				result = result+str(count)
			result = result + c
			count=1
		else :
			count = count+1
	if count :
		result = result+str(count)
	return result


print(compress_string("aaabbcccccca"))	
