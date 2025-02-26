class Session:
    def __init__(self, filmas, data, laikas, pabaigos_laikas, maxRezervaciju):
        self.filmas = filmas
        self.data = data
        self.laikas = laikas
        self.pabaigos_laikas = pabaigos_laikas
        self.maxRezervaciju = maxRezervaciju
        self.rezervacija = 0

    def __repr__(self):
        return f"{self.data} {self.laikas} - {self.pabaigos_laikas} - {self.filmas} rezervacijos: {self.rezervacija}/{self.maxRezervaciju}"
