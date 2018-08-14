import graphics

class Paddle:

    def __init__(self,height,width,speed,color):

        self.height = height
        self.width = width
        self.speed = speed
        self.color = color

        self.paddle = graphics.Rectangle(graphics.Point(0,0),graphics.Point(0+self.width,0+self.height))
        self.paddle.setFill(self.color)


    def draw(self,win):

        self.paddle.draw(win)

    def glide(self,dir,fps):

        self.paddle.move(0,dir*self.speed/fps)

    def setLocation(self,x,y):

        self.paddle.move(x-(self.paddle.getCenter().getX()),y-(self.paddle.getCenter().getY()))

    def getXRange(self):

        return self.paddle.getP1().getX(), self.paddle.getP2().getX()

    def getYRange(self):

        return self.paddle.getP1().getY(),self.paddle.getP2().getY()


class Ball:

    def __init__(self,radius,speed,color,fps):

        self.radius = radius
        self.speed = speed
        self.color = color

        self.dx = self.speed /fps
        self.dy = self.speed/fps*2/4       

        self.ball = graphics.Circle(graphics.Point(0,0),self.radius)
        self.ball.setFill(self.color)


    def draw(self,win):

        self.ball.draw(win)

    def setLocation(self,x,y):

        self.ball.move(x-self.ball.getCenter().getX(),y-self.ball.getCenter().getY())

    def moveBehavior(self,center,width,height,fps,win,paddle): 
        
        if self.ball.getCenter().getY()+self.radius >= height:
            self.dy = -self.dy
        if self.ball.getCenter().getY()-self.radius <= 0:
            self.dy = -self.dy
        if self.ball.getCenter().getX()+self.radius >= width:
            self.dx = -self.dx
        if self.ball.getCenter().getX()-self.radius <= 0:
            self.ball.undraw()

        paddleXLeft, paddleXRight = paddle.getXRange()
        paddleYLow , paddleYHigh = paddle.getYRange()

        if (self.ball.getCenter().getX()-self.radius <= paddleXRight and self.ball.getCenter().getX()+self.radius >= paddleXLeft
            and self.ball.getCenter().getY()+self.radius > paddleYLow and self.ball.getCenter().getY()-self.radius < paddleYHigh):
            self.dx = -self.dx


        self.ball.move(self.dx,self.dy)



    def getXRange(self):

        return self.ball.getCenter().getX()-self.radius, self.ball.getCenter().getX()+self.radius

    def getYRange(self):

        return self.ball.getCenter().getY()-self.radius, self.ball.getCenter().getY()+self.radius


def main():

    win = graphics.GraphWin('Paddle Game',800,800,autoflush = True)
    win.setBackground('gray')
    win.setCoords(0,0,10,10)

    ball = Ball(0.2,5,'blue',30)
    ball.setLocation(5,5)
    ball.draw(win)

    paddle = Paddle(4,.3,11,'blue')
    paddle.draw(win)

    paddle.setLocation(1.5,5)
    

    while True:

        graphics.update(30)

        ball.moveBehavior(graphics.Point(5,5),10,10,30,win,paddle)

        key = win.checkKey()

        if key == 'Up':

            paddle.glide(1,30)

        elif key == 'Down':

            paddle.glide(-1,30)

        if key == 'r':

            ball = Ball(0.2,5,'blue',30)
            ball.setLocation(5,5)
            ball.draw(win)




if __name__=='__main__': main()




