"""Project OC DAP 4 file with the application commands."""

from app.config import CommandField


class ExitApplication:
    """Project exit_application command class."""

    def __init__(self):
        """Init exit_application command class."""
        pass

    def exe_command(self):
        """Return True to exit application."""
        return True

    def is_valid(self, command_name):
        """Return if user input matches the command name from config file."""
        if command_name == CommandField.EXIT:
            return True
        else:
            return False


class PrintUnknownCommand:
    """Project print_unknown command class."""

    def __init__(self, viewer):
        """Init print_unknown command class."""
        self.viewer = viewer

    def exe_command(self):
        """Execute command and return False to not exit application."""
        self.viewer.warning = "command unknown"
        return False

    def is_valid(self, command_name):
        """Return True (Command always valid and may be replaced with user input)."""
        return True
