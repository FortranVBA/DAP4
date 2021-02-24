"""Project OC DAP 4 file with tournament related class."""


class AddPlayer:
    """Project application class."""

    def __init__(self, _app, viewer, tournament):
        """Init Application class."""
        self._app = _app
        self.viewer = viewer
        self.tournament = tournament

    def exe_command(self):
        """(Put description here)."""
        from app.models.player import Player
        import re

        name_new = input("Enter player name : ")
        surname_new = input("Enter player surname : ")

        date_format = re.compile(".{2}/.{2}/.{4}")
        birthday_new = input("Enter player birth date (format dd/mm/yyyy): ")
        while not date_format.match(birthday_new):
            print("Only authorized format is dd/mm/yyyy")
            birthday_new = input("Enter player birth date (format dd/mm/yyyy): ")

        sex_new = input("Enter player sex (M or F): ")
        while sex_new not in ["M", "F"]:
            print("Only authorized values are 'M' or 'F'")
            sex_new = input("Enter player sex (M or F): ")

        ranking_new = input("Enter player ranking : ")
        while not self.is_string_positive_integer(ranking_new):
            print("Only authorized values are positive integers")
            ranking_new = input("Enter player ranking : ")

        new_player = Player(
            name_new, surname_new, birthday_new, sex_new, int(ranking_new)
        )
        self.tournament.players_index.append(new_player.player_index)

        self.viewer.warning = ""

        return False

    def is_string_positive_integer(self, input_string):
        """(Put description here)."""
        try:
            int(input_string)
            if int(input_string) > 0:
                return True
            else:
                return False
        except ValueError:
            return False


class CompleteEndTurn:
    """Project application class."""

    def __init__(self, turn):
        """Init Application class."""
        self.turn = turn

    def exe_command(self):
        """(Put description here)."""
        for result in self.turn.get_matches_results():
            if len(result) == 0:
                return False

        from datetime import datetime

        self.turn.time_end = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

        return False


class CreateNextTurn:
    """Project application class."""

    def __init__(self, _app, viewer, tournament):
        """Init Application class."""
        self._app = _app
        self.viewer = viewer
        self.tournament = tournament

    def exe_command(self):
        """(Put description here)."""
        from app.controllers.edit_turn import EditTurnController

        for turn in self.tournament.turns.values():
            for result in turn.get_matches_results():
                if len(result) == 0:
                    self.viewer.warning = "results missing"

                    return False

        self._app.change_controller(EditTurnController(self.tournament, None, True))

        self.viewer.warning = ""

        return False


class CreateTournament:
    """Project application class."""

    def __init__(self, _app, viewer):
        """Init Application class."""
        self._app = _app
        self.viewer = viewer

    def exe_command(self):
        """(Put description here)."""
        from app.controllers.edit_tournament import EditTournamentController

        self._app.change_controller(EditTournamentController(None, True))

        self.viewer.warning = ""

        return False


class EditTournamentDate:
    """Project application class."""

    def __init__(self, tournament):
        """Init Application class."""
        self.tournament = tournament

    def exe_command(self):
        """(Put description here)."""
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
        """(Put description here)."""
        import re

        date_format = re.compile(".{2}/.{2}/.{4}")
        for date in input_string.split():
            if not date_format.match(date):
                return False

        return True


class EditTournamentDescription:
    """Project application class."""

    def __init__(self, tournament):
        """Init Application class."""
        self.tournament = tournament

    def exe_command(self):
        """(Put description here)."""
        new_description = input("Enter tournament description : ")
        self.tournament.description = new_description

        return False


class EditTournamentLocation:
    """Project application class."""

    def __init__(self, tournament):
        """Init Application class."""
        self.tournament = tournament

    def exe_command(self):
        """(Put description here)."""
        new_location = input("Enter tournament location : ")
        self.tournament.location = new_location

        return False


class EditTournamentTimeControl:
    """Project application class."""

    def __init__(self, tournament):
        """Init Application class."""
        self.tournament = tournament

    def exe_command(self):
        """(Put description here)."""
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


