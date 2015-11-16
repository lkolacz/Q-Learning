# -*- coding: utf-8 -*-
import random;

from qsettings import LearningSettings


class QLearning(object):
    """
    The main class of the Library.
    For each distinct task a new instance should be created.
    """

    last_action = None
    qfunction = None
    #private ActionFactory actions;
    actions_factory = None
    last_state = None
    current_state = None
    config = None

    def __init__(self, actions_factory, config=None, qfunction=None):
        self.actions_factory = actions_factory
        self.qfunction = qfunction or SimpleQFunction(actions_factory)
        self.config = config or LearningSettings()

    def choose_action(self, state=None):
        """
        Choose next action from given state.
        @rtype: Action
        """
        choice = None

        if random.random() > self.config.exploration_ratio:
            choice = self.qfunction.getBestAction(s);
        else:
            if not state:
                state = self.current_state
            choice = self.actions_factory.get_random_action(state)

        self.lastAction = choice
        return choice

    def set_feedback(self, reward):
        gamma = self.config.get_gamma();
        beta = self.config.get_beta();
        delta = reward + gamma * self.get_best_qvalue() - self.get_last_qvalue()
        last_q = function.getValue(lastState, lastAction);
        new_q = last_q + beta * delta;

        self.qfunction.put(self.last_state, self.last_action, new_q)


    def get_last_qvalue(self):
        """
        Q-function value for the chosen action in prev state.
        """
        return self.qfunction.get_value(self.last_state, self.last_action);

    def get_best_qvalue(self):
        """
        Q-function value for the best action possible in current state
        """
        best_action = self.qfunction.get_best_action(self.current_state)
        return self.qfunction.get_value(self.current_state, best_action)

    def set_state(self, state):
        """
        Set current state to last state and given state to current state.
        """
        self.last_state = self.current_state
        self.current_state = state

    def set_result(self, state, reward):
        self.set_state(state)
        self.set_feedback(reward)

    def get_qfunction(self):
        return self.qfunction
