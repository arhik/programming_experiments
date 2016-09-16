import unittest
from intset import IntSet, is_subset

class TestIntSet(unittest.TestCase):
    def test_empty(self):
        s = IntSet([])

    def test_list(self):
        s = IntSet([1,2,3,4])

    def test_tuple(self):
        s = IntSet((1,2,3,4))

    def test_duplicates_list(self):
        s = IntSet([1,2,3,4,5,4,5,3,2])
        self.assertEqual(IntSet([1,2,3,4,5]), s)

    def test_duplicates_tuples(self):
        s = IntSet((1,2,3,4,2,1,2,3,5))
        self.assertEquals(IntSet([1,2,3,4,5]),s)

    def test_issubset(self):
        s = IntSet([1,2,3,4])
        t = IntSet([1,2,3])
        self.assertEqual(t.issubset(s), False)
        self.assertEqual(s.issubset(t), True)

    def test_empty_subsets_issubset(self):
        s = IntSet([])
        t = IntSet([])
        self.assertEqual(t.issubset(s), True)
        self.assertEqual(s.issubset(t), True)

    def test_one_empty_issubset(self):
        s = IntSet([])
        t = IntSet([1,2,3,4,5,6,7])
        self.assertEqual(t.issubset(s), True)
        self.assertEqual(s.issubset(t), False)

class TestIsSubset(unittest.TestCase):
    def test_issubset_true(self):
        self.assertEqual(is_subset([1,2,3,34],[1,2,3]), True)

    def test_issubset_false(self):
        self.assertFalse(is_subset([1,2,3,4],[1,2,3,4,5,6]), False)

    def test_issubset_true_repeated(self):
        self.assertTrue(is_subset([1,2,3,3,1,2,1,2,4,2,3,2,4,2,2,4], [1,2,3,2,2,2,1,2,3,4,2,2,1,2]))

    def test_issubset_false_repeated(self):
        self.assertFalse(is_subset([1,2,3,4,2,23,4,23,2,2,1,2,3], [1,2,3,4,4,34,4,5]))

    def test_issubset_empty_sets(self):
        self.assertTrue(is_subset([], []))

    def test_issubset_rhs_empty(self):
        self.assertTrue(is_subset([1,3,3,4,3,2,3,3,4],[]))

    def test_issubset_lhs_empty(self):
        self.assertFalse(is_subset([],[1,32,4,3,2]))

    def test_issubset_invalid_input(self):
        with self.assertRaises(TypeError):
            is_subset(['q','qe',1,2,3],[1,23,3,4,54])

if __name__=='__main__':
    unittest.main()


