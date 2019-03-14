import re

file_name = input("Enter file_name: ")
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
	lines = lines.replace(str(i), str(i*2))

fp = open(file_name,'w')
fp.write(lines)
fp.close()