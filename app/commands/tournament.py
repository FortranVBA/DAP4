"""Project OC DAP 4 file with the tournament commands."""

from app.config import CommandField


class CreateNextTurn:
    """Project create_next_turn command class."""

    def __init__(self, _app, viewer, tournament):
        """Init create_next_turn command class."""
        self._app = _app
        self.viewer = viewer
        self.tournament = tournament

    def exe_command(self):
        """Execute command and return False to not exit application."""
        from app.controllers.edit_turn import EditTurnController

        for turn in self.tournament.turns.values():
            for result in turn.get_matches_results():
                if len(result) == 0:
                    self.viewer.warning = "results missing"

                    return False

        self._app.change_controller(EditTurnController(self.tournament, None, True))

        self.viewer.warning = ""

        return False

    def is_valid(self, command_name):
        """Return if user input matches the command name from config file."""
        if command_name == CommandField.CREATE_NEXT_TURN:
            return True
        else:
            return False


class CreateTournament:
    """Project create_tournament command class."""

    def __init__(self, _app, viewer):
        """Init create_tournament command class."""
        self._app = _app
        self.viewer = viewer

    def exe_command(self):
        """Execute command and return False to not exit application."""
        from app.controllers.edit_tournament import EditTournamentController

        self._app.change_controller(EditTournamentController(None, True))
        self.viewer.warning = ""
        return False

    def is_valid(self, command_name):
        """Return if user input matches the command name from config file."""
        if command_name == CommandField.NEW:
            return True
        else:
            return False


class EditTournamentDate:
    """Project edit_tournament_date command class."""

    def __init__(self, tournament):
        """Init edit_tournament_date command class."""
        self.tournament = tournament

    def exe_command(self):
        """Execute command and return False to not exit application."""
        new_date = input(
            "Enter tournament date (format dd/mm/yyyy separated by blank space): "
        )
        while not self.is_date_format_correct(new_date):
            print("Only authorized format is dd/mm/yyyy separated by blank space")
            new_date = input(
                "Enter tournament date (format dd/mm/yyyy separated by blank space): "
            )

        self.tournament.date = new_date

        return False

    def is_date_format_correct(self, input_string):
        """Return if a string follow the correct date format xx/xx/xxxx."""
        import re

        date_format = re.compile(".{2}/.{2}/.{4}")
        for date in input_string.split():
            if not date_format.match(date):
                return False

        return True

    def is_valid(self, command_name):
        """Return if user input matches the command name from config file."""
        if command_name == CommandField.TOURNAMENT_DATE:
            return True
        else:
            return False


class EditTournamentDescription:
    """Project edit_tournament_description command class."""

    def __init__(self, tournament):
        """Init edit_tournament_description class."""
        self.tournament = tournament

    def exe_command(self):
        """Execute command and return False to not exit application."""
        new_description = input("Enter tournament description : ")
        self.tournament.description = new_description

        return False

    def is_valid(self, command_name):
        """Return if user input matches the command name from config file."""
        if command_name == CommandField.TOURNAMENT_DESCRIPTION:
            return True
        else:
            return False


class EditTournamentLocation:
    """Project edit_tournament_location command class."""

    def __init__(self, tournament):
        """Init edit_tournament_location command class."""
        self.tournament = tournament

    def exe_command(self):
        """Execute command and return False to not exit application."""
        new_location = input("Enter tournament location : ")
        self.tournament.location = new_location

        return False

    def is_valid(self, command_name):
        """Return if user input matches the command name from config file."""
        if command_name == CommandField.TOURNAMENT_LOCATION:
            return True
        else:
            return False


class EditTournamentTimeControl:
    """Project edit_tournament_time_control command class."""

    def __init__(self, tournament):
        """Init edit_tournament_time_control command class."""
        self.tournament = tournament

    def exe_command(self):
        """Execute command and return False to not exit application."""
        new_time_control = input(
            "Enter tournament time control (bullet, blitz or rapide): "
        )
        while new_time_control not in ["bullet", "blitz", "rapide", ""]:
            print("Only authorized values are 'bullet', 'blitz', 'rapide'")
            print("or leave it blank.")
            new_time_control = input(
                "Enter tournament time control (bullet, blitz or rapide): "
            )

        self.tournament.time_control = new_time_control

        return False

    def is_valid(self, command_name):
        """Return if user input matches the command name from config file."""
        if command_name == CommandField.TOURNAMENT_TIME:
            return True
        else:
            return False


