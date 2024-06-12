grid = [[6,5,9,8], [6,4,8,6], [9,8,4,7]]
supply = [20, 35, 55]
demand = [36, 32, 24, 18]
INF = 10**3
n = len(grid)
m = len(grid[0])
ans = 0


def findDiff(grid):
	rowDiff = []
	colDiff = []
	for i in range(len(grid)):
		arr = grid[i][:]
		arr.sort()
		rowDiff.append(arr[1]-arr[0])
	col = 0
	while col < len(grid[0]):
		arr = []
		for i in range(len(grid)):
			arr.append(grid[i][col])
		arr.sort()
		col += 1
		colDiff.append(arr[1]-arr[0])
	return rowDiff, colDiff


# цикл працює, доки не вичерпаються як попит, так і пропозиція
while max(supply) != 0 or max(demand) != 0:
	# знаходження різниці рядків і стовпців
	row, col = findDiff(grid)

	maxi1 = max(row)

	maxi2 = max(col)

	if(maxi1 >= maxi2):
		for ind, val in enumerate(row):
			if(val == maxi1):
				# пошук мінімального елемента в індексі сітки, де максимальний був знайдений у різниці рядків
				mini1 = min(grid[ind])
				for ind2, val2 in enumerate(grid[ind]):
					if(val2 == mini1):
						mini2 = min(supply[ind], demand[ind2])
						ans += mini2 * mini1
						supply[ind] -= mini2
						demand[ind2] -= mini2
						if(demand[ind2] == 0):
							for r in range(n):
								grid[r][ind2] = INF
						else:
							grid[ind] = [INF for i in range(m)]
						break
				break
	#якщо елемент рядка diff max більший за елемент col diff max
	else:
		for ind, val in enumerate(col):
			if(val == maxi2):
				# знаходження мінімального елемента в індексі сітки, де максимальний був знайдений у col різниці
				mini1 = INF
				for j in range(n):
					mini1 = min(mini1, grid[j][ind])

				for ind2 in range(n):
					val2 = grid[ind2][ind]
					if val2 == mini1:
						mini2 = min(supply[ind2], demand[ind])
						ans += mini2 * mini1
						supply[ind2] -= mini2
						demand[ind] -= mini2
						if(demand[ind] == 0):
							for r in range(n):
								grid[r][ind] = INF
						else:
							grid[ind2] = [INF for i in range(m)]
						break
				break

print("Найкраще рішення є ", ans)