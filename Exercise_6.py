def PatternUnlock(N, hits):
	keyboardList = [[6, 1, 9], [5, 2, 8], [4, 3, 7]]
	x_prev = 0
	y_prev = 0
	result = 0

	for i in range(N):
		print("#############    I = ", i)
		if i == 0:
			#print("i = 0 line")
			for x in range(len(keyboardList)):
				for y in range(len(keyboardList)):
					if hits[i] == keyboardList[x][y]:
						print("hits[i] = ", hits[i])
						print("keyboardList[x][y] = ", keyboardList[x][y])
						print("x = ", x)
						print("y = ", y)
						x_prev = x
						y_prev = y
						print("x_prev = ", x_prev)
						print("y_prev = ", y_prev)
						break
		else:
			#print("i > 0 line")
			for x in range(len(keyboardList)):
				for y in range(len(keyboardList)):
					if hits[i] == keyboardList[x][y]:
						print("hits[i] = ", hits[i])
						print("keyboardList[x][y] = ", keyboardList[x][y])
						print("x = ", x)
						print("y = ", y)
						print("x_prev = ", x_prev)
						print("y_prev = ", y_prev)
						if y-y_prev == 1 or y_prev-y == 1:
							if x_prev != x:
								result += 2**0.5
								x_prev = x
								y_prev = y
								#print("result = ", result)
								break
							else:
								result += 1
								x_prev = x
								y_prev = y
								#print("result = ", result)
								break
						else:
							result += 1
							x_prev = x
							y_prev = y
							break
							#print("result = ", result)
	print("result = ", round(result, 5))
