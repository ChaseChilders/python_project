from game_title import game_board
from question_functions import avengers_100
from question_functions import avengers_500
from question_functions import avengers_1000

points = [0]

game_board()

def question_select():
  movie_select = input("""
  What is the movie category you would like to answer questions from? """)
  amount_select = input("""
  What amount of money would you like to try and win? """)
  if movie_select == "The Avengers":
    if amount_select == "100":
      points += (avengers_100())
  if movie_select == "The Avengers":
    if amount_select == "$500":
      points += (avengers_500())
  if movie_select == "The Avengers":
    if amount_select == "$1000":
      points += (avengers_1000())
  

while True:
  question_select()