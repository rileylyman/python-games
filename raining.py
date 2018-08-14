import graphics
import random

class RainDrop:

    def __init__(self,color):

        self.color = color

        self.z = random.randint(0,20)

        if self.z < 10:

            self.len = random.randint(5,10) / 10
            self.speed = random.randint(5,10) / 20

        else:

            self.len = random.randint(10,20) / 10
            self.speed = random.randint(5,10) / 10

        self.drop = graphics.Line(graphics.Point(0,0), graphics.Point(0,self.len))
        self.drop.setFill(color)
        self.drop.setWidth(0)

    def createDrop(self,color):

        self.z = random.randint(0,20)

        if self.z < 10:

            self.len = random.randint(5,10) / 10
            self.speed = random.randint(1,5) / 10

        else:

            self.len = random.randint(10,20) / 10
            self.speed = random.randint(5,10) / 10

        self.drop = graphics.Line(graphics.Point(0,0), graphics.Point(0,self.len))
        self.drop.setFill(color)
        self.drop.setWidth(0)

    def fall(self):

        self.drop.move(0,-self.speed)

    def begin(self,win):

        self.drop.move(random.random() * 10, random.random() * 30 + 10)
        self.drop.draw(win)

    def getTop(self):

        return self.drop.getP2().getY()

    def recreate(self):
        
        #self.splash()

        self.drop.undraw()
        self.createDrop(self.color)


class Window:

    def __init__(self,title,bkgcolor,width,height):

        self.title = title
        self.bkgcolor = bkgcolor
        self.width = width
        self.height = height

    def create(self):

        self.win = graphics.GraphWin(self.title,self.width,self.height)
        self.win.setBackground(self.bkgcolor)
        self.win.setCoords(0,0,10,10)

        return self.win
    
class FallingRain:

    def __init__(self):

        drop_count = 500

        self.win = Window('Rain','gray',800,800)
        self.win = self.win.create()

        self.drops = []
        for i in range(drop_count):

            drop = RainDrop('purple')
            drop.begin(self.win)
            self.drops.append(drop)

    def go(self):

        while True:

            for drop in self.drops:

                drop.fall()

                if drop.getTop() <= 0:
                    drop.recreate()
                    drop.begin(self.win)


if __name__ == '__main__':

    app = FallingRain()
    app.go()