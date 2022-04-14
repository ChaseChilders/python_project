from playsound import playsound
# # def question_select():
#   movie_select = input("What is the movie category you would like to answer questions from? ")
#   amount_select = input("What amount of money would you like to try and win? ")

def avengers_100():
  answer = input("""  

Who is the Director of S.H.I.E.L.D? 

    A) Phil Coulson

    B) Nick Fury

    C) Natasha Romanov

    D) Steve Rogers
    
    Print A, B, C, or D: """)
  if answer == "B":
      print("""
      You got it correct! """)
      return 100
  else:
      print("""
      You got it wrong :( """)
      return 0


def avengers_500():
  answer = input("""  

What is the item that Loki steals in order to take over earth?

  A) Thor's Hammer

  B) Captain America's Hammer

  C) Tesseract

  D) Helicopter

  Print A, B, C, or D: """)
  if answer == "C":
    print("""
    You got it correct! """)
    return 500
  else:
    print("""
    You got it wrong :( """)
    return 0

def avengers_1000():
  answer = input("""  

What is used to destroy the wormhole generator that Loki built?

  A) The Hulk

  B) Loki's Scepter

  C) Nuclear Missile

  D) An Arrow

  print A, B, C, or D: """)
  if answer == "B":
    print("""
    You got it correct! """)
    return 1000
  else:
    print("""
    You got it wrong :( """)
    return 0

def infinity_war100():
  answer = input("""  

Who kills Loki in the beginning of Infinity War?

  A) Thor

  B) The Hulk

  C) Tony Stark

  D) Thanos

  Print A, B, C, or D: """)
  if answer == "D":
    print("""
    You got it correct! """)
    return 100
  else: 
    print("""
    You got it wrong :( """)
    return 0

def infinity_war500():
  answer = input("""  

Who attacked Thanos allowing him to break free of the Avengers and go to earth to retrieve the final stone?

  A) Quill

  B) Peter Parker

  C) Nebula

  D) Drax
  
  Print A, B, C, or D: """)
  if answer == "A":
    print("""
    You got it correct! """)
    return 500
  else:
    print("""
    You got it wrong :( """)
    return 0

def infinity_war1000():
  answer = input("""  

What planet were Tony and Nebula stranded on after Thanos snapped his fingers?

  A) Earth

  B) Nidavellir

  C) Titan

  D) Knowhere

  Print A, B, C, or D: """)
  if answer == "C":
    print("""
    You got it correct! """)
    return 500
  else:
    print("""
    You got it wrong :( """)
    return 0

def endgame_100():
  answer = input("""  

Who rescued Tony and Nebula from the space ship in the beginning of Endgame?

  A) Captain America

  B) Thanos

  C) Dr. Strange

  D) Captain Marvel

  Print A, B, C, or D: """)
  if answer == "D":
    print("""
    You got it right! """)
    return 100
  else:
    print("""
    You got it wrong :( """)
    return 0

def endgame_500():
  answer = input("""  
  
When the Avengers went back in time, where did Rocket take the Time Stone from?

  A) Tony's Briefcase

  B) Loki's Room

  C) Thor's Mom

  D) Jane's pocket
  
  Print A, B, C, or D: """)
  if answer == "D":
    print("""
    You got it right! """)
    return 500
  else:
    print("""
    You got it wrong :( """)
    return 0

def endgame_1000():
  answer = input(""" 

After Tony's death and funeral, who was appointed the new ruler of Asgard?

  A) Valkyrie

  B) Rocket

  C) Thor

  D) Stephen Strange
  
  Print A, B, C, or D: """)
  if answer == "A":
    print("""
    You got it right! """)
    return 1000
  else: 
    print("""
    You got it wrong :( """)
    return 0