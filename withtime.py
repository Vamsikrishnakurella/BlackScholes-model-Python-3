import numpy as np
import scipy.stats as si
import sympy as sy
import matplotlib.pyplot as plt
x = []
y = []
def euro(S, K, T, r, sigma):
    
    #S: spot price
    #K: strike price
    #T: time to maturity
    #r: interest rate
    #sigma: volatility of underlying asset
    
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    
    call = (S * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0))
    
    return call

for i in range(1,5,1):
    x.append(i)
    y.append(euro(50,100,i,0.05,0.25))
    print(euro(50,100,i,0.05,0.25))

plt.plot(x,y)
plt.show()
