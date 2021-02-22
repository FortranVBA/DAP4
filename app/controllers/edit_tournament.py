"""Project OC DAP 4 file with tournament related class."""

from app.controllers.commands import PrintUnknownCommand
from app.controllers.commands import GotoRankingMenu
from app.controllers.commands import GotoTurnsMenu
from app.controllers.commands import GotoTournamentsMenu

from app.views.edit_tournament import EditTournamentViewer

from app.config import CommandField

from app.models.tournament import Tournament


class EditTournamentController:
    """Project application class."""

    def __init__(self, tournament, is_new):
        """Init Application class."""
        self._app = None

        if is_new:
            name_new = input("Enter your tournament name : ")
            self.tournament = Tournament(name_new)
        else:
            self.tournament = tournament

        self.command_names = {
            CommandField.EXIT: self.exit_application,
            CommandField.BACK: self.goto_tournaments_menu,
            CommandField.TURNS: self.goto_turns_menu,
            CommandField.UNKNOWN: self.print_unknown_command,
            CommandField.RANKING: self.goto_ranking_menu,
        }

        self.viewer = EditTournamentViewer()

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

    def goto_tournaments_menu(self):
        """(Put description here)."""
        return GotoTournamentsMenu(self._app, self.viewer).exe_command()

    def goto_turns_menu(self):
        """(Put description here)."""
        return GotoTurnsMenu(self._app, self.viewer, self.tournament).exe_command()

    def goto_ranking_menu(self):
        """(Put description here)."""
        return GotoRankingMenu(self._app, self.viewer, self.tournament).exe_command()

    def print_unknown_command(self):
        """(Put description here)."""
        return PrintUnknownCommand(self.viewer).exe_command()
