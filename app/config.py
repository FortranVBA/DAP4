"""Project OC DAP 4 file with config related variables and class."""


class CommandField:
    """Object with field string names matchings."""

    add_player_c = "ap"
    back_c = "b"
    create_next_turn_c = "cnt"
    edit_tournament_c = "eto"
    edit_turn_c = "etu"
    turns_c = "etus"
    exit_c = "ex"
    generate_players_c = "gp"
    main_c = "m"
    match_result_c = "mr"
    new_c = "n"
    players_c = "p"
    print_c = "pr"
    save_players_c = "sp"
    unknown_c = "uk"
    tournaments_c = "t"


class ViewName:
    """Object with field string names matchings."""

    view_main = "v_main"
    view_tournaments = "v_tournaments"
    view_players = "v_players"
    view_print = "v_print"
    view_edit_tournament = "v_edit_tour"
    view_turns = "v_turns"
    view_edit_turn = "v_edit_turn"
