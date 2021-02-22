"""Project OC DAP 4 file with tournament related class."""

from app.controllers.commands import PrintUnknownCommand

from app.views.edit_tournament import EditTournamentViewer

from app.config import CommandField
from app.config import ViewName

from app.models.player import Player


class EditPlayerController:
    def __init__(self, player, is_new):
        """Init Application class."""
        if is_new:
            name_new = input("Enter your tournament name : ")
            self.tournament = Tournament(name_new)
