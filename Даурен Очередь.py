class queue:
    someList = []
    def push(self, *args):
        self.someList.append(*args)

    def display(self):
        print(self.someList)

    def pop(self):
        self.someList.pop(0)

    def qsize(self):
        print(len(self.someList))

    def empty(self):
        if self.someList == self.someList.clear():
            print(True)
        else:
            print(False)

    def full(self):
        if self.someList != self.someList.clear():
            print(True)
        else:
            print(False)


e = queue()
e.push(1)
e.push(2)
e.push(3)
e.push(4)
e.display()
e.pop()
e.display()
e.qsize()
e.empty()
e.full()

