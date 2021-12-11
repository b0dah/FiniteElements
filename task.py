import numpy as np

from progonka import Progonka


class Task:
    a = 0
    b = 0
    N = 0
    delta_x = 0
    sigma1 = 0
    sigma2 = 0
    alpha = 0
    mu = 0
    lambda_ = 0
    s = 0
    p1 = 0
    cond_left = None
    cond_left_deriv = None
    cond_right = None
    cond_right_deriv = None
    answer = np.array([])

    def configure_parameters(self, a, b, N, sigma1, sigma2, alpha, mu, lambda_, s,
                             cond_left=None, cond_left_deriv=None, cond_right=None, cond_right_deriv=None):
        self.a = a
        self.b = b
        self.N = N
        self.delta_x = (b - a) / (N - 1)
        self.sigma1 = sigma1
        self.sigma2 = sigma2
        self.alpha = alpha
        self.mu = mu
        self.lambda_ = lambda_
        self.s = s
        self.cond_left = cond_left
        self.cond_left_deriv = cond_left_deriv
        self.cond_right = cond_right
        self.cond_right_deriv = cond_right_deriv

    def get_coefficients(self, x):
        sigma = self.sigma1 if x <= 0.4 else self.sigma2
        k0 = - (x + self.s)
        k1 = self.alpha * (self.mu - x) - self.lambda_ * sigma
        k2 = sigma**2 / 2
        return k0, k1, k2

    def get_c(self, x):
        k0, k1, k2 = self.get_coefficients(x)
        return (6 * k2 + 3 * k1 * self.delta_x + k0 * self.delta_x**2) / (6 * self.delta_x)

    def get_b(self, x):
        k0, k1, k2 = self.get_coefficients(x)
        b1 = (-6 * k2 + 3 * k1 * self.delta_x + 2 * k0 * self.delta_x**2) / (6 * self.delta_x)
        b2 = (-6 * k2 - 3 * k1 * self.delta_x + 2 * k0 * self.delta_x**2) / (6 * self.delta_x)
        if x == 0:
            return b1
        elif x == self.b:
            return b2
        else:
            return b1 + b2

    def get_a(self, x):
        k0, k1, k2 = self.get_coefficients(x)
        return (6 * k2 - 3 * k1 * self.delta_x + k0 * self.delta_x**2) / (6 * self.delta_x)

    def execute(self):

        D = np.zeros((self.N,))

        M = np.zeros((self.N, self.N))
        for i in range(M.shape[0]):
            M[i][i] = self.get_b(i * self.delta_x)
            if i != 0:
                M[i][i - 1] = self.get_b(i * self.delta_x)
            if i != M.shape[1] - 1:
                M[i][i + 1] = self.get_a(i * self.delta_x)

        if self.cond_left_deriv is not None:
            D[0] = self.cond_left_deriv

        if self.cond_right_deriv is not None:
            D[-1] = (self.cond_right_deriv * self.sigma2**2) / 2

        if self.cond_right is not None:
            D[-1] = self.cond_right
            M[-1][-1] = 1
            M[-1][-2] = 0

        if self.cond_left is not None:
            D[0] = self.cond_left
            M[0][0] = 1
            M[0][1] = 0

        self.answer = np.linalg.solve(M, D)

        # A = [self.get_a(i * self.delta_x) for i in range(1, self.N)]
        # B = [self.get_b(i * self.delta_x) for i in range(self.N)]
        # C = [self.get_c(i * self.delta_x) for i in range(self.N - 1)]
        #
        # if self.cond_left_deriv is not None:
        #     D[0] = self.cond_left_deriv
        #
        # if self.cond_right_deriv is not None:
        #     D[-1] = (self.cond_right_deriv * self.sigma2**2) / 2
        #
        # if self.cond_right is not None:
        #     D[-1] = self.cond_right
        #     B[-1] = 1
        #     A[-1] = 0
        #
        # if self.cond_left is not None:
        #     D[0] = self.cond_left
        #     B[0] = 1
        #     C[0] = 0
        #
        # progonka = Progonka()
        # progonka.configure(A, B, C, D)
        # progonka.execute()
        # self.answer = progonka.answer

    def write_file(self, filename):
        with open(filename, 'w') as file:
            for i in range(len(self.answer)):
                print(f"{self.delta_x * i} {abs(self.answer[i])}\n")
                file.write(f"{self.delta_x * i} {abs(self.answer[i])}\n")

    def show(self):
        X = [i * self.delta_x for i in range(len(self.answer))]
        import pylab
        pylab.figure(1)
        pylab.plot(X, abs(self.answer))
        pylab.grid()
        pylab.show()
