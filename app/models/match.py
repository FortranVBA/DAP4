"""Project OC DAP 4 file with tournament related class."""


class Match:
    """Player characteristics to be handled by application."""

    def __init__(self, opponents, result):
        """Init Match class."""
        self.opponents = tuple(opponents)
        self.result = tuple(result)

    def update_result(self, score_p1, score_p2):
        """(Put description here)."""
        self.result = (score_p1, score_p2)
