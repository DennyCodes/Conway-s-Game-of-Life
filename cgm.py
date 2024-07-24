f=open("boat.in")
import time
lines=f.readlines()
cell=0
for i in range(len(lines)):
  lines[i]=lines[i].strip()
print(lines)
def coord(lines):
  cord=[]
  for i in range(len(lines)):
    cor=lines[i].split()
    cord.append(int(cor[0]))
    cord.append(int(cor[1]))

  return cord
  
def newGrid(cord):
  grids=[]
  for i in range(30):
    row=[]
    for j in range(60):
      row.append('-')
    grids.append(row)
  print(cord)
  while len(cord)>0:
    print(cord)
    grids[cord[0]][cord[1]]='o'
    cord.remove(cord[0])
    cord.remove(cord[0])
  #if cord[0]
  return grids
grid=newGrid(coord(lines))
#grid[11][31]='o'
def printGrid(grid):
  for i in range(30):
    for j in range(60):
      print(grid[i][j],end='')
    print("")


#step grid
#Any live cell with fewer than 2 live neigbor dies 
## any live cell with 2 or 3 LIVES open
##### more than 3 ALIVE neighbor dies
# # #Any DEAD cell with EXACTLY THREE live neigbors becomes REBIRTHED/birthed for first time. 
def neighbor(grid,x,y):
  counter=0
  if y<59 and x<29:
    if grid[x-1][y] == 'o':
      counter+=1
    if grid[x-1][y+1] == 'o':
      counter+=1
    if grid[x-1][y-1] == 'o':
      counter+=1
    if grid[x][y-1] == 'o':
      counter+=1
    if grid[x][y+1] == 'o':
      counter+=1
    if grid[x+1][y+1] == 'o':
      counter+=1
    if grid[x+1][y] == 'o':
      counter+=1
    if grid[x+1][y-1] == 'o':
      counter+=1  
  else:
    if grid[x-1][y] == 'o':
      counter+=1
    if grid[x-1][y-1] == 'o':
      counter+=1
    if grid[x][y-1] == 'o':
      counter+=1
  return counter
    

  
def stepGrid(grid):
  dup=[]
  for i in range(30):
    row=[]
    for j in range(60):
      row.append('-')
    dup.append(row)
  
  for i in range(30):
    for j in range(60):
      n=neighbor(grid,i,j)
  #check uno 
      if n <= 1:
        dup[i][j]='-'
  #check dos
      elif (n == 2 or n == 3) and grid[i][j] == 'o':
        dup[i][j]='o'
  #check tres
      elif n > 3:
        dup[i][j]='-'
  #check cuatro
      elif grid[i][j] == '-' and n==3:
        dup[i][j]='o'
      else:
        dup[i][j]=grid[i][j]
  grid=dup
  return dup

printGrid(grid)
while True:
  grid=stepGrid(grid)
  printGrid(grid)
  time.sleep(0.1)
f.close()











