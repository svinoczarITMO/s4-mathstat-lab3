import numpy as np
import matplotlib.pyplot as plt

def grade(samples, n):
    thetas, bias, vars, mses = [0] * n, [0] * n, [0] * n, [0] * n
    for i in range(n):
        thetas[i] = (np.sqrt(3*np.var(samples[i])))
        bias[i] = abs((np.sqrt(3*np.var(samples[i]))) - 10)
        vars[i] = abs(np.var(samples[i]) - np.var(samples, ddof=1))
        mses[i] = np.mean((thetas[i]-10)**2)
    return thetas, bias, vars, mses


for n in range(10, 101, 10):
    samples = np.random.uniform(low=-10, high=10, size=(1000, 100))
    thetas, bias, vars, mses = grade(samples, n)
    
    count_bias = []
    count_vars = []
    count_mses = []
    
    count_bias.append(sum(1 for value in bias if value > 0.3))
    count_vars.append(sum(1 for value in vars if value > 0.5))
    count_mses.append(sum(1 for value in mses if value > 0.05))

    labels = ['']
    x = np.arange(len(labels))
    width = 0.25

    plt.figure(figsize=(10, 6))
    plt.bar(x - width, count_bias, width, color='blue', label='Bias')
    plt.bar(x, count_vars, width, color='green', label='Variance')
    plt.bar(x + width, count_mses, width, color='red', label='MSE')

    plt.xlabel('Arrays')
    plt.xticks(x, labels)
    plt.legend()
    plt.grid(True)
    plt.show()
