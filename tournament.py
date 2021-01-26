"""Project OC DAP 4 file with tournament related class."""


class Tournament:
    """Tournament characteristics to be handled by application."""

    def __init__(self):
        """Init Tournament class."""
        self.name = "Unknown"
        self.location = "Unknown"
        self.date = "Unknown"
        self.turn_number = 4
        self.round = []
        self.players = []
        self.time_control = ""
        self.description = ""

    def create_tournament(self):
        """(Put description here)."""
        pass

    def add_player(self):
        """(Put description here)."""
        pass

    def generate_couples(self):
        """(Put description here)."""
        pass

    def update_match_results(self):
        """(Put description here)."""
        pass


class Player:
    """Player characteristics to be handled by application."""

    def __init__(self):
        """Init Player class."""
        self.name = "Unknown"
        self.surname = "Unknown"
        self.birth_date = ""
        self.sex = ""
        self.ranking = 99


class Match:
    """Player characteristics to be handled by application."""

    def __init__(self):
        """Init Match class."""
        self.opponents = []
        self.result = []

    def update_result(self):
        """(Put description here)."""
        pass


class MainController:
    """Main controller to be handled by application."""

    def __init__(self):
        """Init MainController class."""
        pass

    def run(self):
        """(Put description here)."""
        pass


class MainViewer:
    """Main viewer to be handled by application."""

    def __init__(self):
        """Init MainViewer class."""
        self.current_view = "main"
        self.current_error = ""

    def display(self):
        """(Put description here)."""
        if self.current_view == "main":
            print(" ")
            print(" ")
            if not self.current_error == "":
                print(self.display_error(self.current_error))
            print("Main menu")
            print("Command list :")
            print("new to create a new tournament")
            print("print to generate reports")
            print("exit to quit application")
        elif self.current_view == "new":
            print(" ")
            print(" ")
            if not self.current_error == "":
                print(self.display_error(self.current_error))
            print("You are creating a new tournament")
            print("Command list :")
            print("back to go back to main menu")
            print("exit to quit application")
        elif self.current_view == "print":
            print(" ")
            print(" ")
            if not self.current_error == "":
                print(self.display_error(self.current_error))
            print("What report do you want ?")
            print("Command list :")
            print("back to go back to main menu")
            print("exit to quit application")

    def display_error(self, error):
        """(Put description here)."""
        if error == "command unknown":
            return "Warning : this command is not valid"
        else:
            return "Warning : unknown error occured"


class Application:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        self.player_list = []
        self.tournament_list = []
        self.viewer = MainViewer()
        self.exit = False

    def run(self):
        """Run  Application class."""
        while not self.exit:
            self.viewer.display()
            self.exit = self.get_command(input("Enter your command: "))

        return

    def get_command(self, command):
        """(Put description here)."""
        if command == "exit":
            return True

        elif self.viewer.current_view == "main":
            if command == "new":
                self.viewer.current_view = "new"
                self.viewer.current_error = ""
            if command == "print":
                self.viewer.current_view = "print"
                self.viewer.current_error = ""
            else:
                self.viewer.current_error = "command unknown"

        elif self.viewer.current_view == "new":
            if command == "back":
                self.viewer.current_view = "main"
                self.viewer.current_error = ""
            else:
                self.viewer.current_error = "command unknown"

        elif self.viewer.current_view == "print":
            if command == "back":
                self.viewer.current_view = "main"
                self.viewer.current_error = ""
            else:
                self.viewer.current_error = "command unknown"

        else:
            self.viewer.current_error = "command unknown"

        return False
