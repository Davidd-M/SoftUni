rows = int(input())

maze = []

for row in range(rows):
    current_row = input()
    maze.append(current_row)
maze_row = maze[1]
print(maze_row[2])
print(maze_row[3])
print('\n'.join(maze))
