#!/usr/bin/python -tt
# Daniel Oppecker
# daniel.oppecker@gmail.com

from Tkinter import *
import re

class Game(object):
  def __init__(self):
    self.master = Tk()
    self.master.title("Tic Tac Totally Awesome")
    self.w = Canvas(self.master, width=230, height=200, background="white")
    self.w.pack()
    
    self.x_piece = PhotoImage(file="x.gif")
    self.o_piece = PhotoImage(file="o.gif")
    self.board_image = PhotoImage(file="board.gif")
    self.x_wins = PhotoImage(file="x_wins.gif")
    self.o_wins = PhotoImage(file="o_wins.gif")
    self.game_draw = PhotoImage(file="game_draw.gif")
    
    self.board = ["1","2", "3", "4", "5", "6", "7", "8", "9"]
    self.piece = 'X'
    self.piece_image = self.x_piece
    
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
      move -= 1
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
    current_board = ''.join(self.board)
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
      self.w.unbind("<Button-1>")
      self.b = Button(self.master, text="Play Again?", command=self.restart_game)
      self.b.pack()
      if self.piece == "X":
        self.w.create_image(118, 100, image=self.x_wins)
      elif self.piece == "O":
        self.w.create_image(118, 100, image=self.o_wins)
      return "Player " + self.piece + " Wins!"
      
    elif (current_board.count('X') == 5) & (current_board.count('O') == 4):
      self.w.unbind("<Button-1>")
      self.w.create_image(118, 100, image=self.game_draw)
      self.b = Button(self.master, text="Play Again?", command=self.restart_game)
      self.b.pack()
      return "It's A Draw"
    elif (current_board.count('X') == 4) & (current_board.count('O') == 5):
      self.w.unbind("<Button-1>")
      self.w.create_image(118, 100, image=self.game_draw)
      self.b = Button(self.master, text="Play Again?", command=self.restart_game)
      self.b.pack()
      return "It's A Draw"
    else:
      return False

  def restart_game(self):
    print "yay?"
    #self.w = Canvas(self.master, width=230, height=200, background="white")
    #self.w.create_image(120,100, image=self.board_image,)
    self.w.delete(ALL)
    self.b.destroy()
    self.print_board()
    print "wee?"
    self.w.bind("<Button-1>", lambda event, x=self.piece: self.update_board(event, x))
    self.piece = 'X'
    self.piece_image = self.x_piece
    self.board = ["1","2", "3", "4", "5", "6", "7", "8", "9"]
    
      
  def switch_player(self):
    if self.piece == 'X':
      self.piece = 'O'
      self.piece_image = self.o_piece
    else:
      self.piece = 'X'
      self.piece_image = self.x_piece
    
  def run_game(self):
    game_over = False
    self.print_board()

  def update_board(self, event, x):
      print "clicked at x= " + str(event.x) + " y= " + str(event.y)
      #check which space on board list move corresponds to
      input_valid, board_x, board_y = self.validate_input(event.x, event.y)
      #if input_valid is False, don't update board, otherwise update board
      if input_valid != -1:
        self.board[input_valid] = self.piece
        self.w.create_image(board_x, board_y, image=self.piece_image)
        print self.check_win_draw()
        self.switch_player()
      print self.board
      
  def validate_input(self, x, y):
    #figure out which spot in self.board the coordinates correspond to
    board_index = self.get_board_index(x, y)
    #check if that board spot is open
    #board_index, board_x, board_y = check_if_open(board_index)
    #if spot is open, board_index will be 0-8 otherwise it will be False
    return self.check_if_open(board_index[0]), board_index[1], board_index[2]
    
  def check_if_open(self, board_index):
    if (self.board[board_index] != "X") & (self.board[board_index] != "O"):
      return board_index
    else:
      return -1
    
  def get_board_index(self, x, y):
    if (x < 64) & (y < 52):
      return 0, 40, 25
    elif (x > 54) & (x < 160) & (y < 52):
      return 1, 112, 25
    elif (x > 162) & (y < 52):
      return 2, 190, 25
    elif (x < 64) & (y >53) & (y < 135):
      return 3, 40, 90
    elif (x < 160) & (x > 65) & (y < 134) & (y > 53):
      return 4, 115, 100
    elif (x > 161) & (y > 53) & (y < 134):
      return 5, 190, 100
    elif (x <64) & (y > 135):
      return 6, 40, 165
    elif (x < 160) & (x > 65) & (y > 135):
      return 7, 110, 165
    elif (x > 161) & (y >135):
      return 8, 190, 165
        
  def print_board(self):
    self.w.create_image(120,100, image=self.board_image,)
    self.w.bind("<Button-1>", lambda event, x=self.piece: self.update_board(event, x))

def main():
  the_game = Game()
  the_game.run_game()
  mainloop()

if __name__ == '__main__':
  main()