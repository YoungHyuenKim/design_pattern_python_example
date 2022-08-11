from state_pattern.state import *
from typing import List, Optional


class PushDownAutoMataContext:
    def __init__(self, init_state_list: Optional[List[State]] = None):
        self._state_list: List[State] = init_state_list if init_state_list is not None else list()
        self.cnt_a_state = 0
        self.cnt_b_state = 0
        self.cnt_c_state = 0

    @property
    def current_state(self) ->State:
        return self._state_list[-1] if not self.empty() else None

    def add_state(self, state: State):
        state.context = self
        self._state_list.append(state)
        self.current_state.enter()

    def pop(self):
        if len(self._state_list):
            state = self._state_list.pop(-1)
            state.exit()

    def empty(self):
        return len(self._state_list) == 0

    def do_something(self, action):
        if self.empty():
            print("Idle")
            if action == "A":
                self.add_state(AConfigState())
            elif action == "B":
                self.add_state(BConfigState())
            elif action == "C":
                self.add_state(CConfigState())
            return

        state = self.current_state.do_something(inputs=action)
        if type(state) == type(self.current_state):
            return
        if state is not None:  # call exit method...
            self.add_state(state)
        else:
            self.pop()

    def __repr__(self):
        return f"a : {self.cnt_a_state}\nb : {self.cnt_b_state}\nc : {self.cnt_c_state}"




