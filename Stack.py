class Stack:
    def __init__(self):
        self.__stack_list = []  # instance variable, private, name mangled

    def push(self, val: [int, float]) -> None:
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


class SumStack(Stack):
    def __init__(self):
        super().__init__()             # note that self is not filled in
        # Stack.__init__(self)        this will work, but super() preferred
        self.__sum = 0  # private instance variable

    def get_sum(self):
        return self.__sum

    def push(self, val: [int, float]) -> None:
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val
