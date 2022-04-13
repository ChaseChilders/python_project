
def question_select():
  movie_select = input("What is the movie category you would like to answer questions from? ")
  amount_select = input("What amount of money would you like to try and win? ")

def avengers_100():
  if movie_select == "The Avengers":
    if amount_select == "$100":
      question = input("""Who is the Director of S.H.I.E.L.D? 
      a) Phil Coulson
      b) Nick Fury
      c) Natasha Romanov
      d) Steve Rogers""")
      if avengers_100 == "b":
        print("You got it correct!")
        player_new_total = player_total + question_total
        print(f"Your total is ${player_new_total}")
      else:
        print("You got it wrong :( ")
        print(f"Your total is {player_total}")


def avengers_500():
  if movie_select == "The Avengers":
    if amount_select == "$500":
      answer = input("""What is the item that Loki steals in order to take over earth?
      a) Thor's Hammer
      b) Captain America's Hammer
      c) Tesseract
      d) Helicopter
      """)
      if answer == "c":
        print("You got it correct!")
        player_new_total = player_total + question_total
        print(f"Your total is ${player_new_total}")
      else:
        print("You got it wrong :( ")
        print(f"Your total is {player_total}")

def avengers_1000():
  if movie_select == "The Avengers":
    if amount_select == "$1000":
      avengers_1000 = input("""What is used to destroy the wormhole generator that Loki built?
      a) The Hulk
      b) Loki's Scepter
      c) Nuclear Missile
      d) An Arrow
      """)
      if avengers_1000 == "b":
        print("You got it correct!")
        player_new_total = player_total + question_total
        print(f"Your total is ${player_new_total}")
      else:
        print("You got it wrong :( ")
        print(f"Your total is {player_total}")