import unittest

from sorted import SortedSet

class TestConstruction(unittest.TestCase):
    def test_empty(self):
        s = SortedSet([])

    def test_from_sequence(self):
        s = SortedSet([5,3,4,2,56])

    def test_with_duplicates(self):
        s = SortedSet([8,8,8])

    def test_from_iterable(self):
        def gen678():
            yield 6
            yield 4
            yield 3

        g = gen678()
        s = SortedSet(g)
    def test_none(self):
        s = SortedSet()


class TestContainer(unittest.TestCase):
    def  setUp(self):
        s = SortedASet([6,7,3,9])

    def test_positive_contain(self):
        self.assetTrue(6 in self.s)

    def test_negative_contain(self):
        self.assertFalse(2 in self.s)

    def test_positive_not_contained(self):
        self.assertTrue(5 not in self.s)

    def test_negative_contained(self):
        self.assertFalse(9 not in self.s)

if __name__=='__main__':
    unittest.main()
