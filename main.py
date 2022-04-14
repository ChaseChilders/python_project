from game_title import game_board
from question_functions import avengers_100
from question_functions import avengers_500
from question_functions import avengers_1000
from question_functions import infinity_war100
from question_functions import infinity_war500
from question_functions import infinity_war1000
from question_functions import endgame_100
from question_functions import endgame_500
from question_functions import endgame_1000 
from jeopardy_board import jeopardy_boards
from playsound import playsound
from question_functions import play_music

points = 0

game_board() 

jeopardy_boards()

def question_select():
  global points
  movie_select = input("""
  What is the movie category you would like to answer questions from? """)
  amount_select = input("""
  What amount of money would you like to try and win? """)
  if movie_select == "The Avengers":
    if amount_select == "$100":
      points += avengers_100()
      jeopardy_boards()
  if movie_select == "The Avengers":
    if amount_select == "$500":
      points += avengers_500()
      jeopardy_boards()
  if movie_select == "The Avengers":
    if amount_select == "$1000":
      points += avengers_1000()
      jeopardy_boards()
  if movie_select == "Infinity War":
    if amount_select == "$100":
      points += infinity_war100()
      jeopardy_boards()
  if movie_select == "Infinity War":
    if amount_select == "$500":
      points += infinity_war500()
      jeopardy_boards()
  if movie_select == "Infinity War":
    if amount_select == "$1000":
      points += infinity_war1000()
      jeopardy_boards()
  if movie_select == "Endgame":
    if amount_select == "$100":
      points += endgame_100()
      jeopardy_boards()
  if movie_select == "Endgame":
    if amount_select == "$500":
      points += endgame_500()
      jeopardy_boards()
  if movie_select == "Endgame":
    if amount_select == "$1000": 
      points += endgame_1000()
      jeopardy_boards()
  if movie_select == "x":
    if amount_select == "x":
      print(f"""
      
      Thank you for playing!
      
      You finished with ${points}
      
      """)
      playsound('The-Avengers-Theme-Song.mp3')
      exit()


while True:
  question_select()