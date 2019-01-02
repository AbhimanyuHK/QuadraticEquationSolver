class QuadraticEquation(object):

    def __init__(self, a1, a2, c, eq=0):
        """

        :param a1: X**2 Square index.
        :param a2: X    Meddule index.
        :param c: C     Constants
        :param eq:      Mostly equal to zero
        """
        self.a1 = a1
        if self.a1 == 0:
            raise Exception("Not a Quatratic Equation")
        self.a2 = a2
        self.c = c
        self.eq = eq
        if self.eq:
            self.c = self.c - self.eq

    def solve(self):
        m = self.a1 * self.c
        sol = []
        m2 = m // 2
        if m < 0:
            lt = [j for j in range(m2, m2 * (-1)) if j != 0]
        else:
            lt = range(1, m2)
        for i in lt:
            if m % i == 0:
                j = m / i
                if self.a2 == i + j:
                    sol.append((i, int(j)))

        return sol
