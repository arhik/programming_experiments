class SortedSet:
    def __init__(self, s = None):
        self._items =  sorted(s) if s is not None else []
