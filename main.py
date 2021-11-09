"""
Escape Alfred
  - on turtle
  - wasd for controls
  - Alfred asks weird questions. Answer them wrong and you die.
  - A survival game where Alfred chases you for the rest of your life, seeking for your attention. Once you're caught, you'll never be free.

"""

import turtle
import time

from player import Player
from angerBar import AngerBar
from alfredManager import AlfredManager
from choiceScreen import ChoiceScreen

DELAY = 0.05
SCREEN_SIZE = 600


screen = turtle.Screen() # Singleton
screen.title("Escape Alfred")
screen.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)

def runGame():
  screen.tracer(0) # only redraw when update is called
  player = Player(screenSize=SCREEN_SIZE, startX=0, startY=0)
  player.registerKeypresses(screen)
  angerBar = AngerBar(screenSize=SCREEN_SIZE)
  alfredManager = AlfredManager(player=player, screenSize=SCREEN_SIZE)

  while not alfredManager.checkDeath():
    screen.listen()

    angerBar.update()
    alfredManager.manageAlfreds(anger=angerBar.numSegments)
    alfredManager.update()
    player.update()
    screen.update()
    time.sleep(DELAY)

    if(len(angerBar.segments)>= angerBar.maxLength):
      turtle.clearscreen()
      return True
      
  turtle.clearscreen()
  return False

def askChoices():
  screen.bgcolor("black")
  choiceScreen = ChoiceScreen(SCREEN_SIZE)
  choiceScreen.writeQuestion()
  choiceScreen.writeChoices()
  while(choiceScreen.playerChosen==False):
    choiceScreen.update()
  
  turtle.clearscreen()
  return choiceScreen.restart

def showWinScreen():
  screen.bgcolor("yellow")
  turtle.hideturtle()
  turtle.write("CONGRATULATIONS,\nYOU ESCAPED ALFRED!!", align="center", font=("Comic Sans", 30, "normal"))
  screen.update()

def showLoseScreen():
  screen.bgcolor("black")
  screen.bgpic("gameOver.gif")
  screen.update()


# MAIN GAME LOOP
win = False
while True:
  if runGame(): 
    showWinScreen()
    break
  
  if not askChoices():
    showLoseScreen()
    break

time.sleep(5) # show ending screen for 5 seconds
turtle.done()
