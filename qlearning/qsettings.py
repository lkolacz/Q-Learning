

class LearningSettings(object):

    beta = 0.5;
    gamma = 0.9;
    exploration_ratio = 0.5;
    exploration_enabled = true;
    learning = true;

    def get_beta(self):
        return self.beta

    def set_beta(self, beta):
        self.beta = beta

    def get_gamma(self):
        return self.gamma

    def set_gamma(self, gamma):
        self.gamma = gamma

    def is_learning(self):
        return self.learning is True

    def get_learning(self):
        return self.learning

    def set_learning(self, learning):
        self.learning = learning

    def get_exploration_ratio(self):
        return self.exploration_ratio

    def set_exploration_ratio(self, exploration_ratio):
        self.exploration_ratio = exploration_ratio

    def get_exploration_enabled(self):
        return self.exploration_enabled

    def set_exploration_enabled(self, exploration_enabled):
        self.exploration_enabled = exploration_enabled

    def __unicode__(self):
        return "gamma: {}; beta: {}; exploration: {}%".format(
            self.get_gamma(), self.get_beta(), self.get_exploration_ratio())
