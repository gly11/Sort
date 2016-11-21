# coding:utf8
import time
import sort_numbers



READ = open("NUM.txt", "r")
document = READ.read()
list_b = document.split(" ")

lenth = len(list_b)

for i in range(lenth):
	list_b[i] = int(list_b[i])

list_i = list_b
	
start_b = time.clock()
sort_numbers.bubble_sort(list_b)
end_b = time.clock()
running_time_b = end_b - start_b

start_i = time.clock()
sort_numbers.insertion_sort(list_i)
end_i = time.clock()
running_time_i = end_i - start_i

WRITE_B = open("BUBBLE_SORTED.txt", "w")
WRITE_I = open("INSERTION_SORTED.txt", "w")


for x in range(lenth):
	WRITE_B.write(str(list_b[x]))
	if x < lenth-1:
		WRITE_B.write(" ")
	else:
		WRITE_B.write("\n")
		
writing_b = "Running time: " + str( running_time_b ) + "Seconds"
WRITE_B.write(writing_b)


for x in range(lenth):
	WRITE_I.write(str(list_i[x]))
	if x < lenth-1:
		WRITE_I.write(" ")
	else:
		WRITE_I.write("\n")
		
writing_i = "Running time: " + str( running_time_i ) + "Seconds"
WRITE_I.write(writing_i)