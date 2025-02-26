class Vartotojas:
    def __init__(self, username):
        self.username = username
        self.vertino = []

    def __repr__(self):
        return f"{self.username} {self.vertino}"
