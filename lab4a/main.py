import cinema


class ReservationError(Exception):

    def __init__(self, number):
        self.message = "This seat is already occupied"
        self.number = number
        Exception.__init__(self, self.message + f": {number}")


class Main:
    cinema1 = cinema.Cinema()
    usersList = []

    isFull = True
    for seat in cinema1.hall.values():
        if seat[0] == 0:
            isFull = False
            break

    if isFull:
        raise ValueError("Cinema is full")

    seatID = "16"
    userName = "Zbigniew"
    userLastname = "Boniek"

    if cinema1.hall[seatID][0] == 0:
        if not (userName, userLastname) in usersList:
            cinema1.reserve(seatID, userName, userLastname)
        else:
            raise ValueError("You've already made a reservation.")
    else:
        raise ReservationError(seatID)

    usersList.append((userName, userLastname))

    print(cinema1.hall)

    seatID = "16"
    userName = "Zbigniew"
    userLastname = "Boni"

    if cinema1.hall[seatID][0] == 1 and cinema1.hall[seatID][1] == userName and cinema1.hall[seatID][2] == userLastname:
        cinema1.cancelReservation("16")
    else:
        raise ValueError("It's not your seat.")
    print(cinema1.hall)
