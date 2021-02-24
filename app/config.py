"""Project OC DAP 4 file with config related variables and class."""


class CommandField:
    """Object with field string names matchings."""

    ADD_PLAYER = "ap"
    BACK = "b"
    CREATE_NEXT_TURN = "cnt"
    EDIT_PLAYER = "ep"
    EDIT_TOURNAMENT = "eto"
    EDIT_TURN = "etu"
    TURNS = "etus"
    EXIT = "ex"
    GENERATE_PLAYERS = "gp"
    LOAD_PLAYERS = "lp"
    LOAD_TOURNAMENTS = "lt"
    MATCHES = "m"
    MATCH_RESULT = "mr"
    NEW = "n"
    PLAYERS = "p"
    PLAYERS_ALPHABETIC = "pa"
    PLAYERS_RANKING = "pr"
    RANKING = "r"
    SAVE_PLAYERS = "sp"
    SAVE_TOURNAMENTS = "st"
    TOURNAMENT_DATE = "tda"
    TOURNAMENT_LOCATION = "tl"
    TOURNAMENT_TURN_NUMBER = "ttu"
    TOURNAMENT_TIME = "tti"
    TOURNAMENT_DESCRIPTION = "tde"

    UNKNOWN = "uk"
    UPDATE_RANKING = "ur"
    TOURNAMENTS = "t"


class ViewName:
    """Object with field string names matchings."""

    MAIN = "v_main"
    TOURNAMENTS = "v_tournaments"
    RANKING = "v_ranking"
    PLAYERS = "v_players"
    EDIT_TOURNAMENT = "v_edit_tour"
    TURNS = "v_turns"
    EDIT_TURN = "v_edit_turn"
