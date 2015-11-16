

class State(object):

    uid = None

    def get_id(self):
        """
        Each state have unique id.
        """
        return self.uid

    def get_distance(self, state):
        """
        Return measure of difference between two states.
        It is used by ref NearestNeighbourApproximator.
        If other QFunction implementation is used,
        than implementation of this method is irrelevant.
        """
        return None  # TODO
