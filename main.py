from black_scholes import black_scholes

# Sample data
S = 100  # Current stock price
X = 105  # Strike price
T = 1    # Time to expiration (1 year)
r = 0.05 # Risk-free interest rate (5%)
sigma = 0.2  # Volatility (20%)

# Calculate the option prices
call_price = black_scholes(S, X, T, r, sigma, option_type="call")
put_price = black_scholes(S, X, T, r, sigma, option_type="put")

# Print the results
print(f"Call option price: {call_price:.2f}")
print(f"Put option price: {put_price:.2f}")
