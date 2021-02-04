"""Project OC DAP 4 file with tournament related class."""


class Errors:
    """Main viewer to be handled by application."""

    def __init__(self):
        """(Put description here)."""
        pass

    @staticmethod
    def display_error(error):
        """(Put description here)."""
        if error == "command unknown":
            return "Warning : this command is not valid"
        else:
            return "Warning : unknown error occured"

    @staticmethod
    def display(current_error):
        """(Put description here)."""
        print(" ")
        print(" ")
        if not current_error == "":
            print(Errors.display_error(current_error))
