"""Project OC DAP 4 file with tournament related class."""

from app.controllers.commands import PrintUnknownCommand
from app.controllers.commands import GeneratePlayers
from app.controllers.commands import AddPlayer
from app.controllers.commands import GotoEditPlayer
from app.controllers.commands import ListPlayersAlphabeticalCommand
from app.controllers.commands import ListPlayersRankingCommand
from app.controllers.commands import ExitApplication
from app.controllers.commands import GoBackMenu

from app.views.tournament_ranking import TournamentRankingViewer


class TournamentRankingController:
    """Project application class."""

    def __init__(self, tournament):
        """Init Application class."""
        self._app = None

        self.tournament = tournament

        self.command_names = []

        self.viewer = TournamentRankingViewer()

    def get_command(self):
        """(Put description here)."""
        command_input = input("Enter your command: ")

        self.update_commands()

        for command in self.command_names:
            if command.is_valid(command_input):
                self.command = command

    def display(self):
        """(Put description here)."""
        self.viewer.display(self.tournament)

    def update_commands(self):
        """(Put description here)."""
        self.command_names = [
            PrintUnknownCommand(self.viewer),
            ExitApplication(),
            GoBackMenu(self._app, self.viewer, "edit_tournament", self.tournament),
            GotoEditPlayer(self._app, self.viewer, self.tournament),
            ListPlayersAlphabeticalCommand(self.viewer),
            ListPlayersRankingCommand(self.viewer),
            AddPlayer(self._app, self.viewer, self.tournament),
            GeneratePlayers(self._app, self.viewer, self.tournament),
        ]

        if len(self.tournament.turns) > 0:
            del self.command_names[-2]
