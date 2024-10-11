import matplotlib.pyplot as plt
import numpy as np
from black_scholes import black_scholes

def plot_option_prices(S_range, X, T, r, sigma):
    call_prices = []
    put_prices = []
    
    for S in S_range:
        call_prices.append(black_scholes(S, X, T, r, sigma, option_type="call"))
        put_prices.append(black_scholes(S, X, T, r, sigma, option_type="put"))

    plt.plot(S_range, call_prices, label="Call Option Price")
    plt.plot(S_range, put_prices, label="Put Option Price")
    plt.xlabel("Stock Price (S)")
    plt.ylabel("Option Price")
    plt.legend()
    plt.title("Black-Scholes Option Prices")
    plt.show()

if __name__ == "__main__":
    S_range = np.linspace(50, 150, 100)  # Stock prices from 50 to 150
    X = 100  # Strike price
    T = 1    # Time to expiration (1 year)
    r = 0.05 # Risk-free interest rate (5%)
    sigma = 0.2  # Volatility (20%)

    plot_option_prices(S_range, X, T, r, sigma)
