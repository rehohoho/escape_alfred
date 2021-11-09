"""
Contains AlfredManager class only
"""

from alfred import HappyAlfred, AngryAlfred, CrazyAlfred


MAX_ANGER_ALFREDS = 2
MAX_CRAZY_ALFREDS = 2


class AlfredManager:
  """
  Manages the Alfreds in the game, and its interactions with player
    1.	Adds or removes different types of Alfreds depending on game progress (anger).
    2.	Detect collision with player
  """

  def __init__(self, player, screenSize):
    self.screenSize = screenSize
    self.player = player
    self.alfreds = {
      "happy": [],
      "angry": [],
      "crazy": []
    }

  ###### happy alfred ######
  def _addHappyAlfred(self):
    """ Adds an instance of HappyAlfred in the game screen. """

    happyAlfred = HappyAlfred(
      player=self.player, 
      screenSize=self.screenSize, 
      startX=0, 
      startY=-200)
    
    self.alfreds["happy"].append(happyAlfred)
    print("Happy Alfred {alfredNum} has entered the game.".format(
      alfredNum=len(self.alfreds["happy"])
    ))

  def _removeHappyAlfred(self):
    """ Removes an instance of HappyAlfred. """
    del self.alfreds["happy"][-1]

  ###### angry alfred ######
  def _addAngryAlfred(self):
    """ Adds an instance of AngryAlfred in the game screen. """
    angryAlfred= AngryAlfred(
      player=self.player, 
      screenSize=self.screenSize, 
      startX=0, 
      startY=-200)
    
    self.alfreds["angry"].append(angryAlfred)
    print("Angry Alfred {alfredNum} has entered the game.".format(
      alfredNum=len(self.alfreds["angry"])
    ))
  
  def _removeAngryAlfred(self):
    """ Removes an instance of AngryAlfred. """
    del self.alfreds["angry"][-1]

  ###### crazy alfred ######
  def _addCrazyAlfred(self):
    """ Adds an instance of CrazyAlfred in the game screen. """
    crazyAlfred= CrazyAlfred(
      player=self.player, 
      screenSize=self.screenSize, 
      startX=0, 
      startY=0)
    
    self.alfreds["crazy"].append(crazyAlfred)
    print("Crazy Alfred {alfredNum} has entered the game.".format(
      alfredNum=len(self.alfreds["crazy"])
    ))

  def _removeCrazyAlfred(self):
    """ Removes an instance of CrazyAlfred. """
    del self.alfreds["crazy"][-1]
  
  ###### alfred's manager lol ######
  def manageAlfreds(self, anger):
    """
    -	Adds a HappyAlfred instance if anger is below 5.
    -	Adds an AngryAlfred instance if anger is above 5 and ensures that the number of AngryAlfred instances is below 5.
    -	Adds a CrazyAlfred instance if anger is above 10 and ensures that the number of CrazyAlfred instances is below 5.
    """
    currHappyAlfreds = len(self.alfreds["happy"])
    tarHappyAlfreds = min(anger, 5)
    if currHappyAlfreds < tarHappyAlfreds:
      self._addHappyAlfred()
    elif currHappyAlfreds > tarHappyAlfreds:
      self._removeHappyAlfred()
    
    # adds one after 5 anger, max 5
    currAngryAlfreds = len(self.alfreds["angry"])
    tarAngryAlfreds = min(max(0, anger-5), MAX_ANGER_ALFREDS)
    if currAngryAlfreds < tarAngryAlfreds:
      self._addAngryAlfred()
    elif currAngryAlfreds > tarAngryAlfreds:
      self._removeAngryAlfred()

    # adds one after 10 anger, max 5
    currCrazyAlfreds= len(self.alfreds["crazy"])
    tarCrazyAlfreds= min(max(0, anger-10), MAX_CRAZY_ALFREDS)
    if currCrazyAlfreds < tarCrazyAlfreds:
      self._addCrazyAlfred()
    elif currCrazyAlfreds > tarCrazyAlfreds:
      self._removeCrazyAlfred()

  def _checkCollisionEntities(self, entity1, entity2):
    """ Checks if two instances collide. """
    deltXfromCenter = abs(entity1.x - entity2.x)
    deltYfromCenter = abs(entity1.y - entity2.y)
    deltXfromEnds = deltXfromCenter - entity1.halfWidth - entity2.halfWidth
    deltYfromEnds = deltYfromCenter - entity1.halfHeight - entity2.halfHeight

    return deltXfromEnds < 0 and deltYfromEnds < 0

  def checkDeath(self):
    """ 
    Returns: Boolean
      - True if any of the Alfred instances collide with the player, otherwise returns False.
    """
    for alfredList in self.alfreds.values():
      for alfred in alfredList:
        if self._checkCollisionEntities(self.player, alfred):
          return True
    
    return False

  def update(self):
    """ Updates all Alfred instances. """
    for alfredList in self.alfreds.values():
      for alfred in alfredList:
        alfred.update()
