import os
import secrets

from fastapi import HTTPException

from dao.player_dao import PlayerDao
from utils.log_utils import log
from business_object.game_mode_factory import GameModeFactory


class GameService:
    """Service that manages games."""

    @log
    def play(self, id_player: int, id_opponent: int, game_mode : str, **kwargs):
        """Executes a single round of a coin-flip game between two players.
        Args:
            id_player (int): The unique identifier of the first player.
            id_opponent (int): The unique identifier of the opponent.
            choice (str, optional): The player's choice ('heads' or 'tails'). Defaults to "heads".
        Returns:
            dict: A dictionary containing the match details and new elo
        Raises:
            HTTPException: 400 if the two players are the same.
            HTTPException: 404 if one or both players are not found in the database.
        """
        if id_player == id_opponent:
            raise HTTPException(status_code=400, detail="Two different players required")

        p1 = PlayerDao().find_by_id(id_player)
        p2 = PlayerDao().find_by_id(id_opponent)
        mode = GameModeFactory.get_mode(game_mode)

        if not p1 or not p2:
            raise HTTPException(status_code=404, detail="Player not found")

        game = mode.play(p1,p2,**kwargs)

        ScoringStrategy.update_player_ratings(game)

        player_dao.update(p1)
        player_dao.update(p2)

        return game

    
