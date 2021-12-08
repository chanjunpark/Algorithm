
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("underflow")
            exit()

class Solution:
    def trap(self, height: List[int]) -> int:
        floor_stack = Stack()
        top = -1
        rain_water = 0

        for x in range(len(height)):
            while not floor_stack.is_empty() and height[x] > height[floor_stack.peek()]:
                top = floor_stack.pop()
                if floor_stack.is_empty():
                    break
                distance = x - floor_stack.peek() - 1
                quantity = min(height[x], height[floor_stack.peek()] ) -height[top]
                rain_water += distance * quantity
            floor_stack.push(x)
            print(x, floor_stack.stack)

        return rain_water

