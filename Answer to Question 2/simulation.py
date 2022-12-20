import numpy as np
import seaborn as sns
sns.set()

from matplotlib import pyplot as plt
from threading import Thread
from time import sleep

class Simulate:
    def __init__(self, a, b, c, d, k1, k2, k3, epsilon=1e-3):
        self.a  = a
        self.b  = b
        self.c  = c
        self.d  = d
        self.k1 = k1
        self.k2 = k2
        self.k3 = k3
        self.t  = 0
        self.e  = epsilon
        self.history = {"a":[], "b":[], "c":[], "d":[]}
        self.running = 1
        
    def record(self):
        while self.running:
            self.history["a"].append(self.a)
            self.history["b"].append(self.b)
            self.history["c"].append(self.c)
            self.history["d"].append(self.d)
            for i in range(100):
                t = i

        
    def fk1(self, k1):
        e = self.e * k1
        for i in range(int(1/self.e/k1)):
            if self.a <= e or self.b <= e:
                break
            self.a -= e
            self.b -= e
            self.c += e
        
    def fk2(self, k2):
        e = self.e * k2
        for i in range(int(1/self.e/k2)):
            if self.c <= e:
                break
            self.a += e
            self.b += e
            self.c -= e
        
    def fk3(self, k3):
        e = self.e * k3
        for i in range(int(1/self.e/k3)):
            if self.c <= e:
                break
            self.a += e
            self.c -= e
            self.d += e
    
    def print_state(self, t=50):
        format_ = """
        In time step %s (min):
            S  = %s um
            E  = %s um
            ES = %s um
            P  = %s um
                  """
        print(format_%(t, self.b, self.a, self.c, self.d))
    
    def run(self, n=50):
        Thread(target=self.record, args=()).start()
        for i in range(50):
            a, b, c, d = self.a, self.b, self.c, self.d
            self.print_state(self.t + i)
            Thread(target=self.fk1, args=(self.k1,)).start()
            Thread(target=self.fk3, args=(self.k3,)).start()
            Thread(target=self.fk2, args=(self.k2,)).start()
            if abs(self.a - a) < self.e**2 and abs(self.d - d) < self.e**2 and abs(self.c - c) < self.e**2:
                self.running = 0
                break
                
    def plot(self):
        plt.figure(figsize=(10,6))
        plt.plot(self.history["a"], alpha=.8, label="E")
        plt.plot(self.history["b"], alpha=.8, label="S")
        plt.plot(self.history["c"], alpha=.8, label="ES")
        plt.plot(self.history["d"], alpha=.8, label="P")
        plt.title('The simulation for the enzyme reaction')
        plt.xlabel('x')
        plt.ylabel('y(um)')
        plt.legend()
        plt.show()
        
if __name__ == "__main__":
    s = Simulate(1, 10, 0, 0, 100, 600, 150)
    s.run()
    s.plot()