import player 

def build_maze():

	maze = [] 

	with open("data/maze_structure.txt", "r") as maze_data:

		while True:

			line = maze_data.readline()
			maze.append(list(line))

			if not line: break

	for row in maze:
		print(" ".join(map(str, row)))

if __name__ == '__main__':
    build_maze()
