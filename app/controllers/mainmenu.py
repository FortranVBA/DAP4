"""Project OC DAP 4 file with tournament related class."""

from app.controllers.commands import PrintUnknownCommand
from app.controllers.commands import GotoPlayersMenu
from app.controllers.commands import GotoTournamentsMenu


from app.views.mainmenu import MainMenuViewer

from app.config import CommandField


class MainMenuController:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        self._app = None

        self.command_names = {
            CommandField.EXIT: self.exit_application,
            CommandField.TOURNAMENTS: self.goto_tournaments_menu,
            CommandField.PLAYERS: self.goto_players_menu,
            CommandField.UNKNOWN: self.print_unknown_command,
        }

        self.viewer = MainMenuViewer()

    def display(self):
        """(Put description here)."""
        self.viewer.display()

    def exe_command(self, command):
        """(Put description here)."""
        if command in self.command_names:
            return self.command_names[command]()
        else:
            return self.command_names[CommandField.UNKNOWN]()

    def exit_application(self):
        """(Put description here)."""
        return True

    def goto_tournaments_menu(self):
        """(Put description here)."""
        return GotoTournamentsMenu(self._app, self.viewer).exe_command()

    def goto_players_menu(self):
        """(Put description here)."""
        return GotoPlayersMenu(self._app, self.viewer).exe_command()

    def print_unknown_command(self):
        """(Put description here)."""
        return PrintUnknownCommand(self.viewer).exe_command()
