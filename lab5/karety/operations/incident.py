class Incident:
    __max_id = 0

    def __init__(self, description, priority, time, name, lastname, phone_number):
        Incident.__max_id += 1
        self.id = Incident.__max_id
        self.description = description
        self.priority = priority
        self.time = time
        self.name = name
        self.lastname = lastname
        self.phone_number = phone_number

    @classmethod
    def get_max_id(cls):
        return cls.__max_id

    def __repr__(self):
        return f"Incident(id={self.id!r}, priority= {self.priority}, time={self.time}, " \
               f"description={self.description!r}, name={self.name}, lastname={self.lastname}, phone number={self.phone_number})"

    def __str__(self):
        return f"Incident {self.id}: {self.description}"
