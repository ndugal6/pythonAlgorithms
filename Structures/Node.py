from copy import copy


class Node(object):
    def __init__(self, value):
        self.children = []
        self.value = value
        self.parent = None

    def add_child(self, new_child):
        new_child.parent = self
        self.children.append(new_child)
        self.children.sort(key=lambda x: x.degree())
        return self

    def remove_child(self, child):
        self.children = [node for node in self.children if node != child]
        self.children.sort(key=lambda x: x.degree())
        return self

    def degree(self):
        return len(self.children)

    def duplicate(self):
        return copy(self)

    @property
    def depth(self):
        return 0 if self.parent is None else self.parent.depth + 1

    def __eq__(self, other):
        if type(other) is int:
            return self.value == other
        return self.value == other.value

    def __ne__(self, other):
        if type(other) is int:
            return not (self.value == other)
        return not (self.value == other.value)

    def __lt__(self, other):
        if type(other) is int:
            return self.value < other
        return self.value < other.value

    def __gt__(self, other):
        if type(other) is int:
            return self.value > other
        return self.value > other.value

    def __le__(self, other):
        if type(other) is int:
            return self.value <= other
        return self.value <= other.value

    def __ge__(self, other):
        if type(other) is int:
            return self.value >= other
        return self.value >= other.value

    def __repr__(self):
        indent = self.depth * '\t'
        child_str = ''
        for child in self.children:
            child_str += f'${child}'
        return f'{indent}{self.value}\n{child_str}'
