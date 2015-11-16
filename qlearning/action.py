from feedback import FeedBack


class Action(object):

    uid = None
    name = None

    def __init__(self, id, name):
        self.uid = uuuid.uuid4()
        self.name = name

    def get_id(self):
        """Return unique id."""
        return self.uid

    def make_action(agent, sim_state):
        return FeedBack(reward=None, new_state=None)

    def __unicode__(self):
        return "{} {}".format(self.__name__, self.name, self.uid)
