class Cinema:

    def __init__(self):
        self.hall = {"1": [0], "2": [0], "3": [0], "4": [0], "5": [0], "6": [0], "7": [0], "8": [0], "9": [0],
                     "10": [0], "11": [0], "12": [0], "13": [0], "14": [0], "15": [0], "16": [0], "17": [0], "18": [0],
                     "19": [0], "20": [0], "21": [0], "22": [0], "23": [0], "24": [0], "25": [0]}

    def reserve(self, id, name, lastname):
        self.hall[id][0] = 1
        self.hall[id].append(name)
        self.hall[id].append(lastname)

    def cancelReservation(self, id):
        self.hall[id][0] = 0
        self.hall[id].pop(1)
        self.hall[id].pop(1)

