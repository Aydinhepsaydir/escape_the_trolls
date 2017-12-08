def build_maze():

	array = [] 

	with open("data/maze_structure.txt", "r") as data:

		while True:

			x = data.readline()
			array.append(list(x))

			if not x: break

	for row in array:
		print(" ".join(map(str, row)))

if __name__ == '__main__':
    build_maze()
