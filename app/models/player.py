"""Project OC DAP 4 file with tournament related class."""


class Player:
    """Player characteristics to be handled by application."""

    def __init__(self, name, surname, birth, sex, ranking):
        """Init Player class."""
        self.name = name
        self.surname = surname
        self.birth_date = birth
        self.sex = sex
        self.ranking = ranking
