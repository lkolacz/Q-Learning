

class FeedBack(object):
    """
    Any class that needs to be used by Library for action representation
    has to implement this interface
    """
    reward = None
    new_state = None

    def __init__(self, reward, new_state):
        self.reward = reward
        self.new_state = new_state

    def get_reward(self):
        """Each action should return reward."""
        return self.reward

    def get_new_state(self):
        """ Each action should return new state. """
        return self.new_state

