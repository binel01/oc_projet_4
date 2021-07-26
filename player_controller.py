
from player_model import Player
from player_view import PlayerView

class PlayerController:
    """
    Contrôleur de la classe Player
    """
    def __init__(self):
        self.model = Player(self)
        self.view = PlayerView(self)

    def home(self):
        option = self.view.home()