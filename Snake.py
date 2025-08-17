import random

BOARD_WIDTH = 8
BOARD_HEIGHT = 8
SNAKE = ["B2", "B3", "B4", "C4", "D4"]
ORIENTATION = 4
APPLE = ""
APPLE_LIVES = 12
APPLE_GOT_EATEN = False
LIVES = 3
SCORE = 0
BIGGER_SNAKE = False
INVALID = False


def _7_submit_score():
  name = input('Your name for the history: ')
  lines = f"{name} - Score: {SCORE}- Lives: {LIVES} - Snake Length: {len(SNAKE)}\n"
  with open("history.txt", "a") as f:
    f.write(lines)

  lines = []
  with open("history.txt", "r") as f:
     for text in f:
       line = text.strip()
       lines.append(str(line))
  if len(lines) > 4:
    del lines[0]
    with open("history.txt", "w") as f:
      for counter in range(0, 4):
        f.write(lines[counter] + '\n')

  print("\n")
  print("History:")
  with open("history.txt", "r") as f:
    for line in f:
      print(line, end='')


def random_spawn():
  global APPLE
  helpchr = (chr(random.randint(65, 72)) + chr(random.randint(0, 7) + 48))
  while 1:
    if helpchr in SNAKE or helpchr == APPLE:
      helpchr = (chr(random.randint(65, 72)) + chr(random.randint(0, 7) + 48))
    else:
      break
  APPLE = helpchr


def _6_spawn_apple():
  global SNAKE, APPLE, APPLE_GOT_EATEN, APPLE_LIVES, LIVES, INVALID

  if APPLE_GOT_EATEN is True or APPLE_LIVES == 0:
    random_spawn()

  if APPLE_LIVES > 0 and APPLE_GOT_EATEN is not True:
    APPLE_LIVES -= 1
  else:
    if APPLE_GOT_EATEN is True:
      APPLE_LIVES = 12
    else:
      if APPLE_LIVES == 0 and APPLE_GOT_EATEN is not True:
        APPLE_LIVES = 12
        LIVES -= 1

  if INVALID is True:
    APPLE_LIVES += 2

  if LIVES == 0:
    _7_submit_score()
    exit(0)


def _5_detect_collision():
  global SNAKE
  if ORIENTATION == 4 and (ord(SNAKE[len(SNAKE) - 1][0]) + 1 == 73):
   return True
  if ORIENTATION == 2 and (ord(SNAKE[len(SNAKE) - 1][0]) - 1 == 64):
   return True
  if ORIENTATION == 3 and (int(SNAKE[len(SNAKE) - 1][1]) - 1 == -1):
   return True
  if ORIENTATION == 5 and (int(SNAKE[len(SNAKE) - 1][1]) + 1 == 8):
    return True
  for counter in range(1, len(SNAKE) - 2):
   if ORIENTATION == 4 and chr(ord(SNAKE[len(SNAKE) - 1][0]) + 1) + SNAKE[len(SNAKE) - 1][1] == SNAKE[counter]:
     return True
   if ORIENTATION == 2 and chr(ord(SNAKE[len(SNAKE) - 1][0]) - 1) + SNAKE[len(SNAKE) - 1][1] == SNAKE[counter]:
     return True
   if ORIENTATION == 3 and SNAKE[len(SNAKE) - 1][0] + str(int(SNAKE[len(SNAKE) - 1][1]) - 1) == SNAKE[counter]:
     return True
   if ORIENTATION == 5 and SNAKE[len(SNAKE) - 1][0] + str(int(SNAKE[len(SNAKE) - 1][1]) + 1) == SNAKE[counter]:
     return True


