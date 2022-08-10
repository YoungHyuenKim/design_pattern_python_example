from state_pattern.state import *


class Context:
    _state = None

    def __init__(self, state: State):
        self._state = state

        self.cnt_a_state = 0
        self.cnt_b_state = 0
        self.cnt_c_state = 0

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state: State):
        self._state = state
        self._state.context = self

    def do_something(self, action):
        state = self._state.do_something(context=self, inputs=action)
        if state is not None:
            del self._state  # call exit method...
            state.enter()
            self._state = state

    def __repr__(self):
        return f"a : {self.cnt_a_state}\nb : {self.cnt_b_state}\nc : {self.cnt_c_state}"
