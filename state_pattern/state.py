from __future__ import annotations
from typing import Optional, TypeVar, Union, TYPE_CHECKING
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from state_pattern.context import Context


class BaseState(ABC):
    @abstractmethod
    def __init__(self, is_init=False):
        self._first = not is_init
        self.context = None

    @property
    def first(self):
        return self._first

    @first.setter
    def first(self, ob: bool):
        if not ob:
            self._first = False
        else:
            raise NotImplemented("")

    @abstractmethod
    def enter(self):
        self.first = False

    @abstractmethod
    def exit(self):
        pass

    @abstractmethod
    def do_something(self, inputs) -> Optional[BaseState]:
        """
        :param context:
        :param inputs:
        :return: None : if return None, end current_State
        """
        raise NotImplementedError("")


State = TypeVar("State", bound=BaseState)


class AConfigState(BaseState):
    def __init__(self, is_init=False):
        super(AConfigState, self).__init__(is_init)

    def enter(self):
        if self.first:
            super(AConfigState, self).enter()
            print("Enter A")

    def exit(self):
        super(AConfigState, self).exit()
        print("Exit A")

    def do_something(self, inputs) -> Optional[State]:

        # Do Some Thing...
        self.context.cnt_a_state += 1
        print("Do A")
        # some condition....
        if inputs == "A":
            return self.__class__()
        elif inputs == "B":
            return BConfigState()
        elif inputs == "C":
            return CConfigState()
        return None

    def __repr__(self):
        return "state A"


class BConfigState(BaseState):
    def __init__(self, is_init=False):
        super(BConfigState, self).__init__(is_init)

    def enter(self):
        if self.first:
            super(BConfigState, self).enter()
            print("Enter B")

    def exit(self):
        super(BConfigState, self).exit()
        print("Exit B")

    def do_something(self, inputs) -> Optional[State]:
        # Do Some Thing...
        self.context.cnt_b_state += 1
        print("Do B")
        # some condition....
        if inputs == "A":
            return AConfigState()
        elif inputs == "B":
            return self.__class__()
        elif inputs == "C":
            return CConfigState()
        return None

    def __repr__(self):
        return "state B"


class CConfigState(BaseState):
    def __init__(self, is_init=False):
        super(CConfigState, self).__init__(is_init)

    def enter(self):
        if self.first:
            super(CConfigState, self).enter()
            print("Enter C")

    def exit(self):
        super(CConfigState, self).exit()
        print("Exit C")

    def do_something(self, inputs) -> Optional[State]:

        # Do Some Thing...
        self.context.cnt_c_state += 1
        print("Do C")
        # some condition....
        if inputs == "A":
            return AConfigState()
        elif inputs == "B":
            return BConfigState()
        elif inputs == "C":
            return self.__class__()
        return None

    def __repr__(self):
        return "state C"
