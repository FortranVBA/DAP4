"""Project OC DAP 4 file with tournament related class."""

from app.views.edit_turn import EditTurnViewer

from app.config import CommandField
from app.config import ViewName

# from app.models.turn import Turn


class EditTurnController:
    """Project application class."""

    def __init__(self, tournament, turn, is_new):
        """Init Application class."""
        self.current_view = ViewName.EDIT_TURN
        self.tournament = tournament

        if is_new:
            name_new = input("Enter turn name : ")
            self.tournament.get_next_turn(name_new)
            self.turn = self.tournament.turns[name_new]
        else:
            self.turn = turn

        self.command_names = {
            CommandField.EXIT: self.exit_application,
            CommandField.BACK: self.goto_turns_menu,
            CommandField.MATCH_RESULT: self.enter_score,
            CommandField.UNKNOWN: self.print_unknown_command,
        }

        self.viewer = EditTurnViewer()

    def display(self):
        """(Put description here)."""
        self.viewer.display(self.tournament, self.turn)

    def exe_command(self, command):
        """(Put description here)."""
        if command in self.command_names:
            return self.command_names[command]()
        else:
            number = 1
            for match in self.turn.matches:
                if command == str(number) + CommandField.MATCH_RESULT:
                    return self.command_names[CommandField.MATCH_RESULT](match)
                number += 1

            return self.command_names[CommandField.UNKNOWN]()

    def exit_application(self):
        """(Put description here)."""
        return True

    def print_unknown_command(self):
        """(Put description here)."""
        self.viewer.warning = "command unknown"

        return False

    def goto_turns_menu(self):
        """(Put description here)."""
        self.current_view = ViewName.TURNS

        self.viewer.warning = ""

        return False

    def enter_score(self, match):
        """(Put description here)."""
        score_player_1 = input(f"Enter score player {match.opponents[0]} : ")
        score_player_2 = input(f"Enter score player {match.opponents[1]} : ")
        match.update_result(score_player_1, score_player_2)

        return False
