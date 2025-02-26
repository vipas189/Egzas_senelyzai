from datetime import datetime, timedelta


def add_minutes_to_time(time1, time2):
    karoce = datetime.strptime(time1, "%H:%M").time()
    time1_delta = datetime.combine(datetime.today(), karoce)
    time2_delta = timedelta(minutes=time2)
    new_time = time1_delta + time2_delta
    return new_time.strftime("%H:%M")


def is_time_in_range(start1, end1, start2, end2):
    start1 = datetime.strptime(start1, "%H:%M").time()
    end1 = datetime.strptime(end1, "%H:%M").time()
    start2 = datetime.strptime(start2, "%H:%M").time()
    end2 = datetime.strptime(end2, "%H:%M").time()

    return not (end1 <= start2 or end2 <= start1)


def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Prašome įvesti skaičių!")


def get_valid_year(prompt):
    while True:
        try:
            davaice = int(input(prompt))
            if 1 <= davaice <= 2025:
                return
            raise ValueError
        except ValueError:
            print("Ivesk normaliai metus!!!")


def get_valid_trukme(prompt):
    while True:
        try:
            davaice = int(input(prompt))
            if 1 <= davaice <= 300:
                return
            raise ValueError
        except ValueError:
            print("Ivesk normaliai trukme!!!")


def get_valid_age(prompt):
    while True:
        try:
            davaice = int(input(prompt))
            if 1 <= davaice <= 100:
                return
            raise ValueError
        except ValueError:
            print("Ivesk normaliai amziu!!!")


def get_valid_date(prompt):
    while True:
        try:
            return datetime.strptime(input(prompt), "%Y-%m-%d").date()
        except ValueError:
            print("Netinkamas formatas, data privalo rasytis pvz: (YYYY-MM-DD)")


def get_valid_time(prompt):
    while True:
        try:
            convert = datetime.strptime(input(prompt), "%H:%M").time()
            return convert.strftime("%H:%M")
        except ValueError:
            print("Netinkamas formatas, laikas privalo rasytis pvz: (HH:MM)")
