"""Project OC DAP 4 file with tournament related class."""

from app.controllers.commands import PrintUnknownCommand
from app.controllers.commands import GotoRankingMenu
from app.controllers.commands import GotoTurnsMenu
from app.controllers.commands import GotoTournamentsMenu
from app.controllers.commands import EditTournamentLocation
from app.controllers.commands import EditTournamentDate
from app.controllers.commands import EditTournamentTurnNumber
from app.controllers.commands import EditTournamentTimeControl
from app.controllers.commands import EditTournamentDescription

from app.views.edit_tournament import EditTournamentViewer

from app.config import CommandField

from app.models.tournament import Tournament


class EditTournamentController:
    """Project application class."""

    def __init__(self, tournament, is_new):
        """Init Application class."""
        self._app = None

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

        self.command_names = {
            CommandField.EXIT: self.exit_application,
            CommandField.BACK: self.goto_tournaments_menu,
            CommandField.TURNS: self.goto_turns_menu,
            CommandField.UNKNOWN: self.print_unknown_command,
            CommandField.RANKING: self.goto_ranking_menu,
            CommandField.TOURNAMENT_LOCATION: self.edit_tournament_location,
            CommandField.TOURNAMENT_DATE: self.edit_tournament_date,
            CommandField.TOURNAMENT_TURN_NUMBER: self.edit_tournament_turns_number,
            CommandField.TOURNAMENT_TIME: self.edit_tournament_time_control,
            CommandField.TOURNAMENT_DESCRIPTION: self.edit_tournament_description,
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

    def edit_tournament_location(self):
        """(Put description here)."""
        return EditTournamentLocation(self.tournament).exe_command()

    def edit_tournament_date(self):
        """(Put description here)."""
        return EditTournamentDate(self.tournament).exe_command()

    def edit_tournament_turns_number(self):
        """(Put description here)."""
        return EditTournamentTurnNumber(self.tournament).exe_command()

    def edit_tournament_time_control(self):
        """(Put description here)."""
        return EditTournamentTimeControl(self.tournament).exe_command()

    def edit_tournament_description(self):
        """(Put description here)."""
        return EditTournamentDescription(self.tournament).exe_command()
