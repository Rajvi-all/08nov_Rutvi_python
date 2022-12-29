# Python3 code to convert a tuple
# into a string using a for loop


def convertTuple(tup):
	
	str = ''
	for item in tup:
		str = str + item
	return str


tuple = ('d', 'u', 'm', 'h', 'v')
str = convertTuple(tuple)
print(str)
