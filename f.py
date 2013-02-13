def double(x):
	return 2* x

def triple(x):
	return 3*x
	
def for_each(values, func):
	result = []
	for v in values:
		temp = func(v)
		result.append(temp)
	return result
	
numbers = [1,3,5]
result = for_each(numbers, double)

	
print 'double f', numbers, 'is', result

another = []
for n in numbers:
	temp = triple(n)
	another.append(temp)
	
print 'triple f', numbers, 'is', another

