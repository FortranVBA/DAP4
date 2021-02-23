"""Project OC DAP 4 file with tournament related class."""

from app.controllers.commands import PrintUnknownCommand
from app.controllers.commands import LoadPlayerDatabase
from app.controllers.commands import SavePlayerDatabase
from app.controllers.commands import GotoMainMenu
from app.controllers.commands import GotoEditPlayer
from app.controllers.commands import ListPlayersAlphabeticalCommand
from app.controllers.commands import ListPlayersRankingCommand

from app.views.players import PlayersViewer

from app.models.player import Player

from app.config import CommandField


class PlayersController:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        self._app = None

        self.command_names = {
            CommandField.EXIT: self.exit_application,
            CommandField.BACK: self.goto_main_menu,
            CommandField.UNKNOWN: self.print_unknown_command,
            CommandField.EDIT_PLAYER: self.goto_edit_player_menu,
            CommandField.SAVE_PLAYERS: self.save_database,
            CommandField.LOAD_PLAYERS: self.load_database,
            CommandField.PLAYERS_ALPHABETIC: self.list_alphabetical,
            CommandField.PLAYERS_RANKING: self.list_ranking,
        }

        self.viewer = PlayersViewer()

    def display(self):
        """(Put description here)."""
        self.viewer.display()

    def exe_command(self, command):
        """(Put description here)."""
        if command in self.command_names:
            return self.command_names[command]()
        else:
            number = 1
            for player in Player.get_all.values():
                if command == str(number) + CommandField.EDIT_PLAYER:
                    return self.command_names[CommandField.EDIT_PLAYER](player)
                number += 1

            return self.command_names[CommandField.UNKNOWN]()

    def exit_application(self):
        """(Put description here)."""
        return True

    def goto_main_menu(self):
        """(Put description here)."""
        return GotoMainMenu(self._app, self.viewer).exe_command()

    def save_database(self):
        """(Put description here)."""
        return SavePlayerDatabase(self.viewer).exe_command()

    def load_database(self):
        """(Put description here)."""
        return LoadPlayerDatabase(self.viewer).exe_command()

    def print_unknown_command(self):
        """(Put description here)."""
        return PrintUnknownCommand(self.viewer).exe_command()

    def goto_edit_player_menu(self, player):
        """(Put description here)."""
        return GotoEditPlayer(self._app, self.viewer, player, None).exe_command()

    def list_alphabetical(self):
        """(Put description here)."""
        return ListPlayersAlphabeticalCommand(self.viewer).exe_command()

    def list_ranking(self):
        """(Put description here)."""
        return ListPlayersRankingCommand(self.viewer).exe_command()
