from decimal import Decimal


class NearestNeighbourApproximator(SimpleQFunction):
    """
    This is an implementation of k-Nearest Neighbours approximator,
    which can be used to represent Q-function data.
    """

    # number of neighbours from which estimation is taken
    knn = None

    def __init__(self, action_factory, knn=3):
        super(NearestNeighbourApproximator, self).__init__(
            actions_factory=actions_factory, *args, **kwargs)
        self.knn = knn

    def get_value(self, state, action):
        storedValue = self.get_stored_value(state, action)
        if storedValue is not None:
            return storedValue;
        else:
            value = 0

        # get k nearest neighbour states
        kNN = getNerestStates(state, action, self.knn)
        sumOfValues = 0
        for neighbour in kNN:
            sumOfValues += self.values.get(neighbour).get(action)

        # neighbours can be != k when there is not enough values stored
        neighbours = kNN.size();
        if neighbours > 0:
            value = sumOfValues/neighbours

        return value

    def get_actions(self, state):
        actionValues = []
        for action in self.actions.iterator():
            actionValues.put(action, self.get_value(state, action))

        return actionValues

    def put(self, state, action, double):
        actions = self.get_stored_actions(state)
        actions.put(action, double);
        # remember action
        self.actions.add(action)

    def get_stored_actions(state):
        """
        Retrieves from Q-functionan existing map of action-values for the given state.
        If no such map exist creates new one (empty) and binds it to Q-function.
        """
        actionValues = values.get(state);
        if actionValues is None:
            actionValues = ActionValue()
            values.put(state, actionValues);

        return actionValues

    def get_nerest_states(state, action, knn):
        """
        Finds k nearest states which have stored value for desired action.
        """
        if knn < 1:
            raise Exception("Illegal number of neighbours."
                            " Cannot be less than 1.")

        nearest = []
        maxApprovedDistance = Decimal.MAX_VALUE

        for item_state in states():

            someState = item_state
            distance = item_state.get_distance(state)

            if (len(nearest) < knn or distance < maxApprovedDistance) and\
                    (values.get(item_state).get(action) != None):
                someNeighbour = StateDistance(someState, distance)
                nearest.add(someNeighbour)
                # find farthest of the k-nearest states
                # Collections.sort(nearest);
                lastIndex = len(nearest)-1
                if len(nearest) > k:
                    # remove farthest (k+1) state
                    nearest.remove(lastIndex)
                    lastIndex-=1

                maxApprovedDistance = nearest.get(lastIndex).get_distance();

        nearestStates = []
        for state_distance in nearest:
            nearestStates.add(state_distance.get_state())

        return nearestStates;

    def set_knn(self, knn):
        this.knn = knn


class ActionValue(object):

    def __init__(self, action, val):
        self.action = action
        self.val = val


class StateDistance(object):

    state = None
    distance = None

    def __init__(self, state, distance):
        self.state = state
        self.distance = distance

    def compare_to(self, other_state_distance):
        return self.get_distance() - otherStateDistance.get_distance()

    def get_distance(self):
        return self.distance

    def set_distance(self, distance):
        self.distance = distance

    def get_state(self):
        return self.state

    def __unicode__(self):
        return "state: {}; distance: {};".format(
            self.get_state, self.get_distance()
        )
