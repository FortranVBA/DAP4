"""Project OC DAP 4 file with tournament related class."""

from app.controllers.commands import PrintUnknownCommand
from app.controllers.commands import GotoEditTournament
from app.controllers.commands import GeneratePlayers
from app.controllers.commands import AddPlayer

from app.views.tournament_ranking import TournamentRankingViewer

from app.config import CommandField


class TournamentRankingController:
    """Project application class."""

    def __init__(self, tournament):
        """Init Application class."""
        self._app = None

        self.tournament = tournament

        self.command_names = {
            CommandField.EXIT: self.exit_application,
            CommandField.ADD_PLAYER: self.add_player,
            CommandField.GENERATE_PLAYERS: self.generate_player,
            CommandField.BACK: self.goto_edit_tournament_menu,
            CommandField.UNKNOWN: self.print_unknown_command,
        }

        self.viewer = TournamentRankingViewer()

    def display(self):
        """(Put description here)."""
        self.viewer.display(self.tournament)

    def exe_command(self, command):
        """(Put description here)."""
        if command in self.command_names:
            return self.command_names[command]()
        else:
            return self.command_names[CommandField.UNKNOWN]()

    def exit_application(self):
        """(Put description here)."""
        return True

    def add_player(self):
        """(Put description here)."""
        return AddPlayer(self._app, self.viewer, self.tournament).exe_command()

    def generate_player(self):
        """(Put description here)."""
        return GeneratePlayers(self._app, self.viewer, self.tournament).exe_command()

    def print_unknown_command(self):
        """(Put description here)."""
        return PrintUnknownCommand(self.viewer).exe_command()

    def goto_edit_tournament_menu(self):
        """(Put description here)."""
        return GotoEditTournament(self._app, self.viewer, self.tournament).exe_command()
