import math
import numpy as np
from numpy import random

class Balloons:
    def __init__(self, N = 10):
        self.N = N
        self.current_balloon = 0
        self.max = 10
        self.min = 0
        self.probs = np.array([-1] * (self.max - self.min))
        self.balloons = [-1] * N
        print(*self.probs, sep = ", ")
        
        # for i in range(N):
        #     self.balloons[i] = np.random.choice(self.probs, p=self.probs) + 1

        # print("Balloons" + self.balloons)


    def getBallons(self):
        return self.balloons.copy()

    def getprobs(self):
        print('getting probs ;_')
        totalprobs = 0
        for i in range(self.min, self.max):
            n = 50
            prob = 0
            for e in range(n):
                prob += self.dist(i + 1.0 * e/n) * 1.0 * e/n
            self.probs[i] = prob
            totalprobs += prob
        
        for i in range(len(self.probs)):
            self.probs[i] /= totalprobs

class GaussianBalloons(Balloons):
    def __init__(self, N = 10):
        super().__init__(N)
        self.type = "GAUSSIAN"
        self.mean = random.randint(self.min, self.max)
        self.var = random.randint(1, 3 * self.max)
        self.std = math.sqrt(self.var)
        super().getprobs()
        
    def dist(self, x):
        return 1.0/ (self.std * math.sqrt(2 * math.pi)) * math.e ** (-1 * (x - self.mean)**2 / (2 * self.var))


class UniformBalloons(Balloons):
    def __init__(self, N = 10):
        super().__init__(N)
        self.type = "UNIFORM"
        super().getprobs()
        
    def dist(self, x):
        if x < self.min:
            return 0
        if x > self.max: 
            return 0
        else:
            return 1/(self.max - self.min)

class GeometricBalloons(Balloons):
    def __init__(self, N = 10):
        super().__init__(N)
        self.type = "GEOMETRIC"
        self.p = random.randint(10) * 1.0 / 10
        super().getprobs()
        
    def dist(self, x):
        return ((1 - self.p) ** math.floor(x - 1)) * self.p
        
class LimitBalloons(Balloons):
    def __init__(self, N = 10):
        super().__init__(N)
        self.type = "LIMIT"
        self.limit = random.randint(self.min, self.max)
        super().getprobs()
        
    def dist(self, x):
        if x < self.limit: 
            return 0
        if x >= self.limit and x <= self.limit + 1: 
            return 1



        
