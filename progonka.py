import numpy as np


class Progonka:

    A = np.array([0])
    B = np.array([])
    C = np.array([0])
    D = np.array([])
    answer = np.array([])
    sizeSystem = 0

    def configure(self, A, B, C, D):
        self.A = np.append(self.A, np.array(A))
        self.B = np.array(B)
        self.C = np.append(np.array(C), self.C)
        self.D = np.array(D)
        self.sizeSystem = len(D)
        self.answer = np.array([0j for _ in range(self.sizeSystem)])

    def execute(self):
        alfa_array, betta_array = self.get_coefficients()
        for i in range(len(self.answer) - 1, -1, -1):
            if i == self.sizeSystem - 1:
                self.answer[i] = betta_array[i]
            else:
                self.answer[i] = alfa_array[i] * self.answer[i + 1] + betta_array[i]

    def get_coefficients(self):
        alfa_array = []
        betta_array = []
        gamma_array = []
        for i in range(self.sizeSystem):
            if i == 0:
                gamma_array.append(self.B[0])
                alfa_array.append(-self.C[0]/gamma_array[0])
                betta_array.append(self.D[0]/gamma_array[0])
            elif i == self.sizeSystem-1:
                gamma_array.append(self.B[i] + self.A[i] * alfa_array[i - 1])
                betta_array.append((self.D[i] - self.A[i] * betta_array[i - 1]) / gamma_array[i])
            else:
                gamma_array.append(self.B[i] + self.A[i] * alfa_array[i - 1])
                alfa_array.append(-self.C[i]/gamma_array[i])
                betta_array.append((self.D[i] - self.A[i] * betta_array[i - 1]) / gamma_array[i])
        return alfa_array, betta_array
