from datetime import datetime
from business_object.player import Player


class Game  :
    """
    Class representing a Game.
    Attributes:
        id_game (int): The unique identifier for the game.
        player1(Player): The player number 1.
        player2(Player): The player number 2.
        game_mode (str): The game's mode (“coinflip” or “dice”).
        winner (Player|None): The game's winner ( Player or None if it is a draw).
        description (str): Details about the game.
        timestamp (datetime): The game's time.
    """

    def __init__(
        self,
        player1:Player,
        player2:Player,
        game_mode:str,
        winner:Player|None,
        description:str,
        timestamp:datatime
        ):
        """Constructor"""
        self.id=None
        self.player1=player1
        self.player2=player2
        self.game_mode=game_mode
        self.winner=winner
        self.description=description
        self.timestamp=timestamp

    
    def __str__(self):
        """Returns a string representation of the game.
        Returns:
            str: A string containing the players, type of the game and the winner.
        """
        return (
            f"{self.game_mode} between "
            f"{self.player1.username} and {self.player2.username}. "
            f"Winner: {winner_name}"
        )

        