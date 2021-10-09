import pandas as pd

def create_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

def fib(n):
    if n <= 2: return 1

    return fib(n - 1) + fib(n - 2)
