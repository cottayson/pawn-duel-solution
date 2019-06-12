from bunch import *

def step(bunch):
	arr = []
	for i in range(len(bunch)):
		for amount in range(1, 4): # максимум 3 монеты
			if amount > bunch[i]:
				break
			b = bunch.copy()
			if amount == b[i]:
				del b[i]
			else:
				# amount < b[i]
				b[i] -= amount
			b.sort()
			if b not in arr:
				arr.append(b)
	arr.sort()
	return arr

def winToStr(lose):
	return "lose" if lose else "win"

def isLose(nextStates, loseBunches):
	for state in nextStates:
		for currentBunches in loseBunches:
			if state in currentBunches:
				return False
	return True

def calculate(allLoseBunches, iteration):
	# iteration = amount of coins
	loseBunches = allLoseBunches[-3:]
	# проверяем только крайние три справа
	# => по правилам игры максимум f = (-3) монеты
	seq = getBunchSequenceMaxBunches(iteration, maxBunches=3, maxCoins=100)
	loseStates = []
	for i in range(len(seq)):
		currentState = seq[i]
		nextStates = step(currentState)
		lose = isLose(nextStates, loseBunches)
		if lose:
			loseStates.append(currentState)
		# print()
		# print(str(i) + ') ' + winToStr(lose))
		# print(str(seq[i]) + ' =>', nextStates)
	return loseStates
	
loseBunches = []

#0
loseBunches.append([
	[]
])

#1
loseBunches.append([
	
])

for index in range(2, 20):
	print("\nindex: " + str(index))
	loseStates = calculate(loseBunches, index)
	loseBunches.append(loseStates)
	printList(loseStates)

# [число монет: проигрышные кучи]
# 0: нет особых куч
# 1: 1
# 2: нет особых куч
# 3: 111
# 4: 22
# 5: 11111, 14, 5
# 6: 1122, 123, 33
# 7: 1{7}, 1114, 115
# 8: 111122, 11123, 1133, 2222, 224, 26
# 9: 1{9}, 111114, 11115, 144, 18, 45, 9
# 10: 1{6}22, 1{5}23, 111133, 112222, 11224, 1126, 12223, 1225, 1234, 127, 136, 2233, 235, 334, 37
# 11: 1{11}, 1{7}4, 1{6}5, 11144, 1118, 1145, 119, 155