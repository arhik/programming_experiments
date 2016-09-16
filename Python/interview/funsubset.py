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

    def __repr__(self):
        return("IntSet with elements {}".format(set(self.set_elems)))

    def issubset(self,b):
        if isinstance(b, IntSet):
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
    return(a.issubset(b))
