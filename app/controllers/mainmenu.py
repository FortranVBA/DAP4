"""Project OC DAP 4 file with tournament related class."""

from app.views.mainmenu import MainMenuViewer

from app.models.tournament import Tournament

from app.config import CommandField
from app.config import ViewName


class MainMenuController:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        self.command_names = {}
        self.command_names[CommandField.exit_c] = self.exit_application
        self.command_names[CommandField.new_c] = self.goto_create_menu
        self.command_names[CommandField.tournaments_c] = self.goto_tournaments_menu
        self.command_names[CommandField.print_c] = self.goto_print_menu
        self.command_names[CommandField.unknown_c] = self.print_unknown_command

        self.arguments_needed = {}
        self.arguments_needed[CommandField.exit_c] = self.return_no_argument
        self.arguments_needed[CommandField.new_c] = self.return_arguments_create_menu
        self.arguments_needed[
            CommandField.tournaments_c
        ] = self.return_arguments_tournaments_menu
        self.arguments_needed[CommandField.print_c] = self.return_arguments_print_menu
        self.arguments_needed[CommandField.unknown_c] = self.return_no_argument

        self.viewer = MainMenuViewer()

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

    def exit_application(self, arguments):
        """(Put description here)."""
        return True

    def return_arguments_create_menu(self):
        """(Put description here)."""
        arguments = []
        arguments.append("tournament_list")
        arguments.append("controller")
        arguments.append("edit_tournament_controller")
        return arguments

    def goto_create_menu(self, arguments):
        """(Put description here)."""
        tournament_list = arguments[0]
        current_view = arguments[1].current_view
        edit_tournament_controller = arguments[2]

        name_new = input("Enter your tournament name : ")
        tournament_list[name_new] = Tournament(name_new)

        current_view = ViewName.view_edit_tournament
        edit_tournament_controller.set_selected_tournament(tournament_list[name_new])

        arguments[0] = tournament_list
        arguments[1].current_view = current_view
        arguments[2] = edit_tournament_controller

        self.viewer.warning = ""

        return False

    def return_arguments_tournaments_menu(self):
        """(Put description here)."""
        arguments = []
        arguments.append("controller")
        arguments.append("tournaments_controller")
        arguments.append("tournament_list")
        return arguments

    def goto_tournaments_menu(self, arguments):
        """(Put description here)."""
        current_view = arguments[0].current_view
        tournaments_controller = arguments[1]
        tournament_list = arguments[2]

        current_view = ViewName.view_tournaments
        tournaments_controller.set_tournament_names(tournament_list)

        arguments[0].current_view = current_view
        arguments[1] = tournaments_controller
        arguments[2] = tournament_list

        self.viewer.warning = ""

        return False

    def return_arguments_print_menu(self):
        """(Put description here)."""
        arguments = []
        arguments.append("controller")
        return arguments

    def goto_print_menu(self, arguments):
        """(Put description here)."""
        current_view = arguments[0].current_view

        current_view = ViewName.view_print

        arguments[0].current_view = current_view

        self.viewer.warning = ""

        return False

    def print_unknown_command(self, arguments):
        """(Put description here)."""
        self.viewer.warning = "command unknown"

        return False

    def return_no_argument(self):
        """(Put description here)."""
        return []
