import unittest
from progonka import Progonka
import numpy as np


class TestProgonka(unittest.TestCase):

    answer = np.array([])

    def setUp(self):
        self.progonka = Progonka()

    def test1(self) -> None:
        self.progonka.configure(
            A=np.array([5, 1]),
            B=np.array([2, 4, -3]),
            C=np.array([-1, 2]),
            D=np.array([3, 6, 2])
        )
        self.answer = [round(64 / 43, 3), round(-1 / 43, 3), round(-29 / 43, 3)]

    def test2(self) -> None:
        self.progonka.configure(
            A=np.array([2, 2, 3]),
            B=np.array([5, 4.6, 3.6, 4.4]),
            C=np.array([-1, -1, -0.8]),
            D=np.array([2, 3.3, 2.6, 7.2])
        )
        self.answer = [round(0.2 * 0.628 + 0.4, 3), round(0.2 * 0.64 + 0.5, 3), round(0.2 * 1.2 + 0.4, 3), round((7.2 - 3 * 0.4) / 5, 3)]

    def test3(self) -> None:
        self.progonka.configure(
            A=np.array([1, 1, 1]),
            B=np.array([2, 10, -5, 4]),
            C=np.array([1, -5, 2]),
            D=np.array([-5, -18, -40, -27])
        )
        self.answer = [-3, 1, 5, -8]

    def test4(self) -> None:
        self.progonka.configure(
            A=np.array([-2, 0.1, -1]),
            B=np.array([10, 9, 4, 8]),
            C=np.array([1, 1, -1]),
            D=np.array([5, -1, -5, 40])
        )
        self.answer = [1 / 2, 0, 0, 5]

    def test5(self) -> None:
        self.progonka.configure(
            A=np.array([-2, 0]),
            B=np.array([10, 9, 4]),
            C=np.array([1, 1]),
            D=np.array([5, -1, -5])
        )
        self.answer = [round(179 / 368, 3), round(25 / 184, 3), round(-5 / 4, 3)]

    def test6(self) -> None:
        self.progonka.configure(
            A=np.array([-20, 0]),
            B=np.array([1, 9, 4]),
            C=np.array([11, 1]),
            D=np.array([5, -10, -5])
        )
        self.answer = [round(565 / 916, 3), round(365 / 916, 3), round(-5 / 4, 3)]

    def tearDown(self) -> None:
        self.progonka.execute()
        self.assertEqual(list(self.progonka.answer), self.answer)
