def PatternUnlock(N, hits):
	keyboardList = [[6, 1, 9], [5, 2, 8], [4, 3, 7]]
	x_prev = 0
	y_prev = 0
	result = 0

	for i in range(N):
		if i == 0:
			for x in range(len(keyboardList)):
				for y in range(len(keyboardList)):
					if hits[i] == keyboardList[x][y]:
						x_prev = x
						y_prev = y
						break
		else:
			for x in range(len(keyboardList)):
				for y in range(len(keyboardList)):
					if hits[i] == keyboardList[x][y]:
						if y-y_prev == 1 or y_prev-y == 1:
							if x_prev != x:
								result += 2**0.5
								x_prev = x
								y_prev = y
								break
							else:
								result += 1
								x_prev = x
								y_prev = y
								break
						else:
							result += 1
							x_prev = x
							y_prev = y
							break
	res = str(int(round(result, 5) * 100000))
	return(res)
