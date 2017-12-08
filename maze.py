def build_maze():

	array = []
	with open("data/maze_structure.txt", "r") as text:
		for line in text:
			maze_wall = text.readline()
			array.append(maze_wall.split())

	for i in array:
		print(i)

if __name__ == '__main__':
    build_maze()
