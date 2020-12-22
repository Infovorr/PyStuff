import random
import sort
import sys
import time

if __name__ == '__main__':
	insertion = [0]
	merging = [0]
	quicking = [0]
	inserTime = 0
	merTime = 0
	quickTime = 0
	sampleSize = 25		#Determines the number of samples for the profiler
	
	for i in range(sampleSize):
		x = random.sample(range(99990), 10000)
		startTime = time.time()
		sort.inSort(x)
		endTime = time.time()
		insertion.append(endTime - startTime)
		
	for i in range(sampleSize):
		x = random.sample(range(99990), 10000)
		startTime = time.time()
		sort.merSort(x)
		endTime = time.time()
		merging.append(endTime - startTime)
		
	for i in range(sampleSize):
		x = random.sample(range(99990), 10000)
		startTime = time.time()
		sort.quickSort(x)
		endTime = time.time()
		quicking.append(endTime - startTime)
		
	for i in range(sampleSize):
		inserTime += insertion[i]
		merTime += merging[i]
		quickTime += quicking[i]
	
	inserTime = inserTime / sampleSize
	merTime = merTime / sampleSize
	quickTime = quickTime / sampleSize
	
	print("Insertion sort averaged " + str(inserTime) + " seconds")
	print("Merge sort averaged " + str(merTime) + " seconds")
	print("Quick sort averaged " + str(quickTime) + " seconds")