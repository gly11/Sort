# coding:utf8
# shuffle num
import random

WRITE = open("NUM.txt", "w")

l = []

for x in range(500):
	# l.append("%s ") % (str(random.randint(0, 1000)))    // err in this line
	l.append(str(random.randint(0, 10000)))
	l.append(" ")

lenth = len(l)
for m in range(lenth-1):
		WRITE.write(l[m])