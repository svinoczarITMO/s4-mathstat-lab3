import numpy as np
import matplotlib.pyplot as plt

def grade(samples, n):
    thetas, bias, vars, mses = [0] * n, [0] * n, [0] * n, [0] * n
    for i in range(n):
        thetas[i] = (np.sqrt(3*np.var(samples[i])))
        bias[i] = abs(thetas[i] - 10)
        vars[i] = abs(np.var(samples[i]) - np.var(samples, ddof=1))
        mses[i] = np.mean((thetas[i]-10)**2)
    mle_thetas = [thetas[i] for i in range(n)]
    return thetas, bias, vars, mses, tuple(mle_thetas)

mse_mles = []
for n in range(100, 1001, 100):
    samples = np.random.uniform(low=-10, high=10, size=(n, 100))
    thetas, bias, vars, mses, mle_thetas = grade(samples, n)
    
    mse_mles.append(np.mean((mle_thetas - 10)**2))
    
print("MSE for MLE estimates: ", np.mean(mse_mles))
