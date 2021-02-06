"""Project OC DAP 4 file with tournament related class."""

from app.controllers.controller import Controller


class Application:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        self.player_list = {}
        self.tournament_list = {}
        self.controller = Controller(self.player_list, self.tournament_list)
        self.exit = False

    def run(self):
        """Run  Application class."""
        while not self.exit:
            self.controller.display()

            arguments = 
            self.exit = self.controller.get_command(arguments)

            self.controller.clear_screen()
        return

    def get_arguments(self):
        

" sty -> coloration de la console"
