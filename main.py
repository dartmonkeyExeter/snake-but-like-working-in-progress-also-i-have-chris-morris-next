import random
import time
import os
import keyboard

def init_maze():
    maze = [["-" for i in range(0, 24)]]
    maze += [[" " for i in range(0, 24)] for j in range(12)]
    maze += [["-" for i in range(0, 24)]]

    for jidx, row in enumerate(maze):
        for idx, cell in enumerate(row):
            if cell == " " and (idx == 0 or idx == 23):
                maze[jidx][idx] = "|"
    return maze


def place_apple(maze):
    while True:
        row = random.randint(1, 10)
        col = random.randint(0, 23)
        if maze[row][col] == " ":
            maze[row][col] = "*"
            break
        else:
            continue

def drawMaze(maze):
    for i in maze:
        print("".join(i))

directions_dict = {
    "w": "up",
    "a": "left",
    "s": "down",
    "d": "right",
}
directions_list = ["up", "left", "down", "right"]

def gameloop():    
    maze = init_maze()
    global direction
    state = "gamelooping"
    direction = "right"
    source = (5, 0)
    row = source[0]
    col = source[1]
    length = 3
    old_parts = []
    place_apple(maze)

    while state == "gamelooping":
        os.system("cls")
        if direction == "right":
            col = col + 1
        elif direction == "left":
            col = col - 1
        elif direction == "up":
            row = row - 1
        elif direction == "down":
            row = row + 1

        if (
            maze[row][col] == "|"
            or maze[row][col] == "|"
            or maze[row][col] == "-"
            or maze[row][col] == "+"
        ):
            print(f"snake dead\nscore: {length-3}")
            state = "lost"
        elif maze[row][col] == " ":
            print("")
            maze[row][col] = "+"
            old_parts.append([row, col])
            check = len(old_parts) - length
            if check != 0:
                for i in range(check):
                    maze[old_parts[0][0]][old_parts[0][1]] = " "
                    old_parts.pop(0)
        elif maze[row][col] == "*":
            maze[row][col] = "+"
            length += 1
            old_parts.append([row, col])
            check = len(old_parts) - length
            if check != 0:
                for i in range(check):
                    maze[old_parts[0][0]][old_parts[0][1]] = " "
                    old_parts.pop(0)
            place_apple(maze)

        drawMaze(maze)

        start_time = time.time()
        where_to_go = ""
        while time.time() - start_time < 0.2:
            if keyboard.is_pressed('w'):
                where_to_go = 'w'
            elif keyboard.is_pressed('a'):
                where_to_go = 'a'
            elif keyboard.is_pressed('s'):
                where_to_go = 's'
            elif keyboard.is_pressed('d'):
                where_to_go = 'd'

        try:
            next_direction = directions_dict[where_to_go]
            dir_idx = directions_list.index(next_direction)
            if dir_idx + 2 == directions_list.index(direction) or dir_idx - 2 == directions_list.index(direction):
                pass
            else:
                direction = next_direction
        except KeyError:
            pass

while True:
    gameloop()
    play_again = input("play again? (y/n) ")
    if play_again == "n":
        break
