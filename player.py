from enums.disc_color import DiscColor

class Player:

    def __init__(self, name: str, disc_color: DiscColor):
        self.name = name
        self.disc_color = disc_color

    def get_name(self) -> str:
        return self.get_name

    def get_disc_color(self) -> str:
        return self.get_disc_color