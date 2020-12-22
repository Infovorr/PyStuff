def quickSort(container):
	left = 0
	right = len(container) - 1
	quickSortHandler(container, left, right)
	
def quickSortHandler(container, left, right):
	if left < right:
		midpoint = container[right]
		cutoff = split(container, midpoint, left, right - 1)
		swapA = container[right]
		swapB = container[cutoff]
		container[cutoff] = swapA
		container[right] = swapB
		quickSortHandler(container, left, cutoff - 1)
		quickSortHandler(container, cutoff + 1, right)
		
def split(container, midpoint, left, right):
	x = left
	y = left
	while y <= right:
		if container[y] < midpoint:
			swapA = container[x]
			swapB = container[y]
			container[x] = swapB
			container[y] = swapA
			x += 1
		y += 1
	return x
	
	
def inSort(container):
	size = len(container)
	for index in range(1, size):
		insert(container, index)
		
def insert(container, index):
	item = container[index]
	while index > 0 and container[index-1] > item:
		container[index] = container[index-1]
		index -= 1
	container[index] = item
	
	
def merge(containerA, containerB):
	containerC = []
	x = 0
	y = 0
	aSize = len(containerA)
	bSize = len(containerB)
	while x < aSize and y < bSize:
		if containerA[x] < containerB[y]:
			containerC.append(containerA[x])
			x += 1
		else:
			containerC.append(containerB[y])
			y += 1
	containerC.extend(containerA[x:])
	containerC.extend(containerB[y:])
	return containerC
	
def merSort(container):
	contSize = len(container)
	midpoint = contSize // 2
	if contSize <= 1:
		return container[:]
	left = container[:midpoint]
	right = container[midpoint:]
	leftCont = merSort(left)
	rightCont = merSort(right)
	return merge(leftCont, rightCont)