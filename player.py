from dataclasses import dataclass
from enums.disc_color import DiscColor

@dataclass(frozen=True)
class Player:
    # def __init__(self, name: str, disc_color: DiscColor):
    #     self.name = name
    #     self.disc_color = disc_color
    name: str
    disc_color: DiscColor

    def get_name(self) -> str:
        return self.name

    def get_disc_color(self) -> DiscColor:
        return self.disc_color