class EditTournamentTurnNumber:
    """Project application class."""

    def __init__(self, tournament):
        """Init Application class."""
        self.tournament = tournament

    def exe_command(self):
        """(Put description here)."""
        new_turn_number = input("Enter number of tournament turns : ")
        while not self.is_string_positive_integer(new_turn_number):
            print("Only authorized values are positive integers.")
            new_turn_number = input("Enter number of tournament turns : ")

        self.tournament.turn_number = new_turn_number

        return False

    def is_string_positive_integer(self, input_string):
        """(Put description here)."""
        try:
            int(input_string)
            if int(input_string) > 0:
                return True
            else:
                return False
        except ValueError:
            return False


class EnterScore:
    """Project application class."""

    def __init__(self, match):
        """Init Application class."""
        self.match = match

    def exe_command(self):
        """(Put description here)."""
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

        return False


class GeneratePlayers:
    """Project application class."""

    def __init__(self, _app, viewer, tournament):
        """Init Application class."""
        self._app = _app
        self.viewer = viewer
        self.tournament = tournament

    def exe_command(self):
        """(Put description here)."""
        from app.models.player import Player

        for number in range(1, 9):
            new_player = Player(
                "Name" + str(number),
                "Surname" + str(number),
                "birthday_new",
                "sex_new",
                21 + 2 * number,
            )
            self.tournament.players_index.append(new_player.player_index)

        self.viewer.warning = ""

        return False


class GoBackMenu:
    """Project application class."""

    def __init__(self, _app, viewer, tournament):
        """Init Application class."""
        self._app = _app
        self.viewer = viewer
        self.tournament = tournament

    def exe_command(self):
        """(Put description here)."""
        if self.tournament:
            from app.controllers.tournament_ranking import TournamentRankingController

            self._app.change_controller(TournamentRankingController(self.tournament))

            self.viewer.warning = ""

        else:
            from app.controllers.players import PlayersController

            self._app.change_controller(PlayersController())

            self.viewer.warning = ""

        return False


class GotoEditPlayer:
    """Project application class."""

    def __init__(self, _app, viewer, player, tournament):
        """Init Application class."""
        self._app = _app
        self.viewer = viewer
        self.player = player
        self.tournament = tournament

    def exe_command(self):
        """(Put description here)."""
        from app.controllers.edit_player import EditPlayerController

        self._app.change_controller(EditPlayerController(self.player, self.tournament))

        self.viewer.warning = ""

        return False


class GotoEditTournament:
    """Project application class."""

    def __init__(self, _app, viewer, tournament):
        """Init Application class."""
        self._app = _app
        self.viewer = viewer
        self.tournament = tournament

    def exe_command(self):
        """(Put description here)."""
        from app.controllers.edit_tournament import EditTournamentController

        self._app.change_controller(EditTournamentController(self.tournament, False))

        self.viewer.warning = ""

        return False


class GotoEditTurnMenu:
    """Project application class."""

    def __init__(self, _app, viewer, tournament, turn):
        """Init Application class."""
        self._app = _app
        self.viewer = viewer
        self.tournament = tournament
        self.turn = turn

    def exe_command(self):
        """(Put description here)."""
        from app.controllers.edit_turn import EditTurnController

        self._app.change_controller(
            EditTurnController(self.tournament, self.turn, False)
        )

        self.viewer.warning = ""

        return False


class GotoMainMenu:
    """Project application class."""

    def __init__(self, _app, viewer):
        """Init Application class."""
        self._app = _app
        self.viewer = viewer

    def exe_command(self):
        """(Put description here)."""
        from app.controllers.mainmenu import MainMenuController

        self._app.change_controller(MainMenuController())

        self.viewer.warning = ""

        return False


class GotoPlayersMenu:
    """Project application class."""

    def __init__(self, _app, viewer):
        """Init Application class."""
        self._app = _app
        self.viewer = viewer

    def exe_command(self):
        """(Put description here)."""
        from app.controllers.players import PlayersController

        self._app.change_controller(PlayersController())

        self.viewer.warning = ""

        return False


