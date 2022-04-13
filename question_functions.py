
# # def question_select():
#   movie_select = input("What is the movie category you would like to answer questions from? ")
#   amount_select = input("What amount of money would you like to try and win? ")

def avengers_100():
  answer = input("""Who is the Director of S.H.I.E.L.D? 
    a) Phil Coulson
    b) Nick Fury
    c) Natasha Romanov
    d) Steve Rogers
    
    print a, b, c, or d
    
    """)
  if answer == "b":
      print("You got it correct! ")
      return 100
  else:
      print("You got it wrong :( ")
      return 0


def avengers_500():
  answer = input("""What is the item that Loki steals in order to take over earth?
  a) Thor's Hammer
  b) Captain America's Hammer
  c) Tesseract
  d) Helicopter

  print a, b, c, or d

  """)
  if answer == "c":
    print("You got it correct! ")
    return 500
  else:
    print("You got it wrong :( ")
    return 0

def avengers_1000():
  answer = input("""What is used to destroy the wormhole generator that Loki built?
  a) The Hulk
  b) Loki's Scepter
  c) Nuclear Missile
  d) An Arrow

  print a, b, c, or d

  """)
  if answer == "b":
    print("You got it correct! ")
    return 1000
  else:
    print("You got it wrong :( ")
    return 0

def infinity_war100():
  answer = input("""Who kills Loki in the beginning of Infinity War?
  a) Thor
  b) The Hulk
  c) Tony Stark
  d) Thanos

  print a, b, c, or d

  """)
  if answer == "d":
    print("You got it correct! ")
    return 100
  else: 
    print("You got it wrong :( ")
    return 0

def infinity_war500():
  answer = input("""Who attacked Thanos allowing him to break free of the Avengers and go to earth to retrieve the final stone?
  a) Quill
  b) Peter Parker
  c) Nebula
  d) Drax
  
  print a, b, c, or d

  """)
  if answer == "a":
    print("You got it correct! ")
    return 500
  else:
    print("You got it wrong :( ")
    return 0

def infinity_war1000():
  answer = input("""What planet were Tony and Nebula stranded on after Thanos snapped his fingers?
  a) Earth
  b) Nidavellir
  c) Titan
  d) Knowhere

  print a, b, c, or d

  """)
  if answer == "c":
    print("You got it correct! ")
    return 500
  else:
    print("You got it wrong :( ")
    return 0

def endgame_100():
  answer = input("""Who rescued Tony and Nebula from the space ship in the beginning of Endgame?
  a) Captain America
  b) Thanos
  c) Dr. Strange
  d) Captain Marvel

  print a, b, c, or d
  
  """)
  if answer == "d":
    print("You got it right! ")
    return 100
  else:
    print("You got it wrong :( ")
    return 0

def endgame_500():
  answer = input("""When the Avengers went back in time, where did Rocket take the Time Stone from?
  a) Tony's Briefcase
  b) Loki's Room
  c) Thor's Mom
  d) Jane's pocket
  
  print a, b, c, or d

  """)
  if answer == "d":
    print("You got it right! ")
    return 500
  else:
    print("You got it wrong :( ")
    return 0

def endgame_1000():
  answer = input("""After Tony's death and funeral, who was appointed the new ruler of Asgard?
  a) Valkyrie
  b) Rocket
  c) Thor
  d) Stephen Strange
  
  """)
  if answer == "a":
    print("You got it right! ")
    return 1000
  else:
    print("You got it wrong :( ")
    return 0 