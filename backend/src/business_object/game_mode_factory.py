from abc import ABC, abstractmethod
from business_object.game import Game
from business_object.player import Player
from business_object.game_mode import GameMode
import secrets
from datetime import datetime

class GameModeFactory :


    @classmethod
    def get_mode(cls, game_mode: str) -> GameMode:
        """
        Returns the corresponding GameMode object.
        Args:
            game_mode (str): The identifier of the game mode (e.g., 'coinflip', 'dice').
        Returns:
            GameMode: An instance of a class implementing GameMode.
        Raises:
            ValueError: If the requested game_mode is not supported.
        """

        if game_mode == "coinflip":
            return CoinFlipMode()

        if game_mode == "dice":
            return DiceMode()

        raise ValueError(
            f"Unsupported game mode: {game_mode}"
        )