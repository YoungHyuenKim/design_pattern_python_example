from state_pattern.pushdown_automata_context import PushDownAutoMataContext
from state_pattern.state import *


if __name__ == '__main__':

    context = PushDownAutoMataContext()
    print(f"context2 current state: {context.current_state}")
    context.do_something(action="A")  # Idle, Enter A
    print(f"current state: {context.current_state}") # [A]
    context.do_something(action="A")  # Do A
    print(f"current state: {context.current_state}")  # [A]
    context.do_something(action="END")  # Do A Exit A
    print(f"current state: {context.current_state}")  # [None]
    context.do_something(action="END")  # Idle
    print(f"current state: {context.current_state}")  # [None]
    context.do_something(action="B")  # Enter B
    print(f"current state: {context.current_state}")  # [B]
    context.do_something(action="B")  # Do B
    print(f"current state: {context.current_state}")  # [B]
    context.do_something(action="B")  # Do B,
    print(f"current state: {context.current_state}")  # [B]
    context.do_something(action="C")  # Do B, Exit B, Enter C
    print(f"current state: {context.current_state}")  # [C]
    context.do_something(action="End")  # Do C, Exit C
    print(f"current state: {context.current_state}")  # [B]
    context.do_something(action="End")  # Do B, Exit B
    print(f"current state: {context.current_state}")  # [None]