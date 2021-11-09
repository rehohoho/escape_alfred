"""
MovableEntity class
"""

import turtle
import math


class MoveableEntity:
  """
  1. Keeps the entity within the screen borders. 
  2. Tracks entity’s speed, coordinates, collision status with the border. 
  """

  def __init__(self, 
    screenSize, 
    startX=0, 
    startY=0, 
    defaultSpeed=1,
    width=0,
    height=0):
    
    self.entity = turtle.Turtle()
    self.entity.color("black")
    self.entity.penup()

    self.borderCoord = int(screenSize / 2) - 1

    self.speed = defaultSpeed

    self.x = self.entity.xcor()
    self.y = self.entity.ycor()

    self.entity.setx(startX)
    self.entity.sety(startY)

    self.isCollided = False

    self.halfHeight = int(height/2)
    self.halfWidth = int(width/2)


  def _checkBorderCollision(self):
    """
    Returns: Boolean, true if the entity’s coordinates for next step is out of range of the screen size
    """
    heading = self.entity.heading() #the bearing of entity
    nextX = self.x + self.speed * math.cos(heading * math.pi / 180)
    nextY = self.y + self.speed * math.sin(heading * math.pi / 180)

    if nextX > 0:
      nextX += self.halfWidth
    else:
      nextX -= self.halfWidth
    
    if nextY > 0:
      nextY += self.halfHeight
    else:
      nextY -= self.halfHeight

    # checks if instance collides with the border
    return nextX >= self.borderCoord or nextX <= -self.borderCoord or nextY >= self.borderCoord or nextY <= -self.borderCoord
  

  def update(self):
    """
    1. Ensures the entity does not go out of the screen’s borders.
      - Move player backwards when player touches the border.
      - Update collision state with border
    2. Moves entity forward by its speed.
    3. Update coordinates collision state with border
    """
    if self._checkBorderCollision(): 
      self.entity.backward(1) ###
      self.isCollided = True
      return
    
    self.isCollided = False
    self.entity.forward(self.speed)
    self.x = self.entity.xcor()
    self.y = self.entity.ycor()
