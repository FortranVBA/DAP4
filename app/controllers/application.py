"""Project OC DAP 4 file with tournament related class."""

from app.controllers.edit_tournament import EditTournamentController
from app.controllers.mainmenu import MainMenuController
from app.controllers.print import PrintMenuController
from app.controllers.tournaments import TournamentMenuController
from app.controllers.turns import TurnsController

from app.views.edit_tournament import EditTournamentViewer
from app.views.errors import Errors
from app.views.mainmenu import MainMenuViewer
from app.views.print import PrintMenuViewer
from app.views.tournaments import TournamentMenuViewer
from app.views.turns import TurnsViewer
from app.views.viewer import Viewer

from app.config import CommandField

import os


class Application:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        self.player_list = {}
        self.tournament_list = {}
        self.viewer = Viewer()
        self.exit = False

    def run(self):
        """Run  Application class."""
        while not self.exit:
            self.exit = self.get_command()
            os.system("cls")
        return

    def get_command(self):
        """(Put description here)."""
        if self.viewer.current_view == CommandField.main_c:
            Errors.display(self.viewer.current_error)
            MainMenuViewer.display()
            return MainMenuController.get_command(self.tournament_list, self.viewer)

        elif self.viewer.current_view == CommandField.tournaments_c:
            Errors.display(self.viewer.current_error)
            TournamentMenuViewer.display(self.tournament_list)
            return TournamentMenuController.get_command(self.viewer)

        elif self.viewer.current_view == CommandField.print_c:
            Errors.display(self.viewer.current_error)
            PrintMenuViewer.display()
            return PrintMenuController.get_command(self.viewer)

        elif self.viewer.current_view == CommandField.edit_c:
            Errors.display(self.viewer.current_error)
            EditTournamentViewer.display(
                self.tournament_list[self.viewer.selected_tournament], self.player_list
            )
            return EditTournamentController.get_command(
                self.tournament_list, self.player_list, self.viewer
            )

        elif self.viewer.current_view == CommandField.edit_turns:
            Errors.display(self.viewer.current_error)
            TurnsViewer.display(self.tournament_list[self.viewer.selected_tournament])
            return TurnsController.get_command(
                self.tournament_list[self.viewer.selected_tournament],
                self.player_list,
                self.viewer,
            )

        return False


" sty -> coloration de la console"
