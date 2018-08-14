import graphics
import random

width = 12
height = 12
bomb_fill_percent = 12

class Tile:

    def __init__(self,x,y,is_bomb): # Initialize a tile object with location, and two bools governing bomb status and if it is shown 

        self.pos = (x,y)
        self.is_bomb = is_bomb
        self.is_shown = False

    def CountBombNeighbors(self,grid): # Takes the grid and counts how many of this tile's neighbors are bombs

        # We will add to this list and then cycle through
        tiles_to_check = []

        for i in [-1,0,1]:
            for j in [-1,0,1]:

                if i == -1 and self.pos[0] == 0:
                    pass
                elif j == -1 and self.pos[1] == 0:
                    pass
                elif i == 1 and self.pos[0] == width-1:
                    pass
                elif j == 1 and self.pos[1] == height - 1:
                    pass
                elif not(i == 0 and j == 0):
                    tiles_to_check.append((self.pos[0]+i,self.pos[1]+j))

        count = 0
        for tile in tiles_to_check:
            if grid.get(tile).is_bomb:
                count += 1

        return count

    def show(self,win,grid): # Shows the value of the tile to the screen, needs the grid to check how many bombs border it 

        if not self.is_shown:

            print(self.pos)

            if self.is_bomb:
                text = graphics.Text(graphics.Point(self.pos[0]+0.5,self.pos[1]+0.5),'b')
                text.setSize(30)
                text.draw(win)
            else:
                n = self.CountBombNeighbors(grid)
                if n > 0:
                    text = graphics.Text(graphics.Point(self.pos[0]+0.5,self.pos[1]+0.5),n)
                else: 
                    text = graphics.Rectangle(graphics.Point(self.pos[0],self.pos[1]),graphics.Point(self.pos[0]+1,self.pos[1]+1))
                    text.setFill('light grey')
                text.draw(win)

            self.is_shown = True

class Game:

    def __init__(self): # Makes an empty dictionary to track tiles

        self.grid = {}

    def MakeWin(self): # Draws a window with a number of grids equal to the height and width set at the top of program 

        win = graphics.GraphWin('Mine Sweeper', 800, 800)
        win.setCoords(0,0,width,height)
        win.setBackground('white')

        for x in range(1,width):

            line = graphics.Line(graphics.Point(x,0),graphics.Point(x,height))
            line.draw(win)

        for y in range(1,height):

            line = graphics.Line(graphics.Point(0,y),graphics.Point(width,y))
            line.draw(win)

        return win 

    def SetGrid(self): # Fills a dictionary with tiles which are randomly chosen to either be bombs or not 

        for x in range(width):
            for y in range(height):

                if random.randint(0,100) < bomb_fill_percent:

                    self.grid[(x,y)] = Tile(x,y,True)

                else: self.grid[(x,y)] = Tile(x,y,False)

    def show(self): # Uncovers the entire screen 

        for x in range(width):
            for y in range(height):

                self.grid.get((x,y)).show(self.win,self.grid)

    def ClearField(self,tile): # Shows all touching 0 tiles, and includes one more number tile

        #push this tile to the stack
        self.stack.append(tile)
        #check all neighbors
        for i in [-1,0,1]:
            for j in [-1,0,1]:

                if (i != 0 or j != 0):
                    #show the ones that are not bombs
                    if self.grid.get((tile.pos[0] + i,tile.pos[1]+j)) and self.grid.get((tile.pos[0]+i,tile.pos[1]+j)) not in self.stack:

                        if not self.grid.get((tile.pos[0]+i,tile.pos[1]+j)).is_bomb:
                            self.grid.get((tile.pos[0]+i,tile.pos[1]+j)).show(self.win,self.grid)

                            #for the ones that are 0 and are not marked, repeat above 
                            if self.grid.get((tile.pos[0]+i,tile.pos[1]+j)).CountBombNeighbors(self.grid) == 0:
                                self.ClearField(self.grid.get((tile.pos[0]+i,tile.pos[1]+j)))


    def handleClick(self,click): # If bomb is clicked, show whole board, otherwise show the tile and if 0, clear field 

        selectedTile = self.grid.get((int(click.getX()),int(click.getY())))
        n = selectedTile.CountBombNeighbors(self.grid)

        if selectedTile.is_bomb:

            self.show()

        elif n > 0:

            selectedTile.show(self.win,self.grid)

        else:
            selectedTile.show(self.win,self.grid)
            self.ClearField(selectedTile)

    def play(self): # Initializes game window, fills the grid dictionary and sets random bombs, creates a stack to not recheck tiles

        self.win = self.MakeWin()
        self.SetGrid()

        self.stack = []

        while True:

            click = self.win.checkMouse()
            if click:
                self.handleClick(click)

if __name__ == '__main__':

    game = Game()
    game.play()
