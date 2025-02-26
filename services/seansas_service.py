import services.data_handler as dataa
from utils.utils import is_time_in_range
from models.seansas import Session
from config import session_path


class SessionServices:
    def __init__(self):
        self.sessionList = dataa.load(session_path)

    def add(self, filmas, data, laikas, pabaigos_laikas, maxRezervaciju):
        session = Session(filmas, data, laikas, pabaigos_laikas, maxRezervaciju)
        for value in self.sessionList:
            if value.data == data and is_time_in_range(
                value.laikas, value.pabaigos_laikas, laikas, pabaigos_laikas
            ):
                print("Toks laikas jau yra!!!")
                return
        self.sessionList.append(session)
        dataa.save(session_path, self.sessionList)

    def display(self):
        for index in range(len(self.sessionList)):
            print(f"{index+1}. {self.sessionList[index]}")

    def remove(self, index):
        if not self.sessionList:
            print("Seansu dar nera!!!")
            return
        if index in range(1, len(self.sessionList) + 1):
            self.sessionList.pop(index - 1)
            dataa.save(session_path, self.sessionList)
        else:
            print("Tokio seanso nera!!!")

    def reserve(self, index, tickets):
        if not self.sessionList:
            print("Seansu dar nera!!!")
            return
        if index in range(1, len(self.sessionList) + 1) and (
            tickets + self.sessionList[index - 1].rezervacija
            <= self.sessionList[index - 1].maxRezervaciju
            and tickets >= 0
        ):
            self.sessionList[index - 1].rezervacija += tickets
            dataa.save(session_path, self.sessionList)
        else:
            print("Tokio seanso nera arba virsijote rezervaciju limita!!!")
