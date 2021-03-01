"""Project OC DAP 4 file with the edit_turn controller."""

from app.commands.application import PrintUnknownCommand
from app.commands.tournament import EnterScore
from app.commands.application import ExitApplication
from app.commands.navigation import GoBackMenu

from app.views.edit_turn import EditTurnViewer


class EditTurnController:
    """Project edit_turn controller class."""

    def __init__(self, tournament, turn, is_new):
        """Init edit_turn controller class."""
        self._app = None
        self.tournament = tournament
        self.viewer = EditTurnViewer()

        if is_new:
            already_exists = True
            while already_exists:
                name_new = input("Enter your turn name : ")
                if name_new in tournament.turns:
                    print("This name is already taken, please enter another one.")
                else:
                    already_exists = False

            self.tournament.get_next_turn(name_new)
            self.turn = self.tournament.turns[name_new]
        else:
            self.turn = turn

        self.command_names = []

    def display(self):
        """Display the controller view."""
        self.viewer.display(self.tournament, self.turn)

    def get_command(self):
        """Get the user input and convert it to a command instance."""
        command_input = input("Enter your command: ")

        # The 1st command in list must always be the PrintUnknownCommand, which is used
        # as default command.
        self.command_names = [
            PrintUnknownCommand(self.viewer),
            ExitApplication(),
            GoBackMenu(self._app, self.viewer, "turns", self.tournament),
            EnterScore(self.turn),
        ]

        for command in self.command_names:
            if command.is_valid(command_input):
                self.command = command
