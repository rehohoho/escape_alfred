"""
Definition for different Alfreds
Contains main logic for Alfreds, visuals, chasing logic, collision
"""

import time
import random
import turtle

from movableEntity import MoveableEntity


HAPPY_SPEED = 2.5
HAPPY_WIDTH = 80 #100
HAPPY_HEIGHT = 63 #79
CRAZY_SPEED = 0.0
CRAZY_CHARGE_SPEED = 8.0
CRAZY_REST_DURATION = 4.0 
CRAZY_WIDTH = 150 #200
CRAZY_HEIGHT = 208 #278 
ANGRY_SPEED = 0.0
ANGRY_CHARGE_SPEED = 10.0
ANGRY_REST_DURATION = 5.0 
ANGRY_WIDTH = 80 #100
ANGRY_HEIGHT = 110 #139

turtle.register_shape("angryAlfred.gif")
turtle.register_shape("happyAlfred.gif")
turtle.register_shape("crazyAlfred.gif")


class BaseAlfred(MoveableEntity):
  """ 
  Default Alfred

  Behaviour:
    1.	Move forward till it hits the wall
    2.	Stops when it hits the wall

  Holds helper methods to face player or get player position.  
  """

  def __init__(self, player, screenSize, startX, startY, defaultSpeed,width, height):
    super().__init__(screenSize, startX, startY, defaultSpeed, width, height)
    self.target = player

  def getPlayerPosition(self):
    """
    Returns Tuple<int, int>
      - X and Y coordinates of the player's current position.
    """
    return self.player.x, self.player.y
  
  def facePlayer(self):
    """ Makes the turtle object face the player. """
    targetHeading = self.entity.towards(self.target.x, self.target.y)
    self.entity.seth(targetHeading)
  

class HappyAlfred(BaseAlfred):
  """ Behaviour: Slowly chases player """

  def __init__(self, player, screenSize, startX, startY, defaultSpeed=HAPPY_SPEED, width=HAPPY_WIDTH, height=HAPPY_HEIGHT):
    super().__init__(player, screenSize, startX, startY, defaultSpeed, width, height)
    self.entity.shape("happyAlfred.gif")
  
  def update(self):
    """
    To be called during main loop to update turtle drawings on TurtleScreen.
      1.	Commands the turtle object to face the player
      2.	Move Alfred forward by its speed. Stop if it hits border. 
    """
    self.facePlayer()
    super().update()


class AngryAlfred(BaseAlfred):
  """ 
  Behaviour:
    1.	Stop moving. 
    2.	Continuously face player for a fixed time declared in constants.
    3.	Charge at player till it hits a wall
  """

  def __init__(self, player, screenSize, startX, startY, defaultSpeed=ANGRY_SPEED, width=ANGRY_WIDTH, height=ANGRY_HEIGHT):
    super().__init__(player, screenSize, startX, startY, defaultSpeed, width, height)
    self.lastChargeTime = time.time()
    self.entity.color("green")
    self.entity.shape("angryAlfred.gif")

  def _charge(self):
    """
    1.	Commands the turtle object to face the player
    2.	Set to charging speed
    """
    self.facePlayer()
    self.speed = ANGRY_CHARGE_SPEED

  def update(self):
    """
    To be called during main loop to update turtle drawings on TurtleScreen.
      1.	Checks the time elapsed and commands Alfred to charge at the player after a specified time.
      2.	Stops Alfred if it collides with the border.
    """
    if(time.time() - self.lastChargeTime >= ANGRY_REST_DURATION):
      self._charge()
      self.lastChargeTime = time.time()
    
    if(self.isCollided==True):
      self.speed = 0.0

    super().update()


class CrazyAlfred(BaseAlfred):
  """
  Behaviour:
    1.	Randomly face a direction
    2.	Charge towards the direction
  """
  
  def __init__(self, player, screenSize, startX, startY, defaultSpeed=CRAZY_SPEED, width=CRAZY_WIDTH, height=CRAZY_HEIGHT):
    super().__init__(player, screenSize, startX, startY, defaultSpeed, width, height)
    self.entity.color("red")
    self.lastChargeTime= time.time()
    self.entity.shape("crazyAlfred.gif")
  
  def _chargeRandom(self):
    """ Commands the turtle object to randomly face a direction and charge. """
    randomDirection = random.randint(0,360)
    self.entity.left(randomDirection)
    self.speed= CRAZY_CHARGE_SPEED

  def update(self):
    """
    To be called during main loop to update turtle drawings on TurtleScreen.
      1.	Checks the time elapsed and commands Alfred to charge to a random direction after a specified time.
      2.	Stops Alfred if it collides with the border.
    """
    if(time.time() - self.lastChargeTime >= CRAZY_REST_DURATION):
      self._chargeRandom()
      self.lastChargeTime = time.time()
    
    if(self.isCollided==True):
      self.speed = 0.0
    
    super().update()
