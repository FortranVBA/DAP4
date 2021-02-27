"""Project OC DAP 4 file with tournament related class."""

from app.config import CommandField


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

    def is_valid(self, command_name):
        """(Put description here)."""
        if command_name == CommandField.ADD_PLAYER:
            return True
        else:
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

    def is_valid(self, command_name):
        """(Put description here)."""
        if command_name == CommandField.CREATE_NEXT_TURN:
            return True
        else:
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

    def is_valid(self, command_name):
        """(Put description here)."""
        if command_name == CommandField.NEW:
            return True
        else:
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

    def is_valid(self, command_name):
        """(Put description here)."""
        if command_name == CommandField.TOURNAMENT_DATE:
            return True
        else:
            return False


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

    def is_valid(self, command_name):
        """(Put description here)."""
        if command_name == CommandField.TOURNAMENT_DESCRIPTION:
            return True
        else:
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

    def is_valid(self, command_name):
        """(Put description here)."""
        if command_name == CommandField.TOURNAMENT_LOCATION:
            return True
        else:
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

    def is_valid(self, command_name):
        """(Put description here)."""
        if command_name == CommandField.TOURNAMENT_TIME:
            return True
        else:
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

    def is_valid(self, command_name):
        """(Put description here)."""
        if command_name == CommandField.TOURNAMENT_TURN_NUMBER:
            return True
        else:
            return False


class EnterScore:
    """Project application class."""

    def __init__(self, turn):
        """Init Application class."""
        self.match = None
        self.turn = turn

    def exe_command(self):
        """(Put description here)."""
        self.input_new_score()
        self.complete_end_turn()

        return False

    def input_new_score(self):
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

    def complete_end_turn(self):
        """(Put description here)."""
        for result in self.turn.get_matches_results():
            if len(result) == 0:
                return False

        from datetime import datetime

        self.turn.time_end = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    def is_valid(self, command_name):
        """(Put description here)."""
        number = 1
        for match in self.turn.matches:
            if len(match.opponents) == 2:
                if command_name == str(number) + CommandField.MATCH_RESULT:
                    self.match = match
                    return True
                number += 1

        return False


class ExitApplication:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        pass

    def exe_command(self):
        """(Put description here)."""
        return True

    def is_valid(self, command_name):
        """(Put description here)."""
        if command_name == CommandField.EXIT:
            return True
        else:
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

    def is_valid(self, command_name):
        """(Put description here)."""
        if command_name == CommandField.GENERATE_PLAYERS:
            return True
        else:
            return False


class GoBackMenu:
    """Project application class."""

    def __init__(self, _app, viewer, menu_name, tournament):
        """Init Application class."""
        self._app = _app
        self.viewer = viewer
        self.menu_name = menu_name
        self.tournament = tournament

    def exe_command(self):
        """(Put description here)."""
        if self.menu_name == "main":
            return self.go_to_main_menu()
        if self.menu_name == "edit_tournament":
            return self.go_to_edit_tournament()
        if self.menu_name == "tournaments":
            return self.go_to_tournaments_menu()
        if self.menu_name == "turns":
            return self.go_to_turns_menu()
        elif self.tournament:
            return self.go_to_tournament_ranking()
        else:
            return self.go_to_players_menu()

    def go_to_main_menu(self):
        """(Put description here)."""
        from app.controllers.mainmenu import MainMenuController

        self._app.change_controller(MainMenuController())

        self.viewer.warning = ""

        return False

    def go_to_tournament_ranking(self):
        """(Put description here)."""
        from app.controllers.tournament_ranking import TournamentRankingController

        self._app.change_controller(TournamentRankingController(self.tournament))
        self.viewer.warning = ""
        return False

    def go_to_players_menu(self):
        """(Put description here)."""
        from app.controllers.players import PlayersController

        self._app.change_controller(PlayersController())
        self.viewer.warning = ""
        return False

    def go_to_tournaments_menu(self):
        """(Put description here)."""
        from app.controllers.tournaments import TournamentMenuController

        self._app.change_controller(TournamentMenuController())
        self.viewer.warning = ""
        return False

    def go_to_edit_tournament(self):
        """(Put description here)."""
        from app.controllers.edit_tournament import EditTournamentController

        self._app.change_controller(EditTournamentController(self.tournament, False))

        self.viewer.warning = ""

        return False

    def go_to_turns_menu(self):
        """(Put description here)."""
        from app.controllers.turns import TurnsController

        self._app.change_controller(TurnsController(self.tournament))

        self.viewer.warning = ""

        return False

    def is_valid(self, command_name):
        """(Put description here)."""
        if command_name == CommandField.BACK:
            return True
        else:
            return False


