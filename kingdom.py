from monarchy import Monarchy


class Kingdom(Monarchy):
    def __init__(self,  population=None, area=None,
                 type_of_monarchy=None, name_of_monarch=None):
        super(Kingdom, self).__init__(population, area,
                                      type_of_monarchy)
        self._name_of_monarch = name_of_monarch

    def __str__(self):
        return super(Monarchy, self).__str__() + "\nName of monarch: {0}.\n".format(self._name_of_monarch)
