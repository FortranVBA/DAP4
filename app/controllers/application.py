"""Project OC DAP 4 file with the main application class."""

from app.controllers.main_menu import MainMenuController


class Application:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        self.change_controller(MainMenuController())
        self.is_exit = False

    def run(self):
        """Run the main loop of application."""
        while not self.is_exit:
            self.controller.display()

            self.controller.get_command()
            self.is_exit = self.controller.command.exe_command()

            self.separate_screen()
        return

    def separate_screen(self):
        """Separate the terminal with blank lines and line separators."""
        print(" ")
        print(" ")
        print("-----------------------------------")
        print("-----------------------------------")
        print("-----------------------------------")
        print(" ")
        print(" ")

    def change_controller(self, new_controller):
        """Change the active controller and gives it the app reference."""
        self.controller = new_controller
        self.controller._app = self
