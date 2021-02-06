"""Project OC DAP 4 file with tournament related class."""

from app.views.mainmenu import MainMenuViewer
from app.views.errors import Errors


from app.models.tournament import Tournament


from app.config import CommandField


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

    def display(self):
        """(Put description here)."""
        Errors.display(self.viewer.current_error)
        MainMenuViewer.display()

    def get_arguments(self):
        """(Put description here)."""
        return

    def get_command(self, tournament_list, viewer):
        """(Put description here)."""
        command = input("Enter your command: ")

        if command in self.command_names.keys:
            return self.command_names[command]()
        else:
            return self.command_names[CommandField.unknown_c]()

    def exit_application(self):
        return True

    def goto_create_menu(self):
        name_new = input("Enter your tournament name : ")
        tournament_list[name_new] = Tournament(name_new)

        viewer.selected_tournament = name_new
        viewer.current_view = CommandField.edit_tournament_c
        viewer.current_error = ""

        return False

    def goto_tournaments_menu(self):
        viewer.current_view = CommandField.tournaments_c
        viewer.current_error = ""

    def goto_print_menu(self):
        viewer.current_view = CommandField.print_c
        viewer.current_error = ""

    def print_unknown_command(self):
        viewer.current_error = "command unknown"
