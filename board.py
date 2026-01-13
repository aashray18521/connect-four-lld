from dataclasses import dataclass, field
from typing import List, Optional

from enums.disc_color import DiscColor

@dataclass
class Board:
    rows: int = 6
    cols: int = 7
    grid: List[List[Optional[DiscColor]]] = field(init=False)

    def __post_init__(self) -> None:
        self.grid = [[None for _ in range(self.cols)] for _ in range(self.rows)]

    def get_columns(self) -> int:
        return self.cols
    
    def get_rows(self) -> int:
        return self.rows
    
    def can_place(self, column) -> int:
        # TODO: Business Logic
        return True
    
    def place_disk(self, player, column) -> int: # row where the disc will fall
        # TODO: Business Logic
        return None
    
    def check_win(self, player, row, column) -> bool:
        # TODO: Business Logic
        return False
    
    def is_board_full(self) -> bool:
        # TODO: Business Logic
        return False