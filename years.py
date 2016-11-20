f = open('years.txt', 'r')
writer = open('mult.txt', 'w')
#writer = open('clean_yr.txt', 'w')
# for line in f:
# 	writer.write(line[:4])
# 	writer.write("\n")
for line in f:
	if "^" in line:
		writer.write("1" + "\n")
	else:
		writer.write("0" + "\n")

f.close()
writer.close()

