"""Project OC DAP 4 file with the tournament_ranking controller."""

from app.commands.application import PrintUnknownCommand
from app.commands.player import GeneratePlayers
from app.commands.player import AddPlayer
from app.commands.navigation import GotoEditPlayer
from app.commands.player import ListPlayersAlphabeticalCommand
from app.commands.player import ListPlayersRankingCommand
from app.commands.application import ExitApplication
from app.commands.navigation import GoBackMenu

from app.views.tournament_ranking import TournamentRankingViewer


class TournamentRankingController:
    """Project tournament_ranking controller class."""

    def __init__(self, tournament):
        """Init tournament_ranking controller class."""
        self._app = None

        self.tournament = tournament

        self.command_names = []

        self.viewer = TournamentRankingViewer()

    def display(self):
        """Display the controller view."""
        self.viewer.display(self.tournament)

    def get_command(self):
        """Get the user input and convert it to a command instance."""
        command_input = input("Enter your command: ")

        self.update_commands()

        for command in self.command_names:
            if command.is_valid(command_input):
                self.command = command

    def update_commands(self):
        """Delete the player creation commands if the tournament already started."""
        # The 1st command in list must always be the PrintUnknownCommand, which is used
        # as default command.
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
