import sys
source = file(sys.argv[1], 'r')
#first_line = source.readline()
#first_line = first_line.strip()
number = 0
for line in source:
	#temp = line.strip()
	date, breed, count = line.split(',')
	try:
		count = int(count)
	except ValueError:
		continue
	number +=count
	#print date
#print first_line
#print "number of lines: ", number
print number
source.close()