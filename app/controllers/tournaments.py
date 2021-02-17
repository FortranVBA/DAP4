"""Project OC DAP 4 file with tournament related class."""

from app.controllers.edit_tournament import EditTournamentController

from app.views.tournaments import TournamentMenuViewer

from app.models.tournament import Tournament

from app.config import CommandField
from app.config import ViewName


class TournamentMenuController:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        self.current_view = ViewName.view_tournaments
        self.sub_controller = None

        self.command_names = {
            CommandField.new_c: self.goto_create_menu,
            CommandField.exit_c: self.exit_application,
            CommandField.back_c: self.goto_main_menu,
            CommandField.unknown_c: self.print_unknown_command,
            CommandField.edit_tournament_c: self.goto_edit_tournament_menu,
            CommandField.save_tournaments_c: self.save_database,
            CommandField.load_tournaments_c: self.load_database,
        }

        self.viewer = TournamentMenuViewer()

    def display(self):
        """(Put description here)."""
        if self.current_view == ViewName.view_tournaments:
            self.viewer.display()
        else:
            self.sub_controller.display()

    def exe_command(self, command):
        """(Put description here)."""
        if self.current_view == ViewName.view_tournaments:
            if command in self.command_names:
                return self.command_names[command]()
            else:
                number = 1
                for tournament in Tournament.get_all.values():
                    if command == str(number) + CommandField.edit_tournament_c:
                        return self.command_names[CommandField.edit_tournament_c](
                            tournament
                        )
                    number += 1

                return self.command_names[CommandField.unknown_c]()
        else:
            is_exit = self.sub_controller.exe_command(command)
            if self.sub_controller.current_view == ViewName.view_tournaments:
                self.current_view = ViewName.view_tournaments
                self.sub_controller = None
            return is_exit

    def exit_application(self):
        """(Put description here)."""
        return True

    def goto_main_menu(self):
        """(Put description here)."""
        self.current_view = ViewName.view_main

        self.viewer.warning = ""

        return False

    def print_unknown_command(self):
        """(Put description here)."""
        self.viewer.warning = "command unknown"

        return False

    def goto_create_menu(self):
        """(Put description here)."""
        self.sub_controller = EditTournamentController(None, True)

        self.current_view = ViewName.view_edit_tournament

        self.viewer.warning = ""

        return False

    def goto_edit_tournament_menu(self, tournament):
        """(Put description here)."""
        self.sub_controller = EditTournamentController(tournament, False)

        self.current_view = ViewName.view_edit_tournament

        self.viewer.warning = ""

        return False

    def save_database(self):
        """(Put description here)."""
        Tournament.save_tinyDB()

        self.viewer.warning = ""

        return False

    def load_database(self):
        """(Put description here)."""
        Tournament.load_fromtinyDB()

        self.viewer.warning = ""

        return False
