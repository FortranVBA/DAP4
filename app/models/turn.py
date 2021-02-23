"""Project OC DAP 4 file with tournament related class."""

from app.models.match import Match


class Turn:
    """Player characteristics to be handled by application."""

    def __init__(self, name, matches_input, matches_result):
        """Init Match class."""
        from datetime import datetime

        self.name = name
        self.matches = []
        self.time_begin = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        self.time_end = ""

        for match, result in zip(matches_input, matches_result):
            self.matches.append(Match(match, result))

    def return_serialized_turn(self):
        """(Put description here)."""
        matches_input = []
        matches_result = []
        for match in self.matches:
            matches_input.append(match.opponents)
            matches_result.append(match.result)

        return {
            "name": self.name,
            "matches_input": matches_input,
            "matches_result": matches_result,
            "time_begin": self.time_begin,
            "time_end": self.time_end,
        }

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
