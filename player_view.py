

class PlayerView:
    """
    Vue du modèle Player
    """
    def __init__(self, controller):
        self.controller = controller

    def home(self):
        """
        Affiche la page d'accueil de la gestion des joueurs
        """
        message = """Bienvenue sur la page de gestion des joueurs\n
            [1] Créer un nouveau joueur\n
            [2] Afficher la liste des joueurs\n
        Entrez le numéro de l'action souhaitée\n
        """
        option = input(message)
        return option

