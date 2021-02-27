"""Project OC DAP 4 file with tournament related class."""

from app.controllers.commands import PrintUnknownCommand
from app.controllers.commands import GotoPlayersMenu
from app.controllers.commands import GotoTournamentsMenu
from app.controllers.commands import ExitApplication

from app.views.mainmenu import MainMenuViewer


class MainMenuController:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        self._app = None
        self.command = None
        self.viewer = MainMenuViewer()

        self.command_names = []

    def get_command(self):
        """(Put description here)."""
        command_input = input("Enter your command: ")

        self.command_names = [
            PrintUnknownCommand(self.viewer),
            ExitApplication(),
            GotoTournamentsMenu(self._app, self.viewer),
            GotoPlayersMenu(self._app, self.viewer),
        ]

        for command in self.command_names:
            if command.is_valid(command_input):
                self.command = command

    def display(self):
        """(Put description here)."""
        self.viewer.display()
