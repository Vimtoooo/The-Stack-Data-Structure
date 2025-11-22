
# TODO: Create a stack data structure!

class Stack:

    # This instance attribute will store the elements inside the list, internally
    def __init__(self):
        self._stack: list[int] = []

    def push(self, elem: int):
        self._stack.append(elem)
    
    def top(self) -> int:
        return self._stack[len(self._stack) - 1]

    def pop(self) -> int:
        return self._stack.pop()