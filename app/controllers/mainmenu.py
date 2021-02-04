"""Project OC DAP 4 file with tournament related class."""

from app.models.tournament import Tournament

from app.config import CommandField


class MainMenuController:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        pass

    @staticmethod
    def get_command(tournament_list, viewer):
        """(Put description here)."""
        command = input("Enter your command: ")

        if command == CommandField.exit_c:
            return True
        elif command == CommandField.new_c:
            name_new = input("Enter your tournament name : ")
            tournament_list[name_new] = Tournament(name_new)

            viewer.selected_tournament = name_new
            viewer.current_view = CommandField.edit_c
            viewer.current_error = ""
        elif command == CommandField.tournaments_c:
            viewer.current_view = CommandField.tournaments_c
            viewer.current_error = ""
        elif command == CommandField.print_c:
            viewer.current_view = CommandField.print_c
            viewer.current_error = ""
        else:
            viewer.current_error = "command unknown"

        return False
