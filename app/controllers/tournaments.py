"""Project OC DAP 4 file with tournament related class."""

from app.views.tournaments import TournamentMenuViewer

from app.config import CommandField
from app.config import ViewName


class TournamentMenuController:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        self.current_view = ViewName.view_tournaments
        self.sub_controller = None

        self.command_names = {}
        self.command_names[CommandField.exit_c] = self.exit_application
        self.command_names[CommandField.back_c] = self.goto_main_menu
        self.command_names[CommandField.unknown_c] = self.print_unknown_command

        self.viewer = TournamentMenuViewer()

    def display(self):
        """(Put description here)."""
        self.viewer.display()

    def exe_command(self, command):
        """(Put description here)."""
        if command in self.command_names:
            return self.command_names[command]()
        else:
            return self.command_names[CommandField.unknown_c]()

    def set_tournament_names(self, tournament_list):
        """(Put description here)."""
        name_list = []
        for tournament in tournament_list.values():
            name_list.append(tournament.name)
        self.viewer.set_tournament_names(name_list)

    def exit_application(self):
        """(Put description here)."""
        return True

    def return_arguments_main_menu(self):
        """(Put description here)."""
        arguments = []
        arguments.append("controller")
        return arguments

    def goto_main_menu(self):
        """(Put description here)."""
        self.current_view = ViewName.view_main

        self.viewer.warning = ""

        return False

    def print_unknown_command(self):
        """(Put description here)."""
        self.viewer.warning = "command unknown"

        return False
