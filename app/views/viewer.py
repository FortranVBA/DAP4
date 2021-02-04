"""Project OC DAP 4 file with tournament related class."""

from app.config import CommandField


class Viewer:
    """Main viewer to be handled by application."""

    def __init__(self):
        """(Put description here)."""
        self.current_view = CommandField.main_c
        self.current_error = ""
        self.selected_tournament = ""
