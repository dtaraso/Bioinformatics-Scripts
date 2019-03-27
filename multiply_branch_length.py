import re
import sys

file_name = sys.argv[1]
branch_length_factor = float(sys.argv[2])
with open(file_name) as fp:
    lines = fp.read().strip()
    fp.close()

branch_lengths = []
count = 0
for i in re.split('[:,)]',lines):
	try:
		j = float(i)
		branch_lengths.append(j)
	except ValueError:
		continue

for i in branch_lengths:
	lines = lines.replace(str(i), str(i*branch_length_factor))

fp = open(file_name,'w')
fp.write(lines)
fp.close()