class EditTournamentTurnNumber:
    """Project edit_tournament_turn_number command class."""

    def __init__(self, tournament):
        """Init edit_tournament_turn_number command class."""
        self.tournament = tournament

    def exe_command(self):
        """Execute command and return False to not exit application."""
        new_turn_number = input("Enter number of tournament turns : ")
        while not self.is_string_positive_integer(new_turn_number):
            print("Only authorized values are positive integers.")
            new_turn_number = input("Enter number of tournament turns : ")

        self.tournament.turn_number = new_turn_number

        return False

    def is_string_positive_integer(self, input_string):
        """Return if a string is a positive integer."""
        try:
            int(input_string)
            if int(input_string) > 0:
                return True
            else:
                return False
        except ValueError:
            return False

    def is_valid(self, command_name):
        """Return if user input matches the command name from config file."""
        if command_name == CommandField.TOURNAMENT_TURN_NUMBER:
            return True
        else:
            return False


class EnterScore:
    """Project enter_score command class."""

    def __init__(self, turn):
        """Init enter_score command class."""
        self.match = None
        self.turn = turn

    def exe_command(self):
        """Execute command and return False to not exit application."""
        self.input_new_score()
        self.complete_end_turn()

        return False

    def input_new_score(self):
        """Ask for score input and update match results."""
        score_player_1 = input(f"Enter score player {self.match.opponents[0]} : ")
        value_incorrect = True
        while value_incorrect:
            if score_player_1 in ["0", "0.5", "1"]:
                value_incorrect = False
            else:
                print("Incorrect value (put 0 / 0.5 or 1)")
                score_player_1 = input(
                    f"Enter score player {self.match.opponents[0]} : "
                )

        score_player_2 = input(f"Enter score player {self.match.opponents[1]} : ")
        value_incorrect = True
        while value_incorrect:
            if score_player_2 in ["0", "0.5", "1"]:
                value_incorrect = False
            else:
                print("Incorrect value (put 0 / 0.5 or 1)")
                score_player_2 = input(
                    f"Enter score player {self.match.opponents[1]} : "
                )

        self.match.update_result(score_player_1, score_player_2)

    def complete_end_turn(self):
        """Complete the end turn timedate if all matches have been played."""
        for result in self.turn.get_matches_results():
            if len(result) == 0:
                return False

        from datetime import datetime

        self.turn.time_end = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    def is_valid(self, command_name):
        """Return if user input matches the command name from config file."""
        number = 1
        for match in self.turn.matches:
            if len(match.opponents) == 2:
                if command_name == str(number) + CommandField.MATCH_RESULT:
                    self.match = match
                    return True
                number += 1

        return False


class ListMatchesCommand:
    """Project list_matches command class."""

    def __init__(self, viewer):
        """Init list_matches command class."""
        self.viewer = viewer

    def exe_command(self):
        """Execute command and return False to not exit application."""
        self.viewer.warning = "matches"
        return False

    def is_valid(self, command_name):
        """Return if user input matches the command name from config file."""
        if command_name == CommandField.MATCHES:
            return True
        else:
            return False


class LoadTournamentDatabase:
    """Project load_tournament_database command class."""

    def __init__(self, viewer):
        """Init load_tournament_database command class."""
        self.viewer = viewer

    def exe_command(self):
        """Execute command and return False to not exit application."""
        from app.models.tournament import Tournament

        Tournament.load_fromtinyDB()
        self.viewer.warning = ""
        return False

    def is_valid(self, command_name):
        """Return if user input matches the command name from config file."""
        if command_name == CommandField.LOAD_TOURNAMENTS:
            return True
        else:
            return False


class SaveTournamentDatabase:
    """Project save_tournament_database command class."""

    def __init__(self, viewer):
        """Init save_tournament_database command class."""
        self.viewer = viewer

    def exe_command(self):
        """Execute command and return False to not exit application."""
        from app.models.tournament import Tournament

        Tournament.save_tinyDB()
        self.viewer.warning = ""
        return False

    def is_valid(self, command_name):
        """Return if user input matches the command name from config file."""
        if command_name == CommandField.SAVE_TOURNAMENTS:
            return True
        else:
            return False
