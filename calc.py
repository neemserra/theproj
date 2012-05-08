import sys
import math

x = []
for line in open(sys.argv[1]):
   num = int(line)
   x.append(num)

avg = sum(x) / float(len(x))

diffs = []
for num in x:
   diff = num - avg
   diffs.append(diff**2)

stddev = math.sqrt(sum(diffs) / float(len(x)))

print 'the average is', sum(x) / float(len(x))
print 'sumsqdiffs is', sum(diffs)
print 'stddev is', stddev
