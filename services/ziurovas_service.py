import services.data_handler as data
from models.vartotojas import Vartotojas
from config import ziurovas_path


class ZiurovasService:
    def __init__(self):
        self.ziurovasList = data.load(ziurovas_path)

    def registration(self, username):
        vartotojas = Vartotojas(username)
        for value in self.ziurovasList:
            if value.username == vartotojas.username:
                print("Tokas vartotojo vardas jau yra.")
                return False
        print(f"Sekmingai prisiregistravote {username}")
        self.ziurovasList.append(vartotojas)
        data.save(ziurovas_path, self.ziurovasList)
        return True

    def login(self, username):
        for value in self.ziurovasList:
            if value.username == username:
                print(f"Sekmingai prisijungta {username}")
                return True
        print("Tokio prisijungimo vardo nera")
        return False
