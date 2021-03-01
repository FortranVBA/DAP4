"""Project OC DAP 4 file with tournament related class."""

from app.config import CommandField


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
                    self.player = Player.get_all[player_name]
                    return True
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
