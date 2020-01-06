#!/usr/bin/env python
# coding: utf-8

# # Designing a Game Playing AI Using MinMax with α - β Pruning
# ## Introduction
# SangSeung (Jay) Lee
# Credit to Sari Sadiya
# Our objective is to use Min-Max with alpha / beta pruning to find a winning strategy for either player. Moreover, both players will try to win as fast as possible.

# In[1]:


import numpy as np
import itertools


# ## Tic Tac Toe
# Also known as "Noughts and Crosses". The roots of this game can be traced back to ancient Egyp, where such game boards have been found on roofing tiles dating from around 1300 BCE. It was also one of the first computer games; In 1952, ritish computer scientist Alexander S. Douglas developed OXO (or Noughts and Crosses) for the EDSAC computer at the University of Cambridge. His implememntation used MinMax and was able to play a perfect game against a human oponent.
#
# This class implememnts a TicTacToa game. The followng are the methods:
# * make_copy   : returns a copy of the game object.
# * move(ii,jj) : the player who's turn it is will check cell ii,jj
# * children    : returns a list of all game objects that result from 1 move
# * result      : returns the result, always between \[-1,1\]. A negative result indicates a player 2 win, 0 indicates a tie.
# * final_move  : return true if the current game is at a final state.

# In[2]:


class game_TicTacToe:
    def __init__(self):
        self.ROWS = 3
        self.COLS = 3
        self.board = np.zeros((self.ROWS, self.COLS))
        self.player = 1;
        self.numMoves = 1;

    def make_copy(self):
        newGame = game_TicTacToe()
        newGame.board = self.board.copy()
        newGame.player = self.player
        return newGame

    def move(self, ii, jj):
        if self.board[ii, jj] == 0:
            self.board[ii, jj] = self.player
        self.player *= -1
        self.numMoves += 1;
        return

    def children(self):
        children = []
        for ii, jj in np.argwhere(self.board == 0):
            newGame = self.make_copy()
            newGame.move(ii, jj)
            children.append(newGame)
        return children

    def result(self):
        PL1 = 3.0
        PL2 = -3.0
        if max(np.sum(self.board, axis=0)) == PL1 or max(np.sum(self.board, axis=1)) == PL1 or np.trace(
                self.board) == PL1 or np.trace(np.fliplr(self.board)) == PL1:
            return 1 / self.numMoves
        if min(np.sum(self.board, axis=0)) == PL2 or min(np.sum(self.board, axis=1)) == PL2 or np.trace(
                self.board) == PL2 or np.trace(np.fliplr(self.board)) == PL2:
            return -1 / self.numMoves
        return 0

    def final_move(self):
        return self.ROWS * self.COLS == len(np.nonzero(self.board)[0]) or (self.result() !=0)


# ## Chomp (Gale-Game)
# This is a newer game was developed by the mathematician David Gale (still kickin in cali). The game is usually formulated in terms of a chocolate bar were each of two players tries to avoid eating the last square. The players in turn choose one block and "eat it" (remove from the board), together with those that are below it and to its right. The top left block is "poisoned" and the player who eats this loses.
#
# This class implememnts a Chomp game. The followng are the methods:
# * make_copy   : returns a copy of the game object.
# * move(ii,jj) : the player who's turn it is will check cell ii,jj
# * children    : returns a list of all game objects that result from 1 move
# * result      : returns the result, always between \[-1,1\]. A negative result indicates a player 2 win, 0 indicates a tie.
# * final_move  : return true of the current game is at a final state.

# In[3]:


class game_Chomp:
    def __init__(self, ROWS=3, COLS=3):
        self.ROWS = ROWS
        self.COLS = COLS
        self.board = np.zeros((self.ROWS, self.COLS))
        self.player = 1;
        self.numMoves = 1;

    def make_copy(self):
        newGame = game_Chomp(self.ROWS, self.COLS)
        newGame.board = self.board.copy()
        newGame.player = self.player
        newGame.numMoves = self.numMoves
        return newGame

    def move(self, ii, jj):
        self.board[ii:self.ROWS, jj:self.COLS] = self.player;
        self.player *= -1
        self.numMoves += 1
        return

    def children(self):
        children = []
        for ii, jj in np.argwhere(self.board == 0):
            newGame = self.make_copy()
            newGame.move(ii, jj)
            children.append(newGame)
        return children

    def result(self):
        return -self.board[0, 0] / float(self.numMoves)

    def final_move(self):
        return self.ROWS * self.COLS == len(np.nonzero(self.board)[0]) #or (self.result != 0)

# # Show_game
#
# Given a list of "boards" (every game class has a board field) this method will draw the game. For instance it might draw the following TicTacToa game:

# In[23]:


"""
Given a list of "boards" (every game class has a board field) this method will draw the game. 
For instance it might draw the following TicTacToa game:
"""


# In[4]:


