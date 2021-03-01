"""Project OC DAP 4 file with tournament related class."""

from app.config import CommandField


class ExitApplication:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        pass

    def exe_command(self):
        """(Put description here)."""
        return True

    def is_valid(self, command_name):
        """(Put description here)."""
        if command_name == CommandField.EXIT:
            return True
        else:
            return False


class PrintUnknownCommand:
    """Project application class."""

    def __init__(self, viewer):
        """Init Application class."""
        self.viewer = viewer

    def exe_command(self):
        """(Put description here)."""
        self.viewer.warning = "command unknown"
        return False

    def is_valid(self, command_name):
        """(Put description here)."""
        return True
