
class Heap:
    def __init__(self, type):
        self.type = type
        self.root = None

    def peek(self): #  find a maximum item of a max-heap, or a minimum item of a min-hea
        pass


    def push(self): # "adding a new key to the heap"
        pass

    def pop(self): # returns the node of maximum value from a max heap [or minimum value from a min heap] after removing it from the heap
        pass

    """pop root and push a new key. More efficient than pop followed by push, since only need to balance once,  
    not twice, and appropriate for fixed-size heaps."""
    def replace(self):
        pass

    def create(self): #create an empty heap
        pass

    def heapify(self): # create a heap out of given array of elements
        pass

    def unionize(self): # joining two heaps to form a valid new heap containing all the elements of both, preserving the original heaps.
        pass

    def meld(self): #joining two heaps to form a valid new heap containing all the elements of both, destroying the original heaps.
        pass

    def size(self): #eturn the number of items in the heap.
        pass

    def is_empty(self): # return true if the heap is empty, false otherwise.
        pass

    def increase_key(self): #updating a key within a max- or min-heap, respectively
        pass

    def decrease_key(self): ##updating a key within a max- or min-heap, respectively
        pass

    def delete(self): # delete an arbitrary node (followed by moving last node and sifting to maintain heap)
        pass

    def sift_up(self): #move a node up in the tree, as long as needed; used to restore heap condition after insertion. Called "sift" because node moves up the tree until it reaches the correct level, as in a sieve.
        pass

    def sift_down(self): #move a node down in the tree, similar to sift-up; used to restore heap condition after deletion or replacement.
        pass



