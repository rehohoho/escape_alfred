"""
Player Class
"""

from movableEntity import MoveableEntity


MAX_SPEED = 5
SPEED_INCREMENT = 1
TURN_STEP_SIZE = 20


class Player(MoveableEntity):
  """
  Creates controllable entity by the player, with the following key controls:
    -	Left key: Turns the player twenty degrees to the left.
    -	Right key: Turns the player twenty degrees to the right.
    -	Up key: Increases the player’s speed.
    -	Down key: Decreases the player’s speed.
  """

  def __init__(self, screenSize, startX, startY):
    super().__init__(screenSize, startX, startY, width=10, height=10)

  def _moveLeft(self):
    """ Rotates the player to the left. """
    self.entity.left(TURN_STEP_SIZE)

  def _moveRight(self):
    """ Rotates the player to the right. """
    self.entity.right(TURN_STEP_SIZE)
  
  def _moveFaster(self):
    """ Increases the speed of the player. """
    self.speed = min(self.speed + SPEED_INCREMENT, MAX_SPEED)
  
  def _moveSlower(self):
    """ Decreases the speed of the player. """
    self.speed = max(self.speed - SPEED_INCREMENT, 0)

  def registerKeypresses(self, screen):
    """ Binds all Player keyboard controlling methods to keypress events. """
    screen.onkeypress(self._moveLeft, "Left")
    screen.onkeypress(self._moveRight,"Right")
    screen.onkeypress(self._moveFaster, "Up")
    screen.onkeypress(self._moveSlower, "Down")
