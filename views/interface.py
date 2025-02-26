from services.film_service import FilmServices
from services.seansas_service import SessionServices
from services.organizatoiurs_service import OrganizatoriusService
from services.ziurovas_service import ZiurovasService
from views.interface_organizatorius import operator_mode
from views.interface_vartotojas import user_mode


def festivalis():
    film = FilmServices()
    session = SessionServices()
    organizatorius = OrganizatoriusService()
    ziurovas = ZiurovasService()

    print("Sveiki atvyke i filmu festivali!!!")

    while True:
        mode = input(
            "Prasome pasirinkti programos rezima skaciukais (1 raba 2):\n1. Operatorius\n2. Vartotojas\n3. Iseiti\n"
        )
        if mode == "1":
            print("Prisijungete kaip operatorius")
            admin = True
            login_reg(film, session, organizatorius, ziurovas, admin)
            break
        elif mode == "2":
            print("Prisijungete kaip Vartotojas")
            admin = False
            login_reg(film, session, ziurovas, ziurovas, admin)
            break
        elif mode == "3":
            print("Viso gero!!!")
            break
        else:
            print("Privalote ivesti skaiciukus (1 - 3)")


def login_reg(film, session, organizatorius, ziurovas, admin):
    while True:
        mode = input("1. Prisijungti\n2. Registruotis\n3. Iseiti\n")
        if mode == "1":
            login(film, session, organizatorius, ziurovas, admin)
            break
        elif mode == "2":
            register(film, session, organizatorius, ziurovas, admin)
            break
        elif mode == "3":
            print("Viso gero!!!")
            break
        else:
            print("Privalote ivesti skaiciukus (1 - 3)")


def login(film, session, organizatorius, ziurovas, admin):
    username = input("Iveskite prisijungimo duomenys: ")
    if admin and organizatorius.login(username):
        operator_mode(film, session, ziurovas)
    elif not admin and ziurovas.login(username):
        user_mode(film, session, username, ziurovas)
    else:
        login_reg(film, session, organizatorius, ziurovas, admin)


def register(film, session, organizatorius, ziurovas, admin):
    username = input("Prisiregistruokite su unikaliu vardu: ")
    if admin and organizatorius.registration(username):
        operator_mode(film, session, ziurovas)
    elif not admin and ziurovas.registration(username):
        user_mode(film, session, username, ziurovas)
    else:
        login_reg(film, session, organizatorius, ziurovas, admin)
