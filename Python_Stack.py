
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

    def size(self) -> int:
        return len(self._stack)

    def empty(self) -> bool:
        
        if not self._stack:
            return True
        return False


# HACK: Wield the Stack class to solve various problems!

# Problem 1: reversed the Stack order
class Problems:
    
    @staticmethod
    def reverse1(a) -> list:
        # Instantiate a Stack object and a reversed list
        arr = Stack()
        a_reversed = a[::-1]

        for elem in a_reversed:
            # Add the elements into the stack
            arr.push(elem)

        # Create a new list to append these value from top to bottom order
        reversed_a: list = []

        for _ in range(arr.size()):
            # Insert the values
            reversed_a.append(arr.top())
        
        # Return the reversed arr!
        return reversed_a
    