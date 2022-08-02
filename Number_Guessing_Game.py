#Number Guessing Game Objectives:
from art import logo
import random 
import os
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5
def difficulty():
  level=input("Choose a dificulty. Type 'easy' or 'hard': ")
  if level=="easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS


def check_answer(user_guess,random_number,turns):
  if user_guess<random_number:
    print("It is too low")
    return turns-1
  elif user_guess>random_number:
    print("It is too high.")
    return turns-1
  else:
    print(f"You got it! The answer is {random_number}")

def game():
  
  print(logo)
  print("Welcome to the Number Guessing Game :)\nI'm thinking of a number between 1 and 100.")
  #Choosing a random number between 1 and 100.
  random_number=random.randint(1,100)
  user_guess=0
  turns=difficulty()
  while user_guess!=random_number:
    print(f"You have {turns} attempts remaining to guess the number.")
    #Let the user guess.
    user_guess=int(input("Guess a number: "))
  #Track the number of turns and reduce by 1 if they get wrong.
    turns=check_answer(user_guess,random_number,turns)
    if turns==0:
      print("You've run out of guess, you lose.")
      return
    elif user_guess!=random_number:
      print("Guess again.")
while input("Do you want to play a guess number? Type 'yes' or 'no': ").lower()=='yes':
  os.system('CLS')
  game()


        