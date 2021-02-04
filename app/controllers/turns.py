"""Project OC DAP 4 file with tournament related class."""

from app.config import CommandField


class TurnsController:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        pass

    @staticmethod
    def get_command(tournament, player_list, viewer):
        """(Put description here)."""
        command = input("Enter your command: ")

        command_unknown = True
        if command == CommandField.exit_c:
            return True
        elif command == CommandField.back_c:
            viewer.current_view = CommandField.main_c
            viewer.current_error = ""

        number = 1
        for turn in tournament.turns:
            if command == str(number) + CommandField.edit_c:
                command_unknown = False

            number += 1

        if command_unknown:
            viewer.current_error = "command unknown"

        return False
