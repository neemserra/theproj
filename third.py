import sys
for filename in sys.argv[1:]:
	print filename
	source = open(filename, 'r')
	first_line = source.readline().strip()
	print 'first line of', filename, 'is', first_line
	source.close()