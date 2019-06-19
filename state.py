from abc import ABC, abstractmethod


class StateCompare(ABC):
    @staticmethod
    @abstractmethod
    def compare(field1, field2, reverse):
        pass


class State(StateCompare):
    def __init__(self, population=None, area=None):
        self._population = population
        self._area = area

    @staticmethod
    def compare(field1, field2, reverse):
        return (not reverse and field1 > field2) or (reverse and field1 < field2)

    def __str__(self):
        return "Population: {0}. \nArea: {1}.".format(self._population, self._area)