class GotoRankingMenu:
    """Project application class."""

    def __init__(self, _app, viewer, tournament):
        """Init Application class."""
        self._app = _app
        self.viewer = viewer
        self.tournament = tournament

    def exe_command(self):
        """(Put description here)."""
        from app.controllers.tournament_ranking import TournamentRankingController

        self._app.change_controller(TournamentRankingController(self.tournament))

        self.viewer.warning = ""

        return False


class GotoTournamentsMenu:
    """Project application class."""

    def __init__(self, _app, viewer):
        """Init Application class."""
        self._app = _app
        self.viewer = viewer

    def exe_command(self):
        """(Put description here)."""
        from app.controllers.tournaments import TournamentMenuController

        self._app.change_controller(TournamentMenuController())

        self.viewer.warning = ""

        return False


class GotoTurnsMenu:
    """Project application class."""

    def __init__(self, _app, viewer, tournament):
        """Init Application class."""
        self._app = _app
        self.viewer = viewer
        self.tournament = tournament

    def exe_command(self):
        """(Put description here)."""
        from app.controllers.turns import TurnsController

        self._app.change_controller(TurnsController(self.tournament))

        self.viewer.warning = ""

        return False


class ListMatchesCommand:
    """Project application class."""

    def __init__(self, viewer):
        """Init Application class."""
        self.viewer = viewer

    def exe_command(self):
        """(Put description here)."""
        self.viewer.warning = "matches"

        return False


class ListPlayersAlphabeticalCommand:
    """Project application class."""

    def __init__(self, viewer):
        """Init Application class."""
        self.viewer = viewer

    def exe_command(self):
        """(Put description here)."""
        self.viewer.warning = "players alphabetical"

        return False


class ListPlayersRankingCommand:
    """Project application class."""

    def __init__(self, viewer):
        """Init Application class."""
        self.viewer = viewer

    def exe_command(self):
        """(Put description here)."""
        self.viewer.warning = "players ranking"

        return False


class LoadPlayerDatabase:
    """Project application class."""

    def __init__(self, viewer):
        """Init Application class."""
        self.viewer = viewer

    def exe_command(self):
        """(Put description here)."""
        from app.models.player import Player

        Player.load_fromtinyDB()

        self.viewer.warning = ""

        return False


class LoadTournamentDatabase:
    """Project application class."""

    def __init__(self, viewer):
        """Init Application class."""
        self.viewer = viewer

    def exe_command(self):
        """(Put description here)."""
        from app.models.tournament import Tournament

        Tournament.load_fromtinyDB()

        self.viewer.warning = ""

        return False


class PrintUnknownCommand:
    """Project application class."""

    def __init__(self, viewer):
        """Init Application class."""
        self.viewer = viewer

    def exe_command(self):
        """(Put description here)."""
        self.viewer.warning = "command unknown"

        return False


class SavePlayerDatabase:
    """Project application class."""

    def __init__(self, viewer):
        """Init Application class."""
        self.viewer = viewer

    def exe_command(self):
        """(Put description here)."""
        from app.models.player import Player

        Player.save_tinyDB()

        self.viewer.warning = ""

        return False


class SaveTournamentDatabase:
    """Project application class."""

    def __init__(self, viewer):
        """Init Application class."""
        self.viewer = viewer

    def exe_command(self):
        """(Put description here)."""
        from app.models.tournament import Tournament

        Tournament.save_tinyDB()

        self.viewer.warning = ""

        return False


class UpdatePlayerRanking:
    """Project application class."""

    def __init__(self, viewer, player):
        """Init Application class."""
        self.viewer = viewer
        self.player = player

    def exe_command(self):
        """(Put description here)."""
        ranking_new = input("Enter new player ranking : ")

        self.player.ranking = ranking_new

        self.viewer.warning = ""

        return False
