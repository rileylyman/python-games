import graphics
import random

class Player:

    def __init__(self,win):

        self.color = 'white'
        self.size = 0.23
        self.jump_distance = 0.6

        self.player = graphics.Circle(graphics.Point(2,5),self.size)
        self.player.draw(win)
        self.player.setFill(self.color)

    def fall(self,down_speed):

        self.player.move(0,down_speed)

    def jump(self):

        self.player.move(0,self.jump_distance/3)

    def isTouchingColumn(self,list):

        for col in list:

            if (self.player.getCenter().getX() + self.size > col.getFirst().getP1().getX() and self.player.getCenter().getX() - self.size <
                col.getFirst().getP2().getX() and (self.player.getCenter().getY() - self.size < col.getFirst().getP2().getY() or
                                           self.player.getCenter().getY() + self.size > col.getSecond().getP1().getY())):
                
                return True

        return False

class Column:

    def __init__(self,win):

        self.hole_location = random.randint(1,9)
        self.win = win

        bottom_column = graphics.Rectangle(graphics.Point(0,0),graphics.Point(0.5,self.hole_location))
        bottom_column.setFill('green')
        top_column = graphics.Rectangle(graphics.Point(0,self.hole_location+2),graphics.Point(0.5,10))
        top_column.setFill('green')

        self.column_list = []
        self.column_list.append(bottom_column)
        self.column_list.append(top_column)

        for column in self.column_list:
            
            column.draw(self.win)

    def getFirst(self):

        return self.column_list[0]

    def getSecond(self):

        return self.column_list[1]

    def move(self,move_speed):

        for column in self.column_list:

            column.move(-move_speed,0)

    def setLocation(self,x):

        for column in self.column_list:

            dx = x - column.getCenter().getX()

            column.move(dx,0)

    def die(self):

        for column in self.column_list:

            column.undraw()

    def getLocation(self):

        return self.column_list[0].getP2().getX()

class Game:

    def __init__(self):

        win = graphics.GraphWin('Flappy Bird', 800, 800)
        win.setBackground('black')
        win.setCoords(0,0,10,10)

        self.win = win

        self.player = Player(self.win)

        self.col1 = Column(win)
        self.col2 = Column(win)
        self.col3 = Column(win)

        self.colList = [self.col1,self.col2,self.col3]

        self.col1.setLocation(5)
        self.col2.setLocation(10)
        self.col3.setLocation(15)

        self.playerFallSpeed = 0
        self.jumpTimer = 0
    def run(self):

        while True:

            graphics.update(30)
            key = self.win.checkKey()
            if key == 'space':

                self.playerFallSpeed = 0
                self.jumpTimer = 3
    
                
            if self.jumpTimer > 0:
                
                self.player.jump()
                self.jumpTimer -= 1

            if self.player.isTouchingColumn(self.colList):

                self.win.close()

            self.playerFallSpeed += 0.005
            self.player.fall(-self.playerFallSpeed)

            for col in self.colList:

                col.move(1/30)
                if col.getLocation() < 0:

                    self.colList.remove(col)
                    col = Column(self.win)
                    col.setLocation(15)
                    self.colList.append(col)

if __name__ == '__main__':

    game = Game()
    game.run()

        
