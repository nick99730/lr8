from state import State


class Monarchy(State):
    def __init__(self, population=None,
                 area=None, type_of_monarchy=None):
        super(Monarchy, self).__init__(population, area)
        self._type_of_monarchy = type_of_monarchy

    def __str__(self):
        return super(Monarchy, self).__str__() + "\nType of" \
               " monarchy: {0}.".format(self._type_of_monarchy)
