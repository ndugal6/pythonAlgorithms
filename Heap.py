from Structures.Node import Node


class Heap(object):
    def __init__(self):
        self.root = None
        self.size = 0
        self.max_degree = 3

    def peek(self): #  find a maximum item of a max-heap, or a minimum item of a min-hea
        return self.root

    def size(self): #eturn the number of items in the heap.
        return self.size

    def is_empty(self): # return true if the heap is empty, false otherwise.
        return self.size == 0

    def increase_key(self): #updating a key within a max- or min-heap, respectively
        pass

    def decrease_key(self): ##updating a key within a max- or min-heap, respectively
        pass

    def create(self): #create an empty heap
        self.__init__()
        return self

    def __repr__(self):
        return f'Root:\n{self.root}'


class MaxHeap(Heap):
    def push(self, new_node): # "adding a new key to the heap"
        self.size += 1
        if self.root is None:
            self.root = new_node
        elif new_node > self.root:
            self.root.value, new_node = new_node, self.root.value
            self.add_down(new_node, self.root)
        elif new_node <= self.root:
            self.add_down(new_node, self.root)


    def pop(self): # returns the node of maximum value from a max heap [or minimum value from a min heap] after removing it from the heap
        value = self.root.duplicate()
        self.delete(self.root)
        return value

    """pop root and push a new key. More efficient than pop followed by push, since only need to balance once,  
    not twice, and appropriate for fixed-size heaps."""
    def replace(self, new_value):
        self.root.value = new_value
        self.sift_down(self.root)

    def heapify(self, values): # create a heap out of given array of elements
        for value in values:
            self.push(Node(value))

    def unionize(self): # joining two heaps to form a valid new heap containing all the elements of both, preserving the original heaps.
        pass

    def meld(self): #joining two heaps to form a valid new heap containing all the elements of both, destroying the original heaps.
        pass

    def delete(self, del_node): # delete an arbitrary node (followed by moving last node and sifting to maintain heap)
        self.size -= 1
        if self.size == 0:
            self.root = None
        del_node.value = float('-inf')
        self.sift_down(del_node)
            

    def sift_up(self, sift_node):  #move a node up in the tree, as long as needed; used to restore heap condition after insertion. Called "sift" because node moves up the tree until it reaches the correct level, as in a sieve.
        if sift_node.parent is None:
            return
        if sift_node <= sift_node.parent:
            return
        sift_node.swap(sift_node.parent)
        self.sift_up(sift_node.parent)
        self.sift_down(sift_node);
    
    def sift_down(self, sift_node): #move a node down in the tree, as long as needed; used to restore heap condition after insertion. Called "sift" because node moves up the tree until it reaches the correct level, as in a sieve.
        if sift_node.degree == 0:
            if sift_node == float('-inf'):
                sift_node.destroy()
            return
        max_child = max(sift_node.children)
        if sift_node >= max_child:
            return
        sift_node.swap(max_child)
        self.sift_down(max_child)




    def add_down(self, new_node, cur_node): #move a node down in the tree, similar to sift-up; used to restore heap condition after deletion or replacement.
        if cur_node.degree < self.max_degree:
            cur_node.add_child(new_node)
        elif new_node >= max(cur_node.children):
            cur_node.add_child(new_node)
            new_node, cur_node = cur_node.children.pop(0), new_node
            self.add_down(new_node, cur_node)
        else:
            cur_node = [node for node in cur_node.children if new_node < node][0]
            self.add_down(new_node, cur_node)

if __name__ == '__main__':
    test = MaxHeap()
    num_list = [10,1,2,3,4,5,6,7,8,9,1,1,4]
    test.heapify(num_list)
    print(f''
          f'peek: {test.peek()}\n'
          f'pop: {test.pop()}\n'
          f'pop: {test.pop()}\n'
          f'peek: {test.peek()}\n'
          f'replace: {test.replace(-2)}\n'
          f'peek: {test.peek()}\n')
    # max_child = max(test.root.children)
    # print(max_child.value)