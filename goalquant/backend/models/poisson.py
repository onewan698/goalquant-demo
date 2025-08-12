import math

def poisson_probability(lmbda, k):
    return (math.exp(-lmbda) * lmbda**k) / math.factorial(k)
