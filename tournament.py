"""Project OC DAP 4 file with tournament related class."""


class Tournament:
    """Tournament characteristics to be handled by application."""

    def __init__(self):
        """Init Tournament class."""
        self.name = "Unknown"
        self.location = "Unknown"
        self.date = "Unknown"
        self.turn_number = 4
        self.round = []
        self.players = []
        self.time_control = ""
        self.description = ""

    def create_tournament(self):
        """(Put description here)."""
        pass

    def add_player(self):
        """(Put description here)."""
        pass

    def generate_couples(self):
        """(Put description here)."""
        pass

    def update_match_results(self):
        """(Put description here)."""
        pass


class Player:
    """Player characteristics to be handled by application."""

    def __init__(self):
        """Init Player class."""
        self.name = "Unknown"
        self.surname = "Unknown"
        self.birth_date = ""
        self.sex = ""
        self.ranking = 99


class Match:
    """Player characteristics to be handled by application."""

    def __init__(self):
        """Init Match class."""
        self.opponents = []
        self.result = []

    def update_result(self):
        """(Put description here)."""
        pass


class MainController:
    """Main controller to be handled by application."""

    def __init__(self):
        """Init MainController class."""
        self.viewer = MainViewer()

    def run(self):
        """(Put description here)."""
        pass


class MainViewer:
    """Main viewer to be handled by application."""

    def __init__(self):
        """Init MainViewer class."""
        pass
