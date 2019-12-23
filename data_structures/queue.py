class Queue:
    def __init__(self, elements: list = None):
        self.items = []
        if elements is not None:
            for i in elements:
                self.enqueue(i)

    def deque(self):
        return self.items.pop(0)

    def enqueue(self, element):
        self.items.append(element)

    def is_empty(self):
        return not bool(len(self.items))

    def __str__(self):
        return str(self.items)
