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
    MATCH_RESULT = "mr"
    NEW = "n"
    PLAYERS = "p"
    RANKING = "r"
    SAVE_PLAYERS = "sp"
    SAVE_TOURNAMENTS = "st"
    UNKNOWN = "uk"
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
