

class ActionFactory(object):
    """
    actions = {
        {
            'action_id': UUID('109c5479-b89e-4379-85ba-7343631016d3'),
            'action': <Action object>,
            'state_id': UUID('9ee05759-26a5-4f71-b6cc-3d4fb3c1920e'),
            'state': <State object>,
        },
        ..
    }
    """
    actions = {}

    def get_random_action(self, state):
        state_actions = filter(
            lambda x: x.get('state_id') == state.get_id(), self.actions)
        return random.choice(state_actions)

    def get_action_by_id(self, action_id):
        return self.actions.get(action_id)
