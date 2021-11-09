"""
AngerBar class
"""

import time
import turtle


N_SQUARES = 15
TIME_FOR_NEW_SQUARE = 4 # in seconds


class AngerBar:
  """
  Manages the game progress:
    - Show AngerBar at the top of the screen
    - Show current score at bottom left of screen
    - Increment the anger / score according to time elapsed
  """

  def __init__(self, screenSize):
    self.screenSize = screenSize
    self.segments = [] # track the squares forming the bar
    self.segmentLength = int(screenSize / N_SQUARES)
    self.maxLength = N_SQUARES
    self.numSegments = 0

    self.startX = - int(screenSize / 2 + 1)
    self.startY = int(screenSize / 2 + 1)

    self.startTime = time.time()

    self.scorePen = turtle.Turtle()
  
  def _updateScoreScreen(self):
    """ Write updated score on the bottom left of the screen """
    self.scorePen.undo()
    self.scorePen.penup()
    self.scorePen.hideturtle()
    self.scorePen.setposition(-self.screenSize/2 + 10, -self.screenSize/2  + 10)
    #self.scorePen.hideturtle()
    scoreString = "Score: {score}".format(score=len(self.segments))
    self.scorePen.write(scoreString, False, align="left", font=["Arial",14,"normal"])
  
  def _addSegment(self):
    """ 
    Lengthen the AngerBar by creating a new segment on the screen.
      - Position of the square is calculated based on maximum number of segments and screenSize.
    """
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.shapesize(self.segmentLength / 21) # default square is 21px
    new_segment.color("red")
    new_segment.penup()

    x = self.startX + len(self.segments) * self.screenSize / N_SQUARES
    new_segment.goto(x, self.startY)

    self.segments.append(new_segment)
    self._updateScoreScreen()
  
  def _removeSegment(self):
    """ Removes the last created segment from the screen. """
    del self.segments[-1]
    self._updateScoreScreen()
  
  def update(self):
    """ Determine whether to add or remove segments from the AngerBar depending on time elapsed. """
    nSquares = (time.time() - self.startTime)/TIME_FOR_NEW_SQUARE + 1
    
    if self.numSegments == int(nSquares): return
    if self.numSegments < int(nSquares):
      self._addSegment()
    else:
      self._removeSegment()
    
    self.numSegments = len(self.segments)
