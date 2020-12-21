#exercise3.py
dic = {'.-':'A' , '-...':'B', '-.-.':'C', '-..':'D', '.' : 'E','..-.':'F',
	'--.':'G', '....':'H', '..':'I','.---':'J','-.-':'K','.-..':'L',
	'--':'M', '-.':'N', '---':'O', '.--.':'P', '--.-':'Q','.-.':'R',
	'...':'S', '-':'T', '..-':'U', '...-':'V', '.--':'W', '-..-':'X',
	'-.--':'Y', '--..':'Z'}

def morse(s):
	result = []
	for word in s.split(" "):
		for char in word.split(" "):
			result.append(dic[char])
		result.append(" ")
	return "".join(result)

print(morse('.... . ... .-.. . . .--. ... . .- .-. .-.. -.--'))
