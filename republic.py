from state import State


class Republic(State):
    def __init__(self, population=None, area=None,
                 term_of_gov=None, nmb_of_reelection=None):
        super(Republic, self).__init__(population, area)
        self._term_of_gov = term_of_gov
        self._nmb_of_reelection = nmb_of_reelection

    def __str__(self):
        return super(Republic, self).__str__() + "\nTerm of government: {0}." \
               "\nNumber of reelection: {1}.".format(self._term_of_gov, self._nmb_of_reelection)

