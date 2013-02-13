
def aggregate(values, func):
	current = values[0]
	for v in values[1:]:
		current = func(current, v)	
	return current
	
def add(a, b):
	return a+b
	
def mult(a, b):
	return a*b

numbers = [1, 3, 5]
print 'numbers are', numbers
print 'add them up', aggregate(numbers, add)
print 'multiply them', aggregate(numbers, mult)