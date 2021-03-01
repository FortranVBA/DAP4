"""Project OC DAP 4 file with the match class."""


class Match:
    """Project match class."""

    def __init__(self, opponents, result):
        """Init Match class."""
        self.opponents = tuple(opponents)
        self.result = tuple(result)

    def update_result(self, score_p1, score_p2):
        """Update match result."""
        self.result = (score_p1, score_p2)
