"""Project OC DAP 4 file with tournament related class."""

from app.controllers.edit_tournament import EditTournamentController
from app.controllers.edit_turn import EditTurnController
from app.controllers.mainmenu import MainMenuController
from app.controllers.print import PrintMenuController
from app.controllers.tournaments import TournamentMenuController
from app.controllers.turns import TurnsController

from app.views.edit_tournament import EditTournamentViewer
from app.views.edit_turn import EditTurnViewer

from app.views.print import PrintMenuViewer
from app.views.tournaments import TournamentMenuViewer
from app.views.turns import TurnsViewer

from app.config import CommandField
from app.config import ViewName

import os


class Controller:
    """Project application class."""

    def __init__(self, player_list, tournament_list):
        """Init Application class."""
        self.current_view = CommandField.main_c
        self.commands_controllers = {}

        self.commands_controllers[ViewName.view_main] = MainMenuController()

        self.current_error = ""
        self.selected_tournament = ""
        self.selected_turn = 0

    def display(self):
        """(Put description here)."""
        self.commands_controllers[self.current_view].display()

    def clear_screen(self):
        """(Put description here)."""
        os.system("cls")

    def get_command(self):
        """(Put description here)."""
        self.commands_controllers[self.current_view].get_command()

        if self.viewer.current_view == CommandField.main_c:
            return MainMenuController.get_command(self.tournament_list, self.viewer)

        elif self.viewer.current_view == CommandField.tournaments_c:
            Errors.display(self.viewer.current_error)
            TournamentMenuViewer.display(self.tournament_list)
            return TournamentMenuController.get_command(self.viewer)

        elif self.viewer.current_view == CommandField.print_c:
            Errors.display(self.viewer.current_error)
            PrintMenuViewer.display()
            return PrintMenuController.get_command(self.viewer)

        elif self.viewer.current_view == CommandField.edit_tournament_c:
            Errors.display(self.viewer.current_error)
            EditTournamentViewer.display(
                self.tournament_list[self.viewer.selected_tournament], self.player_list
            )
            return EditTournamentController.get_command(
                self.tournament_list, self.player_list, self.viewer
            )

        elif self.viewer.current_view == CommandField.turns_c:
            Errors.display(self.viewer.current_error)
            TurnsViewer.display(self.tournament_list[self.viewer.selected_tournament])
            return TurnsController.get_command(
                self.tournament_list[self.viewer.selected_tournament],
                self.player_list,
                self.viewer,
            )

        elif self.viewer.current_view == CommandField.edit_turn_c:
            Errors.display(self.viewer.current_error)
            EditTurnViewer.display(
                self.tournament_list[self.viewer.selected_tournament],
                self.viewer.selected_turn,
                self.player_list,
            )
            return EditTurnController.get_command(
                self.tournament_list[self.viewer.selected_tournament], self.viewer
            )

        return False
