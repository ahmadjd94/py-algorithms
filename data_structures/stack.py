class Stack:
    def __init__(self, elements: list = None):
        self.items = []

        if elements is not None:
            for i in elements:
                self.items.append(i)

    def pop(self):
        return self.items.pop(len(self.items)-1)

    def peak(self):

        return self.items[len(self.items)-1]

    def push(self, element):
        return self.items.append(element)

    def is_empty(self):
        return not bool(len(self.items))

