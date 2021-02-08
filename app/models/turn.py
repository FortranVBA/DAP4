"""Project OC DAP 4 file with tournament related class."""

from app.models.match import Match


class Turn:
    """Player characteristics to be handled by application."""

    def __init__(self, name, matches_input):
        """Init Match class."""
        self.name = name
        self.matches = []
        self.time_begin = ""
        self.time_end = ""

        for match in matches_input:
            self.matches.append(Match(match))

    def get_matches_description(self):
        """(Put description here)."""
        description = []
        for match in self.matches:
            description.append(match.opponents)

        return description

    def get_matches_results(self):
        """(Put description here)."""
        results = []
        for match in self.matches:
            results.append(match.result)

        return results
