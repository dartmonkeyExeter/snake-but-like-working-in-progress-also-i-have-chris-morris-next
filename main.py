import random, time, os
          
#Initialise maze, bombs, laser source and exit gate
maze = [[" -","--","--","--","--","--","--","--","--","--","--","- "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" -","--","--","--","--","--","--","--","--","--","--","- "]
       ]

def drawMaze():

  for i in range(0,12):
    line = ""
    for j in range(0,12):
       line = line + maze[i][j]
    if i>0 and i<10:
      print(" " + line)
    elif i==0 or i==11:
      print("  " + line)
    elif i==10:
      print(" " + line)

def shoot():
  global direction
  state="shooting"
  source = (5,0)
  row = source[0]
  col = source[1]
  direction="right"
  length = 3

  while state=="shooting":
      os.system("cls")
      if direction=="right":
        col = col + 1
      ##Add code here to allow laser to move in all 4 directions  
      elif direction=="left":
        col = col - 1
      elif direction=="up":
        row = row + 1
      elif direction=="down":
        row = row - 1
        
      if maze[row][col]=="  ":
        print("")
        maze[row][col]="++"
        # code here for deleting old snake parts
      elif maze[row][col]==" |" or maze[row][col]=="| " or maze[row][col]=="--":
        print("snake dead")
        state="lost"

      drawMaze()
      time.sleep(0.2)


shoot()
