"""Project OC DAP 4 file with tournament related class."""

from app.views.players import PlayersViewer

from app.config import CommandField
from app.config import ViewName


class PlayersController:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        self.player_number = 0

        self.command_names = {}
        self.command_names[CommandField.exit_c] = self.exit_application
        self.command_names[CommandField.back_c] = self.goto_main_menu
        self.command_names[CommandField.unknown_c] = self.print_unknown_command
        self.command_names[CommandField.save_players_c] = self.save_database

        self.arguments_needed = {}
        self.arguments_needed[CommandField.exit_c] = self.return_no_argument
        self.arguments_needed[CommandField.back_c] = self.return_arguments_main_menu
        self.arguments_needed[CommandField.unknown_c] = self.return_no_argument
        self.arguments_needed[
            CommandField.save_players_c
        ] = self.return_arguments_save_database

        self.viewer = PlayersViewer()

    def display(self):
        """(Put description here)."""
        self.viewer.display()

    def get_arguments(self, command):
        """(Put description here)."""
        if command in self.arguments_needed:
            return self.arguments_needed[command]()
        else:
            return self.arguments_needed[CommandField.unknown_c]()

    def exe_command(self, command, arguments):
        """(Put description here)."""
        if command in self.command_names:
            return self.command_names[command](arguments)
        else:
            return self.command_names[CommandField.unknown_c](arguments)

    def set_player_names(self, player_list):
        """(Put description here)."""
        name_list = []
        for player in player_list.values():
            name_list.append(player.surname + " " + player.name)
        self.viewer.set_player_names(name_list)

    def return_no_argument(self):
        """(Put description here)."""
        return []

    def exit_application(self, arguments):
        """(Put description here)."""
        return True

    def return_arguments_main_menu(self):
        """(Put description here)."""
        arguments = []
        arguments.append("controller")
        return arguments

    def goto_main_menu(self, arguments):
        """(Put description here)."""
        current_view = arguments[0].current_view

        current_view = ViewName.view_main

        arguments[0].current_view = current_view

        self.viewer.warning = ""

        return False

    def return_arguments_save_database(self):
        """(Put description here)."""
        arguments = []
        arguments.append("player_list")
        return arguments

    def save_database(self, arguments):
        """(Put description here)."""
        player_list = arguments[0]

        player_list.save_tinyDB()

        arguments[0] = player_list

        self.viewer.warning = ""

        return False

    def print_unknown_command(self, arguments):
        """(Put description here)."""
        self.viewer.warning = "command unknown"

        return False
