def insertion_sort( lists ):
	
	lenth = len( lists )
	for j in range( 1, lenth ):
		key = lists[j]
		i = j-1
		
		while i >= 0 and lists[i]>key:
			lists[i+1] = lists[i]
			i -= 1
		lists[i+1] = key
		
	return lists
	
def bubble_sort(lists):
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists