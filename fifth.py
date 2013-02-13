import sys

def count_birds(reader, nameofbreed):
   reader.readline() # first line is header, so ignore
   total = 0
   for line in reader:
       date, breed, count = line.split(',')
       if nameofbreed == breed:
			count = int(count)
			total += count
   return total

grand_total = 0
for filename in sys.argv[2:]:
   source = open(filename, 'r')
   total = count_birds(source, sys.argv[1])
   grand_total += total
   print total, filename
   source.close()
print grand_total, 'total'
