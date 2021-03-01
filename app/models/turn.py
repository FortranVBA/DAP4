"""Project OC DAP 4 file with the turn class."""

from app.models.match import Match


class Turn:
    """Project turn class."""

    def __init__(self, name, matches_input, matches_result, time_begin, time_end):
        """Init turn class."""
        self.name = name
        self.matches = []
        self.time_begin = time_begin
        self.time_end = time_end

        for match, result in zip(matches_input, matches_result):
            self.matches.append(Match(match, result))

    def return_serialized_turn(self):
        """Return class attributes as dictionnary."""
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
        """Return the list of match descriptions (match opponents)."""
        description = []
        for match in self.matches:
            description.append(match.opponents)

        return description

    def get_matches_results(self):
        """Return the list of match results (opponent scores)."""
        results = []
        for match in self.matches:
            results.append(match.result)

        return results
