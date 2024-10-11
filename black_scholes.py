import numpy as np
from scipy.stats import norm

def black_scholes(S, X, T, r, sigma, option_type="call"):
    """
    S: Current stock price
    X: Strike price
    T: Time to expiration (in years)
    r: Risk-free interest rate
    sigma: Volatility of the stock
    option_type: "call" or "put"
    """
    d1 = (np.log(S / X) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    if option_type == "call":
        option_price = S * norm.cdf(d1) - X * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        option_price = X * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Option type must be 'call' or 'put'")
    
    return option_price
