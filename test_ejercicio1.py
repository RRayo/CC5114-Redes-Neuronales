import unittest

from perceptron_class import Perceptron, p_sum


class TestPerceptronAnd(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.p_and = Perceptron([1, 1], -1.5)

    def test_testablaVerdad(self):
        assert self.p_and.feed([0, 0]) == 0, "p_and not calculating values correctly"
        assert self.p_and.feed([0, 1]) == 0, "p_and not calculating values correctly"
        assert self.p_and.feed([1, 0]) == 0, "p_and not calculating values correctly"
        assert self.p_and.feed([1, 1]) == 1, "p_and not calculating values correctly"


class TestPerceptronOr(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.p_or = Perceptron([1, 1], -0.5)

    def test_tabla_verdad(self):
        assert self.p_or.feed([0, 0]) == 0, "p_or not calculating values correctly"
        assert self.p_or.feed([0, 1]) == 1, "p_or not calculating values correctly"
        assert self.p_or.feed([1, 0]) == 1, "p_or not calculating values correctly"
        assert self.p_or.feed([1, 1]) == 1, "p_or not calculating values correctly"


class TestPerceptronNand(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.p_nand = Perceptron([-2, -2], 3)

    def test_tabla_verdad(self):
        assert self.p_nand.feed([0, 0]) == 1, "p_nand not calculating values correctly"
        assert self.p_nand.feed([0, 1]) == 1, "p_nand not calculating values correctly"
        assert self.p_nand.feed([1, 0]) == 1, "p_nand not calculating values correctly"
        assert self.p_nand.feed([1, 1]) == 0, "p_nand not calculating values correctly"


class TestPerceptronNot(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.p_not = Perceptron(-1, 1)

    def test_tabla_verdad(self):
        assert self.p_not.feed(1) == 0, "p_not not calculating values correctly"
        assert self.p_not.feed(0) == 1, "p_not not calculating values correctly"


class TestPerceptronSum(unittest.TestCase):

    def test_tabla_verdad(self):
        assert p_sum(0, 0)[0] == 0, "p_sum not calculating values correctly"
        assert p_sum(0, 1)[0] == 1, "p_sum not calculating values correctly"
        assert p_sum(1, 0)[0] == 1, "p_sum not calculating values correctly"
        assert p_sum(1, 1)[0] == 0, "p_sum not calculating values correctly"

        assert p_sum(0, 0)[1] == 0, "p_sum not calculating values correctly"
        assert p_sum(0, 1)[1] == 0, "p_sum not calculating values correctly"
        assert p_sum(1, 0)[1] == 0, "p_sum not calculating values correctly"
        assert p_sum(1, 1)[1] == 1, "p_sum not calculating values correctly"
