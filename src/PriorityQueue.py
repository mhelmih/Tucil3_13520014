from heapq import heappush, heappop

class PriorityQueue:
    """ A class used to represent a priority queue. 
    
    Attributes
    ----------
    heap : list of something
        The container for priority queue
        
    Methods
    -------
    push(k)
        Push value k to the heap with priority
    pop()
        Pop the first value in the heap
    empty()
        Check if the container is empty
    """
    
    def __init__(self):
        self.heap = []

    def push(self, k):
        """ Push value k to the heap with priority. """
        heappush(self.heap, k)

    def pop(self):
        """ Pop and return the first value in the heap. """
        return heappop(self.heap)

    def empty(self):
        """ Check if the container is empty. """
        return not self.heap
