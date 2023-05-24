# Create a Circular List

# A circular list is of finite size, but can infititely be asked for its previous and next elements. This is because it acts like it is joined at the ends and loops around.

# For example, imagine a CircularList of [1, 2, 3, 4]. Five invocations of next() in a row should return 1, 2, 3, 4 and then 1 again. At this point, five invocations of prev() in a row should return 4, 3, 2, 1 and then 4 again.

# Your CircularList is created by passing a vargargs parameter in, e.g. new CircularList(1, 2, 3). Your list constructor/init code should throw an Exception if nothing is passed in.

class CircularList:
    def __init__(self, *args):
        self.args = args
        if not args:
            raise ValueError
        self.length = len(self.args)
        self.counter = Counter()
        
    def next(self):
        if self.counter.start == "on":
            self.counter.add()
            return self.args[self.counter.value % self.length]

        elif self.counter.start == "off":
            self.counter.starting()
            return self.args[0]
            
    def prev(self):
        self.counter.starting()
        self.counter.subtract()
        return self.args[self.counter.value % self.length]

class Counter:
    """helper class that stores the current position of the list"""
    def __init__(self, start_value=0, start="off"):     
        self.value = start_value
        self.start = start
    
    def starting(self):
        self.start = "on"

    def add(self):
        self.value += 1

    def subtract(self):
        self.value -= 1