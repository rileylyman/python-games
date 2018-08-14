import graphics
import random

MaxFillCount = 24

def DrawGrid():

    win = graphics.GraphWin('Sudoku', 800, 800 )
    win.setBackground('white')
    win.setCoords(0,0,9,9)

    for i in [1,2,3,4,5,6,7,8]:

        lineX = graphics.Line(graphics.Point(i,0),graphics.Point(i,9))
        lineY = graphics.Line(graphics.Point(0,i),graphics.Point(9,i))
        
        if (i%3 == 0):
            lineX.setWidth(4)
            lineY.setWidth(4)
        else:
            lineX.setWidth(2)
            lineY.setWidth(2)

        lineX.draw(win)
        lineY.draw(win)

    return win

def MakeSudokuGrid():

    win = DrawGrid()

    gridDict = {}
    for x in range(9):
        for y in range(9):

            entry = graphics.Entry(graphics.Point(x+0.5,y+0.5),5)
            gridDict[(x,y)] = entry
            entry.draw(win)

    while True:

        click = win.checkMouse()
        if click:
            if click.getX() < 1 and click.getY() < 1:
                break

    win.close()

    for x in range(9):
        for y in range(9):

            if gridDict.get((x,y)).getText():
                gridDict[(x,y)] = int(gridDict.get((x,y)).getText())
            else: gridDict[(x,y)] = 0

    return gridDict

def CheckForDuplicate(gridDict,x,y,n):

    hasDuplicateX = False
    hasDuplicateY = False
    hasDuplicateInBox = False

    for i in range(9):
       if (gridDict.get((i,y)) == n and i != x):
           hasDuplicateX = True
    for j in range(9):
        if (gridDict.get((x,j)) == n and j != y):
            hasDuplicateY = True


    modPositionX = (x)%3
    modPositionY = (y)%3
    posDict = {0:[0,1,2], 1:[-1,0,1], 2:[-2,-1,0]}

    for i in posDict.get(modPositionX):
        for j in posDict.get(modPositionY):

            if (i!=0 or j!=0):
                if gridDict.get((x+i,y+j)) == n:
                    hasDuplicateInBox = True


    return hasDuplicateX, hasDuplicateY, hasDuplicateInBox 

def AssignRandomNumbers(win):
   

    fillCount = 0
    gridDict = {}

    for i in range(9):
        for j in range(9):
            
            if fillCount < MaxFillCount:

                n = random.randrange(1,100)
                if n < 30:
                    gridDict[(i,j)] = 1
                    fillCount += 1

                else: gridDict[(i,j)] = 0

            else: gridDict[(i,j)] = 0

    for x in range(9):
        for y in range(9):

            if gridDict.get((x,y)) == 0:
                pass
            else:
                gridDict[(x,y)] = random.randint(1,9)

   
    for x in range(9):
        for y in range(9):
            
            if gridDict.get((x,y)) != 0:
                 hasDuplicateX, hasDuplicateY, hasDuplicateInBox = CheckForDuplicate(gridDict,x,y,gridDict.get((x,y)))

                 while (not ((hasDuplicateX == False) and (hasDuplicateY == False) and (hasDuplicateInBox == False))):

                    gridDict[(x,y)] += 1
                    gridDict[(x,y)] = gridDict[(x,y)]%10
                    if gridDict.get((x,y)) == 0:
                        gridDict[(x,y)] = 1


                    hasDuplicateX, hasDuplicateY, hasDuplicateInBox = CheckForDuplicate(gridDict,x,y,gridDict.get((x,y)))


    return gridDict

def CatalogSpaces(gridDict):

    changeMap = {}

    for x in range(9):
        for y in range(9):
        
            if gridDict.get((x,y)) == 0:
                changeMap[(x,y)] = True
            else: changeMap[(x,y)] = False

    return changeMap

def FindPossibleValues(gridDict,OpenSpaces):
    
    possibleValues = {}
    for x in range(9):
        for y in range(9):

          if OpenSpaces.get((x,y)):

                list = []
                for i in range(1,11):

                    if i != gridDict.get((x,y)):
                        hasDuplicateX, hasDuplicateY, hasDuplicateInBox = CheckForDuplicate(gridDict,x,y,i)
                    else: hasDuplicateX, hasDuplicateY, hasDuplicateInBox = True, True, True

                    if (hasDuplicateX == False and hasDuplicateY == False and hasDuplicateInBox == False):
                        list.append(i)

                possibleValues[(x,y)] = list

          else: possibleValues[(x,y)] = [gridDict.get((x,y))]

    
    return possibleValues

def DrawNumbers(win, gridDict):

    for x in range(9):
        for y in range(9):

            if gridDict.get((x,y)) > 0:

                number = graphics.Text(graphics.Point(x+0.5,y+0.5),gridDict.get((x,y)))
                number.setSize(30)
                number.draw(win)

def GoToNextOpenGrid(changeMap,x,y):

    if y < 8:
        y += 1
  
    else:
        y = 0
        x += 1

    if x > 8: return 9,9

    while changeMap.get((x,y),None) == False:

        if y < 8:
            y += 1
        else:
            y = 0
            x += 1

        if x > 8: return 9,9

    return x,y


def GoToPreviousOpenGrid(changeMap,x,y):

    if y > 0:
        y -=1
    else:
        y = 8
        x -= 1

    while changeMap.get((x,y)) == False and x > 0:

        if y > 0:
            y -= 1
        else:
            y = 8
            x -=1

    if x >= 0:
        return x,y
    else: 
        x,y = 0,0
        if not changeMap.get((x,y)):
            x,y = GoToNextOpenGrid(changeMap,x,y)
            return x, y

def Solve(gridDict):

    OpenSpaces = CatalogSpaces(gridDict)

    x,y = 0,0
    if not  OpenSpaces.get((x,y)):
        x,y = GoToNextOpenGrid(OpenSpaces,x,y)

    while x < 9:

        initialValue = 10

        gridDict[(x,y)] += 1

        print('DEBUG: {0} at cell {1}'.format(gridDict.get((x,y)),(x,y)))

        hx, hy, hb = CheckForDuplicate(gridDict,x,y,gridDict.get((x,y)))

        while (hx == True or  hy == True or hb == True) and gridDict.get((x,y)) != initialValue:

            gridDict[(x,y)] += 1

            print('DEBUG: {0} at cell {1}'.format(gridDict.get((x,y)),(x,y)))
            
            hx,hy,hb = CheckForDuplicate(gridDict,x,y,gridDict.get((x,y)))

        if gridDict.get((x,y)) == initialValue:
            gridDict[(x,y)] = 0
            x,y = GoToPreviousOpenGrid(OpenSpaces,x,y)

        else:
            x,y = GoToNextOpenGrid(OpenSpaces,x,y)

    return gridDict



def main():

    option = str(input('Type \'enter\' for manual entry, or \'random\' for random generation: '))
    
    if option == 'enter':
        gridDict = MakeSudokuGrid()
        win = DrawGrid()
        DrawNumbers(win, gridDict)

    else:
        win = DrawGrid()
        gridDict = AssignRandomNumbers(win)
        DrawNumbers(win,gridDict)

    while True:

        key = win.getKey()
        if key == 's':
            Solve(gridDict)
            DrawNumbers(win,gridDict)
            win.getKey()
        elif key == 'q':
            break
    
    win.close()

if __name__ == "__main__": main()
            
