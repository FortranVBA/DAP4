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

        name_new = input("Enter player name : ")
        surname_new = input("Enter player surname : ")
        birthday_new = input("Enter player birth date : ")
        sex_new = input("Enter player sex : ")
        ranking_new = input("Enter player ranking : ")

        new_player = Player(
            name_new, surname_new, birthday_new, sex_new, int(ranking_new)
        )
        self.tournament.players_index.append(new_player.player_index)

        self.viewer.warning = ""

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


class EnterScore:
    """Project application class."""

    def __init__(self, match):
        """Init Application class."""
        self.match = match

    def exe_command(self):
        """(Put description here)."""
        score_player_1 = input(f"Enter score player {self.match.opponents[0]} : ")
        score_player_2 = input(f"Enter score player {self.match.opponents[1]} : ")
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
