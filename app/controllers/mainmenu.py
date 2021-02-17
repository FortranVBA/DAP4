"""Project OC DAP 4 file with tournament related class."""

from app.controllers.tournaments import TournamentMenuController
from app.controllers.players import PlayersController


from app.views.mainmenu import MainMenuViewer

from app.config import CommandField
from app.config import ViewName


class MainMenuController:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        self.current_view = ViewName.view_main
        self.sub_controller = None

        self.command_names = {}
        self.command_names[CommandField.exit_c] = self.exit_application
        self.command_names[CommandField.tournaments_c] = self.goto_tournaments_menu
        self.command_names[CommandField.players_c] = self.goto_players_menu
        self.command_names[CommandField.unknown_c] = self.print_unknown_command

        self.viewer = MainMenuViewer()

    def display(self):
        """(Put description here)."""
        if self.current_view == ViewName.view_main:
            self.viewer.display()
        else:
            self.sub_controller.display()

    def exe_command(self, command):
        """(Put description here)."""
        if self.current_view == ViewName.view_main:
            if command in self.command_names:
                return self.command_names[command]()
            else:
                return self.command_names[CommandField.unknown_c]()
        else:
            is_exit = self.sub_controller.exe_command(command)
            if self.sub_controller.current_view == ViewName.view_main:
                self.current_view = ViewName.view_main
                self.sub_controller = None
            return is_exit

    def exit_application(self):
        """(Put description here)."""
        return True

    def goto_tournaments_menu(self):
        """(Put description here)."""
        self.sub_controller = TournamentMenuController()

        self.current_view = ViewName.view_tournaments

        self.viewer.warning = ""

        return False

    def goto_players_menu(self):
        """(Put description here)."""
        self.sub_controller = PlayersController()

        self.current_view = ViewName.view_players

        self.viewer.warning = ""

        return False

    def print_unknown_command(self):
        """(Put description here)."""
        self.viewer.warning = "command unknown"

        return False

    def return_no_argument(self):
        """(Put description here)."""
        return []
