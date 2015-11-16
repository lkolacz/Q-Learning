from qfunction import QFunction


class SimpleQFunction(QFunction):
    values = None
    #wywalic ten action factory i zamiast tego zbior dostepnych akcji neich bedzie?
    actions_factory = None

    def __init__(self, actions_factory):
        self.actions_factory = actions_factory

    def put(self, state, action, value):
        actions = self.get_actions(state)
        action_id = action.get_id()
        actions.put(action_id, value)

    def get_value(self, state, action):
        value = self.get_stored_value(state, action)
        if not value:
            value = 0
        return value

    def get_stored_value(self, state, action):
        actions = self.values.get_actions(state)
        value = None
        if actions and actions.contain(action):
            value = actions.get(action)
        return value

    def get_best_action(self, state):
        actions = self.get_actions(state)
        best_action_id = None
        best_action_val = 0
        for action in actions.iterator():
            action_id = action.get_id()
            curr_val = actions.get_by_id(action_id)
            if(best_action_id is None or curr_val > best_action_val):
                best_action_id = action_id
                best_action_val = actions.get_by_id(best_action_id)

        if best_action_id:
            best = self.factory.get_action_by_id(best_action_id)
        else:
            best = self.factory.get_random_action(state)
        return best

    def get_actions(self, state):
        state_id = state.get_id()
        actions = None
        if self.values.contain_by_id(state_id):
            actions = self.values.get(state_id)
        else:
            actions = Action();
            self.values.put(state_id, actions)
        return actions
