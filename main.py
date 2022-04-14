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
import os

points = 0

# jeopardy_boards()

def question_select():
  global points
  movie_select = input("""
  What is the movie category you would like to answer questions from? """)
  amount_select = input("""
  What amount of money would you like to try and win? """)
  if movie_select == "The Avengers":
    if amount_select == "$100":
      points += avengers_100()
      playsound('Sounds/decoy.mp3')
      os.system('clear')
      game_board()
      jeopardy_boards()
  if movie_select == "The Avengers":
    if amount_select == "$500":
      points += avengers_500()
      playsound('Sounds/electricity.mp3')
      os.system('clear')
      game_board()
      jeopardy_boards()
  if movie_select == "The Avengers":
    if amount_select == "$1000":
      points += avengers_1000()
      playsound('Sounds/spangley.mp3')
      os.system('clear')
      game_board()
      jeopardy_boards()
  if movie_select == "Infinity War":
    if amount_select == "$100":
      points += infinity_war100()
      playsound('Sounds/galaga.mp3')
      os.system('clear')
      game_board()
      jeopardy_boards()
  if movie_select == "Infinity War":
    if amount_select == "$500":
      points += infinity_war500()
      playsound('Sounds/grows.mp3')
      os.system('clear')
      game_board()
      jeopardy_boards()
  if movie_select == "Infinity War":
    if amount_select == "$1000":
      points += infinity_war1000()
      playsound('Sounds/hulkroar4.mp3')
      os.system('clear')
      game_board()
      jeopardy_boards()
  if movie_select == "Endgame":
    if amount_select == "$100":
      points += endgame_100()
      playsound('Sounds/spear.mp3')
      os.system('clear')
      game_board()
      jeopardy_boards()
  if movie_select == "Endgame":
    if amount_select == "$500":
      points += endgame_500()
      playsound('Sounds/yay.mp3')
      os.system('clear')
      game_board()
      jeopardy_boards()
  if movie_select == "Endgame":
    if amount_select == "$1000": 
      points += endgame_1000()
      playsound('Sounds/petty.mp3')
      os.system('clear')
      game_board()
      jeopardy_boards()
  if movie_select == "x":
    if amount_select == "x":
      print(f"""



              _____________               ______      __  __                 __________                 ______________              _____                        _______                                        
              ___  __/__  /_______ __________  /__    _ \/ /_________  __    ___  ____/_____________    ___  __ \__  /_____ _____  ____(_)_____________ _        ___    |__   ____________________ _____________
              __  /  __  __ \  __ `/_  __ \_  //_/    __  /_  __ \  / / /    __  /_   _  __ \_  ___/    __  /_/ /_  /_  __ `/_  / / /_  /__  __ \_  __ `/        __  /| |_ | / /  _ \_  __ \_  __ `/  _ \_  ___/
              _  /   _  / / / /_/ /_  / / /  ,<       _  / / /_/ / /_/ /     _  __/   / /_/ /  /        _  ____/_  / / /_/ /_  /_/ /_  / _  / / /  /_/ /__       _  ___ |_ |/ //  __/  / / /  /_/ //  __/  /    
              /_/    /_/ /_/\__,_/ /_/ /_//_/|_|      /_/  \____/\__,_/      /_/      \____//_/         /_/     /_/  \__,_/ _\__, / /_/  /_/ /_/_\__, /_( )      /_/  |_|____/ \___//_/ /_/_\__, / \___//_/     
                                                                                                                            /____/              /____/ _|/                                 /____/               

      
                                                                                            YOU FINISHED WITH ${points}
      
      """)
      playsound('Sounds/The-Avengers-Theme-Song.mp3')
      exit()


while True:
  question_select()