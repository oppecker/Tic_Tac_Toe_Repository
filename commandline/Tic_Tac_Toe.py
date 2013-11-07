#!/usr/bin/python -tt
# Daniel Oppecker
# daniel.oppecker@gmail.com

import re
import AI

class Game_Board(object):
  def __init__(self):
    self.board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    
  def print_board(self):
    board_as_string = ''.join(self.board)
    print " %c | %c | %c \n---+---+---\n %c | %c | %c \n---+---+---\n %c | %c | %c" % (
    board_as_string[0], board_as_string[1], board_as_string[2], 
    board_as_string[3], board_as_string[4], board_as_string[5], 
    board_as_string[6], board_as_string[7], board_as_string[8])
      
  def return_board(self):
    return self.board
    
  def update_board(self, piece, location):
    self.board[location] = piece
    
class Game(object):
  def __init__(self):
    self.board = Game_Board()
    self.piece = 'X'
    self.game_bot = AI.AI('O')
    
  def prompt_and_verify_move(self):
    valid = False
    input_prompt = "Player " + self.piece + " Enter Move (1-9): "
    move = raw_input(input_prompt)
    while (valid == False):
      #first convert to an integer and . If the input move can not be converted to an int, it is not valid.
      try:
        move = int(move)
      except ValueError:
        move = raw_input("Invalid Input\nEnter Move (1-9): ")
        continue
      #convert move to index an of board
      #move -= 1
      #next check if the move integer is between 0 and 8. otherwise it is not a valid index for the board string
      if (move > 8) | (move < 0):
        move = raw_input("Invalid Input\nEnter Move (1-9): ")
        continue
      #next check if the space on the board is open.
      if (self.board.return_board()[move] == 'X') | (self.board.return_board()[move] == 'O'):
        move = raw_input("Invalid Input\nEnter Move (1-9): ")
        continue
      valid = True
    
    return move
    
  def check_win_draw(self):
    current_board = ''.join(self.board.return_board())
    pattern = re.compile(
    '((OOO|XXX)\w\w\w\w\w\w)|'
    '(\w\w\w(XXX|OOO)\w\w\w)|'
    '(\w\w\w\w\w\w(OOO|XXX))|'
    '(X\w\wX\w\wX\w\w)|(O\w\wO\w\wO\w\w)|'
    '(\wX\w\wX\w\wX\w)|(\wO\w\wO\w\wO\w)|'
    '(\w\wX\w\wX\w\wX)|(\w\wO\w\wO\w\wO)|'
    '(X\w\w\wX\w\w\wX)|(O\w\w\wO\w\w\wO)|'
    '(\w\wX\wX\wX\w\w)|(\w\wO\wO\wO\w\w)')
    if pattern.match(current_board):
      return "Player " + self.piece + " Wins!"
      
    elif (current_board.count('X') == 5) & (current_board.count('O') == 4):
      return "It's A Draw"
    elif (current_board.count('X') == 4) & (current_board.count('O') == 5):
      return "It's A Draw"
    else:
      return False

  def switch_player(self):
    if self.piece == 'X':
      self.piece = 'O'
    else:
      self.piece = 'X'
    
  def run_game(self):
    game_mode = self.choose_mode()
    if game_mode == "1":
      self.single_player()
    else:
      self.multi_player()
    
  def single_player(self):
    print "single player fun time"
    game_over = False
    self.board.print_board()
    while(game_over == False):
      #prompt for move
      input = self.prompt_and_verify_move()
      #update board using 'x' as piece until turn system is implemented
      self.board.update_board(self.piece, input)
      self.board.print_board()
      #check for a win or draw
      game_over = self.check_win_draw()
      #switch to other player
      self.switch_player()
      self.board.update_board(self.piece, self.game_bot.move(self.board.board))

      self.board.print_board()
      game_over = self.check_win_draw()
      self.switch_player()
      #NOW DO COMPUTERS MOVE
      #Determine correct move from position
      #Update board with the move
      #print the board
      #switch to other player
    
  def multi_player(self):
    game_over = False
    self.board.print_board()
    #enter while loop of game play
    while(game_over == False):
      #prompt for move
      input = self.prompt_and_verify_move()
      #update board using 'x' as piece until turn system is implemented
      self.board.update_board(self.piece, input)
      self.board.print_board()
      #check for a win or draw
      game_over = self.check_win_draw()
      #switch to other player
      self.switch_player()
    print game_over
    
  def choose_mode(self):
    game_mode = -1
    while (game_mode != "1") & (game_mode != "2"):
      input_prompt = "Enter 1 for single player mode, 2 for double player mode:"
      game_mode = raw_input(input_prompt)
    return game_mode

def main():
  game = Game()
  game.run_game()
    
if __name__ == '__main__':
  main()