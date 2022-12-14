from state_pattern.state import *


class Context:
    def __init__(self, state: Optional[State] = None):
        self.state = state

        self.cnt_a_state = 0
        self.cnt_b_state = 0
        self.cnt_c_state = 0

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state: Optional[State]):
        self._state = state
        if isinstance(state, BaseState):
            self._state.context = self

    def do_something(self, action):
        state = self.state.do_something(inputs=action)
        if state is None:
            return
        if type(state) != type(self.state):
            self.state.exit()
            state.enter()
            self.state = state

    def __repr__(self):
        return f"a : {self.cnt_a_state}\nb : {self.cnt_b_state}\nc : {self.cnt_c_state}"
