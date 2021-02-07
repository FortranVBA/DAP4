"""Project OC DAP 4 file with tournament related class."""

from app.config import CommandField


class EditTurnController:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        self.selected_turn = ""

    @staticmethod
    def get_command(tournament, viewer):
        """(Put description here)."""
        command = input("Enter your command: ")

        command_unknown = True
        if command == CommandField.exit_c:
            return True

        elif command == CommandField.back_c:
            viewer.current_view = CommandField.turns_c
            viewer.current_error = ""

        number = 1
        for match in tournament.turns[viewer.selected_turn].matches:
            if command == str(number) + CommandField.match_result_c:
                score_player_1 = input(f"Enter score player {match.opponents[0]} : ")
                score_player_2 = input(f"Enter score player {match.opponents[1]} : ")
                match.update_result(score_player_1, score_player_2)
                command_unknown = False

            number += 1

        if command_unknown:
            viewer.current_error = "command unknown"

        return False
