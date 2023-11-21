import random, time, os, keyboard

maze = [["--" for i in range(0, 12)]]
maze += [[" " for i in range(0, 24)] for j in range(12)]
maze += [["--" for i in range(0, 12)]]
for jidx, row in enumerate(maze):
    for idx, cell in enumerate(row):
        if cell == " " and (idx == 0 or idx == 23):
            maze[jidx][idx] = "|"

def place_apple():
    while True:
        row = random.randint(1, 10)
        col = random.randint(0, 23)
        if maze[row][col] == " ":
            maze[row][col] = "*"
            break
        else:
            continue

def drawMaze():
    for i in maze:
        print("".join(i))

directions_dict = {
    "w": "up",
    "a": "left",
    "s": "down",
    "d": "right",
}
directions_list = ["up", "left", "down", "right"]

def shoot():
    global direction
    state = "shooting"
    direction = "right"
    source = (5, 0)
    row = source[0]
    col = source[1]
    length = 5
    old_parts = []
    place_apple()
    while state == "shooting":
        os.system("cls")
        if direction == "right":
            col = col + 1
        elif direction == "left":
            col = col - 1
        elif direction == "up":
            row = row - 1
        elif direction == "down":
            row = row + 1

        if maze[row][col] == " ":
            print("")
            maze[row][col] = "+"
            old_parts.append([row, col])
            check = len(old_parts) - length
            if check != 0:
                for i in range(check):
                    maze[old_parts[0][0]][old_parts[0][1]] = " "
                    old_parts.pop(0)
        elif maze[row][col] == "|" or maze[row][col] == "|" or maze[row][col] == "--" or maze[row][col] == "+":
            print("snake dead")
            state = "lost"
        elif maze[row][col] == "*":
            maze[row][col] = "+"
            length += 1
            old_parts.append([row, col])
            check = len(old_parts) - length
            if check != 0:
                for i in range(check):
                    maze[old_parts[0][0]][old_parts[0][1]] = " "
                    old_parts.pop(0)
            place_apple()
        
        drawMaze()
        
        start_time = time.time()
        where_to_go = ""
        while time.time() - start_time < 0.1:
            if keyboard.is_pressed('w'):
                where_to_go = 'w'
                break
            elif keyboard.is_pressed('a'):
                where_to_go = 'a'
                break
            elif keyboard.is_pressed('s'):
                where_to_go = 's'
                break
            elif keyboard.is_pressed('d'):
                where_to_go = 'd'
                break
        time.sleep(0.2)
        try:
            next_direction = directions_dict[where_to_go]
            dir_idx = directions_list.index(next_direction)
            if dir_idx + 2 == directions_list.index(direction) or dir_idx - 2 == directions_list.index(direction):
                pass
            else:
                direction = next_direction
        except KeyError:
            pass
        
shoot()
