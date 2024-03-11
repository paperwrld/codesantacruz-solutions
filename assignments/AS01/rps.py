import numbers
import random

numGames = int(input("best of?"))
playerScore = 0
comScore = 0

gameOn = True;

options = ["rock", "paper", "scissors"]

while gameOn:
  randNum = random.randint(0,2)
  comChoice = options[randNum]
  playerChoice = input("choose rock, paper, or scissors: ")

  if playerChoice == comChoice:
    print("tie")
  elif playerChoice == "rock":
    if comChoice == "scissors":
      playerScore += 1
      print("W")
    else:
      print("L")
      comScore += 1
  elif playerChoice == "paper":
    if comChoice == "rock":
      playerScore += 1
      print("W")
    else:
      print("L")
      comScore += 1
  elif playerChoice == "scissors":
    if comChoice == "paper":
      playerScore += 1
      print("W")
    else:
      print("L")
      comScore += 1

  print("player's score: " + str(playerScore) + " , computer's score: " + str(computerScore))

  if playerScore > numGames:
    print("player wins! GG")
    gameOver = True
  elif comScore > numGames:
    print("computer wins! GG")
    gameOver = True