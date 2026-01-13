from dataclasses import dataclass, field
from typing import Optional

from board import Board
from player import Player
from enums.game_state import GameState

@dataclass
class Game:
    # def __init__(self, player1, player2):
    #     self.player1 = player1
    #     self.player2 = player2
    #     self.board = Board()
    #     self.winner = Optional[Player]
    #     self.current_player = self.get_current_player()
    #     self.state = self.get_current_game_state()
    player1: Player
    player2: Player
    board: Board = field(default_factory=Board)
    winner: Optional[Player] = None
    current_player: Optional[Player] = field(init=False)
    game_state: GameState = field(init=False)
    
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
    
    def make_move(self, player, column) -> bool: ## Can throw exception(s) for invalid moves instead of "False"
        if(self.game_state != GameState.IN_PROGRESS):
            return False
        if(player != self.current_player):
            return False
        if(column <= 0 or column >= self.board.get_columns()):
            return False
        if(not self.board.can_place(column)):
            return False
        
        row = self.board.place_disk(player=player, column=column)

        if(self.board.check_win(player=player, row=row, column=column)):
            self.game_state = GameState.WIN
            self.winner = player
        elif(self.board.is_board_full()):
            self.game_state = GameState.DRAW
        else: # switch turn
            if(player == self.player1):
                self.current_player = self.player2
            else:
                self.current_player = self.player1
        return True