def _4_move_snake():
  global SNAKE, SCORE, ORIENTATION, BIGGER_SNAKE
  SCORE += 1
  if BIGGER_SNAKE is False:
    del SNAKE[0]
  if ORIENTATION == 4:
    SNAKE.append((chr(ord(SNAKE[len(SNAKE) - 1][0]) + 1) + (SNAKE[len(SNAKE) - 1][1])))
  if ORIENTATION == 2:
    SNAKE.append((chr(ord(SNAKE[len(SNAKE) - 1][0]) - 1) + (SNAKE[len(SNAKE) - 1][1])))
  if ORIENTATION == 3:
    SNAKE.append((SNAKE[len(SNAKE) - 1][0]) + str(int(SNAKE[len(SNAKE) - 1][1]) - 1))
  if ORIENTATION == 5:
    SNAKE.append((SNAKE[len(SNAKE) - 1][0]) + str(int(SNAKE[len(SNAKE) - 1][1]) + 1))


def _3_is_snake(row, column):
  global SNAKE, ORIENTATION
  for counter in range(0, len(SNAKE)):
    if row == ord(SNAKE[counter][0]) and column == int(SNAKE[counter][1]):
      if counter == len(SNAKE) - 1:
        if ORIENTATION == 2:
          return 2
        if ORIENTATION == 3:
          return 3
        if ORIENTATION == 4:
          return 4
        if ORIENTATION == 5:
          return 5
      else:
        return 1
  return 0


def _2_is_apple(row, column):
  global APPLE
  if row == ord(APPLE[0]) and column == int(APPLE[1]):
   return 1
  else:
   return 0


def _1_print_game_board():
  global LIVES, APPLE_LIVES, SCORE, BIGGER_SNAKE, APPLE_GOT_EATEN, INVALID
  line = "----------------------------"
  field = [" ", " ", " ", " ", " ", " ", " ", " "]
  snake = [" ", "+", "∧", "<", "v", ">"]
  empty_field_symbol = " "
  apple_field_symbol = "O"

  if SNAKE[len(SNAKE) - 1] == APPLE:
    BIGGER_SNAKE = True
    APPLE_GOT_EATEN = True
    _6_spawn_apple()

  if APPLE_LIVES == 0 or INVALID is True:
    _6_spawn_apple()
  INVALID = False

  print(f"Lives: {LIVES} - Apple Lives: {APPLE_LIVES} - Score: {SCORE}")
  print(line)
  for counter in range(0, BOARD_HEIGHT):
    print(f'{chr(65 + counter)} |', end='')
    for counter1 in range(0, BOARD_WIDTH):
      if _3_is_snake(65 + counter, counter1) != 0:
          field[counter1] = snake[_3_is_snake(65 + counter, counter1)]
          print(" " + field[counter1] + " ", end='')
      else:
        if _2_is_apple(65 + counter, counter1) == 1:
          field[counter1] = apple_field_symbol
          print(" " + field[counter1] + " ", end='')
        else:
          field[counter1] = empty_field_symbol
          print(" " + field[counter1] + " ", end='')
    print("|")
  print(line)
  print("    0  1  2  3  4  5  6  7")

  if SNAKE[len(SNAKE) - 1] != APPLE:
    BIGGER_SNAKE = False
    APPLE_GOT_EATEN = False
    _6_spawn_apple()


def moving(button):
  if button == 'w':
    return 2
  if button == 'a':
    return 3
  if button == 's':
    return 4
  if button == 'd':
    return 5
  if button == '':
    return ORIENTATION


def main():
  global ORIENTATION, SCORE, APPLE_GOT_EATEN, INVALID
  controls = ['', 'q', 'w', 'a', 's', 'd']
  if APPLE == "":
   random_spawn()
  while 1:
    _1_print_game_board()
    button = input('input [w a s d]:')
    if button not in controls:
      button = ''
    orientation2 = ORIENTATION
    if button != 'q':
      ORIENTATION = moving(button)
    else:
      exit(0)
    if button == '' or (orientation2 + ORIENTATION) % 2 != 0 or orientation2 == ORIENTATION:
      if _5_detect_collision() is not True:
        _4_move_snake()
      else:
       _7_submit_score()
       exit(0)
    else:
      ORIENTATION = orientation2
      print("INVALID")
      INVALID = True


if __name__ == '__main__':
  main()
