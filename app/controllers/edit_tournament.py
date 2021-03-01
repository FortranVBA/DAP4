"""Project OC DAP 4 file with tournament related class."""

from app.commands.application import PrintUnknownCommand
from app.commands.navigation import GotoRankingMenu
from app.commands.navigation import GotoTurnsMenu
from app.commands.tournament import EditTournamentLocation
from app.commands.tournament import EditTournamentDate
from app.commands.tournament import EditTournamentTurnNumber
from app.commands.tournament import EditTournamentTimeControl
from app.commands.tournament import EditTournamentDescription
from app.commands.application import ExitApplication
from app.commands.navigation import GoBackMenu

from app.views.edit_tournament import EditTournamentViewer

from app.models.tournament import Tournament


class EditTournamentController:
    """Project application class."""

    def __init__(self, tournament, is_new):
        """Init Application class."""
        self._app = None
        self.viewer = EditTournamentViewer()

        if is_new:
            already_exists = True
            while already_exists:
                name_new = input("Enter your tournament name : ")
                if name_new in Tournament.get_all:
                    print("This name is already taken, please enter another one.")
                else:
                    already_exists = False

            self.tournament = Tournament(name_new)
        else:
            self.tournament = tournament

        self.command_names = []

    def display(self):
        """(Put description here)."""
        self.viewer.display(self.tournament)

    def get_command(self):
        """(Put description here)."""
        command_input = input("Enter your command: ")

        self.command_names = [
            PrintUnknownCommand(self.viewer),
            ExitApplication(),
            GoBackMenu(self._app, self.viewer, "tournaments", None),
            GotoTurnsMenu(self._app, self.viewer, self.tournament),
            GotoRankingMenu(self._app, self.viewer, self.tournament),
            EditTournamentLocation(self.tournament),
            EditTournamentDate(self.tournament),
            EditTournamentTurnNumber(self.tournament),
            EditTournamentTimeControl(self.tournament),
            EditTournamentDescription(self.tournament),
        ]

        for command in self.command_names:
            if command.is_valid(command_input):
                self.command = command
