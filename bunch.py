# 4 = {[1,sum(3)]} {[2,sum(2)]}
# 4 = {[1,1,2]} {[2,sum(2)]}
# [x1 <= x2 <= x3 <= ...]

# 4 = { 1111, 112, 13, 22, }
# 3 = { [1, 1, 1], [1, 2], [3] }
# 2 = { [1, 1], [2] }
# 1 = { [1] }

def getBunchSequenceTest(sum):
	if(sum == 1):
		return [ [1] ]
	if(sum == 2):
		return [ [1, 1], [2] ]
	if(sum == 3):
		return [ [1,1,1], [1,2], [3] ]
	if(sum == 4):
		return [ [1,1,1,1], [1,1,2], [1,3], [2,2], [4] ]
	if(sum == 5):
		return [[1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 3], [1, 2, 2], [1, 4], [2, 3], [5]]
	if(sum == 6):
		return [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 2], [1, 1, 1, 3], [1, 1, 2, 2], [1, 1, 4], [1, 2, 3], [1, 5], [2, 2, 2], [2, 4], [3, 3], [6]]
	if(sum == 7):
		return [[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 2], [1, 1, 1, 1, 3], [1, 1, 1, 2, 2], [1, 1, 1, 4], [1, 1, 2, 3], [1, 1, 5], [1, 2, 2, 2], [1, 2, 4], [1, 3, 3], [1, 6], [2, 2, 3], [2, 5], [3, 4], [7]]
	if(sum == 8):
		return [[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 2], [1, 1, 1, 1, 1, 3], [1, 1, 1, 1, 2, 2], [1, 1, 1, 1, 4], [1, 1, 1, 2, 3], [1, 1, 1, 5], [1, 1, 2, 2, 2], [1, 1, 2, 4], [1, 1, 3, 3], [1, 1, 6], [1, 2, 2, 3], [1, 2, 5], [1, 3, 4], [1, 7], [2, 2, 2, 2], [2, 2, 4], [2, 3, 3], [2, 6], [3, 5], [4, 4], [8]]
	if(sum == 9):
		return [[1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 2], [1, 1, 1, 1, 1, 1, 3], [1, 1, 1, 1, 1, 2, 2], [1, 1, 1, 1, 1, 4], [1, 1, 1, 1, 2, 3], [1, 1, 1, 1, 5], [1, 1, 1, 2, 2, 2], [1, 1, 1, 2, 4], [1, 1, 1, 3, 3], [1, 1, 1, 6], [1, 1, 2, 2, 3], [1, 1, 2, 5], [1, 1, 3, 4], [1, 1, 7], [1, 2, 2, 2, 2], [1, 2, 2, 4], [1, 2, 3, 3], [1, 2, 6], [1, 3, 5], [1, 4, 4], [1, 8], [2, 2, 2, 3], [2, 2, 5], [2, 3, 4], [2, 7], [3, 3, 3], [3, 6], [4, 5], [9]]
	else:
		raise('ошибка')

def allElemsGreater(seqlist, n):
	for i in range(len(seqlist)):
		if seqlist[i] < n:
			return False
	return True

def getBunchSequence(sum):
	arr = []
	for i in range(1, sum // 2 + 1):
		# print(i)
		if sum - i < 10:
			seqlist = getBunchSequenceTest(sum - i)
		else:
			seqlist = getBunchSequence(sum - i)
		for j in range(len(seqlist)):
			x = [i] + seqlist[j]
			# print([i],"+", seqlist[j],"=",x)
			if allElemsGreater(seqlist[j], i):
				arr.append(x)
	arr.append([sum])
	return arr
	
def getBunchSequenceMaxBunches(sum, maxBunches, maxCoins):
	arr = []
	for i in range(1, sum // 2 + 1):
		# print(i)
		if sum - i < 2:
			seqlist = getBunchSequenceTest(sum - i)
		else:
			seqlist = getBunchSequence(sum - i)
		for j in range(len(seqlist)):
			x = [i] + seqlist[j]
			# print([i],"+", seqlist[j],"=",x)
			if len(x) <= maxBunches and max(x) <= maxCoins:
				if allElemsGreater(seqlist[j], i):
					arr.append(x)
	x = [sum]
	if len(x) <= maxBunches and max(x) <= maxCoins:
		arr.append(x)
	return arr
		
def getBunchBySearch(sum):
	# функция недописана
	# должна использовать поиск в глубину
	arr = []
	sumOfArr = 0
	n = 1
	i = 0
	arr.append(0)
	while n < sum:
		sumOfArr
		arr[i] = n
		n += 1
	
 	
def printList(arr):
	for i in arr:
		print(i)
#s = []
# print(allElemsGreater([1,1], 2))
# print(allElemsGreater([1,3], 2))
# print(allElemsGreater([2,2], 2))
if __name__=='__main__':
	for i in range(0, 13):
		print(str(i) + ')')
		printList(getBunchSequenceMaxBunches(i, maxBunches=3, maxCoins=6))
		print()