class GotoEditPlayer:
    """Project application class."""

    def __init__(self, _app, viewer, tournament):
        """Init Application class."""
        self._app = _app
        self.viewer = viewer
        self.player = None
        self.tournament = tournament

    def exe_command(self):
        """(Put description here)."""
        from app.controllers.edit_player import EditPlayerController

        self._app.change_controller(EditPlayerController(self.player, self.tournament))

        self.viewer.warning = ""

        return False

    def is_valid(self, command_name):
        """(Put description here)."""
        from app.models.player import Player

        if self.tournament:
            number = 1
            for player_name, score in self.tournament.get_player_scores().items():
                if command_name == str(number) + CommandField.EDIT_PLAYER:
                    player = Player.get_all[player_name]
                    return self.command_names[CommandField.EDIT_PLAYER](player)
                number += 1
        else:
            number = 1
            for player in Player.get_all.values():
                if command_name == str(number) + CommandField.EDIT_PLAYER:
                    self.player = player
                    return True
                number += 1

        return False


class GotoEditTournament:
    """Project application class."""

    def __init__(self, _app, viewer):
        """Init Application class."""
        self._app = _app
        self.viewer = viewer
        self.tournament = None

    def exe_command(self):
        """(Put description here)."""
        from app.controllers.edit_tournament import EditTournamentController

        self._app.change_controller(EditTournamentController(self.tournament, False))

        self.viewer.warning = ""

        return False

    def is_valid(self, command_name):
        """(Put description here)."""
        from app.models.tournament import Tournament

        number = 1
        for tournament in Tournament.get_all.values():
            if command_name == str(number) + CommandField.EDIT_TOURNAMENT:
                self.tournament = tournament
                return True
            number += 1
        return False


class GotoEditTurnMenu:
    """Project application class."""

    def __init__(self, _app, viewer, tournament):
        """Init Application class."""
        self._app = _app
        self.viewer = viewer
        self.tournament = tournament
        self.turn = None

    def exe_command(self):
        """(Put description here)."""
        from app.controllers.edit_turn import EditTurnController

        self._app.change_controller(
            EditTurnController(self.tournament, self.turn, False)
        )

        self.viewer.warning = ""

        return False

    def is_valid(self, command_name):
        """(Put description here)."""
        number = 1
        for turn in self.tournament.turns.values():
            if command_name == str(number) + CommandField.EDIT_TURN:
                self.turn = turn
                return True
            number += 1

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

    def is_valid(self, command_name):
        """(Put description here)."""
        if command_name == CommandField.PLAYERS:
            return True
        else:
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

    def is_valid(self, command_name):
        """(Put description here)."""
        if command_name == CommandField.RANKING:
            return True
        else:
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

    def is_valid(self, command_name):
        """(Put description here)."""
        if command_name == CommandField.TOURNAMENTS:
            return True
        else:
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

    def is_valid(self, command_name):
        """(Put description here)."""
        if command_name == CommandField.TURNS:
            return True
        else:
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

    def is_valid(self, command_name):
        """(Put description here)."""
        if command_name == CommandField.MATCHES:
            return True
        else:
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

    def is_valid(self, command_name):
        """(Put description here)."""
        if command_name == CommandField.PLAYERS_ALPHABETIC:
            return True
        else:
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

    def is_valid(self, command_name):
        """(Put description here)."""
        if command_name == CommandField.PLAYERS_RANKING:
            return True
        else:
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

    def is_valid(self, command_name):
        """(Put description here)."""
        if command_name == CommandField.LOAD_PLAYERS:
            return True
        else:
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

    def is_valid(self, command_name):
        """(Put description here)."""
        if command_name == CommandField.LOAD_TOURNAMENTS:
            return True
        else:
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

    def is_valid(self, command_name):
        """(Put description here)."""
        return True


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

    def is_valid(self, command_name):
        """(Put description here)."""
        if command_name == CommandField.SAVE_PLAYERS:
            return True
        else:
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

    def is_valid(self, command_name):
        """(Put description here)."""
        if command_name == CommandField.SAVE_TOURNAMENTS:
            return True
        else:
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

    def is_valid(self, command_name):
        """(Put description here)."""
        if command_name == CommandField.UPDATE_RANKING:
            return True
        else:
            return False
