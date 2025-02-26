import services.data_handler as data
from config import organizatorius_path


class OrganizatoriusService:
    def __init__(self):
        self.organizatoriusList = data.load(organizatorius_path)

    def registration(self, username):
        for value in self.organizatoriusList:
            if value == username:
                print("Tokas vartotojo vardas jau yra.")
                return False
        print(f"Sekmingai prisiregistravote {username}")
        self.organizatoriusList.append(username)
        data.save(organizatorius_path, self.organizatoriusList)
        return True

    def login(self, username):
        for value in self.organizatoriusList:
            if value == username:
                print(f"Sekmingai prisijungta {username}")
                return True
        print("Tokio prisijungimo vardo nera")
        return False
