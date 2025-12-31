from board import Board
from player import Player
from game_state import GameState

from typing import Optional

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = Board()
        self.winner = Optional[Player]
        self.current_player = self.get_current_player()
        self.state = self.get_current_game_state()
    
    def get_current_player(self) -> Player:
        if self.current_player is None or self.current_player == self.player2:
            return self.player1
        else:
            return self.player2
    
    def get_current_game_state(self) -> GameState:
        if self.winner is not None:
            return GameState.WIN
        # elif     ## DRAW     
        else:   ## IN_PROGRESS
            return  GameState.IN_PROGRESS

    def get_winner(self) -> Optional[Player]:
        return self.winner

    def get_board(self) -> Board:
        return self.board