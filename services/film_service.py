from models.film import Film
from config import films_path, ziurovas_path, rating_path
import services.data_handler as data


class FilmServices:
    def __init__(self):
        self.filmList = data.load(films_path)
        self.ratings = data.load(rating_path)

    def add(
        self,
        pavadinimas,
        trukme,
        zanras,
        rezisierius,
        isleidimo_metai,
        amziaus_reitingas,
    ):
        film = Film(
            pavadinimas, trukme, zanras, rezisierius, isleidimo_metai, amziaus_reitingas
        )
        if not self.filmList:
            self.filmList.append(film)
            self.ratings.append([])
            data.save(rating_path, self.ratings)
            data.save(films_path, self.filmList)
            return
        for value in self.filmList:
            if repr(value).lower() == repr(film).lower():
                print("Toks filmas jau yra")
                return
        self.filmList.append(film)
        self.ratings.append([])
        data.save(rating_path, self.ratings)
        data.save(films_path, self.filmList)

    # tprsm cia yra kazkas tokio, jei pagausi, suprasi del ko taip dariau xddd
    def remove(self, title, ziurovas):  # Seni neisivaizduoju kaip tu perskaityis
        for index in range(len(self.filmList) - 1, -1, -1):  # bet cia viskas gerai veik
            if title.lower() == self.filmList[index].pavadinimas.lower():
                self.ratings.pop(index)
                ziurovas.ziurovasList[0].vertino.remove(index + 1)
                for indexx, value in enumerate(ziurovas.ziurovasList[0].vertino):
                    if value > (index + 1):
                        ziurovas.ziurovasList[0].vertino[indexx] = value - 1
                data.save(rating_path, self.ratings)
                data.save(ziurovas_path, ziurovas.ziurovasList)
                self.filmList.pop(index)
                data.save(films_path, self.filmList)
                return  # jeigu veikia as nekeisiu kol kas ciki briki 20 valandu
        print("Tokio filmo nera")  # cia praleista
        return

    def update(
        self,
        titleToChange,
        newPavadinimas,
        newTrukme,
        newZanras,
        newRezisiserius,
        newIsleidimo_metai,
        newAmziaus_reitingas,
        ziurovas,
    ):
        film = Film(
            newPavadinimas,
            newTrukme,
            newZanras,
            newRezisiserius,
            newIsleidimo_metai,
            newAmziaus_reitingas,
        )
        for index in range(len(self.filmList)):
            if repr(film).lower() == repr(self.filmList[index]).lower():
                return
            elif titleToChange.lower() == self.filmList[index].pavadinimas.lower():
                self.ratings[index] = []
                ziurovas.ziurovasList[0].vertino.remove(index + 1)
                self.filmList[index] = film
                data.save(rating_path, self.ratings)
                data.save(ziurovas_path, ziurovas.ziurovasList)
                data.save(films_path, self.filmList)
                return
        print("Tokio filmo nera arba jis jau egzistuoja")
        return

    def display(self):
        for index in range(len(self.filmList)):
            print(f"{index+1}. {self.filmList[index]}")

    def search(self, titleOrProducer):
        found = [
            film
            for film in self.filmList
            if titleOrProducer.lower()
            in {film.pavadinimas.lower(), film.rezisierius.lower()}
        ]
        if found:
            print("\n".join(map(str, found)))
        else:
            print("Tokio filmo nera")

    def filter(self, genre):
        found = [film for film in self.filmList if genre.lower() in film.zanras.lower()]
        if found:
            print("\n".join(map(str, found)))
        else:
            print("Tokio filmo nera")

    def rate(self, index, rating, username, ziurovas):
        usr_index = None
        for indexx, value in enumerate(ziurovas.ziurovasList):
            if value.username == username:
                usr_index = indexx
                break
        if not self.filmList:
            print("Filmu dar nera!!!")
            return
        if (
            index in range(1, len(self.filmList) + 1)
            and 10 >= rating >= 1
            and not (index in ziurovas.ziurovasList[usr_index].vertino)
        ):
            self.ratings[index - 1].append(rating)
            self.filmList[index - 1].rating = self.average_rating(index - 1)
            ziurovas.ziurovasList[usr_index].vertino.append(index)
            data.save(rating_path, self.ratings)
            data.save(films_path, self.filmList)
            data.save(ziurovas_path, ziurovas.ziurovasList)
        elif index in ziurovas.ziurovasList[usr_index].vertino:
            print("Vartotojas jau vertino")
            return
        else:
            print("Tokio filmo nera arba ivestas neteisingas ivertinimas!!!")

    def average_rating(self, index):
        if self.ratings:
            return sum(self.ratings[index]) / len(self.ratings[index])
        else:
            return 0
