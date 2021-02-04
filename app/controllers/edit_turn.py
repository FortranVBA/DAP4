"""Project OC DAP 4 file with tournament related class."""

from app.config import CommandField


class EditTurnController:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        pass

    @staticmethod
    def get_command(viewer):
        """(Put description here)."""
        command = input("Enter your command: ")

        if command == CommandField.exit_c:
            return True

        elif command == CommandField.back_c:
            viewer.current_view = CommandField.turns_c
            viewer.current_error = ""

        else:
            viewer.current_error = "command unknown"

        return False
