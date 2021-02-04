"""Project OC DAP 4 file with tournament related class."""

from app.config import CommandField


class EditTournamentViewer:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        pass

    @staticmethod
    def display(tournament, player_list):
        """(Put description here)."""
        print(f"You are editing tournament {tournament.name}")
        print(f" Location :  {tournament.location}")
        print(f" Date  {tournament.date}")
        print(f" Number of turns  {tournament.turn_number}")
        print(f"Number of rounds : {len(tournament.turns)}")
        print(f"Number of players : {len(tournament.players_index)}")
        print(f" Time control {tournament.time_control}")
        print(f"Description  {tournament.description}")
        print(" ")
        print("Command list :")
        print(" - " + CommandField.add_player_c + " to add player")
        print(" - " + CommandField.generate_players_c + " to generate 8 players")
        print(" - " + CommandField.turns_c + " to view and edit turns")
        print(" - " + CommandField.create_next_turn_c + " to create the next turn")
        print(" - " + CommandField.back_c + " to go back to main menu")
        print(" - " + CommandField.exit_c + " to quit application")
