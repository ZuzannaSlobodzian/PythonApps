from math import sqrt

from .incident import Incident


class IncidentQueue:

    def __init__(self):
        self.__queue = []

    def __getitem__(self, position):
        return self.__queue[position]

    def __setitem__(self, position, value):
        self.__queue[position] = value

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self.__queue):
            result = self.__queue[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

    def __contains__(self, incident):
        return incident in self.__queue

    def __repr__(self):
        return f"IncidentQueue({self.__queue!r})"

    def __str__(self):
        if len(self):
            return "\n".join([f"{' ' * (4 * idx)}{incident}" for idx, incident in enumerate(self.__queue)])
        else:
            return "Empty queue"

    def __add__(self, other):
        if isinstance(other, Incident):
            new__queue = IncidentQueue()
            new__queue.__queue = self.__queue[:]
            new__queue += other
            return new__queue
        else:
            return NotImplemented

    def __radd__(self, other):
        if isinstance(other, Incident):
            new__queue = IncidentQueue()
            new__queue += other
            new__queue.__queue += self.__queue
            return new__queue
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Incident):
            self.__queue.append(other)
        return self

    def __call__(self, id):
        for incident in self.__queue:
            if incident.id == id:
                return incident
            pass
        raise ValueError("No incident found with the given ID")

    def __lt__(self, other):
        return len(self.__queue) < len(other.__queue)

    def __gt__(self, other):
        return len(self.__queue) > len(other.__queue)

    def __bool__(self):
        return bool(self.__queue)

    def __len__(self):
        return len(self.__queue)

    def incident_management(self, ambulances: 'list'):
        self.__queue = sorted(self.__queue, key=lambda x: (x.priority, x.time))
        available_ambulances = list(filter(lambda x: x.status == "available", ambulances))
        ambulances_on_mission = list(filter(lambda x: x.status == "on mission", ambulances))

        ambulance_for_incident = []
        for incident in self.__queue:

            if available_ambulances:
                distances = []

                if isinstance(available_ambulances, list):
                    for a in available_ambulances:
                        distance = sqrt(
                            (a.location[0] - incident.location[0]) ** 2 + (a.location[1] - incident.location[1]) ** 2)
                        distances.append((distance, a.id))

                    sorted_ambulances = sorted(distances, key=lambda x: x[0])

                    choosen_ambulance = list(filter(lambda x: x.id == sorted_ambulances[0][1], ambulances))
                    ambulance_for_incident.append((incident, choosen_ambulance[0]))

                    i = 0
                    for r in available_ambulances:
                        if r.id == sorted_ambulances[0][1]:
                            available_ambulances.pop(i)
                        i += 1
                else:
                    ambulance_for_incident.append((incident, available_ambulances))

            elif ambulances_on_mission:
                distances = []

                if isinstance(ambulances_on_mission, list):
                    for a in ambulances_on_mission:
                        distance = sqrt(
                            (a.location[0] - incident.location[0]) ** 2 + (a.location[1] - incident.location[1]) ** 2)
                        distances.append((distance, a.id))

                    sorted_ambulances = sorted(distances, key=lambda x: x[0])

                    choosen_ambulance = list(filter(lambda x: x.id == sorted_ambulances[0][1], ambulances))
                    ambulance_for_incident.append((incident, choosen_ambulance[0]))

                    i = 0
                    for r in ambulances_on_mission:
                        if r.id == sorted_ambulances[0][1]:
                            ambulances_on_mission.pop(i)
                        i += 1
                else:
                    ambulance_for_incident.append((incident, ambulances_on_mission))

            else:
                ambulance_for_incident.append((incident, None))

        for i in ambulance_for_incident:
            print(i)


if __name__ == "__main__":
    queue = IncidentQueue()
    incident1 = Incident(1, "Power outage in sector 4")
    incident2 = Incident(2, "Fire alarm in building 21")
    incident4 = Incident(4, "Fire alarm in building 129")

    print(f"---------- wyświetlanie za pomocą __str__ ----------")
    print(queue)

    print(f"---------- dodanie za pomocą __iadd__ ----------")
    queue += incident1
    queue += incident2
    print(queue)
    print(f"---------- dodanie za pomocą __add__ ----------")
    queue = queue + incident4
    print(queue)

    print(f"---------- dostęp za pomocą __getitem__ ----------")
    print(queue[0])
    print(f"---------- sprawdzenie za pomocą __contains__ ----------")
    print(incident1 in queue)

    print(f"---------- iteracja za pomocą __iter__ i __next__ ----------")
    for incident in queue:
        print(incident)

    print(f"---------- dodawanie prawostronne za pomocą __radd__ ----------")
    new_incident = Incident(3, "Test incident")
    queue = new_incident + queue

    print(f"---------- test za pomocą __bool__ ----------")
    if queue:
        print("Queue is not empty.")

    print(f"---------- długość kolejki za pomocą __len__ ----------")
    print(len(queue))

    print(f"---------- wyszukiwanie za pomocą __call__ ----------")
    print(queue(1))
