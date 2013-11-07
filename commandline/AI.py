#!/usr/bin/python -tt
# Daniel Oppecker
# daniel.oppecker@gmail.com

import re

class AI(object):
  def __init__(self, piece):
    self.piece = piece
    if self.piece == 'X':
      self.opponent_piece = 'O'
    else:
      self.opponent_piece = 'X'
      
    self.winning_boards = re.compile(
          '((OOO|XXX)\w\w\w\w\w\w)|'
          '(\w\w\w(XXX|OOO)\w\w\w)|'
          '(\w\w\w\w\w\w(OOO|XXX))|'
          '(X\w\wX\w\wX\w\w)|(O\w\wO\w\wO\w\w)|'
          '(\wX\w\wX\w\wX\w)|(\wO\w\wO\w\wO\w)|'
          '(\w\wX\w\wX\w\wX)|(\w\wO\w\wO\w\wO)|'
          '(X\w\w\wX\w\w\wX)|(O\w\w\wO\w\w\wO)|'
          '(\w\wX\wX\wX\w\w)|(\w\wO\wO\wO\w\w)')
          
    self.current_turn = self.piece

  def is_game_over(self, board):
    if self.winning_boards.match(''.join(board)):
      if board.count('X') > board.count('O'): #if there is a winner and there are more X's than O's, the X player has won
        if self.piece == 'X': #return 1 if computer is the X player, else -1
          #print "X wins " + "".join(board)
          return 1
        else:
          #print "X wins " + "".join(board)
          return -1
      else: #If the winner is not X, then the winner is O
        if self.piece == 'O':
          return 1
        else:
          #print "O wins " + "".join(board)
          return -1
    elif (board.count('X') == 5) & (board.count('O') == 4):
      return 0
    else:
      return "No"
      
  def get_move_dictionary(self, board):
    """Return a dictionary of the open spaces on the board given"""
    move_to_try = {}
    for index, contents in enumerate(board):
      if (contents != "X") & (contents != "O"):
        move_to_try[index] = 0
    return move_to_try

  def which_players_turn(self, board):
    x_count = board.count('X')
    o_count = board.count('O')
    if x_count == o_count: #it is x's turn
      return 'X'
    elif x_count > o_count: #it is o's turn
      return 'O'
    
  def move(self, board):
    possible_moves = self.get_move_dictionary(board)
    #print possible_moves
    for key, value in possible_moves.iteritems():
      #print "Calculating for move " + str(key)
      board[key] = self.piece
      v = self.maxvalue(board)
      board[key] = str(key)
      possible_moves[key] = v
    #print board
    print possible_moves
    tuple_dict = sorted([ (v,k) for k,v in possible_moves.items()], reverse = True)
    return tuple_dict[0][1]
      
      
  def maxvalue(self, board):
    game_state = self.is_game_over(board)
    if game_state != "No":
      #print game_state
      return game_state
    v = -99999
    possible_moves = self.get_move_dictionary(board)
    for key, value in possible_moves.iteritems():
      board[key] = self.opponent_piece
      new_value = self.minvalue(board)
      if new_value > v:
        v = new_value
        possible_moves[key] = v
      board[key] = str(key)
    return v
    
  def minvalue(self, board):
    game_state = self.is_game_over(board)
    if game_state != "No":
      #print game_state
      return game_state
    v = 99999
    possible_moves = self.get_move_dictionary(board)
    for key, value in possible_moves.iteritems():
      board[key] = self.piece
      new_value = self.maxvalue(board)
      if new_value < v:
        v = new_value
        possible_moves[key] = v
      board[key] = str(key)
    return v
        
def main():
  #game_board = ["X", "X", "X", "3", "4", "5", "6", "7", "8"]
  #game_board = ["X", "X", "2", "O", "O", "5", "6", "7", "8"]
  game_board = ["", "", "", "", "", "", "", "", ""]
  Tic_Bot = AI('X')
  print Tic_Bot.move(game_board)

if __name__ == '__main__':
  main()