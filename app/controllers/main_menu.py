"""Project OC DAP 4 file with the main_menu controller."""

from app.commands.application import PrintUnknownCommand
from app.commands.navigation import GotoPlayersMenu
from app.commands.navigation import GotoTournamentsMenu
from app.commands.application import ExitApplication

from app.views.main_menu import MainMenuViewer


class MainMenuController:
    """Project main_menu controller class."""

    def __init__(self):
        """Init main_menu controller class."""
        self._app = None
        self.command = None
        self.viewer = MainMenuViewer()

        self.command_names = []

    def display(self):
        """Display the controller view."""
        self.viewer.display()

    def get_command(self):
        """Get the user input and convert it to a command instance."""
        command_input = input("Enter your command: ")

        # The 1st command in list must always be the PrintUnknownCommand, which is used
        # as default command.
        self.command_names = [
            PrintUnknownCommand(self.viewer),
            ExitApplication(),
            GotoTournamentsMenu(self._app, self.viewer),
            GotoPlayersMenu(self._app, self.viewer),
        ]

        for command in self.command_names:
            if command.is_valid(command_input):
                self.command = command
