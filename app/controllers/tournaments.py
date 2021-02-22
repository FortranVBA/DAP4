"""Project OC DAP 4 file with tournament related class."""

from app.controllers.commands import LoadTournamentDatabase
from app.controllers.commands import SaveTournamentDatabase
from app.controllers.commands import GotoEditTournament
from app.controllers.commands import PrintUnknownCommand
from app.controllers.commands import CreateTournament
from app.controllers.commands import GotoMainMenu

from app.views.tournaments import TournamentMenuViewer

from app.models.tournament import Tournament

from app.config import CommandField


class TournamentMenuController:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        self._app = None

        self.command_names = {
            CommandField.NEW: self.goto_create_menu,
            CommandField.EXIT: self.exit_application,
            CommandField.BACK: self.goto_main_menu,
            CommandField.UNKNOWN: self.print_unknown_command,
            CommandField.EDIT_TOURNAMENT: self.goto_edit_tournament_menu,
            CommandField.SAVE_TOURNAMENTS: self.save_database,
            CommandField.LOAD_TOURNAMENTS: self.load_database,
        }

        self.viewer = TournamentMenuViewer()

    def display(self):
        """(Put description here)."""
        self.viewer.display()

    def exe_command(self, command):
        """(Put description here)."""
        if command in self.command_names:
            return self.command_names[command]()
        else:
            number = 1
            for tournament in Tournament.get_all.values():
                if command == str(number) + CommandField.EDIT_TOURNAMENT:
                    return self.command_names[CommandField.EDIT_TOURNAMENT](tournament)
                number += 1

            return self.command_names[CommandField.UNKNOWN]()

    def exit_application(self):
        """(Put description here)."""
        return True

    def goto_main_menu(self):
        """(Put description here)."""
        return GotoMainMenu(self._app, self.viewer).exe_command()

    def print_unknown_command(self):
        """(Put description here)."""
        return PrintUnknownCommand(self.viewer).exe_command()

    def goto_create_menu(self):
        """(Put description here)."""
        return CreateTournament(self._app, self.viewer).exe_command()

    def goto_edit_tournament_menu(self, tournament):
        """(Put description here)."""
        return GotoEditTournament(self._app, self.viewer, tournament).exe_command()

    def save_database(self):
        """(Put description here)."""
        return SaveTournamentDatabase(self.viewer).exe_command()

    def load_database(self):
        """(Put description here)."""
        return LoadTournamentDatabase(self.viewer).exe_command()
