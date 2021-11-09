"""
ChoiceScreen class
"""

import turtle
import random

turtle.register_shape("box1 copy.gif")


class ChoiceScreen:
  """
  
  """

  def __init__(self, screenSize):
    self.screenSize = screenSize
    self.questionStyle = ('Arial', 30)
    self.answerStyle= ('Arial', 20)

    self.boxes = []
    
    self.questions = [
      "What is Alfred's \n favourite food?", 
      "What to do if \n Alfred is near you?", 
      "There is no war in \nBa Sing Se!", 
      "What is no 4?", 
      "What are the last 4 digits \nof Alfred's phone number?"]
    
    self.choices = [
      ["a) Chicken", "b) Garbage", "u) piece of shit"],
      ["a) Runn...", "b) Sit with him...", "c) What you do for this game"],
      ["Truth", "Falsetto", "Refer to Descartes"],
      ["Fantastic4","numberofpplinourteam","after3"], 
      ["7718", "9280", "0740"]
    ]

    self.answers = [2,0,1,1,2] #these refer to the index of the right answers 

    self.randomIndex = 0

    self.restart = False #will be true if user picks correct answer
    self.playerChosen = False

  def _initBox(self, x=0, y=0, color="white", message=""):
    choice = turtle.Turtle()
    choice.shape("box1 copy.gif")
    choice.setx(x)
    choice.sety(y)
    choice.color(color)
    choice.write(message, font=self.answerStyle,align='center')
    self.boxes.append(choice)

  def show(self):
    for box in self.boxes:
      box.showturtle()
  
  def hide(self):
    for box in self.boxes:
      box.hideturtle()
  
  def writeQuestion(self):
    self.randomIndex= random.randint(0, len(self.questions)-1)
    randomQuestion= self.questions[self.randomIndex]
    turtle.hideturtle()
    turtle.setx(0)
    turtle.sety(100)
    turtle.color("white")
    turtle.write(randomQuestion, font=self.questionStyle, align='center')
    
  def writeChoices(self):
    # bar is of 300x42 pixels, 0 is taken as center
    self._initBox(x=0, y=0, message= self.choices[self.randomIndex][0])
    self._initBox(x=0, y=-72, message= self.choices[self.randomIndex][1]) 
    self._initBox(x=0, y= -144, message= self.choices[self.randomIndex][2])

  def correctAnswer(self):
    self.hide()
    self.restart= True
    print("Nice! You get to see another day.")

  def wrongAnswer(self):
    self.hide()
    print("WRONG!! You l0se c:")

  def checkChoice1(self, x, y): #at choice index 0
    if(self.answers[self.randomIndex]==0):
      self.correctAnswer()
    else:
      self.wrongAnswer()
    
    self.playerChosen= True

  def checkChoice2(self, x, y): #at choice index 1
    if(self.answers[self.randomIndex]==1):
      self.correctAnswer()
    else:
      self.wrongAnswer()
      
    self.playerChosen= True
  
  def checkChoice3(self, x, y): #at choice index 2
    if(self.answers[self.randomIndex]==2):
      self.correctAnswer()
    else:
      self.wrongAnswer()
      
    self.playerChosen= True

  def update(self):
    turtle.listen()
    self.boxes[0].onclick(self.checkChoice1)
    self.boxes[1].onclick(self.checkChoice2)
    self.boxes[2].onclick(self.checkChoice3)
