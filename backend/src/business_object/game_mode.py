from abc import ABC, abstractmethod
from business_object.game import Game
from business_object.player import Player
import secrets
from datetime import datetime

class GameMode(ABC):
    """Service that manages the mode of the game."""
    
    @abstractmethod
    def play(self, p1: Player, p2: Player, **kwargs) -> Game:
        pass

    

class DiceMode(GameMode):

    def play(
        self,
        p1: Player,
        p2: Player,
        choice="heads",
        **kwargs
    ) -> Game:

        d1 = secrets.choice(range(1, 7))
        d2 = secrets.choice(range(1, 7))

        if d1>d2:
        winner = p1 
        elif d2>d1:
             winner=p2
        else : 
            winner = None

        description = (
            f"{p1.username} rolled {d1}."
            f"{p1.username} rolled {d1}."
        )

        return Game(
            player1=p1,
            player2=p2,
            game_mode="dice",
            winner=winner,
            description=description,
            timestamp=datetime.now()
        )

class CoinFlipMode(GameMode):

    def play(
        self,
        p1: Player,
        p2: Player,
        choice="heads",
        **kwargs
    ) -> Game:

        result = secrets.choice(["heads", "tails"])

        winner = p1 if result == choice else p2

        description = (
            f"Coin flip: {result}. "
            f"{p1.username} chose {choice}."
        )

        return Game(
            player1=p1,
            player2=p2,
            game_mode="coinflip",
            winner=winner,
            description=description,
            timestamp=datetime.now()
        )
