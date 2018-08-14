import graphics
import random

def makeScreen(header, size, color):
    window = graphics.GraphWin(header, size * 2, size, autoflush=False)
    window.setBackground(color)
    window.setCoords(0.0,0.0,20.0,10.0)
    return window

def makeObj(win, size, color, start_point):
    
    Obj = graphics.Rectangle(start_point, graphics.Point(start_point.getX() + size, start_point.getY() + size))
    Obj.setFill(color)
    Obj.setOutline('black')
    Obj.setWidth(2)
    Obj.draw(win)
    return Obj

def moveObj(win,Obj,dir):
    
    if dir == 'first':
        dx = 0
        dy = 0
    if dir == 'Right':
        dx = scale
        dy = 0
    if dir == 'Left':
        dx = -scale
        dy = 0
    if dir == 'Up':
        dx = 0
        dy = scale
    if dir == 'Down':
        dx = 0
        dy = -scale

    for j in range(10000):

        graphics.update(upd)

        checkAlign(win,Obj)
        buildSnake(win,Obj,dx,dy)
        checkDir(win,Obj,dx,dy)
        checkEdge(win,Obj)

def buildSnake(win,Obj,dx,dy):

       for i in range(len(Obj)):

           n = i + 2
           if -i - 2 < -len(Obj):

               Obj[0].move(dx/4,dy/4)
               Obj[0].move(dx/4,dy/4)
               Obj[0].move(dx/4,dy/4)
               Obj[0].move(dx/4,dy/4)

           else: Obj[-i-1].move(Obj[-i-2].getP1().getX()-Obj[-i-1].getP1().getX(), Obj[-i-2].getP1().getY()-Obj[-i-1].getP1().getY())

           if n >= len(Obj):
               pass

           elif Obj[0].getP1().getX() == Obj[n].getP1().getX() and Obj[0].getP1().getY() == Obj[n].getP1().getY():
               gameOver(win,Obj)
               main()

def checkDir(win,Obj,dx,dy):

        key = win.checkKey()

        if key == "Up":
            if dy == -scale and len(Obj) > 1:
                pass
            else: moveObj(win,Obj,'Up')
        if key == "Left":
            if dx == scale and len(Obj) > 1:
                pass
            else: moveObj(win,Obj,'Left')
        if key == "Down":
            if dy == scale and len(Obj) > 1:
                pass
            else: moveObj(win,Obj,'Down')
        if key == "Right":
            if dx == -scale and len(Obj) > 1:
                pass
            else: moveObj(win,Obj,'Right')

def checkEdge(win,Obj):

        if Obj[0].getP1().getX() >= 20:
            gameOver(win,Obj)
            main()
            #Obj[0].move(-1 * (Obj[0].getP1().getX()),0)

        if Obj[0].getP2().getX() <= 0:
            gameOver(win,Obj)
            main()
            #Obj[0].move(-1 *(Obj[0].getP2().getX()) + 20,0)

        if Obj[0].getP1().getY() >= 10:
            gameOver(win,Obj)
            main()
            #Obj[0].move(0,-1 * (Obj[0].getP1().getY()))

        if Obj[0].getP2().getY() <= 0:
            gameOver(win,Obj)
            #Obj[0].move(0,-1 *(Obj[0].getP2().getY()) + 10)  

def gameOver(win,Obj):

    win.setBackground('red3')

    food.undraw()

    gameOverText = graphics.Text(graphics.Point(10,5), "You Lose. Final Length: {0}\nPress any key to restart...".format(str(len(Obj))))
    gameOverText.setSize(32)
    gameOverText.draw(win)

    for i in range(len(Obj)):
        Obj[i].undraw()

    win.getKey()
    win.close()
    main()

def checkAlign(win,Obj):

    if Obj[0].getCenter().getX() == food.getCenter().getX() and Obj[0].getCenter().getY() == food.getCenter().getY():

            dx = random.randint(-int(food.getP1().getX()),19-int(food.getP1().getX()))
            dy = random.randint(-int(food.getP1().getY()),9-int(food.getP1().getY()))
            food.move(dx,dy)

            newPoint = graphics.Point(Obj[len(Obj)-1].getP1().getX(),Obj[len(Obj)-1].getP1().getY())
            newPiece = makeObj(win,scale,'white',newPoint)

            Obj.append(newPiece)
           

def main():

    win = makeScreen("Snake Game", 800, 'gray')
    start_point = graphics.Point(10,5)

    global scale 
    scale = .5
    global upd
    upd = 13

    snakeList = []
    snake = makeObj(win, scale, 'white', start_point)
    snakeList.append(snake)

    global food 
    food = makeObj(win,scale,'cyan',graphics.Point(random.randint(1,19),random.randint(1,9)))
    moveObj(win, snakeList,'first')
   

main()