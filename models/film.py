class Film:
    def __init__(
        self,
        pavadinimas,
        trukme,
        zanras,
        rezisierius,
        isleidimo_metai,
        amziaus_reitingas,
    ):
        self.pavadinimas = pavadinimas
        self.trukme = trukme
        self.zanras = zanras
        self.rezisierius = rezisierius
        self.isleidimo_metai = isleidimo_metai
        self.amziaus_reitingas = amziaus_reitingas
        self.rating = ""

    def __repr__(self):
        return f"Pavadinimas: {self.pavadinimas}, Trukme: {self.trukme}, Zanras: {self.zanras}, Rezisierius: {self.rezisierius}, Metai: {self.isleidimo_metai}, Amzius: {self.amziaus_reitingas}, Reitingas: {self.rating}/10"
