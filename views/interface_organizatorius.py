from utils.utils import (
    get_valid_age,
    get_valid_int,
    add_minutes_to_time,
    get_valid_date,
    get_valid_time,
    get_valid_trukme,
    get_valid_year,
)


def operator_mode(film, session, ziurovas):
    while True:
        choice = input(
            "Pasirinkite rezima:\n1. Filmu rezimas\n2. Seansu rezimas\n3. Iseiti\n"
        )
        if choice == "1":
            operator_film_mode(film, ziurovas)
            break
        elif choice == "2":
            operator_session_mode(film, session)
            break
        elif choice == "3":
            print("Viso gero!!!")
            break


# ------------------------------FILM MODE--------------------------------------


def operator_film_mode(film, ziurovas):
    while True:
        choice = input(
            "Pasirinkite veiksma:\n1. Prideti filma\n2. Panaikinti filma\n3. Atnaujinti filmo info\n4. Ieskoti filmo\n5. Filtruoti filmus pagal zanra\n6. Atvaizduoti visus filmus\n7. Iseiti\n"
        )
        if choice == "1":
            add_film(film)
        elif choice == "2":
            remove_film(film, ziurovas)
        elif choice == "3":
            update_film(film, ziurovas)
        elif choice == "4":
            search_film(film)
        elif choice == "5":
            filter_film(film)
        elif choice == "6":
            display_films(film)
        elif choice == "7":
            print("Viso gero!!!")
            break


def add_film(film):
    pavadinimas = input("Iveskite pavadinima: ")
    trukme = get_valid_trukme("Iveskite trukme: ")
    zanras = input("Iveskite zanra: ")
    rezisierius = input("Iveskite rezisieriu: ")
    isleidimo_metai = get_valid_year("Iveskite isleidimo metus: ")
    amziaus_reitingas = get_valid_age("Iveskite amziaus reitina: ")
    film.add(
        pavadinimas, trukme, zanras, rezisierius, isleidimo_metai, amziaus_reitingas
    )


def remove_film(film, ziurovas):
    film.display()
    pavadinimas = input("Iveskite filmo pavadinima kuri norite istrinti: ")
    film.remove(pavadinimas, ziurovas)


def update_film(film, ziurovas):
    film.display()
    esancioFilmoPavadinimas = input(
        "Iveskite esancio filmo pavadinima kuri norite redaguoti: "
    )
    pavadinimas = input("Iveskite pavadinima i kuri norite keisti: ")
    trukme = get_valid_trukme("Įveskite trukmę (minutėmis): ")
    zanras = input("Iveskite zanra i kuri norite keisti: ")
    rezisierius = input("Iveskite rezisieriu i kuri norite keisti: ")
    isleidimo_metai = get_valid_year(
        "Iveskite isleidimo_metus i kuriuos norite keisti: "
    )
    amziaus_reitingas = get_valid_age(
        "Iveskite amziaus reitinga i kuri norite keisti: "
    )
    film.update(
        esancioFilmoPavadinimas,
        pavadinimas,
        trukme,
        zanras,
        rezisierius,
        isleidimo_metai,
        amziaus_reitingas,
        ziurovas,
    )


def search_film(film):
    vardasArRezisierius = input(
        "Iveskite filmo pavadinima ar rezisieriu norint rasti filma: "
    )
    film.search(vardasArRezisierius)


def filter_film(film):
    zanras = input("Iveskite zanra pagal kuri norite filtruoti filmus: ")
    film.filter(zanras)


def display_films(film):
    film.display()


# ----------------------------SESSION MODE-------------------------------------


def operator_session_mode(film, session):
    while True:
        choice = input(
            "Pasirinkite veiksma:\n1. Prideti nauja filmo sesija\n2. Atvaizduoti visas sesijas\n3. Istrinti seansa\n4. Iseiti\n"
        )
        if choice == "1":
            add_session(film, session)
        elif choice == "2":
            display_session(session)
        elif choice == "3":
            remove_session(session)
        elif choice == "4":
            print("Viso gero")
            break


def add_session(film, session):
    while True:
        film.display()
        seansas = get_valid_int("Ivesk is saraso pasirinka filma skaiciuku. ")
        maxRezervacijos = get_valid_int("Iveskite kiek priimsite rezervaciju. ")
        if seansas in range(1, len(film.filmList) + 1):
            date = get_valid_date("Irasyti data formatu (YYYY-MM-DD): ")
            time = get_valid_time("irasyk laika formatu (HH:MM): ")
            session.add(
                film.filmList[seansas - 1],
                date,
                time,
                add_minutes_to_time(time, film.filmList[seansas - 1].trukme),
                maxRezervacijos,
            )
            break
        else:
            print("Tokio filmo sarase nera!!!")


def remove_session(session):
    session.display()
    index = get_valid_int(
        "Iveskite skaiciuka is saraso norint istrinti pasirinkta seansa."
    )
    session.remove(index)


def display_session(session):
    session.display()
