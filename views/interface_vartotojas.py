from utils.utils import get_valid_int
from views.interface_organizatorius import (
    display_films,
    search_film,
    filter_film,
    display_session,
)


def user_mode(film, session, username, ziurovas):
    while True:
        choice = input(
            "Pasirinkite veiksma:\n1. Ieskoti filmo\n2. Filtruoti filmus pagal zanra\n3. Atvaizduoti filmu sesijas\n4. Atvaizduoti visus filmus\n5. Rezervuoti vietas\n6. Ivertinti filma\n7. Iseiti\n"
        )
        if choice == "1":
            search_film(film)
        elif choice == "2":
            filter_film(film)
        elif choice == "3":
            display_session(session)
        elif choice == "4":
            display_films(film)
        elif choice == "5":
            reserve_session(session)
        elif choice == "6":
            rate_film(film, username, ziurovas)
        elif choice == "7":
            print("Viso gero!!!")
            break
        else:
            print("Seniuk davai normaliai ivesk.")


def reserve_session(session):
    display_session(session)
    index = get_valid_int("Iveskite filmo indekso numeri: ")
    biletai = get_valid_int("Iveskite bilietu skaiciu rezervuoti: ")
    session.reserve(index, biletai)


def rate_film(film, username, ziurovas):
    film.display()
    index = get_valid_int("Iveskite filmo indekso numeri: ")
    rating = get_valid_int("Iveskite filmo ivertinima skaiciais (1-10): ")
    film.rate(index, rating, username, ziurovas)
