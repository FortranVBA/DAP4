"""Project OC DAP 4 file with tournament related class."""

from app.config import CommandField


class EditTournamentViewer:
    """Project application class."""

    def __init__(self):
        """(Put description here)."""
        self.warning = ""

        self.tournament_name = ""
        self.tournament_location = ""
        self.tournament_date = ""
        self.tournament_turns_number = ""
        self.tournament_turns_created = ""
        self.tournament_players_number = ""
        self.tournament_time_control = ""
        self.tournament_description = ""

    def set_selected_tournament(
        self,
        name,
        location,
        date,
        turns_number,
        turns_created,
        players_number,
        time_control,
        description,
    ):
        """(Put description here)."""
        self.tournament_name = name
        self.tournament_location = location
        self.tournament_date = date
        self.tournament_turns_number = turns_number
        self.tournament_turns_created = turns_created
        self.tournament_players_number = players_number
        self.tournament_time_control = time_control
        self.tournament_description = description

    def display(self):
        """(Put description here)."""
        self.display_warning()

        print(f"You are editing tournament {self.tournament_name}")
        print(f" Location :  {self.tournament_location}")
        print(f" Date  {self.tournament_date}")
        print(f" Number of turns  {self.tournament_turns_number }")
        print(f"Number of rounds created : {self.tournament_turns_created}")
        print(f"Number of players : {self.tournament_players_number}")
        print(f" Time control {self.tournament_time_control}")
        print(f"Description  {self.tournament_description}")
        print(" ")
        print("Command list :")
        print(" - " + CommandField.add_player_c + " to add player")
        print(" - " + CommandField.generate_players_c + " to generate 8 players")
        print(" - " + CommandField.turns_c + " to view and edit turns")
        print(" - " + CommandField.create_next_turn_c + " to create the next turn")
        print(" - " + CommandField.back_c + " to go back to main menu")
        print(" - " + CommandField.exit_c + " to quit application")

    def get_warning(self):
        """(Put description here)."""
        if self.warning == "command unknown":
            return "Warning : this command is not valid"
        else:
            return "Warning : unknown error occured"

    def display_warning(self):
        """(Put description here)."""
        print(" ")
        print(" ")
        if not self.warning == "":
            print(self.get_warning())
