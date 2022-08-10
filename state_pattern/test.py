from state_pattern.state import *
from state_pattern.context import Context

if __name__ == '__main__':
    context = Context(AConfigState(is_init=True))

    context.do_something(action="A")  # [is_init = False, Enter A], Do A o
    context.do_something(action="A")  # Do A
    context.do_something(action="B")  # Do A, Exit A, Enter B
    context.do_something(action="C")  # Do B, Exit B, Enter C
    context.do_something(action="C")  # Do C,
    context.do_something(action="B")  # Do C, Exit C, Enter B
    context.do_something(action="B")  # Do B,
    context.do_something(action="C")  # Do B, Exit B, Exit C
    context.do_something(action="C")  # Do C,
    context.do_something(action="A")  # Do C, Exit C, Enter A
    context.do_something(action="C")  # Do A, Exit A, Enter C

    print(context)
