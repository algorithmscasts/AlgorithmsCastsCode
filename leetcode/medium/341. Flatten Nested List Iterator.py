# coding=utf-8
"""
Solution 1:
Idea: flatten the list in the initializer and keep track of the index.
"""


class NestedIterator:
    def __init__(self, nestedList):
        def helper(elt):
            res = []
            if elt.isInteger():
                res.append(elt.getInteger())
            else:
                for x in elt.getList():
                    res.extend(helper(x))
            return res

        self.values = []
        for x in nestedList:
            self.values.extend(helper(x))
        self.i = 0

    def next(self):
        value = self.values[self.i]
        self.i += 1
        return value

    def hasNext(self):
        return self.i < len(self.values)


"""
Solution above is not an ideal solution since we don’t really implement an iterator, let’s improve it 
Solution 2:
Idea: put the element in the stack in reverse order so that popping returns the first element,
when the popped element is a list expand it to elements and add it to the stack in reverse order so that again its
first element is at the top.
"""
class NestedIteratorSol2:
    def __init__(self, nestedList):
        self.stack = nestedList[::-1]

    def next(self):
        return self.stack.pop()

    def hasNext(self):
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack.pop()
            self.stack.extend(top.getList()[::-1])
        return False

"""
Solution 3:
Idea: maintain a tuple of current list and its index in a stack 
"""
class NestedIteratorSol3:
    def __init__(self, nestedList):
        self.stack = [[nestedList, 0]]

    def next(self):
        nestedList, i = self.stack[-1]
        self.stack[-1][1] += 1
        return nestedList[i].getInteger()

    def hasNext(self):
        while self.stack:
            elt, i = self.stack[-1]
            if i == len(elt):
                self.stack.pop()
            elif elt[i].isInteger():
                return True
            else:
                self.stack[-1][1] += 1
                self.stack.append([elt[i].getList(), 0])
        return False