def show_game(plays, gameType='TicTacToe'):
    if np.sum(np.sum(np.abs(plays[0]))) != 0:
        plays.reverse()

    def ticks(player):
        if player == 1:
            return 'X'
        if player == -1:
            if gameType == 'TicTacToe':
                return 'O'
            return 'X'
        return ' '

    gameStr = ''
    for play in plays:
        playStr = []
        ROWS, COLS = np.shape(play)
        for i in range(0, ROWS):
            playStr.append('|'.join([' ' + ticks(play[i, j]) + ' ' for j in range(0, COLS)]))
        playStr = '\n-----------\n'.join(playStr)
        gameStr += playStr
        gameStr += '\n\n'
    return gameStr


# # Min Max
#
# Create a class of MinMax that has an alpha beta method.
#
# Params: game object, current alpha, current beta, and True if it's the max turn.
# Returns: a list of the boards of the best game alpha and beta could play, and the result of the game (same as the result of the game object that has the last board)

# In[16]:


GLOBAL_NUM_CALLS = 0


# In[29]:


# min max alpha beta
class minmax_alphabeta(object):
    def __init__(self, game):
        self.game = game
        self.bestPlay = list()
        return

    # get a strategy to win the game
    def minmax(self, game=None, maximizingPlayer=True):
        global GLOBAL_NUM_CALLS
        GLOBAL_NUM_CALLS = GLOBAL_NUM_CALLS + 1
        if game == None:
            game = self.game
        if game.final_move() == True:
            return [game.board], game.result()
        if maximizingPlayer:
            value = -1e99
            NewbestPlay = []
            for child in game.children():
                child_value = game.result()
                child_board, child_value = self.minmax(child, False)
                if value >= child_value:
                    continue
                else:
                    value = child_value
                    NewbestPlay = child_board
            return [game.board] + NewbestPlay, value
        else:
            # COMPLETE ...
            value = 1e99
            for child in game.children():
                child_value = game.result()
                child_board , child_value = self.minmax(child, True)
                if value <= child_value:
                    continue
                else:
                    value = child_value
                    NewbestPlay = child_board
            return [game.board] + NewbestPlay, value
    # get a strategy to win the game

    def alpabeta(self, game=None, a=-np.inf, b=np.inf, maximizingPlayer=True):
        global GLOBAL_NUM_CALLS
        GLOBAL_NUM_CALLS = GLOBAL_NUM_CALLS + 1
        if game == None:
            game = self.game
        if game.final_move() == True:
            return [game.board], game.result()
        if maximizingPlayer:
            value = -1e99
            NewbestPlay = []
            for child in game.children():
                child_value = game.result()
                child_board, child_value = self.alpabeta(child, a,b,False)
                if value >= child_value:
                    continue
                else:
                    value = child_value
                    a = max(value, a)
                    NewbestPlay = child_board
                    if a>= b:
                        break
            return [game.board] + NewbestPlay, value
        else:
            # COMPLETE ...
            value = 1e99
            for child in game.children():
                child_value = game.result()
                child_board, child_value = self.alpabeta(child,a, b, True)
                if value <= child_value:
                    continue
                else:
                    value = child_value
                    b = min(value, b)
                    NewbestPlay = child_board
                    if a>= b:
                        break
            return [game.board] + NewbestPlay, value
# ## Tic Tac Toe Strategy
# Is there a winning strategy for either player in TicTacToa?
# How long can the the loosing player strech the game for?

# In[ ]:

GLOBAL_NUM_CALLS = 0
minmax = minmax_alphabeta(game_TicTacToe())
bestPlay, res = minmax.minmax()
print(show_game(bestPlay))
if res == 0:
    print('A perfect game results in a tie')
else:
    print('player ' + str(int(-np.sign(res) * 1 / 2 + 1.5)) + ' wins in turn ' + str(int(1 / res)))
print('There were ' + str(GLOBAL_NUM_CALLS) + ' calls!')

# In[ ]:

GLOBAL_NUM_CALLS = 0
minmax = minmax_alphabeta(game_TicTacToe())
bestPlay, res = minmax.alpabeta()
print(show_game(bestPlay))
if res == 0:
    print('A perfect game results in a tie')
else:
    print('player ' + str(int(-np.sign(res) * 1 / 2 + 1.5)) + ' wins in turn ' + str(int(1 / res)))
print('There were ' + str(GLOBAL_NUM_CALLS) + ' calls!')

# ## Chomp Strategy
# Is there a winning strategy for either player in TicTacToa?
# How long can the the loosing player strech the game for?

# In[ ]:

GLOBAL_NUM_CALLS = 0
minmax = minmax_alphabeta(game_Chomp(4, 4))
bestPlay, res = minmax.alpabeta()
print(show_game(bestPlay, 'Chomp'))
if res == 0:
    print('A perfect game results in a tie')
else:
    print('player ' + str(int(-np.sign(res) * 1 / 2 + 1.5)) + ' wins in turn ' + str(int(1 / res)))
