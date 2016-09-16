class IntSet:
    def __init__(self, a):
        assert hasattr(a, '__iter__')
        for i in a: self._validate(i)
        self.set_elems = {hash(item):item for item in a}
    
    @staticmethod
    def _validate(x):
        if not isinstance(x, int):
            raise TypeError("Only Integer Arrays are allowed")

    def __contains__(self,a):
        if a in self.set_elems: # Since hash(int a) is an a 
            return True
        else:
            return False
        
    def __iter__(self):
        for i in self.set_elems:
            yield i

    def __eq__(self, rhs):
        if not isinstance(rhs, IntSet):
            raise TypeError("Cannot compare IntSet with an unknown object")
        return self.set_elems == rhs.set_elems

    def __repr__(self):
        return("IntSet with elements {}".format(set(self.set_elems)))

    def issubset(self,b):
        if not isinstance(b, IntSet):
            raise TypeError("Given input is not of IntSet type:")
        for i in b:
            if i not in self:
                return False
        return True


def is_subset(a, b):
    try:
        a = IntSet(a)
        b = IntSet(b)
    except TypeError as e:
        print(e)
        raise e
    return(a.issubset(b))
