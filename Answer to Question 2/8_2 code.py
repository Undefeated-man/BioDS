import numpy as np
import seaborn as sns
sns.set()

from matplotlib import pyplot as plt

def runge_kutta_4(func, x, y0, show=True):
    """
        Func:
            Implement the 4-th Runge Kutta method
        
        Args:
            func: the function defined, taking x and y ()
            x: a numpy array or a list, the range of input
            y0: the initial value
    """
    x     = np.array(x)
    len_  = len(x)
    y     = np.zeros(len_)
    y[0]  = y0
    h     = x[1] - x[0]
    
    for i in range(len_ - 1):
        k1     = fun(x[i], y[i]);
        k2     = fun(x[i]+h/2, y[i] + h * k1/2);
        k3     = fun(x[i]+h/2, y[i] + h * k2/2);
        k4     = fun(x[i]+h,   y[i] + h * k3);
        y[i+1] = y[i] + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6;
        
    if show:  # draw the graph
        plt.figure(figsize=(10,6))
        plt.plot(x, y, alpha=.8)
        plt.title('The fourth-order Runge-Kutta solution')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
        
    return y

# a test function. 
def fun(x, y):
    return (np.exp(-x) - y) / 2
    
    
# Test. This test is using the one on https://zhuanlan.zhihu.com/p/146771778
if __name__ == "__main__":
    runge_kutta_4(fun, np.arange(0, 2, .1), .5)