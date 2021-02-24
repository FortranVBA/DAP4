"""Project OC DAP 4 file with tournament related class."""

from app.controllers.commands import PrintUnknownCommand
from app.controllers.commands import GotoEditTournament
from app.controllers.commands import GeneratePlayers
from app.controllers.commands import AddPlayer
from app.controllers.commands import GotoEditPlayer
from app.controllers.commands import ListPlayersAlphabeticalCommand
from app.controllers.commands import ListPlayersRankingCommand

from app.views.tournament_ranking import TournamentRankingViewer

from app.models.player import Player

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
            CommandField.EDIT_PLAYER: self.goto_edit_player_menu,
            CommandField.BACK: self.goto_edit_tournament_menu,
            CommandField.UNKNOWN: self.print_unknown_command,
            CommandField.PLAYERS_ALPHABETIC: self.list_alphabetical,
            CommandField.PLAYERS_RANKING: self.list_ranking,
        }

        self.viewer = TournamentRankingViewer()

    def display(self):
        """(Put description here)."""
        self.viewer.display(self.tournament)

    def exe_command(self, command):
        """(Put description here)."""
        self.update_commands()
        if command in self.command_names:
            return self.command_names[command]()
        else:
            number = 1
            for player_name, score in self.tournament.get_player_scores().items():
                if command == str(number) + CommandField.EDIT_PLAYER:
                    player = Player.get_all[player_name]
                    return self.command_names[CommandField.EDIT_PLAYER](player)
                number += 1

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

    def goto_edit_player_menu(self, player):
        """(Put description here)."""
        return GotoEditPlayer(
            self._app, self.viewer, player, self.tournament
        ).exe_command()

    def list_alphabetical(self):
        """(Put description here)."""
        return ListPlayersAlphabeticalCommand(self.viewer).exe_command()

    def list_ranking(self):
        """(Put description here)."""
        return ListPlayersRankingCommand(self.viewer).exe_command()

    def update_commands(self):
        """(Put description here)."""
        if len(self.tournament.turns) == 0:
            self.command_names[CommandField.ADD_PLAYER] = self.add_player
            self.command_names[CommandField.GENERATE_PLAYERS] = self.generate_player
        else:
            self.command_names[CommandField.ADD_PLAYER] = self.print_unknown_command
            self.command_names[
                CommandField.GENERATE_PLAYERS
            ] = self.print_unknown_command
